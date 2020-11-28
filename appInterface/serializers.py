from rest_framework import serializers
from . models import polls, Choice, vote

class voteSerializer(serializers.ModelSerializer):
    class Meta:
        model = vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    votes = voteSerializer(many=True, required=False)
    class Meta:
        model = Choice
        fields = '__all__'


class pollsSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = polls
        fields = '__all__'