# Create your views here.
from django.contrib import auth

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator

from django.views.generic import ListView, FormView, CreateView, UpdateView

from app.user.forms import PostForm, UpdateProfileForm

from app.post.models import Post
from app.user.models import Profile


class Userindex(ListView):
    template_name = 'index.html'

    # model = Post
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(reverse('team:team_index'))
    # else:
    #     return HttpResponseRedirect(reverse('user:user_login'))
    # return HttpResponse("Hello, world. You're at the polls index.")

    def get_queryset(self):
        queryset = Post.objects
        return queryset

    def get(self, request, *args, **kwargs):
        return super(Userindex, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['list_post'] = Post.objects
        for i in ctx['object_list']:
            print(i.title)
            print(i.slug)
        return ctx


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        self.request.session['title'] = 'Login page'
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user:index'))
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_form = form.get_user()
        login(self.request, user_form)
        return super().form_valid(form)

    def get_success_url(self):
        link = self.request.POST.get('next', '')
        if link:
            return link
        else:
            return reverse('user:index')


UserLoginView = UserLogin.as_view()


class UserRegister(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse('user:index'))
        else:
            return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            form.instance.is_staff = False
            user = form.save()
            profile = Profile(_id=user.pk)
            profile.other_name = ''
            # profile.avatar = ''
            profile.full_name = ''
            try:
                profile.save()
            except:
                user.delete()
        except:
            pass
        return super().form_valid(form)

    # def form_invalid(self, form):


    def get_success_url(self):
        return reverse('user:user_login')


UserRegisterView = UserRegister.as_view()


class UserUpdateProfile(UpdateView):
    model = User
    template_name = 'update.html'
    form_class = UpdateProfileForm

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        return super(UserUpdateProfile, self).form_valid(form)


UserUpdateProfileView = UserUpdateProfile.as_view()


def UserLogoutView(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('user:login'))


UserindexView = Userindex.as_view()


class CreatePost(FormView):
    template_name = 'create.html'
    form_class = PostForm

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        slug = form.cleaned_data.get('slug')
        comment = form.cleaned_data.get('comments')

        post = Post(title=title)
        post.slug = slug
        # post.comments = comment
        post.save()
        return HttpResponseRedirect(reverse_lazy('user:user_index'))


CreatePostView = CreatePost.as_view()
