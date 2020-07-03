from django.db import models
from django.db.models import Model

# Create your models here.
class StartseiteSektion(models.Model):
    class Meta:
        verbose_name_plural = 'Startseite Sektionen'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class BannerBild(models.Model):
    startseite_sektion = models.ForeignKey('StartseiteSektion', null=True, blank=True, on_delete=models.SET_NULL)
    bild = models.ImageField(null=False, blank=False)
    banner_titel = models.CharField(max_length=50, null=False, blank=False, default='')
    banner_beschreibung = models.CharField(max_length=254, null=False, blank=False, default='')
    call_to_action_button = models.CharField(max_length=50, null=False, blank=False, default='')

class SpielTabelle(models.Model):
    startseite_sektion = models.ForeignKey('StartseiteSektion', null=True, blank=True, on_delete=models.SET_NULL)
    teams = models.CharField(max_length=60, null=True, blank=True)
    ort = models.CharField(max_length=100, null=True, blank=True)
    datum = models.DateField(null=False, blank=False, default='')

    class Meta:
        verbose_name_plural = 'Spiel Tabelle Reihen'

class Empfehlung(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    okkupation = models.CharField(max_length=60, null=False, blank=False)
    empfehlung_profil_bild = models.ImageField(null=False, blank=False)

class Karte(models.Model):
    karten_bild = models.CharField(max_length=254, null=False, blank=False)
    karten_titel = models.CharField(max_length=40, null=False, blank=False)
    karten_beschreibung = models.CharField(max_length=254, null=False, blank=False)
    karten_knopf = models.CharField(max_length=20, null=False, blank=False)
 
class NewsLink(models.Model):
    news_link_title = models.CharField(max_length=40, null=False, blank=False)
    link_image = models.ImageField(null=False, blank=False)
