from rest_framework import serializers

from oci_ai.models import TargetTranslate, ResultTranslate, TranslateHistory

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

