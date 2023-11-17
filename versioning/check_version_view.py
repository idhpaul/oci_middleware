from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import resolve, reverse

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from versioning import versions

class SpecifyVersionSerializer(serializers.Serializer):
   device_platform = serializers.CharField(max_length= 50)
   app_version = serializers.CharField(max_length= 50)

@api_view(['GET'])
def checkVersion(request:HttpRequest):

    serializer = SpecifyVersionSerializer(data=request.data)
    if serializer.is_valid():

        # Specify the version to use for the client 
        print(serializer.data)
        print(versions.VERSION_1)

        return Response(data={
            "api_version" : versions.VERSION_1.base_version,
            "api_version_note" : versions.VERSION_1.notes,

            "client_info" : {
                "device_platform" : serializer.data['device_platform'],
                "app_version" : serializer.data['app_version']
            }
        })
    else:
        print(serializer.error_messages)
        return redirect("/version")

    