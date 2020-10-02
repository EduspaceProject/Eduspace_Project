from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from ..models.user import user_login
from django.contrib.auth.hashers import check_password
class Login(View):
    return_url=None
    def get(self,request):
        Login.return_url=request.GET.get('return_url')
        return render(request, 'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        user = user_login.get_user_by_email(email)
        #print("user",user)
        error_message = None
        if user:
            flag = check_password(password,user.password)
            if flag:
                request.session['customer'] = user.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'


        return render(request, 'login.html', {'error': error_message})

