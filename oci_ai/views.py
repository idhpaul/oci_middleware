from django.http import HttpRequest
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from oci_ai.models import TranslateHistory
from oci_ai.serialize import ResultTranslateSerializer, TargetTranslateSerializer, TranslateHistorySerializer
from oci_ai.oci_language.pretrained_model_translate import runLanguageModel

from core.util import convert_ISO3166_to_ISO639

@api_view(['POST'])
def translate(request:HttpRequest):

    targetTranslate = TargetTranslateSerializer(data=request.data)

    targetTranslate.is_valid(raise_exception=True)

    print("start translate")
    result_translate = runLanguageModel(targetTranslate.data['data']['content'],
                        source_language_code=convert_ISO3166_to_ISO639(targetTranslate.data['data']['sourceLanguageCode']),
                        target_language_code=convert_ISO3166_to_ISO639(targetTranslate.data['data']['targetLanguageCode']))
    print("end translate")
    
    history = TranslateHistorySerializer(data={
        "timestamp" : request.data['timestamp'],
        "userID" : targetTranslate.data['user']['userID'],
        "userAppVersion" : targetTranslate.data['user']['userAppVersion'],
        "beforeLanguageCode" : targetTranslate.data['data']['sourceLanguageCode'],
        "beforeContent" : targetTranslate.data['data']['content'],
        "afterLanguageCode" : targetTranslate.data['data']['targetLanguageCode'],
        "afterContent" : result_translate
    })
    history.is_valid(raise_exception=True)
    history.save()

    return Response(data={
        "resultLanguageCode" : targetTranslate.data['data']['targetLanguageCode'],
        "resultContent" : result_translate
    })

    