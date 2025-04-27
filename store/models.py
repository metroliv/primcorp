from django.db import models

class System(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='systems/', null=True, blank=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='services/', null=True, blank=True)

    def __str__(self):
        return self.title
