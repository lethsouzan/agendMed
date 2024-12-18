from django.db import models

class ASO(models.Model):
    tipo = models.CharField(max_length=150,blank=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False)

    def __str__(self):
        return self.tipo

class Medico(models.Model):
    nome = models.CharField(max_length=150,blank=False)
    crm = models.CharField(max_length=6,blank=False)
    crm_estado = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.nome

    
class Paciente(models.Model):
    nome = models.CharField(max_length=100,blank=False)
    cpf = models.CharField(max_length=11,blank=False)
    funcao = models.CharField(max_length=100,blank=False)
    data_nascimento = models.DateField()
    empresa = models.CharField(max_length=200,blank=False)
    cnpj_empresa = models.CharField(max_length=14,blank=False)
    def __str__(self):
        return f"{self.nome} - {self.cpf}"
    
class Agendamentos(models.Model):
    data_agendamento = models.DateTimeField()
    id_medico = models.ForeignKey(Medico,on_delete=models.PROTECT)
    id_aso = models.ForeignKey(ASO, on_delete=models.PROTECT, null=False)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, null=True)  
    def __str__(self):
        return f"{self.id_paciente.nome} - {self.data_agendamento}"
    
class index(models.Model):
    def __str__(self):
        return 
    
class login(models.Model):
    def __str__(self):
        return 
    
class agendarAso(models.Model):
    def __str__(self):
        return
    
class cadastrarMedico(models.Model):
    def __str__(self):
        return
    
class cadastrarPaciente(models.Model):
    def __str__(self):
        return
    
class Resultados(models.Model):
    def __str__(self):
        return 


    