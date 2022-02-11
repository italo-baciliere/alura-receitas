'''

______________________________________
DIVISÃO DAS AULAS
______________________________________
Iniciando aplicação e subindo o servidor
    Vamos preparar um ambiente virtual e subir o servidor

Template, rotas e views
    Vamos trabalhar com rotas e views no Django

Links, extends e partials
    Vamos refatorar nossas páginas html criando partials

Modelo e banco de dados
    Vamos configurar e conectar nossa aplicação Django com Postgres

Admin, parâmetros e receitas
    Utilizando o Django admin, vamos exibir as receitas do banco

Página do GitHub para mais informações sobre o projeto:
    https://github.com/alura-cursos/alura_receitas_django




______________________________________
DJANGO
______________________________________
Django utiliza o pdrão model-template-view (MTV)

Para trabalhar com o Django, primeiro, precisamos nos certificar que o
Python e o pip (gerenciador de pacotes do Python) estão instalados corretamente no seu computador.

Todas essas versões do Python incluem um banco de dados leve chamado SQLite,
para que você ainda não precise configurar um banco de dados.

No prompt de comando, digite 'python'
Dentro do terminal python, digite:
    >>> python --version
    >>> pip --version
    >>> python -m pip install --upgrade pip




INSTALANDO O DJANGO

No terminal do windows execute:
    $ pip install Django
No terminal interativo do Python, digite:
    >>> import django
    >>> print(django.get_version())

Comando django
    $ django-admin help




______________________________________
ESCREVEDO O SEU PRIMEIRO PROJETO
______________________________________

Um aplicativo do Django é um pacote separado em Python que contém
um conjunto de arquivos relacionados para uma finalidade específica.
Um projeto do Django pode conter qualquer número de aplicativos,
o que reflete o fato de que um host da Web pode servir qualquer número de pontos de
entrada separados de um único nome de domínio.
Nesse caso, o projeto do Django manipula o roteamento de URL e as configurações no
nível do site (nos arquivos urls.py e settings.py),
enquanto cada aplicativo tem seu próprio estilo e comportamento distintos por
meio de seus roteamentos, exibições, modelos, arquivos estáticos e interfaces administrativas internas.

    $ django-admin startproject <nome_do_projeto>
    $ django-admin.py startproject aprendendodjango

Criar projeto direto no diretório

    $ django-admin startproject <nome_do_projeto> .

Inicialiando o projeto

    $ python manage.py runserver

Estrutura do projeto:

    * __init__.py: arquivo vazio que indica um package. Diz ao Python que este diretório deve ser considerado um pacote.
    * settings.py: arquivo de configuração do projeto.
    * urls.py: todas as urls do projeto são definidas aqui.
    * wsgi.py: protocolo que serve http. Ponto de integração entre servidores

Crie o banco de dados antes de podermos usá-las. Para fazer isso, execute o seguinte comando:

    $ python manage.py migrate




______________________________________
APP
______________________________________

Um app é uma aplicação que realiza determinada função.
Por exemplo, uma visualização de receitas, devemos criar um app para essa visualização
Um app pode ser compartilhado entre diferentes projetos.

Ajudar do manage.py

    $ python manage.py help


INICIANDO UM APP
Inicie o app executando essa linha de comando:

    $ python manage.py startapp nome_do_app

Isso criará um diretório, que é apresentada desta forma:
    nome_do_app/
        __init__.py
        admin.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py


REGISTRANDO UM APP

Acesse a pastas 'apps.py' para verificar o nome do app recem criado

    name='receita'

Acesse o arquivo 'settings.py', insira o nome do app no atributo 'INSTALLED_APPS'


ACESSAR O APP

Crie um novo arquivo 'urls.py' na pasta do novo app
Import as 'urls' para o arquivo

    from django.urls import path

Importe todas as 'views' relacionadas a essa url
O arquivo de 'views' faz a manipulação de qual url será exibida na tela

    from . import views

Adicione no arquivo 'urls.py'

    urlpatterns = [
        path('', views.index, name='index')
    ]

Vamos criar a 'view'
Acesse o arquivo 'views.py' do seu app
Insire a função abaixo, mas antes, import o 'request':

    from django.http import HttpResponse

    def index(request):
        return HttpResponse('<h1>Receitas</h1>')

Antes de visualizarmos a view, devemos registrar as nossas rotas
Acesse o arquivo 'urls.py' do projeto
Inclua um 'path' dentro de 'urlpatterns', mas antes,
adicione o 'include' no import da '.urls'

    path('', include('receitas.urls')),





______________________________________
______________________________________
Criando um usuário administrador com o comando abaixo

    $ python manage.py createsuperuser

    - username: italo
    - Email address: italoluciano57@gmail.com
    - Password: pr0c0nc3pt

Agora, abra um navegador da Web e vá para "/ admin /" no seu domínio local -
por exemplo, http://127.0.0.1:8000/admin/




______________________________________
AMBIENTE VIRTUAL
______________________________________

python venv
https://docs.python.org/3/library/venv.html
https://docs.python.org/pt-br/3/library/venv.html

Crie uma pasta para inserir o seu ambiente virtual

Criando um ambiente virtual
    $ python3 -m venv /path/to/new/virtual/environment

Estrutura do ambiente virtual
    /bin - arquivo necessário para carregar o ambiente virtual

Ativar o ambiente virtual
    Linux
    $ /path/to/new/virtual/environment/activate
    Windows
    $ /bin/activate/Scripts/activate.bat

Instalar o Django
    (environment) pip install django

Visualiar modulos instalados no ambiente virtual
    (environment) pip freeze

Atualizar o pip
    $ python -m pip install --upgrade pip




______________________________________
DEPENDENCIAS DO PROJETO
______________________________________

 - Django




______________________________________
CONFIGURAÇÕES PROJETO
______________________________________

No arquivo 'settings.py' altere as seguintes propriedades

https://www.alura.com.br/artigos/timezone-no-django?gclid=Cj0KCQiAxoiQBhCRARIsAPsvo-xssBTyPKYoGLaOt0tIzU3ODGMRVziNKunM8KEgyv4_69VkDmm1iUIaAmi6EALw_wcB
https://github.com/guilhermeonrails/language_code_django/blob/list_languages/list.py
https://github.com/guilhermeonrails/language_code_django/blob/tz_list/list.py
https://docs.djangoproject.com/en/4.0/topics/i18n/
https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/

    LANGUAGE_CODE
    TIME_ZONE




______________________________________
CRIAÇÃO DA VIEW
______________________________________

Create folder 'templates' into receitas app folder
create a file 'index.html'

INFORMAR PARA A VIEW RENDERIZAR A PÁGINA

No arquivo views.py ,a função index que retorna um elemento html,
altere a seguinte linha:

    return HttpResponse('<h1>Receitas</h1>')

para:

    return render(request, 'index.hltml')

Depois remova o import http, pois não estamos
mais utilizando.

    'from django.http import HttpResponse'




______________________________________
GERENCIANDO ARQUIVOS ESTÁTICOS
______________________________________

https://docs.djangoproject.com/pt-br/2.2/howto/static-files/

Abra o arquivo 'settings.py' do projeto.
Dentro da propriedade 'TEMPLATES', insira a caminho para a
raiz da aplicação

    'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')],

Usamos esta configuração para referência a arquivos estáticos
localizados no 'STATIC_ROOT'

    STATIC_URL = 'static/'

Expecificar para o Django onde encontar os arquivos estaticos.
Usamos esta configuração para indicar o caminho absoluto, onde o
'collectstatic' coletará os arquivos estáticos.
Crie o campo:

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Essa configuração define os locais adicionais que o aplicativo
'staticfiles' percorrerá se o localizador 'FileSystemFinder'
estiver ativado, por exemplo. Se você usar o comando de
gerenciamento 'collectstatic' ou 'findstatic' ou usar
a exibição de arquivo estático.
Dizer onde encontramos os arquivos estáticos:

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'alura_receita/static')
    ]


ADICIONANDO OS ARQUIVOS ESTÁTICOS NO PROJETO

Crie uma pasta 'static' na estrutura do projeto.
Copie e cole os arquivos estáticos baixados para dentro da pasta.

    /css
    /fonts
    /img
    /js
    /scss
    /site.css

Agora, vamos imformar para o Django que temos arquivos estáticos
no diretório.

    $ python manage.py help
    [staticfiles]

Faz uma cópia dos arquivos para o Django poder manipular os meus arquivos

    # python manage.py collectstatic

Agora copie e cole os seguintes arquivos para a pasta '/receitas/templates':

    index.html
    receita.html

Após realizar todas as configurações em 'settings.py',
indicando que trabalharemos com arquivos estáticos,
é necessário para carregar uma imagem ou um arquivo css na
nossa aplicação usar a 'template tag' e a 'tag' 'static'
para construir um URL para o caminho relativo.
Com isso, insira no topo da página a seguinte 'template tag':

    {% load static %}

Depois insira a seguinte 'tag' padrão em todos os caminhos da página:

    {% static 'caminho' %}

Para caminhos .html, utilize o seguinte padrãa, retirnado o
.html do link:

    href="{% url 'index' %}"


Exemplo:

    <link rel="icon" href="{% static 'img/core-img/favicon.ico' %}">

Os templates do Django definem o layout e a formatação
final enviados aos usuários finais após o término do processamento
de uma solicitação, podendo ser escrito no formato html ou csv,
entre outros formatos.

Caso queira saber mais sobre Templates:
    https://docs.djangoproject.com/en/2.2/topics/templates/




______________________________________
ESTENDENDO HTML
______________________________________

Crie um folder dentro de templates, chamado 'base.html'
Copie e cole as tags para construção do html base.
Neste projeto terá um arquivo nomeado como 'exemplo_base.html',
como arquivo para futuras consultas

Como indicar a inserção de um trecho (blocos) de código
na minha página html?

Através de código Python!
Insira no arquivo base.html onde você queira inserir o trecho:

    {% block content %} {% endblock %}

Neste caso foi inserido antes da abertura da tag <script>

        {% block content %} {% endblock %}

    <!-- ##### All Javascript Files ##### -->
        <!-- jQuery-2.2.4 js -->
        <script src="{% static 'js/jquery/jquery-2.2.4.min.js"></script>

Agora informe no arquivo que será importado
as seguintes tag:

    {% extends 'base.html' %}
    {% load static %}

Lembre-se, no arquivo que será importado, não deve existir o mesmo trecho de código
do arquivo 'base.html', até porque esse trecho será IMPORTADO. ;)

Por fim, informe o início e fim do bloco que será importado,
inserindo todo o trecho html dentro das tags:

    {% block content %}
        ...
        ...
        ...
    {% endblock %}




______________________________________
ESTENDENDO HTML
______________________________________

partials são pequenos trechos de código html
que podem ser compartilhados com outras páginas.

Crie uma pasta dentro de template: 'partials'.
Crie dentro da pasta uma página html: 'footer.html'
Crie dentro da pasta uma página html: 'menu.html'

Recorte e cole todo o código HTML referente ao menu
e cole dentro da página 'menu.html'.

Insira um trecho de código Python
no arquivo 'index.html':

    {% include 'partials/menu.html' %}

Dentro da página 'menu.html', insira o
carregamento de conteúdo estático:

    {% load static %}

Faça o mesmo para o footer!!




______________________________________
NOMES DE RECEITAS DINÂMICAS
______________________________________




______________________________________
ESTUDAR - DETALHAR
______________________________________

Instrospecção
    - https://pt.wikipedia.org/wiki/Introspec%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29

Filosofia do Django segundo a documentação oficial
    - https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/
'''