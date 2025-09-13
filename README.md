# Desafio para processo seletivo - Workshop Backend Fábrica de Software 2025.2

Este repositório remoto foi desenvolvido como parte do Workshop da Fábrica de Software 2025.2.

## Tecnologias utilizadas

### Back-end:

- **Python 3**: Linguagem de programação base para lógica da aplicação.
- **Django MVT**: 'Framework web Python' para desenvolvimento dos projetos, consumindo 'APIs', criando operações 'CRUD' e renderizando 'templates'.
- **Requests**: Biblioteca para requisição das 'APIs' externa pública para os projetos.
- **ViaCEP**: 'API' externa pública para consumo de dados.

### Front-end:

- **HTML5**: Linguagem de marcação para construção dos 'templates'.

## Funcionalidades:

- **Busca de CEPs**: Busca por CEPs no banco de dados do ViaCEP.
- **Cadastro de CEPs**: Cadastra um CEP pesquisado e armazena no banco de dados.
- **Listagem de CEPs**: Lista e visualiza os CEPs armazenados no banco de dados.
- **Exclusão de CEPs**: Deleta os CEPs armazenados no banco de dados.

## Como rodar o projeto:

### 1. Clonando o repositório

Use o seguinte comando para clonar:

```
bash
git clone https://github.com/soturnacrosta/WorkshopBack-End-Turma2-2025.2
```

### 2. Configurando o projeto

1. **Crie e Ative um Ambiente Virtual (Recomendado)**

Vá na pasta raiz:

```
bash
python -m venv venv
`source venv/bin/activate`

No Windows, use `venv\Scripts\activate`
```

2. **Instale as Dependências**

```bash
pip install django requests
```

3. **Execute as Migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Inicie o Servidor de Desenvolvimento**

```bash
python manage.py runserver
```

### 3. Testando a aplicação

1. **Abra seu navegador e acesse `http://127.0.0.1:8000/`.** 
2. **Utilize as funcionalidades de criar, listar, atualizar e deletar CEPs.**

### Observação Importante: vários projetos

Existem vários projetos Python puro e Python com Django, então observe bem os caminhos das pastas e rode as aplicações. A forma instruída para rodar é generalista.

## Fontes

- https://viacep.com.br/
- https://joaolucasgpc.notion.site/Class-Based-View-1a799b0a3ac58046aef1d89b8fd6846e
