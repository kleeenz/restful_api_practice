from rest_framework import generics
from .models import polls, Choice
from .serializers import pollsSerializer

class PollList(generics.ListCreateAPIView):
    queryset = polls.objects.all()
    serializer_class = pollsSerializer

class PollDetails(generics.RetrieveDestroyAPIView):
    queryset = polls.objects.all()
    serializer_class = pollsSerializer


