from django.shortcuts import render, redirect, get_object_or_404
from .models import ASO, Medico, Paciente, index, login, Agendamentos, Resultados

def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def listaASOs(request):
    listaASOs = ASO.objects.all()
    return render(request,'listaASOs.html',{'listaASOs':listaASOs})

def listaMedicos(request):
    listaMedicos = Medico.objects.all()
    return render(request, 'listaMedicos.html', {'listaMedicos': listaMedicos})

def listaPacientes(request):
    listaPacientes = Paciente.objects.all()
    return render(request,'listaPacientes.html',{'listaPacientes':listaPacientes})

def listaAgendamentos(request):
    listaAgendamentos = Agendamentos.objects.select_related('id_paciente').all()
    return render(request,'listaAgendamentos.html',{'listaAgendamentos':listaAgendamentos})

def agendarAso(request):
    if request.method == 'POST':
        # Processa o formulário
        paciente_id = request.POST.get('id_paciente')
        medico_id = request.POST.get('id_medico')
        aso_id = request.POST.get('id_aso')
        data_agendamento = request.POST.get('data_agendamento')

        print(f"Paciente: {paciente_id}, Médico: {medico_id}, ASO: {aso_id}, Data: {data_agendamento}")


        # Cria o objeto Agendamentos e salva no banco
        Agendamentos.objects.create(
            id_paciente_id=paciente_id,
            id_medico_id=medico_id,
            id_aso_id=aso_id,
            data_agendamento=data_agendamento
        )
        return redirect('listaAgendamentos')  # Redireciona para a lista de agendamentos

    # GET: Renderiza o formulário
    context = {
        'pacientes': Paciente.objects.all(),
        'medicos': Medico.objects.all(),
        'asos': ASO.objects.all(),
    }
    return render(request, 'agendarAso.html', context)

def cadastrarMedico(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome = request.POST.get('nome')
        crm = request.POST.get('crm')
        crm_estado = request.POST.get('crm_estado')

        # Criar o novo objeto Medico
        Medico.objects.create(
            nome=nome,
            crm=crm,
            crm_estado=crm_estado
        )

        # Redirecionar para a lista de médicos
        return redirect('listaMedicos')

    # Caso o método seja GET, renderize o formulário vazio
    return render(request, 'cadastrarMedico.html')

def cadastrarPaciente(request):
    if request.method == 'POST':
        # Capturar os dados do formulário
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        funcao = request.POST.get('funcao')
        data_nascimento = request.POST.get('data_nascimento')
        empresa = request.POST.get('empresa')
        cnpj_empresa = request.POST.get('cnpj_empresa')

        # Criar o novo objeto Medico
        Paciente.objects.create(
            nome=nome,
            cpf=cpf,
            funcao=funcao,
            data_nascimento=data_nascimento,
            empresa=empresa,
            cnpj_empresa=cnpj_empresa
        )

        # Redirecionar para a lista de médicos
        return redirect('listaPacientes')

    # Caso o método seja GET, renderize o formulário vazio
    return render(request, 'cadastrarPaciente.html')

def listaResultados(request):
    listaResultados = Resultados.objects.all()
    return render(request, 'listaResultados.html', {'listaResultados': listaResultados})

#opções Pacientes

def detalharPacientes(request,id):
    return render(request,'detalharPacientes.html',{'dadosPaciente':Paciente.objects.get(id=id)})

def editarPacientes(request,id):
    paciente = Paciente.objects.get(id=id)
    if request.method == "POST":
        paciente.nome = request.POST.get("nome")
        paciente.cpf = request.POST.get("cpf")
        paciente.funcao = request.POST.get("funcao")
        paciente.empresa = request.POST.get("empresa")
        paciente.cnpj_empresa = request.POST.get("cnpj_empresa")

        paciente.save()
        return redirect('listaPacientes')
    else:
        return render(request,'editarPacientes.html',{'dadosPaciente':paciente})
    
def deletarPacientes(request,id):
    try:
        paciente = Paciente.objects.get(id=id)
        paciente.delete()
        return redirect('listaPacientes')
    except Paciente.DoesNotExist:
        messages.error(request,"Paciente não existe!")
        return redirect('listaPacientes')
    except Paciente.Protected.Error:
        messages.error(request,"este paciente está associado a registros de outra tabela")
        return redirect("listaPacientes")
    
#opções Médicos

def detalharMedicos(request,id):
    return render(request,'detalharMedicos.html',{'dadosMedico':Medico.objects.get(id=id)})

def editarMedicos(request,id):
    medico = Medico.objects.get(id=id)
    if request.method == "POST":
        medico.nome = request.POST.get("nome")
        medico.crm = request.POST.get("crm")
        medico.crm_estado = request.POST.get("crm_estado")

        medico.save()
        return redirect('listaMedicos')
    else:
        return render(request,'editarMedicos.html',{'dadosMedico':medico})
    
def deletarMedicos(request,id):
    try:
        medico = Medico.objects.get(id=id)
        medico.delete()
        return redirect('listaMedicos')
    except Medico.DoesNotExist:
        messages.error(request,"Médico não existe!")
        return redirect('listaMedicos')
    except Medico.Protected.Error:
        messages.error(request,"este médico está associado a registros de outra tabela")
        return redirect("listaMedicos")
    
#opções Meus Agendamentos

def detalharAgendamentos(request,id):
    return render(request,'detalharAgendamentos.html',{'dadosAgendamento':Agendamentos.objects.get(id=id)})

def editarAgendamentos(request,id):
    agendamento = get_object_or_404(Agendamentos, id=id)
    if request.method == "POST":
        data_agendamento = request.POST.get("data_agendamento")
        id_medico = request.POST.get("id_medico")
        id_aso = request.POST.get("id_aso")
        id_paciente = request.POST.get("id_paciente")
        

        paciente =get_object_or_404(Paciente, id=id_paciente)
        medico = get_object_or_404(Medico, id=id_medico)
        aso = get_object_or_404(ASO, id=id_aso)

        agendamento.id_paciente = paciente
        agendamento.id_medico = medico
        agendamento.id_aso = aso
        agendamento.data_agendamento = data_agendamento
        
    # Cria o objeto Agendamentos e salva no banco
        agendamento.save()
        return redirect('listaAgendamentos')  # Redireciona para a lista de agendamentos
    
    # GET: Renderiza o formulário
    context = {
        'pacientes': Paciente.objects.all(),
        'medicos': Medico.objects.all(),
        'asos': ASO.objects.all(),
    }
    return render(request, 'editarAgendamentos.html', context)

    
def deletarAgendamentos(request,id):
    try:
        medico = Agendamentos.objects.get(id=id)
        medico.delete()
        return redirect('listaAgendamentos')
    except Agendamentos.DoesNotExist:
        messages.error(request,"Agendamento não existe!")
        return redirect('listaAgendamento')
    except Agendamentos.Protected.Error:
        messages.error(request,"este agendamento está associado a registros de outra tabela")
        return redirect("listaAgendamento")



