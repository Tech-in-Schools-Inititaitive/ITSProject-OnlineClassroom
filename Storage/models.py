from django.conf import settings
from django.db import models

# Create your models here.

def userDocumentUploadPath(filename, instance):
	return 'Storage/{0}_{1}'.format(instance.user_account.user.username, instance.user_account.user.email, filename)

class UploadDocument(models.Model):
	fileName = models.CharField(max_length=500, null=True, blank=True)
	document = models.FileField(upload_to=userDocumentUploadPath, null=True, blank=True)
	limit = models.IntegerField(default=settings.DEFAULT_STORAGE_LIMIT)
	uploaded_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.fileName) + '->' + str(self.uploaded_on)


class Storage(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_storage')
	allDocuments = models.ManyToManyField(UploadDocument, related_name='user_account')
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.user.email) + '->' + str(self.created_date)
