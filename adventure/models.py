from django.db import models
from nanoid import generate

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="static/images/", null=True, blank=True)

    def __str__(self):
        return self.name

class Choice(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="choices")
    text = models.CharField(max_length=255)
    next_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    health_modify = models.IntegerField(default=0)
    def __str__(self):
        return f"From {self.location.name}: {self.text}"

class PlayerStatus(models.Model):
    player_id = models.CharField(
        max_length=10, 
        unique=True, 
        default=lambda: generate(size=10)
    )
    current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    health = models.IntegerField(default=100)
    items = models.JSONField(default=list)

    def __str__(self):
        return f"Player {self.player_id} - Health: {self.health}"

class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
