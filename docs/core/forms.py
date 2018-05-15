from django import forms
from .models import Aluno
from .models import Coordenador
from .models import Professor
from .models import Curso
from .models import Disciplina
from .models import Atividade
from .models import Mensagem

class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ['id', 'login', 'senha', 'nome', 'email', 'dtexpiracao', 'celular']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['id', 'login', 'senha', 'nome', 'email', 'dtexpiracao', 'celular', 'ra', 'foto']

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['id', 'login', 'senha', 'nome', 'email', 'celular', 'dtexpiracao', 'apelido']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['id', 'nome']

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['id', 'nome', 'data', 'status', 'planodeensino', 'cargahoraria', 'competencias', 
                    'habilidades', 'ementa', 'conteudoprogramatico', 'bibliografiabasica', 
                    'bibliografiacomplentar', 'percentualpratico', 'percentualteorico', 'idcoordenador' ]
                    
class AtividadeForm(forms.ModelForm):
    class Meta: 
        model = Atividade
        fields = ['id', 'titulo', 'descricao', 'conteudo', 'tipo', 'extras', 'idprofessor']
        
class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['id', 'idaluno', 'idprofessor', 'assunto', 'referencia', 'conteudo', 'status', 
                    'dtenvio', 'dtresposta', 'resposta']




