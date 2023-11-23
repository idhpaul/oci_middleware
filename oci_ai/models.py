from django.db import models

# class CommonInfo(models.Model):

#     apiVersion = models.CharField(max_length=10)
#     user = models.JSONField()
#     timestamp = models.DateTimeField()

#     class Meta:
#         abstract = True

class TargetTranslate(models.Model):
    apiVersion = models.CharField(max_length=10)
    user = models.JSONField()
    timestamp = models.DateTimeField()
    data = models.JSONField()

    class Meta:
        managed = False

class ResultTranslate(models.Model):
    resultLanguageCode = models.CharField(max_length= 8)
    resultContent = models.TextField()

    class Meta:
        managed = False

class TranslateHistory(models.Model):
    timestamp = models.DateTimeField()
    userID = models.CharField(max_length= 100)
    userAppVersion = models.CharField(max_length= 10)
    beforeLanguageCode = models.CharField(max_length= 8)
    beforeContent = models.TextField()
    afterLanguageCode = models.CharField(max_length= 8)
    afterContent = models.TextField() 

class TargetTranscribe(models.Model):
    apiVersion = models.CharField(max_length=10)
    user = models.JSONField()
    timestamp = models.DateTimeField()
    data = models.JSONField()

    class Meta:
        managed = False

class StateTranscribe(models.Model):
    apiVersion = models.CharField(max_length=10)
    user = models.JSONField()
    timestamp = models.DateTimeField()
    data = models.JSONField()

    class Meta:
        managed = False

class Video(models.Model):
    url = models.TextField()
    thumbnailUrl = models.TextField()
    title = models.TextField()
    like_cnt = models.IntegerField(default=0)
    dislike_cnt = models.IntegerField(default=0)

    class Meta:
        managed = True
        
class VideoCaption(models.Model):
    languageCode = models.CharField(max_length= 8)
    caption = models.TextField()
    video = models.ForeignKey(Video, related_name='captions', on_delete=models.CASCADE)

    class Meta:
        managed = True
    
    #     def save(self, *args, **kwargs):
    #         super().save(*args, **kwargs)
    
    def __str__(self):
        return '%s:%s' % (self.languageCode, self.caption)
