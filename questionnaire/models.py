import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Users(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='F.I.Sh')
    username = models.CharField(max_length=100, null=True, blank=True, verbose_name='Username')
    telegram_id = models.BigIntegerField(null=True, blank=True, unique=True, verbose_name="Telegram ID")
    joined_at = models.DateTimeField(null=True, blank=True, default=datetime.datetime.now(), verbose_name="Qo'shilgan vaqti")

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchilar'
        db_table = 'users'

    def __str__(self):
        return self.full_name


class Branches(models.Model):
    name = models.CharField(max_length=221, null=True, blank=True, verbose_name="Nomi")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'branch'
        verbose_name = "Branch"
        verbose_name_plural = "Filiallar"

    def __str__(self):
        return self.name


class Ranks(models.Model):
    name = models.CharField(max_length=221, null=True, blank=True, verbose_name="Nomi")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'rank'
        verbose_name = "Rank"
        verbose_name_plural = "Lavozimlar"

    def __str__(self):
        return self.name


class Questionnaire(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Foydalanuvchi")
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Filial")
    rank = models.ForeignKey(Ranks, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Lavozim")
    ish_muhiti_va_madaniyati = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], verbose_name="Ish muhiti va madaniyati")
    rivojlanish_va_osish_imkoniyatlari = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], verbose_name="Rivojlanish va o'sish imkoniyatlari")
    ish_haqi_va_mukofotlar = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], verbose_name="Ish haqi va mukofotlar")
    rahbariyat_bilan_munosabat = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ], verbose_name="Rahbariyat bilan munosabat")
    ish_muvozanati_va_farovonligi = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ],
                                                        verbose_name="Ish muvozanati va farovonligi (Ish va hayot muvozanatiga e'tibor, stress darajasi, dam olish va tanaffuslar, ish yuklamasi)")
    created_at = models.DateTimeField(default=datetime.datetime.now(), null=True, blank=True,
                                      verbose_name="Yaratilgan vaqti")

    class Meta:
        db_table = 'questionnaire'
        verbose_name = "Questionnaire"
        verbose_name_plural = "Atvetlar"

    def __str__(self):
        return f"{self.branch} {self.rank}"
