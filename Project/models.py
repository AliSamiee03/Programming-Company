from django.db import models

class Project(models.Model):
    owner = models.ForeignKey('Account.User', on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=55)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title