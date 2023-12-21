from django import  forms
from  django.core import validators 
# def start_with_d(value):
#   if value.isalpha!=True:
#     raise forms.ValidationError('name should contains only alphabet symbols')
# def gmail_verification(value):
#    if value[len(value)-9:]!='gmail.com':
#       raise forms.ValidationError('must be gmail')  
   
class feedbackform(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='password(Again)',widget=forms.PasswordInput)
    feedback=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        cleaned_data = super().clean()
        inputpwd = cleaned_data['password']
        inputrpwd = cleaned_data['rpassword']  # Assuming you have a repeat_password field
        print("Hello man =========================================")
        print("cleaned_data testing::::::::::::::::::::::::::::::",cleaned_data)
        # Uncomment the following lines if you want to check if passwords match
        if inputpwd != inputrpwd:
            raise forms.ValidationError('Passwords do not match')

        name = cleaned_data.get('name') # Replace with your actual field name
        print("Name====================",name)
        if len(name)==0:
            raise forms.ValidationError('Name is required')
        return cleaned_data