from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.serializers import ModelSerializer

from oci_ai.models import StateTranscribe, TargetTranscribe, TargetTranslate, ResultTranslate, TranslateHistory, Video

class TargetTranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TargetTranslate
        fields = '__all__'

class ResultTranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultTranslate
        fields = '__all__'

class TranslateHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslateHistory
        fields = '__all__'

class TargetTranscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TargetTranscribe
        fields = '__all__'

class StateTranscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StateTranscribe
        fields = '__all__'


class VideoViewGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class VideoViewPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ("id", "url", "thumbnailUrl", "title")
