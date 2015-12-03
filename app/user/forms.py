from django import forms

__author__ = 'FRAMGIA\nguyen.huy.quyet'
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.Form):
    title = forms.CharField(label=_("title"), widget=forms.TextInput)
    slug = forms.CharField(label=_("slug"), widget=forms.TextInput)
    # comments = forms.CharField(label=_("comments"), widget=forms.Textarea)

    class Meta:
        fields = ['title', 'slug']


class UpdateProfileForm(forms.Form):
    first_name = forms.CharField(label=_("First name"))
    last_name = forms.CharField(label=_("Last name"))
    email = forms.CharField(label=_("Email "), widget=forms.EmailInput)
    email_confirm = forms.CharField(label=_("Email confirmation"), widget=forms.EmailInput)
    image = forms.ImageField(label=_("avata"))

    class Meta:
        pass

    def clean_email_confirm(self):
        email1 = self.cleaned_data.get('email')
        email_con = self.cleaned_data.get('email_confirm')
        if email1 != email_con:
            raise forms.ValidationError('Email ko trung khop')
        return email1
