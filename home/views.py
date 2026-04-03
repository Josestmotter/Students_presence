from django.shortcuts import render
from .models import Alunos, aulas
from .services import processar_arquivo, presenca_alunos


# Create your views here.
def home(request):
    alunos = Alunos.objects.all()
    dados = None
    aluno_certo = None
    aula = aulas.objects.first()
    numero = request.GET.get("numero")

    if numero:
        aluno_certo = Alunos.objects.filter(numero=int(numero)).first()

    if request.method == "POST":
        arquivo = request.FILES.get("arquivo")

        if arquivo:
            dados, aula = processar_arquivo(arquivo)

            if aulas.objects.filter(aula=aula).exists():
                return render(request, "home/home.html", {
                "erro": f"A aula {aula} já foi enviada."
            })

            aulas.objects.create(aula=aula)


            presenca_alunos(dados)

            alunos = Alunos.objects.all()

            numero = request.GET.get("numero")
            if numero:
                aluno_certo = Alunos.objects.filter(numero=int(numero)).first()

   
    return render(request, "home/home.html", {
        "alunos": alunos,
        "aluno": aluno_certo,
        "aula": aula,
        
        "dados": dados,
    })


    