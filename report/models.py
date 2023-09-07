from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=11)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


LEVEL = [
    ('1a', '1A'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('4a', '4А'),
    ('4b', '4Б'),
    ('5a', '5А'),
    ('5b', '5Б'),
]


class Mount(models.Model):
    winter = models.CharField(max_length=2, choices=LEVEL)
    summer = models.CharField(max_length=2, choices=LEVEL)
    autumn = models.CharField(max_length=2, choices=LEVEL)
    spring = models.CharField(max_length=2, choices=LEVEL)
    beautyTitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)


class Photo(models.Model):
    mount = models.ForeignKey(Mount, on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

