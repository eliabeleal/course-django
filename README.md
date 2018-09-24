# Anotações do Curso de Django

<!-- Instrutor: Gregory Pacheco (Engenheiro/Arquiteto de Software) -->

## Definições

*O que é?*

Framework web baseado em python, ou seja, uma caixa de ferramentas para criação web.

Ler: Documentation/First Steps

PIP é o instalador de pacotes python
VirtualEnv: me isola do sistema operacional. Só deve instalar o django dentro de uma virtual env, pois assim é possível usar várias versões de django para trabalhar em vários projetos
Todo desenvolvimento em Python tem o conceito de ambiente virtual. (virtualenv)
É uma pasta com vários arquivos que isolam o sistema
Usar o pip: só no myenv. Quando dentro de uma virtualenv o python já é python 3.6.

## Comandos

lista o conteúdo do arquivo:

```sh
 eli@PC:~$ cat
```

Entrar no ambiente virtual:

```sh
eli@PC:~$ source myenv/bin/activate

**ou**

eli@PC:~$ . myenv/bin/activate
```

## Aula 06

Criar uma pasta para o projeto:

```sh
eli@PC:~$ mkdir projetoteste
```

Entrar nela:

```sh
eli@PC:~$ cd projetoteste
```

Criar uma virtual env:

```sh
eli@PC:~$ python3 -m venv <nome do ambiente virtual>
```

Se não funcionar:

```sh
eli@PC:~$ sudo apt-get install python3.6-venv
```

Ativar o ambiente virtual:

```sh
eli@PC:~$ source <nome do ambiente virtual>/bin/activate
```

Install Django:

```sh
eli@PC:~$ pip install django
```

Criar o projeto django:

```sh
eli@PC:~$ django-admin startproject <nome do projeto>
```

OBS: para criar um projeto dentro da pasta corrente usar o <.>

Roda o projeto  no servidor local (apenas para os teste locais)

```sh
eli@PC:~$ python manage.py runserver
```

### Analisando um projeto

\_\_init\_\_.py  
_transforma todas as pastas em um pacote python_

settings.py  
_mais importante do projeto_

urls.py  
_onde ficam as URLs, vem apenas com a admin habilitada_

wsgi.py  
_aponta para um servidor, entrepoint, a aplicação começa nele, configurar o servidor_

manage.py  
_tirar proveito do que ele fornece, não será necessário modificar nada nele_

### Analisando o settings

**import os**  
_ver os caminhos do sistema operacional, é um biblioteca_

**BASE_DIR**  
_tem a url base do projeto_

**SECRET_KEY**  
_é preciso manter em segurança, pois faz a criptografia de senhas_

**DEBUG**  
_se está modo de desenvolvimento marca true, senão false, se não expõe informações sensíveis do projeto_

**ALLOWED_HOSTS**  
_endereços que o django vai responder, é o domínio. Pois o django só responde requisições que vem desse domínio_

**INSTALLED_APPS**  
_aplicações que já vem instaladas no django_

**MIDDLEWARE**  
_camadas que o django passa, segurança, sessão, etc_

**ROOT_URLCONF**  
_aponta as URLs principais do django_

**TEMPLATES**  
_são configurações de templates que já vem com o django_

**WSGI_APPLICATION**  
_aponta para a variável application dentro do wsgi_

**DATABASE**  
_configuração de banco de dados_

**AUTH_PASSWORD_VALIDATORS**  
_validadores de senha_

**LANGUAGE_CODE**  
_linguagem usada_

**TIME_ZONE**  
_Local onde roda, ex: America/Sao_Paulo_

**USE_I18N**  
_Se usa internacionalização_

**USE_L10N**  
_Para regionalização_

**USE_TZ**  
_Se quer usar time zone ou não_

**STATIC_URL**  
_pasta base do static_

## AULA 07

**O que é uma requisição web?**  
_É a solicitação de coisas para o servidor, de forma bem básica_  
**Como funciona as requisições?**  
_Com o protocolo http_  

### Passos para as requisições

1. WEB SERVER  
   _servidor que hospeda a aplicação_
2. WSGI  
   _descobre onde está os settings_
3. REQUEST (MIDDLEWARE)  
   _validação da requisição para saber se é seguro_
4. URL RESOLUTION (ROOT-URLCONF)
   _lista das urls_
5. VIEW (views.py)  
   _a função que vai processar a response, pode precisar ir para qualquer um desses, o que ela precisar fazer:_
    1. MODEL (models.py)
    2. MANAGERS
    3. DATABSE
6. TEMPLATE (MIDDLEWARE)  
   _página (html, css, js, imagens)_
7. RESPONSE  
   _quando o template está pronto ele retorna uma response_
8. WSGI  
   _volta para wsgi_

## AULA 08

**O que são URLs?**  
_São os caminhos por onde a requisição vai passar.
No django elas estão na urls.py (porteiro)
Antes ela passa pela validação e segurança_  
**Qual a função?**  
_Informar o que a request precisa_

**O que mudou da versão 1.x para a versão 2.x?**  
_Na 2.x você não precisa escrever necessariamente suas urls com regex. Agora é possível usar funções nativas_

### Criando a primeira URL

1. Adiciona a nova url em urls.py no ulrpatterns

    Na função path o primeiro parâmetro é a nome da url, depois tem a view, que faz o processamento da url. Por padrão o admin já está configurada (é uma aplicação).

    exemplo

    ```py
    path(‘hello/’, hello)
    ```

2. Ainda não existe a função hello(), para criá-la, cria um arquivo com o nome views.py. Nele se faz as funções que serão chamadas na view.

    exemplo

    ```py
    def hello():
        pass
    ```

3. Para que o urls.py reconheça essa nova função, é só fazer o import.

    exemplo

    ```py
    from .views import hello
    ```

4. Mas o django reclama, pois ainda não passamos nenhum parâmetro para essa função. Ainda assim, o django tenta passar um parâmetro que é a request.

    exemplo
    ```py
    def hello(request):
    ```

5. Agora a questão é que a função não está retornando um objeto HttpResponse. Pois toda view retorna ele.

    exemplo
    ```py
    from django.http import HttpResponse

    def hello (request):
        return HttpResponse(‘Olá Mundo’)
    ```

## AULA 09

### VIEWS

**O que são VIEWS (FUNCTIONS)?**  
_É a ação que executa alguma coisa da request. Ela pode ser uma classe (CLASS\_BASE\_VIEW) ou uma função, vamos ver a principio como função_

#### Partes de uma função

```py
def fname(request, ...):
    statements
```

| part         | description                          |
| -----------: | ------------------------------------ |
| `def`        | caracteriza uma função em PYTHON     |
| `fname`      | nome da função                       |
| `()`         | parâmetros da função                 |
| `request`    | principal parâmetro da função django |
| `...`        | demais parâmetros da função          |
| `:`          | inicio dos comandos                  |
| `statements` | comandos                             |

É possível realizar chamada de outras funções dentro do _views.py_ sem precisar apontá-las no _urls.py_. Dessa forma, a função terá um escopo local.

## AULA 10

### MODELS

As views para executar o papel precisa acessar os MODELs. Os prjetos são compostas de APP's. E cada APP executa uma função específica do projeto.

#### Criando uma APP de gerência de clientes

```sh
(myvenv) eli@PC:~$ python manage.py startapp clientes
```

Cria a estrutura da aplicação de gestão de clientes

Nela Temos os arquivdos de:
**\_\_init\_\_.py**  
que prova que isso é um pacote python

##### admin.py

pra registrar os models para aparecer no admin do django

##### apps.pyx

##### models.py

onde se desenvolve os models

##### tests.py

##### views.py

é possível ter views próprias dessa aplicação

#### clientes/models.py

Models são classes que descrevem os modelos do meu negócio. É onde a inteligência estará embutida.

[Documentação](https://docs.djangoproject.com/en/2.1/topics/db/models/)

```py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
```

Na primeira linha, o django já provê um import de uma classe básica de modelos, nela o django concentra boa parte da inteligencia de automação. Essa classe _Person_ já herda de Model. Esse é um exemplo de classe que cria dois atributos de primeiro e último nome. Esse atributos estarão correlacionados com o banco de dados pelos campos _models_

A depois de criar o as classes que serão usadas no model, cria-se o banco de dados. No settings, por padrão usa-se o db.sqlite3. Isso está configurado no settings. Quando se cria o DB a composição dele é baseada nas migrações (migrations). Ela é uma classe que descreve o que vai ter no DB, as tabelas, os registros.

As aplicações que vem junto com o django também precisam ter suas migrações. Para isso usa-se o comando:

```sh
eli@PC:~$ python manage.py migrate
```

Depois desse comando, o django cria tudo que existe nas aplicações e precisa de um DB. Mas as aplicações novas não são criadas automaticamente, é preciso registra-las em INSTALLED_APPS. Basta apenas colocar o nome dela. Depois usa-se o comando:

```sh
eli@PC:~$ python manage.py makemigrations
```

Esse comando cria a migration da aplicação que estamos adicionando. Nesta nova migration, é possível ver como é criada a tabela no DB. Esse comando só cria o arquivo para ser aplicado no DB. Então para aplicar no DB usa-se o comando anterior.

## AULA 11

### DJANGO ADMIN

O Admin é um aplicação que o Django provê que automatiza a criação de Backends. Implementa o OAuth e outras validações. Para comecar a usa-lo é preciso criar os usuários. Com o seguinte comando:

```sh
eli@PC:~$ python manage.py createsuperuser
```

Depois escolhe o user name, email e senha. Depois de logar o django acessa a sessão de administração. Ele já tem um sistema de gestão de grupos e usuários por padrão. O primeiro é criado por linha de comando, mas o sengundo pode ser criado nessa tela. Grupos e usuários são models que o django já traz pronto. Além de poder administrar os models do django é possível administrar os nossos models. Isso é feito no arquivo _admin.py_ do model que criamos. Dessa forma:

```py
from django.contrib import admin
from .models import Person

admin.site.register(Person)
```

Depois que isso é feito, aparecerá o nome da aplicação (clientes) e o model que foi criado (Person). Quando é criado um Person nessa aplicação, o nome que aparecerá será Person object(1). Pois no model que criamos é necessário criar uma função que sete o nome do objecto Person a ser criado com o nome da pessoa, dessa forma:

```py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()

    def __str__(self):
        return self.first_name
```

## AULA 12

### TEMPLATES

Em um cenário normal as views retornam um _template_. Por enquanto nossas _VIEWS_ estão retornando um texto simples. O que não é um cenário realista. O django já provê a renderização de _templates_. Que é basicamente pegar o dado que a gente vai fornecer transformar isso numa RESPONSE, colocar as variáveis que forem necessárias e manda de volta pro navegador.
Para isso é preciso definir no _settings_ onde iremos guardar nossos _TEMPLATES_. Isso é feito na variável **DIRS**. Cria-se uma pasta com os meus _templates_, esta tem que estar ao lado de _manage.py_.

```py
    TEMPLATES = [
        'DIRS': ['<nome da pasta>']
    ]

```

O primeiro arquivo é o _index.html_ (Isso é um _template_). Após criar o _template_, este deve ser carregado dentro da _view_. Para isso usa-se a função _render_. Que vai ler o _template_ e transformar numa _response_.

```py
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')
```

Quando vai mandar de volta o _template_ ele submente a _response_ a todas as validações iniciais (**Middleware**)

Quando for necessário ler uma variável que tem origem em uma _view_, usa-se para isso mais um parâmentro do render, ele recebe uma variável que é lida com a linguagem de _template_ jinja.

```py
from django.shortcuts import render

def fname2(request, nome):
    idade = lerDoBanco(nome)
    return render(request, 'pessoa.html', {'v_idade': idade})
```

Essa variável _v\_idade_ estará disponível para ser lida dentro do _template_

```html
<body>
    A pessoa foi encontrada, ela tem {{ v_idade }} anos
</body>
```

Esse abre e fecha parênteses indica que estamos usando a linguagem de templates do django (jinja). Ainda é possível criar lógicas de programação (códigos):

```html
<body>
    {% if v_idade > 0%}
        A pessoa foi encontrada, ela tem {{v_idade}} anos
    {% else %}
        Pessoa não encontrada
    {% endif %}
</body>
```

Não sendo uma lógica de negócio é permitido colocar no _template_, é apenas uma lógica de usuário.

## AULA 13

### ARQUIVOS ESTÁTICOS

Até agora a gente viu _TEMPLATES_ que são arquivos não estáticos. Pois ele pode ter variáveis, ifs, fors. Enfim, se ele vai ser processado pelo django e entregue na response, será considerado arquivo não estático. Logo, além dos htmls, precisamos entregar arquivos como CSS, JS, Imagens, etc.

#### DEFININDO ONDE ESSES ARQUIVOS IRÃO FICAR

No settings existe uma variável chamada _STATICFILES\_DIRS_. Nela se define o nome do seu diretório que contém os arquivos estáticos.

```py
STATICFILES_DIRS = [
    '<nome do diretório>',
]
```

O projeto vai procurar no diretório raiz. No mesmo nível de TEMPLATES. Pra carregar no TEMPLATE usa-se a template tag:

```html
{% load static %}
```

[Documentação](https://docs.djangoproject.com/pt-br/2.1/howto/static-files/)

Depois disso é possível carregar os arquivos no head

```html
<link rel="stylesheet" href="{% static '<nome do arquivo>' %}">
```

## AULA 14

### Arquivos de Media

Assim como os arquivos estáticos, esses arquivos tem pode difinição que ele será servido da forma que ele está, ele não será processado. A diferença entre os arquivos de media e os arquivos estáticos é que estes são postos no sistema pelo desenvolvedor, já aqueles são carregados pelo usuário. São exemplos: fotos perfil, documentos, vídeos.

#### DEFININDO MEDIA_URL

No arquivo _settings.py_:

```py
# NOME DA URL QUE SERÁ USADA
MEDIA_URL = '/<nome da url(ex. media)>/'

# PASTA ONDE SERÃO SALVOS OS ARQUIVOS DE MEDIA
MEDIA_ROOT = 'media'
```

Cria-se a pasta para salvar os arquivos ao lado das demais. Para pode usar os arquivos de media, usa-se um model que tenha esse campo. No model criado, PERSON, adicionar um campo de _photos_:

```py
# ESSE PRIMEIRO PARÂMETRO PERMITE SALVAR EM UMA SUBPASTA DE MEDIA
# O SEGUNDO E TERCEIRO, PERMITEM QUE ESSE CAMPO SEJA OPCIONAL, SERVE PARA OS DEMAIS TAMBÉM
photo = models.ImageField(upload_to='clients_photos', null='true', blank='true')
```

Agora cria-se o campo no banco, pois toda vez que houver uma alteração dentro dos _MODELS_ é preciso migra-las para o banco.

```sh
eli@PC:~$ python manage.py makemigrations
```

Depois aplica-se essas migrações

```sh
eli@PC:~$ python manage.py migrate
```

##### NOTE

Sempre que utilizar um campo de imagem no django pode ser necessário instalar a biblioteca Pillow que manipula imagem.

```sh
(venv) ~/eli@PC:~$ pip install Pillow
```

Pode ocorrer de os nomes dos arquivos de imagens serem iguais, automaticamente o django faz um rename, mas é possível criar uma função que faça essa manipulação no _upload\_to_, deverá estar no MODEL.

Quando você tentar abrir essa imagem upada, será exibida um Erro 404, pois o servidor não está pronto para servir essa imagem. Um técnica boa é enviar essa imagem para a Amazon.

## AULA 15

### Exibindo arquivos de media

É uma forma de servir os arquivos de media durante o [desenvolvimento](https://docs.djangoproject.com/pt-br/2.1/howto/static-files/#serving-static-files-during-development)

O django não serve arquivos estáticos nem de media. Ele cuida de arquivos **python**. Quando for fazer o deploy, é importante ver uma forma mais profissional de servi-los.  
Mas é possível fazer uma "**gambiarra**" para que, em tempo de desenvolvimento, você possa ver seus arquivos de imagens.
No urls.py

```py
from django.conf import settings
from django.conf.urls.static import static

# USA-SE ESSA FUNÇÃO ESTÁTICA PARA QUE O DJANGO ADICIONE A URL QUE FOI CONFIGURADA PARA MEDIA NO SETTINGS, ASSIM COMO A PASTA QUE INDICA ONDE ESTÁ O ARQUIVO ENVIADO
urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## AULA 16

### Preparar para o Primeiro CRUD

**C**: Create  
**R**: Read  
**U**: Update  
**D**: Delete  

#### 1. STEP

É preciso criar as URLs da nossa aplicação. Pois se todas ficarem aculadas no arquivos urls.py principal, acaba virando uma bagunça. Então para isso cria-se um arquivo urls.py dentro da aplicação de clientes no mesmo nível dos demais arquivos.
**_clients/urls.py_**

```py
from django.urls import path
from .views import persons_list
urlpatterns = [
    # EXEMPLO DE USO
    path('list/', persons_list)
]
```

#### 2. STEP

Criando a view da aplicação **client**
**_clients/views.py_**

```py
from django.shortcuts import render

# EXEMPLO DE USO
def persons_list(request):
    return render(request, 'pessoa.html')
```

#### 3. STEP

**_urls.py_**

```py
#[...]
# INCLUI URLS DE OUTRAS APLICAÇÕES
from django.urls import include
# IMPORTA DESSA FORMA AS URLS DA APLICAÇÃO DE CLIENTES
from clientes import urls as clients_urls

urlpatterns = [
    path('person/', include(clients_urls)),
]
```

## AULA 17

### CRUD - Read

Lendo clientes no banco de dados.

#### 1. Criar um novo template _person.html_

#### 2. Importar o model Person e ler as pessoas do banco

O django possibilita a manipulação/ler de dados do banco através de manager. Por padrão todo model já vem com um manager chamado _objects_  

*_clients/views.py_*

```py
from django.shortcuts import render
# IMPORTANDO PERSON
from .models import Person

# EXEMPLO DE USO
def persons_list(request):
    # LENDO
    # ESSE COMANDO É EQUIVALENTE A select * from person NO SQL
    persons = Person.objects.all()
    # OUTRAS QUERYS
    # persons = Person.objects.get(id=1)
    # PASSANDO A VARIÁVEL PARA O TEMPLATE
    return render(request, 'person.html', {'persons': persons}  )
```

#### 3. Lendo a variável no template

Usando a linguagem de template do Django

```html
<body>
    <ul>
        {% for person in persons %}
            <li>{{ person.first_name }}</li>
        {% endfor %}
    </ul>
</body>
```

## AULA 18

### CRUD - CREATE

Conceito de formulário, iremos contruir todo o caminho que a requisição irá passar. Ao invés de pedir informações para o banco, iremos envia-las para o banco de dados.

**clientes/urls.py**

```py
from .views import persons_new

urlpatterns = [
    # É POSSÍVEL DAR APELIDOS PARA AS URLS
    path('new/', persons_new, name="person_new"),
]
```

**clientes/views.py**

```py
def persons_new(request):
    pass
```

#### templates

Quando a url entregar a view, esta vai entregar um formulário a ser preenchido. Então criamos um template com o nome _person\_form.html_.

```html
<body>
    <!-- a classe action server para referenciar o que o botão irá fazer -->
    <form action="{% url 'person_new' %}" method="POST">
    <!--O botão tem que ter o tipo submite, que enviarar todo o form para a url informada e depois para o servidor-->
        <button type="submit"></button>
    </form>
</body>
```

#### models

[Documentação para o django forms](https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/)

Usaremos o ModelForm que baseado no model irá cria todas as validações do formulário

#### forms

Criando a classe dentro de um arquivo forms na aplicação

**clientes/forms.py**

```py
from django.forms import ModelForm
from .models import Person

# ESSA CLASSE HERDA DO MODELFORM
class PersonForm(ModelForm):
    # CRIANDO UMA SUBCLASSE PARA INDICAR QUAL MODEL SERÁ A REGRA DE NEGÓCIOS PARA ESSE FORM E OS CAMPOS PARA O MESMO
    class Meta:
        model = Person
        # SÃO OS CAMPOS QUE TEMOS NO MODEL
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
```

**clientes/views.py**

Importa-se o form para dentro da view. Existem dois momentos que são necessários tratar. O primeiro é quando enviamos um form novo para nossa página.

```py
from .forms import PersonForm

def persons_new(request):
    # PRIMEIRO MOMENTO, USANDO O request.POST, QUANDO O CLIENTE CLICAR EM SALVAR SERÁ ENVIDADO UM FORMULÁRIO COM OS DADOS PREENCHIDOS. CASO O CLIENTE ESTEJA ABRINDO A PÁGINA PELA PRIMEIRA VEZ, VOCÊ PODE MANDAR UM form VAZIO, USANDO O SEGUNDO PARÂMETRO None
    form = PersonForm(request.POST, none)
    # É PRECISO ENTREGAR ESSE form LÁ PARA A PÁGINA. ALÉM DISSO, QUERO INSERIR DENTRO DO html A VARIÁVEL form.
    return render(request, 'person_form.html', {'form': form})
```

**templates/person_form.html**

```html
<body>
    <form action="{% url 'person_new' %}" method="POST" enctype="multipart/form-data">
        <!--importante sempre incluir em todo formulário a variável csrf_token, que é uma proteção para formulário provida pelo django. Para evitar que esses formulários sejam manipulados do lado do cliente-->
         {{% csrf_token %}}
        <!--exibindo a variável enviada-->
        {{% form %}}
        <button type="submit">Salvar</button>
    </form>
</body>
```

Para concluir é preciso validar o formulário

**clientes/views.py**

```py
from .forms import PersonForm

def persons_new(request):
    form = PersonForm(request.POST, none)
    # VALIDANDO, SE FOR VÁLIDO, ENTÃO RETIRA O FORMULÁRIO DA REQUISIÇÃO E TRANSFORMA EM UM OBJETO SALVANDO-O.
    if form.is_valid():
        form.save()
    return render(request, 'person_form.html', {'form': form})
```

Depois de salvar no BD, vamos redirecionar nossa página para uma outra usando uma função chamada REDIRECT

Para salvar as imagens. É preciso fazer outra verificação. Pegando o request.FILES no PersonForm(). E adicionar no formulário um **enctype="multipart/form-data"**

```py
from .forms import PersonForm
from django.shortcuts import render, redirect

def persons_new(request):
    form = PersonForm(request.POST, request.FILES, none)
    if form.is_valid():
        form.save()
        # MANDA O USUÁRIO PARA UMA URL
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})
```

Uma ultima coisa é adicionar um link para cadastrar um novo cliente em _**person.html**_ usando:

```html
<a href="{% url 'person_new' %}">Novo Cliente</a>
```

## AULA 19

### CRUD - UPDATE

Como tudo começa pelas urls...

**clientes/urls.py**

```py
from .views import persons_update

urlpatterns = [
    path('update/<int:id>', persons_update, name='person_update'),
]
```

Essa url chama uma view da aplicação

**clientes/views.py**

```py
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})
```

Esta função da view, recebe como parâmentro o id da pessoa que será atualizada. O primeiro passo é buscar a pessoa no banco com a função get_object_or_404, essa busca é pela chave primária (id). Logo após, instaciamos o formulário com os dados recuperados da pessoa.

A validação do formulário é feita como nas outras funções, depois o fuxo é recirecionado para a lista de pessoas. Caso o formulário não seja válido, a requisição retorna o prórpio formulário com a instância da pessoa.

No template _person.html_ precisamos "linkar" as pessoas, para que quando clicando nelas seja possível alterá-las.  Para tanto usamos o jinja com a url _person\_update_ passsando também o id do objeto.

```html
<body>
    <ul>
        {% for person in persons %}
            <li><a href="{%url 'person_update' person.id%}">{{ person.first_name}}</a></li>
        {% endfor %}
    </ul>
    <br>
    <a href="{% url 'person_new' %}">Novo Cliente</a>
</body>
```

Uma última coisa a ser feita é retirar o _action_ do botão no _person.html_, pois o django irá referenciar a url que está sendo usada. Por exemplo, quando implementamos o formulário queriamos que ao clicar no botão salvar fosse criado uma nova pessoa, contudo agora queremos atualizar uma.

## AULA 20

### CRUD - DELETE

Tudo começa nas urls

**clientes/urls.py**

```py
from .views import persons_delete

urlpatterns = [
    path('delete/<int:id>', persons_delete, name='person_delete'),
]
```

**clientes/views.py**

```py
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})
```

Uma das formas de criar essa _view_ seria usar o form para confirmar a exclusão, contudo iremos usar apenas o primeiro nome do objeto. Logo, a primeira coisa a ser feita é buscar o objeto com a função _get\_object\_or\_404_. Se quando usarmos a url de deleção sua origem foi de um método **POST**, que é o caso do template _person\_delete\_confirm.html_, deletamos o objeto e redirecionamos para a lista de pessoas. Caso a origem não seja de um método **POST** redirecionamos para o template de confirmação, que detém o método **POST**. Podemos ver esse fluxo dessa forma:

**template/person.html**

Criamos o link para deletar

```html
<body>
    <ul>
        {% for person in persons %}
            <li>
                <a href="{%url 'person_update' person.id%}">{{ person.first_name}}</a>
                <a href="{%url 'person_delete' person.id%}">deletar</a>
            </li>
        {% endfor %}
    </ul>
    <br>
    <a href="{% url 'person_new' %}">Novo Cliente</a>
</body>
```

Esse formulário envia por defaut o método **GET**, portanto não entra no teste. Então será chamado o template:

**template/person\_delete\_confirm.html**

```html
body>
    <h1>Deseja exclui? {{ person.first_name }}</h1>
    <form method="POST" enctype="multipart/form-data">
        {%csrf_token%}
        <button type="submit">Delete</button>
    </form>
</body>
```

Observe que o método agora é **POST**, como esse formulário foi chamado pela view, ele retornará para a mesma e esta excluirá o objeto. Por último a requisição irá para a listagem de pessoas.