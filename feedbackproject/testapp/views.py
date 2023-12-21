from django.shortcuts import render
from .import forms
# Create your views here.

def feedback_view(request):
   if request.method=='GET':
   #  form=forms.feedbackform()
   #  return render(request,'testapp/feedback.html',{'form':form})
    form=forms.feedbackform()
    return render(request,'testapp/feedback.html',{'forms':form})

   if request.method=='POST':
      form=forms.feedbackform(request.POST)
      if form.is_valid():
         print('form validation sucess and printing info')
         print('student name:',form.cleaned_data['name'])
         print('student Roll Number:',form.cleaned_data['rollno'])
         print('student email id:',form.cleaned_data['email'])
         print('student feedback:',form.cleaned_data['feedback'])
         return render(request,'testapp/thanku.html',{'name':form.cleaned_data['name']})
   return render(request,'testapp/feedback.html',{'forms':form})