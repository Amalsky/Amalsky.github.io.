from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import  messages
from .user_form import User_Reg,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request,f'you are account has been updated !')

           return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)




def register(request):
    if request.method=='POST':
        forms=User_Reg(request.POST)
        if forms.is_valid():
            forms.save()
            user=forms.cleaned_data.get('username')
            messages.success(request,f'Congratulations! Your registration was successful {user}. Please login !')
            return redirect('login')
    else:
        forms=User_Reg()
    return render(request,'users/register.html',{'form':forms})
