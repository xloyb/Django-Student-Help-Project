from django.urls import path
from .views import (
    ReactionListCreateAPIView, ReactionRetrieveUpdateDestroyAPIView,
    PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView,
    EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView,
    EvenClubListCreateAPIView, EvenClubRetrieveUpdateDestroyAPIView,
    EvenSocialListCreateAPIView, EvenSocialRetrieveUpdateDestroyAPIView,
    StageListCreateAPIView, StageRetrieveUpdateDestroyAPIView,
    LogementListCreateAPIView, LogementRetrieveUpdateDestroyAPIView,
    TransportListCreateAPIView, TransportRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('reactions/', ReactionListCreateAPIView.as_view(), name='reaction-list-create'),
    path('reactions/<int:pk>/', ReactionRetrieveUpdateDestroyAPIView.as_view(), name='reaction-detail'),
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
    path('even-clubs/', EvenClubListCreateAPIView.as_view(), name='even-club-list-create'),
    path('even-clubs/<int:pk>/', EvenClubRetrieveUpdateDestroyAPIView.as_view(), name='even-club-detail'),
    path('even-socials/', EvenSocialListCreateAPIView.as_view(), name='even-social-list-create'),
    path('even-socials/<int:pk>/', EvenSocialRetrieveUpdateDestroyAPIView.as_view(), name='even-social-detail'),
    path('stages/', StageListCreateAPIView.as_view(), name='stage-list-create'),
    path('stages/<int:pk>/', StageRetrieveUpdateDestroyAPIView.as_view(), name='stage-detail'),
    path('logements/', LogementListCreateAPIView.as_view(), name='logement-list-create'),
    path('logements/<int:pk>/', LogementRetrieveUpdateDestroyAPIView.as_view(), name='logement-detail'),
    path('transports/', TransportListCreateAPIView.as_view(), name='transport-list-create'),
    path('transports/<int:pk>/', TransportRetrieveUpdateDestroyAPIView.as_view(), name='transport-detail'),
]
