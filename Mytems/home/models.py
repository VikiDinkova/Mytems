from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/images')
    brand = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    defloration_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField()


class Favourite(models.Model):
    pass


class Clothes(models.Model):
    MALE = 1
    FEMALE = 2

    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    SEASON_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (AUTUMN, 'Autumn'),
        (WINTER, 'Winter'),
    )

    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='media/images')
    gender = models.IntegerField(choices=GENDER_CHOICES)
    seasons = models.IntegerField(choices=SEASON_CHOICES)
    description = models.TextField()
    color = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class TechAccessory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/images')
    for_tech = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images')
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    location = models.CharField(max_length=100)


class List(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
    tech = models.ManyToManyField(TechAccessory)
    meds = models.ManyToManyField(Drug)
    clothes = models.ManyToManyField(Clothes)


class LendEvent(models.Model):
    person = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
    tech = models.ManyToManyField(TechAccessory)
    meds = models.ManyToManyField(Drug)
    clothes = models.ManyToManyField(Clothes)
    lend_start = models.DateField()
    lend_end = models.DateField()


class ClothesUse(models.Model):
    clothes = models.ForeignKey(Clothes)
    date = models.DateField(auto_now_add=True)


class TechUse(models.Model):
    tech = models.ForeignKey(TechAccessory)
    date = models.DateField(auto_now_add=True)
