from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=250)
    user_name = models.CharField(max_length=250, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    street = models.CharField(max_length=250, null = True, blank = True)
    suite = models.CharField(max_length=250, null = True, blank = True)
    city = models.CharField(max_length=250, null = True, blank = True)
    zipcode = models.CharField(max_length=250, null = True, blank = True)
    geo_lat = models.FloatField(null = True, blank = True)
    geo_lng = models.FloatField(null = True, blank = True)
    phone = models.CharField(max_length=250, null = True, blank = True)
    website = models.CharField(max_length=250, null = True, blank = True)
    company_name = models.CharField(max_length=250, null = True, blank = True)
    company_catchPhrase = models.CharField(max_length=250, null = True, blank = True)
    company_bs = models.CharField(max_length=250, null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.name)
