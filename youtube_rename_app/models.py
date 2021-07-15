from django.db import models

# Create your models here.


class Name_Update_Request(models.Model):
    start_date_time = models.DateTimeField()
    status = models.CharField(max_length=10)
    

    def start_update(self):
        self.status= 'processing'
        self.save()