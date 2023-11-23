from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status, viewsets
from rest_framework.response import Response
from oci_ai.models import Video, VideoCaption

from oci_ai.serialize import StateTranscribeSerializer, TargetTranscribeSerializer, TargetTranslateSerializer, TranslateHistorySerializer, VideoCaptionViewSerializer, VideoViewGetSerializer, VideoViewPostSerializer
from oci_ai.oci_speech.pretrained_model_transcription import getTrnascriptionJob, runSpeechModel
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

@api_view(['POST','GET'])
def transcribe(request:HttpRequest):

    if request.method == 'POST':
        targetTransscribe = TargetTranscribeSerializer(data=request.data)

        targetTransscribe.is_valid(raise_exception=True)

        print("start transcirbe")
        result_transcribe = runSpeechModel(targetTransscribe.data['data']['objectName'])
        print("end transcirbe")
        
        # history = TranslateHistorySerializer(data={
        #     "timestamp" : request.data['timestamp'],
        #     "userID" : targetTranslate.data['user']['userID'],
        #     "userAppVersion" : targetTranslate.data['user']['userAppVersion'],
        #     "beforeLanguageCode" : targetTranslate.data['data']['sourceLanguageCode'],
        #     "beforeContent" : targetTranslate.data['data']['content'],
        #     "afterLanguageCode" : targetTranslate.data['data']['targetLanguageCode'],
        #     "afterContent" : result_translate
        # })
        # history.is_valid(raise_exception=True)
        # history.save()

        return Response(data={
            "resultTranscribeID" : result_transcribe,
        })
    else:
        stateTranslate = StateTranscribeSerializer(data=request.data)

        stateTranslate.is_valid(raise_exception=True)

        print("start translate state")
        result_state_translate = getTrnascriptionJob(stateTranslate.data['data']['transcribeJobID'])
        print("end ranslate state")
        
        return Response(data={
            "resultTranscribeState" : result_state_translate
        })

class VideoViewSet(viewsets.ModelViewSet):

    queryset = Video.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return VideoViewPostSerializer
        if self.action == "retrieve":
            return VideoViewGetSerializer
        return VideoViewGetSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data['data'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request): 
        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        video = self.get_object()
        serializer = self.get_serializer(video)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

class VideoCaptionViewSet(viewsets.ModelViewSet):

    serializer_class = VideoCaptionViewSerializer

    def create(self, request, pk, *args, **kwargs):
        serializer = self.get_serializer(data={
            "languageCode" : request.data['data']['languageCode'],
            "caption" : request.data['data']['caption'],
            "video" : pk
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, pk): 
        queryset = VideoCaption.objects.filter(video=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        video = self.get_object()
        serializer = self.get_serializer(video)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()