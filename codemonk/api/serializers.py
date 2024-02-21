from rest_framework import serializers
from .models import Paragraph, Word
from django.contrib.auth.models import User

class ParagraphSerializer(serializers.ModelSerializer):

  class Meta:
    model = Paragraph
    fields = '__all__'

class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = '__all__'



