from django.urls import path
from . apiviews import PollList, PollDetails


urlpatterns = [
    path('polls/', PollList.as_view(), name = 'polls_list'),
    path('polls/<int:pk>/', PollDetails.as_view(), name = 'polls_details')
]