from rest_framework import generics
from core.models import Post, Logement, Transport, Stage, Evenement
from .serializers import PostSerializer, LogementSerializer, TransportSerializer, StageSerializer, EvenementSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LogementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer

class LogementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer

class TransportListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class TransportRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer

class StageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class StageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class EvenementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer

class EvenementRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
