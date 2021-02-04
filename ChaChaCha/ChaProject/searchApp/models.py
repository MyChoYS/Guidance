from django.db import models

class Academy(models.Model) :
    name = models.CharField(max_length=45)
    address_full = models.CharField(max_length=80)
    address_city = models.CharField(max_length=45)
    address_town = models.CharField(max_length=45)
    fee1 = models.IntegerField()
    fee2 = models.IntegerField()
    bus = models.TextField()
    url = models.TextField()
    phone_number = models.CharField(max_length=45)

    def __str__(self):
        return "main {}-{}-{}-{}-{}-{}-{}-{}-{}-{}".format(self.id, self.name, self.address_full, self.address_city,
                                                           self.address_town, self.fee1, self.fee2, self.bus, self.url,
                                                           self.phone_number)

class TestSite(models.Model) :
    name = models.CharField(max_length=45)
    address_full = models.CharField(max_length=45)
    courseA = models.CharField(max_length=80)
    courseB = models.CharField(max_length=80)
    courseC = models.CharField(max_length=80)
    courseD = models.CharField(max_length=80)
    url = models.TextField()
    phone_number = models.CharField(max_length=45)
