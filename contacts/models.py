from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    phone = models.IntegerField(verbose_name='شماره تماس')
    job = models.CharField(max_length=50, verbose_name='شغل')
    education = models.CharField(max_length=20, verbose_name='تحصیلات')

    def __str__(self):
        return self.first_name
