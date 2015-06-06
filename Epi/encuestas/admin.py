from django.contrib import admin

# Register your models here.

from .models import Encuesta, Pueblo, Individuo, Vivienda


class IndividuoInline(admin.StackedInline):
    model = Individuo
    extra = 3


class ViviendaAdmin(admin.ModelAdmin):
    inlines = [IndividuoInline]


admin.site.register(Encuesta)
admin.site.register(Pueblo)
admin.site.register(Individuo)
admin.site.register(Vivienda, ViviendaAdmin)
