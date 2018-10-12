from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm

form_class = UserForm()
template_name = "lms/login.html"

#class UserForm():

    #display a blank form
def get(self, request):
    form = self.form_class(None)
        

    #process form data
def post(self, request):
    form = self.form_class(request.POST)
    
    if form.is_valid():

            user = form.save(commit=False)

            #cleaned normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('lms/home.html')
                return render(request, self.template_name,{'form':form})

              