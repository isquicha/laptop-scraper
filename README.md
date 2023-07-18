# Laptop Scraper

Faz scraping de laptops do site [webscraper.ip](https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops) e salva em um arquivo json.

## Requisitos

- [Python](https://www.python.org/downloads/) precisa estar instalado em sua máquina, na versão 3.11 ou superior.
- [Pip](https://pip.pypa.io/en/stable/installation/) precisa estar instalado em sua máquina.
    - Ele vem junto com o Python 3.11 ou superior, mas caso não tenha, siga as instruções do link.
    - Em teoria a versão do pip não deve influenciar no resultado do procedimento, mas para deixar explícito, a versão utilizada durante o desenvolvimento foi a 22.3.1

## Instalação

- Clone este repositório
    - `git clone https://github.com/isquicha/laptop-scraper`
    - OU baixe e extraia o .zip por meio do [link de download do GitHub](https://github.com/isquicha/laptop-scraper/archive/refs/heads/main.zip)
- Abra a pasta por meio do terminal
    - `cd laptop-scraper`
- Opcionalmente crie e ative um ambiente virtual
    - `python -m venv .venv`
    - `source .venv/bin/activate`
- Instale as dependências
    - `pip install .`

## Como usar

Utilize o comando `ltscp` para fazer o scraping e salvar os dados em um arquivo json.

Você pode ver as opções de linha de comando disponíveis com `ltscp --help`.  
Algumas das opções são:

- A marca dos laptops, sendo que em inglês a opção é `--brand` ou `-b` seguida do nome da marca, podendo ser uma dentre dell, msi, toshiba, hp, acer, apple, prestigio, asus e lenovo
- A chave de ordenação dos resultados, sendo que em inglês a opção é `--order` ou `-o` seguida do nome do parâmetro de ordenação, podendo ser:
    - `price` para ordenar pelo preço
    - `name` para ordenar pelo nome
    - `brand` para ordenar pela marca
    - `rating` para ordenar pela avaliação
    - `reviews` para ordenar pela quantidade de avaliações
- Se a ordenação deve ser feita por ordem reversa, utilizar a opção `--reverse`
- O arquivo json de saída dos dados, sendo que em inglês a opção é `--file` ou `-f` seguida do nome do arquivo json

### Exemplo de uso

No terminal digite o comando `cd ~ ; ltscp -b lenovo -o price -f lenovo.json ; cd -`.
Após isso será criado um arquivo chamado `lenovo.json` no diretório home do usuário, contendo os laptops da marca Lenovo ordenados pelo preço.

## Contribuindo

Para contribuir com o desenvolvimento do projeto, instale as dependências de desenvolvimento e testes por meio do comando `pip install -e '.[dev]'`.

Faça suas contribuições à vontade, e rode as verificações por meio do utilitário `checks.sh`.
Para isso será necessário dar permissão de execução para ele, por meio do comando `chmod 754 checks.sh`.

Caso prefira, você pode rodar os comandos manualmente.

Convém explicar as ferramentas:

- O `black` verifica a formatação do código
- O `isort` verifica a ordem dos imports
- O `mypy` verifica o tipo das variáveis
- O `flake8` verifica a qualidade do código
    - O `flake8p` é uma variação do flake8 que lê as configurações do arquivo `pyproject.toml`
- O `pytest` roda os testes

Todas essas verificações também rodam ao abrir, no GitHub, um PR (_Pull Request_) que aponte para a branch principal do repositório (`main`), graças ao arquivo [`main.yaml`](./.github/workflows/main.yaml).
