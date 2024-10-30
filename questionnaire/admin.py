from django.contrib import admin
from .models import *


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'username', 'joined_at')
    list_filter = ('joined_at',)
    search_fields = ('full_name', 'username')
    date_hierarchy = 'joined_at'


@admin.register(Branches)
class BranchesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "created_at")
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Ranks)
class RanksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "created_at")
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'branch', "rank", "ish_muhiti_va_madaniyati", "rivojlanish_va_osish_imkoniyatlari",
        "ish_haqi_va_mukofotlar",
        "rahbariyat_bilan_munosabat", "ish_muvozanati_va_farovonligi", "created_at")
    list_filter = ('branch__name', 'rank__name', "created_at")
    search_fields = ('branch__name', "rank__name")
    date_hierarchy = 'created_at'
