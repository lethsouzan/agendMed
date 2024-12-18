from django.contrib import admin
from .models import Paciente,Medico,ASO, Agendamentos

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(ASO)
admin.site.register(Agendamentos)
