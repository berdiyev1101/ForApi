from rest_framework import serializers
from library.models import *

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title','author','subtitle','isbn']
