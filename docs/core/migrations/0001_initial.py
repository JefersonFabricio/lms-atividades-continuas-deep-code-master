# Generated by Django 2.0.4 on 2018-05-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='Login', max_length=30)),
                ('senha', models.IntegerField(db_column='Senha')),
                ('nome', models.CharField(db_column='Nome', max_length=60)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('celular', models.IntegerField(db_column='Celular')),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
                ('ra', models.IntegerField(db_column='RA')),
                ('foto', models.CharField(blank=True, db_column='Foto', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'Aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_column='Titulo', max_length=30)),
                ('descricao', models.CharField(blank=True, db_column='Descricao', max_length=300, null=True)),
                ('conteudo', models.CharField(blank=True, db_column='Conteudo', max_length=500, null=True)),
                ('tipo', models.CharField(db_column='Tipo', max_length=20)),
                ('extras', models.CharField(blank=True, db_column='Extras', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Atividade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Atividadevinculada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotulo', models.CharField(db_column='Rotulo', max_length=5)),
                ('status', models.CharField(db_column='Status', max_length=20)),
                ('dtiniciorespostas', models.DateField(db_column='DtInicioRespostas')),
                ('dtfimrespostas', models.DateField(db_column='DtFimRespostas')),
            ],
            options={
                'db_table': 'AtividadeVinculada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='Login', max_length=30)),
                ('senha', models.IntegerField(db_column='Senha')),
                ('nome', models.CharField(db_column='Nome', max_length=60)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('celular', models.IntegerField(db_column='Celular')),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
            ],
            options={
                'db_table': 'Coordenador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=50)),
                ('sigla', models.CharField(db_column='Sigla', max_length=3)),
            ],
            options={
                'db_table': 'Curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=60)),
                ('data', models.DateField(db_column='Data')),
                ('status', models.CharField(db_column='Status', max_length=8)),
                ('planodeensino', models.CharField(db_column='PlanoDeEnsino', max_length=2000)),
                ('cargahoraria', models.IntegerField(db_column='CargaHoraria')),
                ('competencias', models.CharField(db_column='Competencias', max_length=500)),
                ('habilidades', models.CharField(db_column='Habilidades', max_length=500)),
                ('ementa', models.CharField(db_column='Ementa', max_length=500)),
                ('conteudoprogramatico', models.CharField(db_column='ConteudoProgramatico', max_length=500)),
                ('bibliografiabasica', models.CharField(db_column='BibliografiaBasica', max_length=500)),
                ('bibliografiacomplentar', models.CharField(db_column='BibliografiaComplentar', max_length=500)),
                ('percentualpratico', models.IntegerField(db_column='PercentualPratico')),
                ('percentualteorico', models.IntegerField(db_column='PercentualTeorico')),
            ],
            options={
                'db_table': 'Disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplinaofertada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtiniciomatricula', models.DateField(db_column='DtInicioMatricula')),
                ('dtfimmatricula', models.DateField(db_column='DtFimMatricula')),
                ('ano', models.IntegerField(db_column='Ano')),
                ('semestre', models.IntegerField(db_column='Semestre')),
                ('turma', models.CharField(db_column='Turma', max_length=1)),
                ('metodoligia', models.CharField(blank=True, db_column='Metodoligia', max_length=500, null=True)),
                ('recursos', models.CharField(blank=True, db_column='Recursos', max_length=500, null=True)),
                ('criterioavaliacao', models.CharField(blank=True, db_column='CriterioAvaliacao', max_length=500, null=True)),
                ('planodeaulas', models.CharField(blank=True, db_column='PlanoDeAulas', max_length=500, null=True)),
            ],
            options={
                'db_table': 'DisciplinaOfertada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(db_column='Titulo', max_length=50)),
                ('resposta', models.CharField(db_column='Resposta', max_length=500)),
                ('dtentrega', models.DateField(db_column='DtEntrega')),
                ('status', models.CharField(db_column='Status', max_length=20)),
                ('nota', models.TextField(blank=True, db_column='Nota', null=True)),
                ('dtavaliacao', models.DateField(blank=True, db_column='DtAvaliacao', null=True)),
                ('obs', models.CharField(blank=True, db_column='Obs', max_length=300, null=True)),
            ],
            options={
                'db_table': 'Entrega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(db_column='Assunto', max_length=50)),
                ('referencia', models.CharField(db_column='Referencia', max_length=300)),
                ('conteudo', models.CharField(db_column='Conteudo', max_length=2000)),
                ('status', models.TextField(db_column='Status')),
                ('dtenvio', models.DateField(db_column='DtEnvio')),
                ('dtresposta', models.DateField(blank=True, db_column='DtResposta', null=True)),
                ('resposta', models.CharField(blank=True, db_column='Resposta', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'Mensagem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='Login', max_length=30)),
                ('senha', models.IntegerField(db_column='Senha')),
                ('nome', models.CharField(db_column='Nome', max_length=60)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('celular', models.IntegerField(db_column='Celular')),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
                ('apelido', models.CharField(db_column='Apelido', max_length=30)),
            ],
            options={
                'db_table': 'Professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitacaomatricula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtsolicitacao', models.DateField(db_column='DtSolicitacao')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=10, null=True)),
            ],
            options={
                'db_table': 'SolicitacaoMatricula',
                'managed': False,
            },
        ),
    ]