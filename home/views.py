from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect
import random


from django.views.generic import View, DetailView
from rest_framework import viewsets

from .models import *  #import all models classes with * sign

# Create your views here.
from .serializers import ItemSerializers, CategorySerializers, SubcategorySerializers


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


@login_required
def cart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        quantity = Cart.objects.get(slug =slug).quantity
        quantity = quantity+1
        Cart.objects.filter(slug=slug).update(quantity=quantity)
    else:
        username = request.user
        data = Cart.objects.create(
            user = username,
            slug = slug
        )
        data.save()
    return redirect('home:mycart')

def deletecart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        Cart.objects.filter(slug=slug).delete()
    return redirect('home:mycart')

def removecart(request,slug):
    if Cart.objects.filter(slug =slug).exists():
        quantity = Cart.objects.get(slug =slug).quantity
        quantity = quantity-1
        Cart.objects.filter(slug=slug).update(quantity=quantity)
    return redirect('home:mycart')


class CartView(BaseView):
   def get(self,request):
       self.view['slugs'] = Cart.objects.filter(checkout = False,user=request.user)
       # self.view['cart_items'] = Item.objects.all()
       return render(request, 'cart.html',self.view)


class ContactView(BaseView):
    def get(self,request):

        return  render(request,'contact.html',self.view)

def contact_action(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POST['Message']
        contact_id = random.randint(0,999999)


        data= Contact.objects.create(
            name=name,
            email=email,
            message= message,
            contact_id= contact_id,


        )

        data.save()
        send_email = EmailMessage(
        'Contact your Store',
        f'hello admin {name} is trying to contact .His mail is {email}. His message is {message}',email,'sureshdgl100@gmail.com',
        )
        send_email.send()
        message.sucess(request,'Mail has been Sent')
        return  redirect('home:contact')


#msg = EmailMessage(subject,html,content,from_email, [to])
#msg.content_subtye ="html"
#msg.send()

#API Section
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializers
