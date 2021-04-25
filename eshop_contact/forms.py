from django.core import validators

from django import forms


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا نام و نام خانوادگی خود رو وارد کنید', 'class': 'form-control',
                   'required': "required"}),
        label='نام و نام خانوادگی',
        validators=[
            validators.MaxLengthValidator(150, 'نام و نام خانوادگی وارد شده نمیتواند بیش از 150 کاراکتر باشد')
        ]
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'لطفا ایمیل خود را وارد کنید', 'class': 'form-control', 'required': "required"}),
        label='ایمیل',
        validators=[
            validators.MaxLengthValidator(100, 'ایمیل وارد شده نمیتواند بیش از 100 کاراکتر باشد')
        ]
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'لطفا عنوان پیام را وارد کنید', 'class': 'form-control', 'required': "required"}),
        label='عنوان پیام',
        validators=[
            validators.MaxLengthValidator(200, 'عنوان وارد شده نمیتواند بیش از 200 کاراکتر باشد')
        ]
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'لطفا متن پیام خود را وارد کنید', 'class': 'form-control', 'required': "required",
                   'rows': 8}),
        label='متن پیام',
    )
