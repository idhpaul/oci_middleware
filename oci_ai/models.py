from django.db import models

# Create your models here.

# before translate model
#   not to need db model

# after translate model
#   not to need db model


# mix it 'before translate model' and 'after translate model' then commit to db
class TranslateHistory(models.Model):
    timestamp = models.DateTimeField()
    user_id = models.CharField(max_length= 100)
    user_app_version = models.CharField(max_length= 100)
    before_language_code = models.CharField(max_length= 8)
    before_content = models.TextField()
    after_language_code = models.CharField(max_length= 8)
    after_content = models.TextField()

    class Meta:
        ordering = ['timestamp']

# class User(models.Model):
#     id = models.BigIntegerField(primary_key=True, auto_created=True)
#     email = models.CharField(max_length=45)
#     password = models.CharField(max_length=45, db_column='pass')
#     isPurchace = models.IntegerField()

#     class Meta:
#         managed = False
#         app_label = "service"
#         db_table = 'test_user'


# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#     language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
#     style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

#     owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
#     highlighted = models.TextField()

#     class Meta:
#         ordering = ['created']

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)