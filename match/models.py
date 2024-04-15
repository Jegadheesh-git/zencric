from django.db import models
from player.models import Player

class Tournament(models.Model):
    name = models.CharField(max_length=250)

class MatchType(models.Model):
    name = models.CharField(max_length=250)

class Team(models.Model):
    name = models.CharField(max_length=250)
    players = models.ManyToManyField(Player, related_name='teams')
    # Squad details
    squadA = models.ManyToManyField(Player, related_name='matches_squadA')
    squadB = models.ManyToManyField(Player, related_name='matches_squadB')

class Competition(models.Model):
    name = models.CharField(max_length=250)
    displayName = models.CharField(max_length=250)
    year = models.IntegerField()
    matchType = models.ForeignKey(MatchType,on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    fromDate = models.DateField()
    toDate = models.DateField()
    matchCount = models.IntegerField()
    isWarmUp = models.BooleanField()
    gender = models.CharField(max_length=15,choices=(('Male','Male'),('Female','Female'),('Third gender','Third gender')))
    teams = models.ManyToManyField(Team)

class Stadium(models.Model):
    name = models.CharField(max_length=250)

class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateField()
    over = models.CharField(max_length=15, choices=(('Limited', 'Limited'), ('Un-Limited', 'Un-Limited')))
    numberOfOvers = models.IntegerField()
    inningsCount = models.IntegerField()
    dayOrNight = models.CharField(max_length=15, choices=(('Day', 'Day'), ('Night', 'Night'), ('DayNight', 'DayNight')))
    teamA = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_teamA')
    teamB = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_teamB')
    knockout_choices = (
        ('League', 'League'),
        ('Quarter Final', 'Quarter Final'),
        ('Semi Final', 'Semi Final'),
        ('Final', 'Final'),
        ('Others', 'Others'),
        ('Qualifier', 'Qualifier'),
        ('Eliminator', 'Eliminator'),
        ('Super Four', 'Super Four'),
        ('Third Place', 'Third Place'),
    )
    
    knockout = models.CharField(max_length=25, choices=knockout_choices)

    # Toss details
    tossWonBy = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_toss_won_by')
    option = models.CharField(max_length=15, choices=(('Batting', 'Batting'), ('Fielding', 'Fielding')))
    first = models.CharField(max_length=15, choices=(('Day', 'Day'), ('Under Lights', 'Under Lights')))
    second = models.CharField(max_length=25, choices=(('Day', 'Day'), ('Under Lights', 'Under Lights')))


    # Playing 11 details
    playingA = models.ManyToManyField(Player, related_name='matches_playingA')
    playingB = models.ManyToManyField(Player, related_name='matches_playingB')
    captainA = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_captainA')
    wicketKeeperA = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_wicket_keeperA')
    captainB = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_captainB')
    wicketKeeperB = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_wicket_keeperB')



