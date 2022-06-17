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


class Stock(models.Model):
    num_stock = models.CharField(max_length=255)
    ammonix = models.CharField(max_length=255)
    tovex = models.CharField(max_length=255)
    raccord17ms = models.CharField(max_length=255)
    raccord25ms = models.CharField(max_length=255)
    raccord42ms = models.CharField(max_length=255)
    ligne_tir = models.CharField(max_length=255)
    aei = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







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
    f = (
        ('7500/1', '7500/1'),
        ('7500/2', '7500/2'),
        ('PH1', 'PH1'),
        ('PH2', 'PH2'),
        ('D11', 'D11'),
        ('200B/1', '200B/1'),
        ('E.E', 'E.E'),

    )
    g = (
        ('LABRIKIYINE', 'LABRIKIYINE'),
        ('LABHIRA', 'LABHIRA'),


    )
    observation= models.CharField(max_length=150, choices=g)
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, default=1)
    num_com = models.CharField(max_length=255)
    machine = models.CharField(max_length=150, choices=f)
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
            raccord17ms = (float(self.nbr_trou)) - ((float(self.raccord42ms)) + (float(self.raccord25ms)))
            return raccord17ms
        else:
            return 0

    @property
    def ammonix1(self):
        ammonix1 = (float(self.dossage) * float(self.volume) * 0.001)
        return ammonix1

    @property
    def ammonix(self):
        if (float(self.ammonix1) <= 25):
            return 25
        elif (25 < float(self.ammonix1) <= 50):
            return 50
        elif (50 < float(self.ammonix1) <= 100):
            return 100

        return self.ammonix1

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
        elif (100 < float(self.tovex1) <= 125):
            return 125
        elif (125 < float(self.tovex1) <= 150):
            return 150
        elif (150 < float(self.tovex1) <= 175):
            return 175
        elif (175 < float(self.tovex1) <= 200):
            return 125
        elif (200 < float(self.tovex1) <= 225):
            return 225
        elif (225 < float(self.tovex1) <= 250):
            return 250
        elif (250 < float(self.tovex1) <= 275):
            return 275
        elif (275 < float(self.tovex1) <= 300):
            return 300
        elif (300 < float(self.tovex1) <= 325):
            return 325
        elif (325 < float(self.tovex1) <= 350):
            return 350
        elif (350 < float(self.tovex1) <= 375):
            return 375
        elif (375 < float(self.tovex1) <= 400):
            return 400

    @property
    def dosage_r(self):
        dosage_r = (((float(self.ammonix))/((float(self.nbr_trou))*(float(self.profondeur))*(float(self.maille)))))*100
        dosage_r = str(round(dosage_r, 2))
        return dosage_r


    @property
    def repartition(self):
        repartition = (float((self.ammonix))/float((self.nbr_trou)))/25
        repartition = str(round(repartition, 2))
        return repartition

    @property
    def ci(self):
        ci = float(self.repartition)*25
        ci = str(round(ci, 2))
        return ci

    @property
    def cout_ammonix(self):
        cout_ammonix = float(self.ammonix)*9.05
        return cout_ammonix

    @property
    def cout_tovex(self):
        cout_tovex = float(self.tovex) * 18.45
        return cout_tovex

    @property
    def cout_raccord17ms(self):
        cout_raccord17ms = float(self.raccord17ms) * 35
        return cout_raccord17ms

    @property
    def cout_raccord42ms(self):
        cout_raccord42ms = float(self.raccord42ms) * 35
        return cout_raccord42ms

    @property
    def cout_raccord25ms(self):
        cout_raccord25ms = float(self.raccord25ms) * 35
        return cout_raccord25ms

    @property
    def cout_ligne_tir(self):
        cout_ligne_tir = float(self.ligne_tir) * 1.25
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

    @property
    def rammonix(self):
        rammonix = float(self.stock_id.ammonix) - float(self.ammonix)
        return rammonix

    @property
    def rtovex(self):
        rtovex = float(self.stock_id.tovex) - float(self.tovex)
        return rtovex

    @property
    def araccord17ms(self):
        araccord17ms = float(self.stock_id.raccord17ms) - float(self.raccord17ms)
        return araccord17ms

    @property
    def araccord42ms(self):
        araccord42ms = float(self.stock_id.raccord42ms) - float(self.raccord42ms)
        return araccord42ms

    @property
    def araccord25ms(self):
        araccord25ms = float(self.stock_id.raccord25ms) - float(self.raccord25ms)
        return araccord25ms

    @property
    def rligne_tir(self):
        rligne_tir = float(self.stock_id.ligne_tir) - float(self.ligne_tir)
        return rligne_tir

    @property
    def raei(self):
        raei = float(self.stock_id.aei) - float(self.aei)
        return raei

    @property
    def rendement(self):

        if (((self.machine)) == '7500/1'):
            rendement = (float(self.volume)) / 19.5
            rendement = str(round(rendement, 2))
            return rendement

        elif (((self.machine)) == '7500/2'):
            rendement = (float(self.volume))/21.5
            rendement = str(round(rendement, 2))
            return rendement

        elif (((self.machine)) == 'PH1'):
            rendement = (float(self.volume))/16.5
            rendement = str(round(rendement, 2))
            return rendement

        elif (((self.machine)) == 'PH2'):
            rendement = (float(self.volume))/18
            rendement = str(round(rendement, 2))
            return rendement

        elif (((self.machine)) == '200B1'):
            rendement = (float(self.volume))/9
            rendement = str(round(rendement, 2))
            return rendement

        elif (((self.machine)) == 'D11'):
            rendement = (float(self.volume))/21
            rendement = str(round(rendement, 2))
            return rendement


        elif (((self.machine)) == 'E.E'):
            rendement = (float(self.volume))/18
            rendement= str(round(rendement, 2))
            return rendement




class Sautage(models.Model):
    b = (
        ('42ms,25ms,17ms', '42ms,25ms,17ms'),
        ('42ms,17ms', '42ms,17ms'),

    )
    fouration_id = models.ForeignKey(Fourations, on_delete=models.CASCADE, default=1)
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
    nammonix = models.CharField(max_length=255)
    ntovex = models.CharField(max_length=255)
    nartifice = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Avance(models.Model):
    f = (
        ('7500/1', '7500/1'),
        ('7500/2', '7500/2'),
        ('PH1', 'PH1'),
        ('PH2', 'PH2'),
        ('D11', 'D11'),
        ('E.E', 'E.E'),

    )
    machine = models.CharField(max_length=150, choices=f)
    fouration_id = models.ForeignKey(Fourations, on_delete=models.CASCADE, default=1)
    avance_foration = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def avanveactuel(self):
        avanveactuel =  float(self.avance_foration) - float(self.fouration_id.longueur)
        return avanveactuel



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

class Pfourations(models.Model):
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
    niveau = models.CharField(max_length=150, choices=d)
    panneau = models.CharField(max_length=150, choices=e)
    densite_r = models.CharField(max_length=255)
    largeur = models.CharField(max_length=255)
    hauteur = models.CharField(max_length=255)
    tranche = models.CharField(max_length=255)
    diametre = models.CharField(max_length=255)
    longueur = models.CharField(max_length=50)
    de = models.CharField(max_length=255)
    espacement = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def banquette(self):
        banquette = float(0.0012 * ((2 * float(self.de) / float(self.densite_r)) + 1.5) * float(self.diametre))
        return banquette

    @property
    def ratio1(self):
        ration1 = float(self.hauteur) / float(self.banquette)
        return ration1

    @property
    def ratio(self):
        if(float(self.ratio1) < 3):
            return "Risque de formation des blocs"
        elif(3<float(self.ratio1) < 4):
            return "Bonne fragementation "
        else:
            return "Risque de formation des blocs"



    @property
    def bourrage(self):
        bourrage = float(self.banquette)
        return bourrage

    @property
    def nbr_trou_range(self):
        nbr_trou_range = float(self.longueur) / float(self.banquette)
        return nbr_trou_range

    @property
    def nbr_range(self):
        nbr_range = float(self.largeur) / float(self.espacement)
        return nbr_range

    @property
    def nbr_trou_total(self):
        nbr_trou_total = float(self.nbr_trou_range) * float(self.nbr_range)
        return nbr_trou_total

    @property
    def mf(self):
        mf = float(self.nbr_trou_total) / float(self.hauteur)
        return mf

    @property
    def maille(self):
        maille = float(self.banquette) * float(self.espacement)
        return maille

    @property
    def volume(self):
        volume = float(self.maille) * float(self.hauteur)
        return volume

    @property
    def espacement1(self):
        if(1.10<float(self.espacement)<1.15):
            return "Bonne fragementation"
        else:
            return "Production des blocs"







