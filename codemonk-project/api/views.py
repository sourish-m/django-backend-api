# views.py

from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


from .serializers import ParagraphSerializer
from .models import Paragraph, Word, User
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

from django.db.models import Count


class ParagraphSplitView(GenericAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def post(self, request):

    text = request.data.get('text')

    # Split text into paragraphs
    paragraphs = text.split('\n\n')  

    # Save paragraphs and words
    for paragraph in paragraphs:
      p = Paragraph.objects.create(text=paragraph)
      words = paragraph.split(' ')
      for word in words:
        Word.objects.create(word=word.lower(), paragraph=p)

    return Response("Text saved successfully")

class WordSearchView(GenericAPIView):
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]


  def get(self, request):

    word = request.query_params.get('word')

    # Using Django Count model for sorting paragraphs by word count
    paragraphs = Paragraph.objects.annotate(
      word_count=Count('word')).filter( word__word=word).order_by('-word_count')[:10]

    serializer = ParagraphSerializer(paragraphs, many=True)

    return Response(serializer.data)

  
class RegisterView(APIView):

    def post(self, request):
        
        username = request.data['username']
        email=request.data['email']
        dob=request.data.get('date_of_birth')
        user = User.objects.create(username=username,password=(request.data['password']),email=email,date_of_birth=dob)

        print("user is ",user) # check user is saved

        token = Token.objects.create(user=user)
        print("token is ",token)

        return Response({'token': token.key})