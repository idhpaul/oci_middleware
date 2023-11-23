from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns

from oci_ai import views

video = views.VideoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
video_detail = views.VideoViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})
video_captions = views.VideoCaptionViewSet.as_view({
    'post': 'create',
    'get': 'list',
})
video_caption_detail = views.VideoCaptionViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

urlpatterns = [
    #path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    #path('', views.api_root),

    # 127.0.0.1/ai/translate (OK)
    # 127.0.0.1/ai/translate/ (Failed)
    path('translate', views.translate, name="Translate"),
    path('transcribe', views.transcribe, name="Transcribe"),
    path('video/', video, name="Video"),
    path('video/<int:pk>/', video_detail, name='VideoDetail'),
    path('video/<int:pk>/captions', video_captions, name='VideoCaptions'),
    path('video/<int:pk>/caption', video_caption_detail, name='VideoCaptionDetail'),

    # url 제한을 시킬 수 있음(오류 방지) -> ex) 2000년 이후만 받도록 
    # /snippets/page, /snippets/pages 한번에 사용 가능
    # 일반적으로는 path("pages/", views.test), path("page/", vews.test) 두 개를 작성해야함
    #re_path(r"^pages?/$", views.test)
]
urlpatterns = format_suffix_patterns(urlpatterns)