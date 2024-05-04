from rest_framework import serializers
from core.models import Reaction, Post, Event, EvenClub, EvenSocial, Stage, Logement, Transport

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class EvenClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenClub
        fields = '__all__'

class EvenSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvenSocial
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'

class LogementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logement
        fields = '__all__'

class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'
