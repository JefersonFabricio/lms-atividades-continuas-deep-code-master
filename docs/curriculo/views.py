from django.shortcuts import render, redirect
from curriculo.models import Curso, Disciplina

# Create your views here.
def listaCursos(request):
    contexto ={
        "cursos":Curso.objects.all()
    }
    return render(request, "lista_cursos.html", contexto)

def listarDisciplinas(request):
    contexto ={
        "disciplinas":Disciplina.objects.all()
    }
    return render(request, "lista_disciplinas.html", contexto)

def incluirDisciplina(request):
    context ={}
    if request.POST:
    
        Disciplina.objects.create(
            nome=request.POST.get('nome'),
            data=request.POST.get('data'),
            planodeensino=request.POST.get('planodeensino'),
            competencias=request.POST.get('competencias'),
            status=request.POST.get('status'),
            cargahoraria=request.POST.get('cargahoraria'),
            habilidades=request.POST.get('habilidades'),
            ementa=request.POST.get('ementa'),
            conteudoprogramatico=request.POST.get('conteudoprogramatico'),
            bibliografiabasica=request.POST.get('bibliografiabasica'),
            bibliografiacomplentar=request.POST.get('bibliografiacomplentar'),
            percentualpratico=request.POST.get('percentualpratico'),
            percentualteorico=request.POST.get('percentualteorico')
        )
        return redirect('/disciplinas/')
    else:
        return render(request, 'formDisciplina.html', context)

def alterarDisciplina(request, id):
    context ={}
    if request.POST:
        disciplina = Disciplina.objects.get(id=id)

        disciplina.nome=request.POST.get("nome")
        disciplina.data=request.POST.get("data")
        disciplina.planodeensino=request.POST.get("planodeensino")
        disciplina.competencias=request.POST.get("competencias")
        disciplina.status=request.POST.get("status")
        disciplina.CargaHoraria=request.POST.get("CargaHoraria")
        disciplina.Habilidades=request.POST.get("Habilidades")
        disciplina.Ementa=request.POST.get("Ementa")
        disciplina.ConteudoProgramatico=request.POST.get("ConteudoProgramatico")
        disciplina.BibliografiaBasica=request.POST.get("BibliografiaBasica")
        disciplina.BibliografiaComplentar=request.POST.get("BibliografiaComplentar")
        disciplina.PercentualPratico=request.POST.get("PercentualPratico")
        disciplina.PercentualTeorico=request.POST.get("PercentualTeorico")
    
        disciplina.save()
        return redirect('/disciplinas/')
    else:
        context['disciplina'] = Disciplina.objects.get(id=id)
        return render(request, 'formDisciplina.html', context)


def incluirCurso(request):
    context = {}
    if request.POST:
        Curso.objects.create(
            nome=request.POST.get("nome"),
            sigla=request.POST.get('sigla')
        )
        return redirect("/cursos/")
    else:
        return render(request, "formCurso.html", context)


def alterarCurso(request, id):
    context = {}
    if request.POST:
        curso = Curso.objects.get(id=id)

        curso.nome=request.POST.get("nome")
        curso.sigla=request.POST.get("sigla")

        curso.save()
        return redirect("/cursos/")
    else:
        context['curso'] = Curso.objects.get(id=id)
        return render(request, 'formCurso.html', context)

def formCurso(request, id):
    curso = Curso.objects.get(id=id)
    context={
        'curso':curso
    }
    return render(request, 'formCurso.html', context)

def curso(request, nome):
    cursos ={
        "ADS": {
            "titulo": "Analise e Desenvolvimento de Sistemas",
            "carga_horaria": "2020h"
        },
        "BD": {
            "titulo": "Banco de Dados",
            "carga_horaria": "2040h"
        },
        "GTI": {
            "titulo": "Gestão de tecnologia da Informação",
            "carga_horaria": "2020h"
        }
    }
    curso = cursos[nome]
    
    return render(request, "curso.html", curso)
