from django.contrib.auth.models import User
from .models import slider,Items,Category,Subcategory,ad,Contact
from rest_framework import serializers


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ['title','description','slug','image','label']



class ItemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Items
        fields = ['title','slug','price','discounted_price','status','stock','image','category','subcategory']