from django.shortcuts import render
from django.views.generic import View
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








