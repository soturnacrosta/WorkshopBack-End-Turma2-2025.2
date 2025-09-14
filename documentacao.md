# Dados autorais:

Processo seletivo Fábrica de Software 2025.2.

Projetos do WorkShop Back-End.

Autor do repositório: Mailton Olinto de Oliveira Lemos.

# Objetivo:

Esse repositório tem como objetivo guardar todas as tarefas realizadas no WorkShop Fábrica de Software 2025.2. 

Essa documentação tem como objetivo, em um formato baseado no Scrum, registrar as atividades desse Workshop, além de documentar os softwares relevantes ou necessários desenvolvidos no mesmo.

É valioso criar e desenvolver sempre a documentação para futuras necessidades e oportunidades.

É necessário contextualizar que esse documento está sendo escrito em ambiente de treinamento, workshops e desafios coletivos.

# Desenvolvimento:

Esse projeto utiliza a linguagem Python pura em um primeiro momento e em sequência a implementação do Framework Django. 

A IDE é Visual Studio Code (VSCODE), sendo ambiente WINDOWS em laboratório e LINUX em casa.

Devido a rápida demanda de testes e principalmente entregas, a documentação e programação se baseará em ensinamentos do Scrum, mas na forma que for cabível.

# Definição de pronto:

Uma demanda estará pronto quando sanar todas as necessidades propostas pelos desafiantes e enviado ao repositório remoto do projeto.

## Circuito 1:

### Dia 1:

Foram criados o arquivo `main.py` e o `requirements.txt`: o `requirements.txt` serve para guardar as bibliotecas e as versões das mesmas referente ao projeto, assim resolvendo conflito entre diferentes versões de ambientes em um mesmo projeto.

Também foi criado o `README.md` para apresentação e documentação do projeto.

Foi criado e ativada a venv (ambiente virtual do Python) e sua configuração no .gitignore para não ser inclusa no repositório remoto.

Criado o repositório remoto.

### Dia 2:

Primeiramente, nos foram entregues seis desafios a serem resolvidos e commitados ao Github. Os requisitos eram simples e claros.

Então, desenvolvi quatro (04) aplicações Python puro:

- `01_CalculadoraRaizQ.py`
- `02_ArredondamentoInteligente.py`
- `03_CalcGeoAvancada.py`
- `04_AnimaisSimples.py`
	
O projeto do dia está na pasta:

`└── dia2`
	
Estas sendo em laboratório com ajuda de instrutor, monitores e colegas de trabalho.

O desafio aqui foi o uso da sintaxe Python que é novidade para mim. O paradigma da Orientação a Objetos é confortável de se trabalhar.

Esse dia agregou bastante quanto a troca de ideias com os colegas, aprendemos juntos. 
	
### Dia 2.3:

Esse dia é a continuação das atividades do dia anterior.

Foram desenvolvidas duas (02) aplicações Python puro:

- `05_AnimaisAtributos.py`
- `06_ZooInteligente.py`
	
O projeto do dia está na pasta:

`└── dia2`

Estas sendo em casa. A dificuldade foi menor, pois as quatro aplicações anteriores me preparou e me deixou mais confortável com o desafio.

Aqui foi iniciada a documentação do projeto.

### Dia 3:

Nesse dia foram desenvolvidas oito (08) aplicações Python puro para treinamento de depuração com Excepts. 

- `exercicio1.py`
- `exercicio2.py`
- `exercicio3.py`
- `exercicio4.py`
- `exercicio5.py`
- `exercicio6.py`
- `exercicio7.py`
- `exercicioExtra.py`
	
O projeto do dia está na pasta:

```
└── dia3/
    └── ProjetoDjango/
```

Também foi estudado em casa Requests e em laboratório configuração Django. Notou-se uma melhora na navegação entre pastas do terminal.

As maiores dificuldades foram no quesito configuração de ambiente virtual, onde é necessário estar ativado para fazer alterações nos requisitos técnicos de Python. Como por exemplo, é necessário ativá-lo para poder instalar o Django ou a biblioteca Requests.

### Resultados do Circuito 1:

Foram desenvolvidos quatorze (14) softwares, iniciada a documentação, criado e configurado o ambiente virtual, criado o repositório remoto e iniciado configuração Django.

## Circuito 2

### Dia 1:

Aprofundando no Django, começamos a estudar rotas, requests para API e configuração de API. A maior dificuldade esteve em entender que a pasta 'app' não é criada depois de 'templates' como eu havia entendido através de instruções da inteligencia artificial. 'app' fica antes de 'template', em seguida vem a página renderizada.

O caminho seria: 

```
└── dia4/
  └── projeto/
    └── app/
        └── templates/
            └── home.html
```

Esse erro tornou as coisas mais complicadas durante o treinamento, mas foi resolvido no fim do dia.

O primeiro exercício de hoje, dos dois, está salvo na pasta do dia 3, pois o mesmo foi iniciado no dia anterior.

O projeto do dia está na pasta:

``` 
└── dia3/
    └── ProjetoDjango/
```
	
O segundo projeto está na pasta:

```
└── dia4/
    └── projeto/
```

### Dia 2:

Fomos desafiados a criar um CRUD - Create, Read, Update & Delete com Django e requisições de API em Python. Pudemos aprender e iniciar o desafio em sala de aula. Finalizei em casa.
Os maiores desafios encontrados foram na hora de requisitar os dados da API e na hora de renderizá-los no template, ambos na página de consulta.

Acabei por me prender bastante ao código mostrado em slide, primeiramente.

Depois, para renderizar os dados nos templates, deve-se usar `render()` com `return` e o próprio `template` com o `form`. 

Outro problema notável foi ao tentar requisitar os dados, o objeto `Endereco` era retornado duplicado pois o `form.save()` servia de segundo salvamento. A solução foi apagar essa linha do código.

Vale prestar atenção nos nomes de variáveis utilizados nas classes e na instância dos templates.

O projeto do dia está na pasta:

```
└── dia5/
    └── projeto/
```

Vale salientar que o .gitignore não ignora automaticamente venvs que não seguem o padrão de nomeação venv ou .venv. Ao colocar nomes diferentes, o Git rastreia e envia para o repositório remoto.

Nesse dia não foi entregue o requisito de estrutura base.

### Dia 3:

E finalmente, fomos desafiados a criar uma API Rest. Utilizando o modelo Class Based View e a ferramenta Django Rest Framework. Os maiores empecilhos foram na criação das 'Routes' e sincronização de 'models' com a API.

O projeto do dia está na pasta:

```
└── dia6/
    └── api_root/
```
	
O `README.md` foi formatado em markdown e enviado para o Github.

### Resultados do Circuito 2:

Foram desenvolvidas quatro (04) aplicações, aplicando conceitos de Python, Django Framework, Tamplete Based View e Class Based View. Além de consumo e criação de API e requerimento de CRUD (create-read-update-delete).

A documentação foi melhor desenvolvida e formatada em markdown.

## Circuito 3

### Dia 1:

Dia de receber o desafio final. Primeiramente, me propus a desenvolver uma API que fosse alimentada por uma API pública e depois renderizada em template, assim misturando os modelos MVT e MVC. A API pública seria 'JSONPlaceholder', que simula um sistema de blog. Elaborei os requisitos e objetivos e procedi a começar a programação. Logo vi que estava bem complexo para minhas capacidades.

Decidi por recomeçar do zero para algo mais simples que me fizesse depender menos de inteligencia artificial, algo que eu pudesse fazer mais por eu mesmo.

### Dia 2:

Mantendo a API 'JSONPlaceholder', elaborei por apenas consumir a API e renderizar nos templates, criando operações de CRUD.

Construí a aplicação tranquilamente com os conhecimentos dados em ambiente de trabalho e ajuda dos materiais de estudo dados, sendo as maiores dificuldades nas variáveis nos caminhos das rotas (urls) que devem ter os mesmos nomes das variáveis dos botões dos templates.

Um dos requisitos do desafio era o relacionamento entre duas entidades, que cumpri ao relacionar `Users` e `Posts`. Cada usuário tem um post.

Iniciei e terminei o `README.md` do projeto final e desse projeto.

### Dia 3:

Último dia. Finalizadas ambas as documentações e código revisado.

### Resultados do Circuito 3:

Nesse circuito foram entregues as aplicações do projeto final, assim como os desafios diários e suas devidas documentações.

Como conhecimento valioso destaco a capacidade adquirida de entender problemas que aparecem no terminal.




