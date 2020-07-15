from rest_framework import serializers
from .models import Query

class QuerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = '__all__'
