from django.urls import path
from django.contrib import admin
from app.views import listaPacientes,listaMedicos,listaASOs, index, login, listaAgendamentos,agendarAso, cadastrarMedico, cadastrarPaciente, listaResultados, detalharPacientes, editarPacientes, deletarPacientes, detalharMedicos, editarMedicos, deletarMedicos, detalharAgendamentos, editarAgendamentos, deletarAgendamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listaPacientes/', listaPacientes,name="listaPacientes"),
    path('listaMedicos/', listaMedicos,name="listaMedicos"),
    path('listaASOs/', listaASOs,name="listaASOs"),
    path('index/', index,name="index"),
    path('login/',login,name="login"),
    path('listaAgendamentos/',listaAgendamentos,name="listaAgendamentos"),
    path('agendarAso/', agendarAso, name="agendarAso"),
    path('cadastrarMedico/', cadastrarMedico, name='cadastrarMedico'),
    path('cadastrarPaciente/', cadastrarPaciente, name='cadastrarPaciente'),
    path('listaResultados/', listaResultados, name='listaResultados'),
    path('detalharPacientes/<int:id>',detalharPacientes,name="detalharPacientes"),
    path('editarPacientes/<int:id>',editarPacientes,name="editarPacientes"),
    path('deletarPacientes/<int:id>',deletarPacientes,name="deletarPacientes"),
    path('detalharMedicos/<int:id>',detalharMedicos,name="detalharMedicos"),
    path('editarMedicos/<int:id>',editarMedicos,name="editarMedicos"),
    path('deletarMedicos/<int:id>',deletarMedicos,name="deletarMedicos"),
    path('detalharAgendamentos/<int:id>',detalharAgendamentos,name="detalharAgendamentos"),
    path('editarAgendamentos/<int:id>',editarAgendamentos,name="editarAgendamentos"),
    path('deletarAgendamentos/<int:id>',deletarAgendamentos,name="deletarAgendamentos")
]

