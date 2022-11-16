from django.shortcuts import render,HttpResponseRedirect
from .forms import EditDashboad,EditAdminDashborad
from .forms import SigninForm,Contact
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User, Group
from .models import Bhagavan


from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def signing(request):
    if request.method=="POST":
        fm=SigninForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!') 
            user=fm.save()
            group = Group.objects.get(name='Editor')
            user.groups.add(group)
    else:
        fm=SigninForm()

    return render(request,'sign.html',{'form':fm})

def loging(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                pwd=fm.cleaned_data['password']
                user = authenticate(username=uname,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.info(request, 'Logged in successfully !!')
                    return render(request, 'dashborad.html')
        else:
            fm=AuthenticationForm()
        return render(request, 'login.html', {'form':fm})
    return render(request, 'dashborad.html',)



def contating(request):
    if request.method =='POST':
        rm=Contact(request.POST)
        if rm.is_valid():
            rm.save()

    else:
        rm=Contact()
    return render(request,'contact.html',{'form' : rm})

def lout(request):
    logout(request)
    return render(request,'login.html')

def showdashbord(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            rm=EditDashboad(request.POST)
            if rm.is_valid():
                rm.save()
                messages.info(request, 'Now You can add blog deatils !!!')
        rm=EditDashboad()
        posts = EditDashboad.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        ip = request.session.get('ip')
        return render(request, 'ojas/dashboard.html', {'posts':posts, 'full_name':full_name, 'groups':gps, 'ip':ip})
            #rm=EditDashboad.objects.all()
        return render(request, 'dashborad.html', {'name':request.user.username,'form':rm})
    else:
        return HttpResponseRedirect('ojas/showdashbord')

# def add_blog(request):
#     if request.method == 'POST':
#         form = EditDashboad(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('home')
#     form = EditDashboad()
#     return render(request, 'dashborad.html', {'form': form})    

# def EditUserProfileForm(request):
#     if request.method == 'POST':
#         fm = Bhagavan(request.POST)
#         if fm.is_valid():
#             nm = fm.cleaned_data['heading']
#             pp = fm.cleaned_data['paragram']
#             reg = Bhagavan(heading=nm, paragram=pp)
#             reg.save()
#             messages.info(request, 'Now You can add blog deatils !!!')
#             fm = Bhagavan()
#             return render(request,"adding.html",{'form':fm,'ram':ram})

#     else:
#         fm = Bhagavan()
#     ram = Bhagavan.objects.all()
            
#     return render(request,"adding.html",{'form':fm,'ram':ram})


def add_blog(request):
    if request.method == 'POST':
        fm=EditDashboad(request.POST)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('home')
        
    else:
        fm=EditDashboad()
    ram=Bhagavan.objects.all()
    return render(request,'adding.html',{'form':ram})

def detialsform(request):
    if request.method == 'POST':
        fm = EditDashboad(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['heading']
            pp = fm.cleaned_data['paragram']
            reg = Bhagavan(heading=nm, paragram=pp)
            reg.save()
            messages.info(request, 'Now You can add blog deatils !!!')
            return render(request,'adding.html')
    else:
        fm = EditDashboad()
    ram = Bhagavan.objects.all()
            
    return render(request,"adding.html",{'form':fm,'ram':ram})
def deletedata(request, id):
    if request.method == 'POST':
        pi = Bhagavan.objects.get(pk=id)
        pi.delete()
    return render(request,'adding.html')

def updatedata(request,id):
    if request.method == 'POST':
        pi = Bhagavan.objects.get(pk=id)
        fm = EditDashboad(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm=EditDashboad()
    else:
        pi = Bhagavan.objects.get(pk=id)
        fm = EditDashboad(instance=pi)

    return render(request,"update.html",{'form':fm})



# def edite(request, id):
#     fm=blog.objects.get(pk=id)
#     form=blogform(instance=fm)
#     if request.method=='POST':
#         form=blogform(request.POST,instance=fm)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect('/home')
#     else:
#         return render(request,'edit.html',{'form':form})


# def practice(request):
#     add_blog = Bhagavan(roll=112, city='Bokaro', marks=60)​
#     add_blog.save(force_insert=True)
#     add_blog = Bhagavan.objects.create(name='Sameer', roll=112, city='Bokaro', marks=60, pass_date='2020-5-4')
#     add_blog, created = Bhagavan.objects.get_or_create(name='Sameer', roll=112, city='Bokaro', marks=60, pass_date='2020-5-4')​
#     print(add_blog, created)​
#     return render('practice.html')