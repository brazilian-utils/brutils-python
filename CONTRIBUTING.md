# Contributing

Obrigada por disponibilizar seu tempo para contribuir! 🙇‍♀️🙇‍♂️ Toda ajuda é bem-vinda!

## Instalação
### Requisitos
- [Python 3.7+][python]
- [Poetry][poetry]

'Fork' ou clone o repositório e entre na pasta do projeto:

```shell
$ git clone git@github.com:brazilian-utils/brutils-python.git
$ cd brutils-python
```

Crie uma [virtualenv][virtualenv] para brutils e ative:

```shell
$ make shell
```

**Nota: Você vai precisar rodar `make shell` todas as vezes que abrir um novo terminal.**

Instale as dependências:

```shell
$ make install
```

## Usando localmente

```shell
$ make run-python
```

Agora, você pode usá-lo [da mesma forma descrita no arquivo README.md](/README.md#usage)

## Testes

```shell
$ make test
```

[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
