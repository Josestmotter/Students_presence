#Personal defs here
from home.models import Alunos, aulas
from django.db.models import F
import pandas as pd
from pathlib import Path
from io import TextIOWrapper
BASE_DIR = Path(__file__).resolve().parent.parent


def receber_planilha(request):
    if request.method == "POST":
        caminho = request.FILES.get("arquivo")
    df = pd.read_csv(caminho)
    return df.to_dict(orient="records")

def adicionar_alunos():
    df = pd.read_csv("home/static/home/alunos_presenca.csv")
    dados = df.to_dict(orient="records")
    for pessoa in dados:
        Alunos.objects.get_or_create(
        numero=pessoa["Numero"],
        defaults={
            "nome": pessoa["Nome"],
            "faltas": 0
        }
    )


def presenca_alunos(arquivo_csv):
    for pessoa in arquivo_csv:
        if pessoa["Presenca"] == "Faltou":
            Alunos.objects.filter(numero=pessoa["Numero"]).update(
                faltas=F("faltas") + 1
            )

def processar_arquivo(arquivo):
    arquivo_texto = TextIOWrapper(arquivo.file, encoding="utf-8")
    df = pd.read_csv(arquivo_texto)
    dados = df.to_dict(orient="records")
    aula = df.iloc[1, 3]
    
    return dados, aula


def muda_numero_aula(request):
    if request.method == "POST":
        acao = request.POST.get("acao")
        if acao == "soma":
            aulas.objects.filter(id=1).update(aula=F("aula") + 1
            )
        elif acao == "subtrair":
            aulas.objects.filter(id=1).update(aula=F("aula") - 1
            )
        return aulas.objects.first()