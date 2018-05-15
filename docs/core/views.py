from django.shortcuts import render, redirect
from .models import Aluno,Coordenador,Professor,Curso,Disciplina,Atividade,Mensagem
from .forms import AlunoForm,CoordenadorForm,ProfessorForm,CursoForm,DisciplinaForm,AtividadeForm,MensagemForm

# Create your views here.

def alunos(request):
    data = {}
    alunos = Aluno.objects.all()
    return render(request, 'alunos.html', {'alunos': alunos})

def novo_aluno(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        alunos = Aluno.objects.all()
        return render(request, 'alunos.html', {'alunos': alunos})

    return render(request, 'novo_aluno.html', {'form': form})

def atualizar_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        alunos = Aluno.objects.all()
        return redirect("/alunos")
        # return render(request, 'alunos.html', {'alunos': alunos})

    return render(request, 'novo_aluno.html', {'form': form, 'aluno': aluno})

def coordenadores(request):
    coordenadores = Coordenador.objects.all()
    return render(request, 'coordenadores.html', {'coordenadores': coordenadores})

def novo_coordenador(request):
    form = CoordenadorForm(request.POST or None)

    if form.is_valid():
        form.save()
        coordenadores = Coordenador.objects.all()
        return render(request, 'coordenadores.html', {'coordenadores': coordenadores})

    return render(request, 'novo_coordenador.html', {'form': form})

def atualizar_coordenador(request, id):
    coordenador = Coordenador.objects.get(id=id)
    form = CoordenadorForm(request.POST or None, instance=coordenador)

    if form.is_valid():
        form.save()
        coordenadores = Coordenador.objects.all()
        return redirect("/coordenadores")

    return render(request, 'novo_coordenador.html', {'form': form, 'coordenadores': coordenadores})



def professores(request):
    professores = Professor.objects.all()
    return render(request, 'professores.html', {'professores': professores})

def novo_professor(request):
    form = ProfessorForm(request.POST or None)

    if form.is_valid():
        form.save()
        professores = Coordenador.objects.all()
        return render(request, 'professores.html', {'professores': professores})

    return render(request, 'novo_professor.html', {'form': form})

def atualizar_professor(request, id):
    professor = Professor.objects.get(id=id)
    form = ProfessorForm(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        professores = Professor.objects.all()
        return redirect("/professores")

    return render(request, 'novo_professor.html', {'form': form, 'professores': professores})



def novo_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        cursos = Curso.objects.all()
        return render(request, 'cursos.html', {'cursos': cursos})

    return render(request, 'novo_curso.html', {'form': form})

def atualizar_curso(request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(request.POST or None, instance=curso)

    if form.is_valid():
        form.save()
        cursos = Curso.objects.all()
        return redirect("/cursos")

    return render(request, 'novo_curso.html', {'form': form, 'cursos': cursos})

def disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

def nova_disciplina(request):
    form = DisciplinaForm(request.POST or None)

    if form.is_valid():
        form.save()
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

    return render(request, 'nova_disciplina.html', {'form': form})

def atualizar_disciplina(request, id):
    disciplina = Disciplina.objects.get(id=id)
    form = DisciplinaForm(request.POST or None, instance=disciplina)

    if form.is_valid():
        form.save()
        disciplinas = Disciplina.objects.all()
        return redirect("/disciplinas")

    return render(request, 'nova_disciplina.html', {'form': form, 'disciplinas': disciplinas})

def atividades(request):
    atividades = Atividade.objects.all()
    return render(request, 'atividades.html', {'atividades': atividades})

def nova_atividade(request):
    form = AtividadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        atividades = Atividade.objects.all()
        return render(request, 'atividades.html', {'atividades': atividades})

    return render(request, 'nova_atividade.html', {'form': form})

def atualizar_atividade(request, id):
    atividade = Atividade.objects.get(id=id)
    form = AtividadeForm(request.POST or None, instance=atividade)

    if form.is_valid():
        form.save()
        atividades = Atividade.objects.all()
        return redirect("/atividades")

    return render(request, 'nova_atividade.html', {'form': form, 'atividades': atividades})


def mensagens(request):
    mensagens = Mensagem.objects.all()
    return render(request, 'mensagens.html', {'mensagens': mensagens})

def nova_mensagem(request):
    form = MensagemForm(request.POST or None)

    if form.is_valid():
        form.save()
        mensagens = Mensagem.objects.all()
        return render(request, 'mensagens.html', {'mensagens': mensagens})

    return render(request, 'nova_mensagem.html', {'form': form})

def atualizar_mensagem(request, id):
    mensagem = Mensagem.objects.get(id=id)
    form = MensagemForm(request.POST or None, instance=mensagem)

    if form.is_valid():
        form.save()
        mensagens = Mensagem.objects.all()
        return redirect("/mensagens")

    return render(request, 'nova_mensagem.html', {'form': form, 'mensagens': mensagens})




def index(request):
    context={

    }
    return render(request,'index.html',context)
def detalhes_curso(request):
    context={

    }
    return render(request,'detalhes_curso.html')

def cursos(request):
    context = {
        "cursos":[
            {'img':'static/img/ADS.jpg', 'nome':'Analise e Desenvolvimento de Sistemas','resumo':'Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados.Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia.', 'link':'ads'},
            {'img':'static/img/BD.jpg', 'nome':'Banco de Dados','resumo':'O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas dedesenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área.', 'link':'bd'},
            {'img':'static/img/GTI.jpg', 'nome':'Gestão de Tecnologia da Informação','resumo':'A graduação em Gestão da Tecnologia da Informação prepara você para a liderança em TI.Apto a criar soluções para problemas nas organizações, você vai fazer a administração de infraestrutura física e lógica de ambientes informatizados.', 'link':'gti'},
            ],
    }
    return render(request,'cursos.html', context)

def detalhes_diciplinas(request):
    context={

    }
    return render(request,'detalhes_diciplinas.html')
def login(request):
    context={

    }
    return render(request,'login.html')

def pagina_disciplina(request):
    context={

    }
    return render(request,'pagina_disciplina.html')
def lista(request):
    context={
        "listas":[
            {'nome':"Coordenador",},
            {'nome':"Aluno"},
            {'nome':"Professor"},
            {'nome':"Mensagem"},
            {'nome':"Curso"},
            {'nome':"disciplinas"},
            {'nome':"SolicitacaoMatricula"},
            {'nome':"Atividade"},
            {'nome':"AtividadeVinculada"},
            {'nome':"Entrega"}
            ]  
    }
    return render(request,'Listagem.html',context)
def matricula(request):
    context={
        'alunos':[
                    {'nome':'rechadson','RA':'123456'},
                    {'nome':'rechadson1','RA':'1234567'},
                    {'nome':'rechadson2','RA':'1234568'},
                    {'nome':'rechadson33','RA':'123456'},
                    {'nome':'rechadson11','RA':'1234567'},
                    {'nome':'rechadson22','RA':'1234568'},
                    {'nome':'rechadson111','RA':'123456'},
                    {'nome':'rechadson122','RA':'1234567'},
                    {'nome':'rechadson2333','RA':'1234568'},
                    {'nome':'rechadson1113','RA':'123456'},
                    {'nome':'rechadson1133','RA':'1234567'},
                    {'nome':'rechadson2122','RA':'1234568'},
                    {'nome':'rechadson12341','RA':'123456'},
                    {'nome':'rechadson1123411','RA':'1234567'},
                    {'nome':'rechadson24444','RA':'1234568'},
                    {'nome':'rechadson5555','RA':'123456'},
                    {'nome':'rechadson11141','RA':'1234567'},
                    {'nome':'rechadson21444','RA':'1234568'},
                    {'nome':'rechadson1234411','RA':'123456'},
                    {'nome':'rechadson14441123','RA':'1234567'},
                    {'nome':'rechadson212341234','RA':'1234568'},
                ]
            }
    return render(request,'matricula.html',context)

def ads(request):
    context = {
        "titulo": "ADS",
        "titulo_Pag": "Análise e Desenvolvimento de Sistemas",
        "p1": "Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados.<p>O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação.</p>",
        "duracao": "<p>04 Semestres</p><p>2020h</p><h1>Período:</h1><p><b>Matutino</b></p><p>08h00 às 11h40</p><p><b>Mensalidade</b></p><p>R$ 582,00</p><p><b>Norturno</b></p><p>19h00 às 22h40</p><p><b>Mensalidade</b></p><p>R$ 657,00</p>",
        "coord": "Ana Cristina Dos Santos",
        "sobre": "<p>Doutora em Engenharia Elétrica na área de Computação Gráfica e Processamento de Imagens pela Escola Politécnica da Universidade de São Paulo (POLI-USP).<br>Mestre em Ciências de Computação e Matemática Computacional pela USP de São Carlos (ICMC-USP) e Licenciada em Matemática pela UNESP. Foi pesquisadora na Divisão de Informática do Instituto do Coração da Faculdade de Medicina da USP (INCOR-FMUSP).É sócia-diretora da empresa AiiA Serviços e Soluções na área de consultoria em Tecnologia da Informação. Possui experiência na gestão de cursos de graduação na área de Computação e como docente do ensino superior nas áreas de Computação, Engenharia e Tecnologia da Informação.</p><br>",
        'link':'d_ads'
         }
    return (render(request, 'base_curso.html', context))

def gti(request):
    context = {
        "titulo": "GTI",
        "titulo_Pag": "Gestão de Tecnologia da Informação",
        "p1": "<p>A graduação em Gestão da Tecnologia da Informação prepara você para a liderança em TI. Apto a criar soluções para problemas nas organizações, você vai fazer a administração de infraestrutura física e lógica de ambientes informatizados.</p><p>O curso aborda técnicas precisas que servem para executar sistemas informatizados de forma segura para os negócios através do gerenciamento de recursos de tecnologia nas organizações, entre elas software, redes de computadores, bancos de dados e ferramentas para segurança da informação.</p><p>Além disso, você vai aprender a fazer a gestão de pessoas, a elaborar planos de negócios sobre TI e gerir projetos para garantir os acordos de nível de serviços (SLA).</p><p> </p>",
        "duracao": "Duração do Curso<p> 04 Semestres</p><p>| Tecnólogo |</p><p>Duração do Curso:</p><p>2020h</p><p>Modalidade:</p><p>Presencial</p><p>Unidade:</p><p>Barra Funda</p><p>Período:</p><p>Noturno</p><p>| 19h00 às 22h40 |</p><p>Mensalidade:</p><p>Noturno</p><p>R$ 584,00",
        "coord": "Osvaldo Kotaro Takai",
        "sobre": "<p>Professor de Graduação e Pós-Graduação da Faculdade. Consultor da AiiA Serviços e Soluções; tendo realizado diversos cursos de treinamento em Modelagem de Processos de Negócio e de Análise de Sistemas. Desenvolve seu projeto de doutorado junto ao grupo de Banco de Dados do IME-USP. Mestre e Bacharel em Computação pelo ICMC-USP. Atuou como ponto focal em Engenharia de Sistemas na Atech S/A do Grupo EMBRAER. Foi analista na Secretaria da Fazenda/SP na Análise e Especificação da Nova GIA Eletrônica. Participou da Análise e Especificação do Projeto Cartão Nacional de Saúde. Foi docente da UFScar - São Carlos, USP e UNAERP de Ribeirão Preto. Possui Certificação CPRE-FL Certified Professional for Requirements Engineering - Foundation Level, dado pelo IBQTS - Brasil, Licensed Examination Institute, como Licensed Examination Institute do IREB® (International Requirements Engineering Board). ICAgile Certified Professional (ICP) Certificate.</p>",
        'link':'d_gti'  
         }
    return render(request, 'base_curso.html', context)
def bd(request):
    context = {
        "titulo": "bd",
        "titulo_Pag": "Banco de Dados",
        "p1": "<p>O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas de desenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área.</p><p>A graduação mostra a importância da segurança de compartilhamento de dados nas empresas modernas e ensina as melhores técnicas e ferramentas de criação e implementação da mesma.</p><p>Na Impacta, você será preparado para o cenário real de gestão e liderança empresarial, garantindo a capacidade de comunicação e criatividade para solucionar problemas, atingir os melhores resultados, aumentar a produtividade e reduzir custos.</p><p> </p>",
        "duracao": "Duração do Curso<p> 04 Semestres</p><p>| Tecnólogo |</p><p>Duração do Curso:</p><p>2020h</p><p>Modalidade:</p><p>Presencial</p><p>Unidade:</p><p>Barra Funda</p><p>Período:</p><p>Noturno</p><p>| 19h00 às 22h40 |</p><p>Mensalidade:</p><p>Noturno</p><p>R$ 584,00",
        "coord": "Ana Cristina dos Santos",
        "sobre": "<p>Doutora em Engenharia Elétrica na área de Computação Gráfica e Processamento de Imagens pela Escola Politécnica da Universidade de São Paulo (POLI-USP). Mestre em Ciências de Computação e Matemática Computacional pela USP de São Carlos (ICMC-USP) e Licenciada em Matemática pela UNESP. Foi pesquisadora na Divisão de Informática do Instituto do Coração da Faculdade de Medicina da USP (INCOR-FMUSP). É sócia-diretora da empresa AiiA Serviços e Soluções na área de consultoria em Tecnologia da Informação. Possui experiência na gestão de cursos de graduação na área de Computação e como docente do ensino superior nas áreas de Computação, Engenharia e Tecnologia da Informação.</p>",
        'link':'d_bd'
         }
    return render(request, 'base_curso.html', context)



def logica(request):
    context = {
        "titulo": "Lógica",
        "titulo_Pag": "Introdução à lógica da programação",
        "p1": "<blockquote>O curso Introdução à Lógica de Programação objetiva ajudar o aluno a compreender a lógica de programação antes mesmo de trabalhar com quaisquer linguagens.</blockquote> Composto por conceitos, definições e exercícios práticos, o curso visa fazer com que o aluno desenvolva seu raciocínio lógico, enquanto conhece princípios básicos de desenvolvimento como algoritmos, sistemas de numeração, variáveis, entre outros",
        "titulo_intro": "Introdução à Lógica",
        "p2": "<strong>Lógica.</strong><strong>Programa: Tipos de linguagem de programação.</strong><strong>Tradutores: Tipos de tradutores.</strong>",
        "p3": "Interpretar a lógica computacional. Interpretar e desenvolver pseudocódigos, algoritmos e fluxogramas.",
        "avaliacao": "<blockquote>O critério de avaliação se dará através de avaliações contínuas, as AC’s e uma prova, se estabelecendo da seguinte maneira:</blockquote>        <table>        <colgroup span='3'></colgroup>        <tr>        <td>10 avaliações contínuas (Valendo de 0 a 10):</td><td> Representando 60'%' da nota</td>        </tr>        <tr>        <td>1 avaliação (prova) (Valendo de 0 a 10):</td><td>Representando 40'%' da nota.</td>        </tr>        </table>",
        "p4": "<p>Essencial para qualquer pessoa que queira se aprofundar em qualquer uma das sub-áreas da Informática, a Lógica de Programação é tema central para a melhor compreensão de como um computador executa suas tarefas e de como podemos programá-lo para melhor nos atender.</p>        <p>Programá-lo, não significa essencialmente, produzir um software, embora ainda seja a idéia principal que nos remete ao nos depararmos com a palavra programar.</p><p> Pode também significar, em escalasmenores, produzir pequenos scripts para páginas de Web ou desenvolver algumas macros em um aplicativo. Sempre que quiser tirar o melhor proveito de muitos dos aplicativos e outros recursos computacionais, de certa maneira, num nível superficial ou aprofundado, você utlizará conceitos e técnicas aprendidas com o estudo da Lógica de Programação.</p>",
        "biblio": "<p> <strong>•	Guimarães,</strong> Ângelo de Moura - Algorítmos e estruturas de dados / Ângelo de Moura Guimarães, Newton Alberto de Castilho Lages, - [Reimpr.]. - Rio de Janeiro : LTC, 2014, ISBN 978-85-216-0378-8</p> <p> <strong>•	Manzano,</strong> José Augusto N. G. - Algoritmos: Lógica para Desenvolvimento de Programação de Computadores / José Augusto N. G. Manzano, Jayr Figueiredo de Oliveira. 26 Ed. - São Paulo : Érica, 2012, ISBN 978-85-365-0221-2</p><p><strong>•Pereira,</strong> Silvio do Lago - Algoritmos e Lógica de Programação em C: Uma abordagem didática / Silvio do Lago Pereira. - 1 .e - São Paulo : Érica, 2010, ISBN 978-85-365-0327-1</p><p><strong>•	Pereira,</strong> Fábio - Microcontroladores PIC, Programação em C / Fábio Pereira - 7. Ed. - São Paulo, Érica, 2007, ISBN 978-85-7194-935-5</p><p><strong>•	Purdum,</strong> Jack - Beginning C for Arduino, Second Edition: Learn C Programming for theArduino</p>",

         }
    return render(request, 'base_disciplina.html', context)

def devops(request):
    context = {
        "titulo": "DevOps",
        "titulo_Pag": "Ambiente de Desenvolvimento e Operações",
        "p1": "<p>Combinação de filosofias culturais, práticas e ferramentas que aumentam a capacidade de uma empresa de distribuir aplicativos e serviços em alta velocidade.(Amazon);</p><p>Conjunto de princípios, práticas e produtos, que visa ajudar organizações a entregar software de alta qualidade para o mercado de forma mais rápida e ao mesmo tempo minimizar custos e riscos (IBM); DevOps é uma mudança das práticas convencionais de desenvolvimento e entrega de sistemas (iMaster);</p><p> DevOps é mais de que uma tecnologia. Trata-se de uma ideia que exige evolução cultural. São as pessoas, os processos e as ferramentas certas para agilizar o ciclo de vida do aplicativo e torna-lo previsível (Microsoft).</p>",
        "titulo_intro": "Introdução à DevOps",
        "p2": "Diuretics paradis num copo é motivis de denguis. Delegadis gente finis, bibendum egestas augue arcu ut est. Praesent vel viverra nisi. Mauris aliquet nunc non turpis scelerisque, eget. Casamentiss faiz malandris se pirulitá.",
        "p3": "Mussum Ipsum, cacilds vidis litro abertis. Quem num gosta di mé, boa gentis num é. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo! Paisis, filhis, espiritis santis.",
        "avaliacao": "<blockquote>O critério de avaliação se dará através de avaliações contínuas, as AC’s e uma prova, se estabelecendo da seguinte maneira:</blockquote>        <table>        <colgroup span='3'></colgroup>        <tr>        <td>10 avaliações contínuas (Valendo de 0 a 10):</td><td> Representando 60'%' da nota</td>        </tr>        <tr>        <td>1 avaliação (prova) (Valendo de 0 a 10):</td><td>Representando 40'%' da nota.</td>        </tr>        </table>",
        "p4": "<p>Essencial para qualquer pessoa que queira se aprofundar em qualquer uma das sub-áreas da Informática, a Lógica de Programação é tema central para a melhor compreensão de como um computador executa suas tarefas e de como podemos programá-lo para melhor nos atender.</p>        <p>Programá-lo, não significa essencialmente, produzir um software, embora ainda seja a idéia principal que nos remete ao nos depararmos com a palavra programar.</p><p> Pode também significar, em escalasmenores, produzir pequenos scripts para páginas de Web ou desenvolver algumas macros em um aplicativo. Sempre que quiser tirar o melhor proveito de muitos dos aplicativos e outros recursos computacionais, de certa maneira, num nível superficial ou aprofundado, você utlizará conceitos e técnicas aprendidas com o estudo da Lógica de Programação.</p>",
        "biblio": "<p><strong>•	Alves,</strong> Wlliam Pereira - Lógica de Programação de Computadores - Ensino Didático / William Pereira Alves - 1. Ed. - São Paulo, Érica, 2010, ISBN 978-85-365-0289-2</p> <p> <strong>•	Farrer,</strong> Harry - Programação estruturada de computadores : algortimos estruturados / Harry Farrer [et al.] - 3 ed. [Reimpr.] - Rio de Janeiro, LTC 2014, ISBN 978-85-216-1180-6</p><p><strong>•	Niku,</strong> Saeed Benjamin - Intrdoução à robótica : análise, controle, aplicações / Saeed Benjamin Niku : Tradução e revisão técnica Sérgio Gilberto Taboada - Rio de Janeiro : LTC, 2013. ISBN 978-85-216-2237-6</p><strong>•	Schildt,</strong> Hebert - C Completo e Total / <strong>Hebert Schildt,</strong> Pearson; Edição: 3 (1 de janeiro de 1997), ISBN 978-85-346-0595-3</p><p> •	Embedded C Programming and the Atmel AVR / <strong>Richard H. Barnett,</strong><strong> Sarah Cox,</strong> Larry O'Cull, ISBN 9781418039592, 2 ed., 2, Editora CengageLearning, 2012</p>",
         }
    return render(request, 'base_disciplina.html', context)
def tecweb(request):
    context = {
        "titulo": "TecWeb",
        "titulo_Pag": "Tecnologia Web",
        "p1": " disciplina de Tecnologia Para Web visa permitir ao aluno aplicar de forma prática tecnologias como HTML, CSS e Javascript para desenvolvimento e autoração de produtos hipermidiáticos, tais como sites para Web, aplicativos multiplataforma, etc; esclarecer cada etapa do ciclo projetivo de um produto hipermidiático, desde o projeto até a publicação na World Wide Web, através de exercícios e atividades práticas; e colocar em perspectiva o papel do designer em relação à Internet das coisas, encorajando metodologias de desenvolvimento como o design responsivo, o aprimoramento progressivo, foco em acessibilidade e semântica do conteúdo.",
        "p2": "O programa tem um enfoque bastante acentuado na componente prática com o objetivo de tornar transparente para os alunos o processo técnico de elaboração de um website. São apresentadas gradativamente as três tecnologias que constituem os padrões web: HTML, Javascript e CSS",
        "p3": "Mussum Ipsum, cacilds vidis litro abertis. Quem num gosta di mé, boa gentis num é. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo! Paisis, filhis, espiritis santis.",
        "avaliacao": "<blockquote>O critério de avaliação se dará através de avaliações contínuas, as AC’s e uma prova, se estabelecendo da seguinte maneira:</blockquote>        <table>        <colgroup span='3'></colgroup>        <tr>        <td>10 avaliações contínuas (Valendo de 0 a 10):</td><td> Representando 60'%' da nota</td>        </tr>        <tr>        <td>1 avaliação (prova) (Valendo de 0 a 10):</td><td>Representando 40'%' da nota.</td>        </tr>        </table>",
        "p4": "<p>Essencial para qualquer pessoa que queira se aprofundar em qualquer uma das sub-áreas da Informática, a Lógica de Programação é tema central para a melhor compreensão de como um computador executa suas tarefas e de como podemos programá-lo para melhor nos atender.</p>        <p>Programá-lo, não significa essencialmente, produzir um software, embora ainda seja a idéia principal que nos remete ao nos depararmos com a palavra programar.</p><p> Pode também significar, em escalasmenores, produzir pequenos scripts para páginas de Web ou desenvolver algumas macros em um aplicativo. Sempre que quiser tirar o melhor proveito de muitos dos aplicativos e outros recursos computacionais, de certa maneira, num nível superficial ou aprofundado, você utlizará conceitos e técnicas aprendidas com o estudo da Lógica de Programação.</p>",
        "biblio": "<p>Delegadis gente finis, bibendum egestas augue arcu ut est. Quem num gosta di mim que vai caçá sua turmis! Leite de capivaris, leite de mula manquis sem cabeça. Em pé sem cair, deitado sem dormir, sentado sem cochilar e fazendo pose.</p>",
         }
    return render(request, 'base_disciplina.html', context)
def d_ads(request):
    context = {
    "curso": "",
    "um": "<p>Comunicação e Expressão: 80 horas<br />Fundamentos de Banco de Dados: 80 horas<br />Introdução à Internet das Coisas - IoT: 80 horas<br /><a href='logica'>Lógica de Programação:</a> 80 horas<br />Matemática Aplicada: 80 horas</p>",
    "dois": "<p>Linguagem de Programação II: 80 horas<br />Linguagem SQL: 80 horas<br /><a href='tecweb'>Tecnologia Web:</a> 80 horas<br />Engenharia de Software: 80 horas<br />Gestão de Projetos: 40 horas<br /><a href='devops'>Ambiente de Desenvolvimento e Operação - DevOps:</a> 80 horas<br />Sociedade e Sustentabilidade - Optativa: 40 horas<br />Linguagem Brasileira de Sinais - LIBRAS - Optativa: 40 horas</p>",
    "tres": "<p>Desenvolvimento de Aplicações Distribuídas: 80 horas<br />Estrutura de Dados: 80 horas<br />Análise e Modelagem de Sistemas: 80 horas<br />Modelagem de Processos de Negócio: 80 horas<br />Interface Homem-Computador: 40 horas<br />OPE1 - Oficina Projeto Empresa 1: 120 horas</p>",
    "quatro": "<p>Arquitetura e Projeto de Sistemas: 80 horas<br />Desenvolvimento para Dispositivos Móveis: 80 horas<br />Desenvolvimento para Internet das Coisas: 80 horas<br />Qualidade de Software: 80 horas<br />OPE2 - Oficina Projeto Empresa 2: 120 horas<br />Legislação e Ética: 40 horas</p>",
    }
    return render(request, 'base_curricular.html', context)
def d_gti(request):
    context = {
    "curso": "",
    "um": "<p>Comunicação e Expressão: 80 horas (EAD)<br />Banco de Dados: 80 horas<br />Introdução à Internet das Coisas - IoT: 80 horas<br />Linguagem de Programação: 80 horas<br />Lógica da Programação: 80 horas<br />Matemática Aplicada: 80 horas</p>",
    "dois": "<p>Ambiente de Desenvolvimento e Operações - DevOps: 80 horas<br />Análise Exploratória de Dados: 80 horas<br />Sistemas Integrados de Gestão: 80 horas<br />Engenharia de Software: 80 horas<br />Gestão Estratégica de Pessoas: 80 horas<br />Gestão de Projetos: 40 horas (EAD)<br />Optativa (Sociedade e Sustentabilidade / Língua Brasileira de Sinais - LIBRAS): 40 horas (EAD)</p>",
    "tres": "<p>Análise de Viabilidade de Projetos: 80 horas<br />Modelagem de Processos de Negócio: 80 horas<br />Inteligência de Negócios: 80 horas<br />Qualidade de Software: 80 horas<br />Legislação e Ética: 40 horas (EAD)<br />Oficina Projeto Empresa 1 - OPE1: 120 horas (40 EAD)</p>",
    "quatro": "<p>Gestão Estratégica de TI: 80 horas<br />Gestão de Infraestrutura de TI: 80 horas<br />Gestão da Segurança de Informação: 80 horas (EAD)<br />Gestão da Qualidade: 80 horas<br />Governança de TI: 80 horas<br />Oficina Projeto Empresa 2 - OPE2: 80 horas</p>",
    }
    return render(request, 'base_curricular.html', context)
def d_bd(request):
    context = {
    "curso": "",
    "um": "<p>Comunicação e Expressão: 80 horas<br />Fundamentos de Banco de Dados: 80 horas<br />Introdução à Internet das Coisas - IoT: 80 horas<br />Linguagem de Programação: 80 horas<br />Lógica de Programação: 80 horas<br />Matemática Aplicada: 80 horas</p>",
    "dois": "<p>Linguagem SQL: 80 horas<br />Análise Exploratória de Dados: 80 horas<br />Ambiente de Desenvolvimento e Operação - DevOps: 80 horas<br />Desenvolvimento de Sistemas: 80 horas<br />Engenharia de Software: 80 horas<br />Sociedade e Sustentabilidade - Optativa: 40 horas<br />Língua Brasileira de Sinais - LIBRAS - Optativa: 40 horas</p>",
    "tres": "<p>Developing Database: 80 horas<br />Estrutura de Dados: 80 horas<br />Business Intelligence: 80 horas<br />Data Analytics: 80 horas<br />OPE1 - Oficina Projeto Empresa 1: 120 horas</p>",
    "quatro": "<p>Administração de Banco de Dados: 80 horas<br />Qualidade de Governança de Dados: 80 horas<br />Segurança de Banco de Dados: 80 horas<br />Big Data: 80 horas<br />Computação Cognitiva: 80 horas<br />OPE2 - Oficina Projeto Empresa 2: 120 horas<br />Legislação e Ética: 40 horas</p>",
    }
    return render(request, 'base_curricular.html', context)

