from django.db import models
from match.models import Match,Team
from player.models import Player

class DeliveryType(models.Model):
    name = models.CharField(max_length=25)

class CreaseMovement(models.Model):
    name = models.CharField(max_length=25)

class ShotConnection(models.Model):
    name = models.CharField(max_length=25)

class BatSubject(models.Model):
    name = models.CharField(max_length=25)

class Stroke(models.Model):
    name = models.CharField(max_length=25)

class Keeper(models.Model):
    name = models.CharField(max_length=25)

class Batsman(models.Model):
    name = models.CharField(max_length=25)

class Fielding(models.Model):
    name = models.CharField(max_length=25)

class Umpire(models.Model):
    name = models.CharField(max_length=25)

class DismissalType(models.Model):
    name = models.CharField(max_length=25)

class Ball(models.Model):
    over = models.IntegerField()
    ballOver = models.FloatField() 
    matchId = models.ForeignKey(Match,on_delete=models.CASCADE)
    innings = models.IntegerField()
    battingTeam = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='balls_battingTeam')
    bowlingTeam = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='balls_bowlingTeam')
    striker = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_striker')
    nonStriker = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='ball_nonStriker')
    bowler = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_bowler')
    runs = models.IntegerField()
    extras = models.IntegerField()
    penalty = models.IntegerField()
    overThrow = models.IntegerField()
    ballSpeed = models.FloatField()
    batSpeed = models.FloatField()
    ballSpeedMetric = models.CharField(max_length=15, choices=(('KPH', 'KPH'), ('MPH', 'MPH')))
    swingLength = models.FloatField()
    fielder1 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_fielder1')
    fielder2 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_fielder2')
    isBoundary = models.BooleanField()
    isNoBall = models.BooleanField()
    isFreeHit = models.BooleanField()
    shotZone = models.IntegerField()
    wagonWheel = models.IntegerField()
    ffData = models.IntegerField()
    ballRelease = models.IntegerField()
    deliveryType = models.ForeignKey(DeliveryType,on_delete=models.CASCADE)
    creaseMovement = models.ForeignKey(CreaseMovement,on_delete=models.CASCADE)
    shotConnection = models.ForeignKey(ShotConnection,on_delete=models.CASCADE)
    batSubject = models.ForeignKey(BatSubject,on_delete=models.CASCADE)
    stroke = models.ForeignKey(Stroke,on_delete=models.CASCADE)
    keeper = models.ForeignKey(Keeper,on_delete=models.CASCADE)
    batsman = models.ForeignKey(Batsman,on_delete=models.CASCADE)
    fielding = models.ForeignKey(Fielding,on_delete=models.CASCADE)
    umpire = models.ForeignKey(Umpire,on_delete=models.CASCADE)


