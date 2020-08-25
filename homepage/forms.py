from django import forms


class AddPostForm(forms.Form):
    boast = forms.BooleanField(required=False)
    content = forms.CharField(max_length=280)
