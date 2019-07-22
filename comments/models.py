# '''
# from django.db import models
# from django.conf import settings
# from recipes.models import Recipes
# '''
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.contrib.contenttypes.models import ContentType

# '''
# class Comment(models.Model):
#     user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
#     recipe      = models.ForeignKey(Recipes, on_delete=models.DO_NOTHING)
#     content     = models.TextField()
#     timestamp   = models.DateTimeField(auto_now_add=True)

#     def __unicode__(self):
#         return str(self.user.username)

#     def __str__(self):
#         return str(self.user.username)
# '''


# class Comment(models.Model):
#     user        = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.DO_NOTHING)
#     #recipe      = models.ForeignKey(Recipes, on_delete=models.DO_NOTHING)

#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

#     content     = models.TextField()
#     timestamp   = models.DateTimeField(auto_now_add=True)

#     def __unicode__(self):
#         return str(self.user.username)

#     def __str__(self):
#         return str(self.user.username)
