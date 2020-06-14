from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect


from django.views.generic import View, DetailView
from .models import *  #import all models classes with * sign

# Create your views here.
class BaseView(View):
    view={}


class HomeView(BaseView):
    def get(self,request):
        self.view['items'] = Items.objects.all()
        self.view['special_items'] = Items.objects.filter(labels ='special').reverse()[0:12]
        self.view['sliders']= slider.objects.all()
        self.view['category'] = Category.objects.all()
        self.view['subcategory'] = Subcategory.objects.all()
        self.view['add_one']=ad.objects.filter(rank=1)
        self.view['add_second'] = ad.objects.filter(rank=2)
        self.view['add_third'] = ad.objects.filter(rank=3)
        self.view['add_forth'] = ad.objects.filter(rank=4)
        self.view['special_subcat']=Subcategory.objects.filter(labels='special')

        return render(self.request,'index.html',self.view)


class ItemDetailView(DetailView):
    model = 'Item'
    template_name ='single.html'


class SubCategory(BaseView):
    def get(self,id):
        self.view['subcat_items'] = Items.objects.filter(subcategory_id = id)#1slug  value from database and other from
        return render(self.request, 'kitchen.html', self.view)



class SearchView(BaseView):
    def get(self,request):
        query=request.GET.get('query',None)
        if not query:
            return redirect('/')

        self.view['search_query']=Items.objects.filter(title__icontains = query)
        return  render(request,'search_product.html',self.view)



def signup(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['confirm Password']

        if password == cpassword:
            if User.objects.filter(username=username).exists():  #User and exists are django fucntion exists it checks the name is on db or not
                messages.error(request,'The username already exists')
                return render(request,'register.html')

            elif User.objects.filter(email=email).exists():  #User and exists are django fucntion exists it checks the name is on db or not
                messages.error(request,'The email already exists')
                return redirect('/signup')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password

                )

                user.save()
                messages.success(request,'You are registered')
                return render(request,'register.html')

        else:
            messages.success(request, 'Password do not match')
            return render(request,'register.html')

    return render(request,'register.html')


