from django.http import HttpResponse


# Create your views here.

def userindex(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(reverse('team:team_index'))
    # else:
    #     return HttpResponseRedirect(reverse('user:user_login'))
    return HttpResponse("Hello, world. You're at the polls index.")
