# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    c = (
        ("M", "Male"), ("F", "Female")
    )
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    gender = models.CharField(max_length=150,choices=c)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Fourations(models.Model):
    a = (
        ('nonel', 'nonel'),
        ('electrique', 'electrique'),
        ('classique', 'classique'),

    )
    b = (
        ('42ms,25ms,17ms', '42ms,25ms,17ms'),
        ('42ms,17ms', '42ms,17ms'),

    )
    c = (
        ('unique', 'unique'),
        ('etagé', 'étagé'),

    )
    d = (
        ('RT/SB', 'RT/SB'),
        ('RT/SA2', 'RT/SA2'),
        ('INT1/2', 'INT1/2'),
        ('INT2/4', 'INT2/4'),
        ('INT3/4', 'INT3/4'),
        ('INT3/5', 'INT3/5'),
        ('INT5/6', 'INT5/6'),
        ('INT4/5', 'INT4/5'),
        ('INT2/3', 'INT2/3'),
        ('INTSA2/C0', 'INTSA2/C0'),
        ('RT/C0', 'RT/C0'),
        ('RT/C2', 'RT/C2'),
        ('RT/C3', 'RT/C3'),
        ('RT/C4', 'RT/C4'),
        ('RT/C5', 'RT/C5'),

    )
    e = (
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
        ('P5', 'P5'),
        ('P6', 'P6'),
        ('P7', 'P7'),
        ('P8', 'P8')
    )
    mode_tir = models.CharField(max_length=150,choices=a)
    type_tir = models.CharField(max_length=150,choices=b)
    mode_charge = models.CharField(max_length=150,choices=c)
    niveau = models.CharField(max_length=150, choices=d)
    panneau = models.CharField(max_length=150, choices=e)
    largeur = models.CharField(max_length=255)
    nbr_trou_range = models.CharField(max_length=255)
    tranche = models.CharField(max_length=255)
    profondeur = models.CharField(max_length=255)
    dossage = models.CharField(max_length=255)
    nbr_trou = models.CharField(max_length=255)
    maille = models.CharField(max_length=255)
    longueur = models.CharField(max_length=50)
    nbr_range = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def volume(self):
        volume = float((self.largeur)) * float((self.longueur)) * float((self.profondeur))

        return volume

    @property
    def tovex1(self):
        tovex1 = float((self.nbr_trou)) / 2
        return tovex1

    @property
    def tovex(self):
        for i in range(25):
            tovex = float(self.tovex1)
            if (float((self.tovex)) % 25 != 0):
                self.tovex += 1
            else:

                break
        return tovex

    @property
    def surface(self):

        surface = float((self.largeur)) * float((self.longueur))
        return surface

    @property
    def deto500(self):
        deto500 = float(self.nbr_trou)
        return deto500

    @property
    def mf(self):

        mf = float((self.nbr_trou)) * float((self.profondeur))
        return mf

    @property
    def ligne_tir(self):

        ligne_tir = 500
        return ligne_tir

    @property
    def raccord42ms(self):
        if (((self.type_tir)) == '42ms,25ms,17ms'):
            raccord42ms = float(self.nbr_range)
            return raccord42ms
        else:
            raccord42ms = float(self.nbr_trou_range)
        return raccord42ms

    @property
    def raccord25ms(self):
        if (((self.type_tir)) == '42ms,25ms,17ms'):
            raccord25ms = float(self.nbr_range)
            return raccord25ms
        else:
            raccord25ms = float((self.nbr_trou)) - float((self.nbr_trou_range))
        return raccord25ms

    @property
    def raccord17ms(self):
        if (((self.type_tir)) == '42ms,25ms,17ms'):
            raccord17ms = (float(self.nbr_range)) - ((float(self.raccord42ms)) + (float(self.raccord25ms)))
            return raccord17ms
        else:
            return 0

    @property
    def ammonix1(self):
        ammonix1 = float(self.dossage) * float(self.volume) * 0.001
        return ammonix1

    @property
    def ammonix(self):
        if (float(self.ammonix1) <= 25):
            return 25
        elif (25 < float(self.ammonix1) <= 50):
            return 50
        elif (50 < float(self.ammonix1) <= 100):
            return 100
        return ammonix


    @property
    def tovex1(self):
        tovex1 = float((self.nbr_trou)) / 2
        return tovex1



    @property
    def tovex(self):
        if( float(self.tovex1)<= 25):
            return 25
        elif( 25<float(self.tovex1)<= 50):
            return 50
        elif (50 < float(self.tovex1) <= 100):
            return 100
        return tovex


    @property
    def dosage_r(self):
        dosage_r = ((float(self.ammonix))/((float(self.nbr_trou))*(float(self.profondeur))*(float(self.maille))))
        return dosage_r


    @property
    def repartition(self):
        repartition = float((self.ammonix))/float((self.nbr_trou))
        return repartition

    @property
    def ci(self):
        ci = (float((self.ammonix))/float((self.nbr_trou)))
        return ci

    @property
    def cout_ammonix(self):
        cout_ammonix = float(self.ammonix)*10
        return cout_ammonix

    @property
    def cout_tovex(self):
        cout_tovex = float(self.tovex) * 10
        return cout_tovex

    @property
    def cout_raccord17ms(self):
        cout_raccord17ms = float(self.raccord17ms) * 10
        return cout_raccord17ms

    @property
    def cout_raccord42ms(self):
        cout_raccord42ms = float(self.raccord42ms) * 10
        return cout_raccord42ms

    @property
    def cout_raccord25ms(self):
        cout_raccord25ms = float(self.raccord25ms) * 10
        return cout_raccord25ms

    @property
    def cout_ligne_tir(self):
        cout_ligne_tir = float(self.ligne_tir) * 10
        return cout_ligne_tir

    @property
    def aei(self):
        return 0.1
    @property
    def cout_aei(self):
        cout_aei = float(self.aei) * 10
        return cout_aei

    @property
    def cout_global(self):
        cout_global = float(self.cout_ammonix) + float(self.cout_tovex) +  float(self.cout_aei) + float(self.cout_ligne_tir) + float(self.cout_raccord25ms) + float(self.cout_raccord42ms) + float(self.cout_raccord25ms)
        return cout_global

class Sautage(models.Model):
    b = (
        ('42ms,25ms,17ms', '42ms,25ms,17ms'),
        ('42ms,17ms', '42ms,17ms'),

    )
    type_tir = models.CharField(max_length=150,choices=b)
    case_debut = models.CharField(max_length=255)
    equipe = models.CharField(max_length=255)
    son = models.CharField(max_length=255)
    frequence = models.CharField(max_length=255)
    vitesse = models.CharField(max_length=255)
    vitesse_vent = models.CharField(max_length=255)
    humiditer = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    taux_abattage = models.CharField(max_length=255)
    taux_deplacement = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cout(models.Model):

    ammonix = models.CharField(max_length=255)
    tovex = models.CharField(max_length=255)
    raccord17ms = models.CharField(max_length=255)
    raccord25ms = models.CharField(max_length=255)
    raccord42ms = models.CharField(max_length=255)
    cout_global = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Avance(models.Model):
    avance_foration = models.CharField(max_length=255)
    avance_sautage= models.CharField(max_length=255)
    avance_actuel= models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Stock(models.Model):

    ammonix = models.CharField(max_length=255)
    tovex = models.CharField(max_length=255)
    raccord17ms = models.CharField(max_length=255)
    raccord25ms = models.CharField(max_length=255)
    raccord42ms = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)
