from django.shortcuts import render
#from app2.models import User
from app2.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'app2/index.html')

def users(request):
    #user_list = User.objects.order_by('first_name')
    #user_dict = {'users' : user_list}
    #return render(request,'app2/users.html',context=user_dict)

    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR, form invalid')

    return render(request, 'app2/users.html',{'form':form})
