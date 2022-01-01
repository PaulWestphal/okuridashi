from django.db import models

class Rikishi(models.Model):
    home = models.CharField(max_length=200)
    birth_date = models.DateField()
    real_name = models.CharField(max_length=200)

class Banzuke(models.Model):
    date = models.DateField()
    basho_location = models.CharField(max_length=200)

class TournamentDay(models.Model):
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)
    date = models.DateField()
    number = models.IntegerField()

class Shikona(models.Model):
    rikishi = models.ForeignKey(Rikishi, on_delete=models.CASCADE)
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)
    shikona = models.CharField(max_length=200)

class Rank(models.Model):
    rikishi = models.ForeignKey(Rikishi, on_delete=models.CASCADE)
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)
    rank_name = models.CharField(max_length=100)
    rank_number = models.IntegerField()
    rank_direction =  models.CharField(max_length=50)

class Measurement(models.Model):
    rikishi = models.ForeignKey(Rikishi, on_delete=models.CASCADE)
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()

class Heya(models.Model):
    rikishi = models.ForeignKey(Rikishi, on_delete=models.CASCADE)
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)
    heya_name = models.CharField(max_length=200)

class Retirement(models.Model):
    rikishi = models.ForeignKey(Rikishi, on_delete=models.CASCADE)
    banzuke = models.ForeignKey(Banzuke, on_delete=models.CASCADE)

class Bout(models.Model):
    day = models.ForeignKey(TournamentDay, on_delete=models.CASCADE)
    east = models.ForeignKey(Rikishi, on_delete=models.CASCADE, related_name='rikishi_east')
    west = models.ForeignKey(Rikishi, on_delete=models.CASCADE, related_name='rikishi_west')
    winner = models.ForeignKey(Rikishi, on_delete=models.CASCADE, related_name='winner')
    kimarite = models.CharField(max_length=200)
