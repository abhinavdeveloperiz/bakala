from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
    

class gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return f"Gallery Image {self.id}"
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/',null=True, blank=True)

    def __str__(self):
        return self.name