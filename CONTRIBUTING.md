# Contribuindo

Obrigado por dedicar o seu tempo para contribuir! 🙇‍♀️🙇‍♂️ Toda ajuda é bem-vinda!

- [Primeira Contribuição](#primeira-contribuição)
- [Lançar uma Nova Versão](#lançar-uma-nova-versão)
# Primeira Contribuição

Como fazer a sua primeira contribuição:

- [1. Crie uma Conta no GitHub](#1-crie-uma-conta-no-github)
- [2. Encontre uma Issue para Trabalhar](#2-encontre-uma-issue-para-trabalhar)
- [3. Instale o Git](#3-instale-o-git)
- [4. Faça um Fork do Projeto](#4-faça-um-fork-do-projeto)
- [5. Clone o Seu Fork](#5-clone-o-seu-fork)
- [6. Crie um Novo Branch](#6-crie-um-novo-branch)
- [7. Execute o brutils Localmente](#7-execute-o-brutils-localmente)
- [8. Faça as Suas Alterações](#8-faça-as-suas-alterações)
- [9. Teste as Suas Alterações](#9-teste-as-suas-alterações)
- [10. Faça o Commit e Envie as Suas Alterações](#10-faça-o-commit-e-envie-as-suas-alterações)
- [11. Adicione Entradas no CHANGELOG.md](#11-adicione-entradas-no-changelogmd)
- [12. Crie um PR no GitHub](#12-crie-um-pr-no-github)
- [13. Atualize o Seu Branch se Necessário](#13-atualize-o-seu-branch-se-necessário)

### 1. Crie uma Conta no GitHub

Certifique-se de ter uma [conta no GitHub][github-join] e esteja logado nela.

### 2. Encontre uma Issue para Trabalhar

Visite a [página de issues do brutils][brutils-issues] e encontre uma issue com a qual você gostaria
de trabalhar e que ainda não tenha sido atribuída a ninguém.

Deixe um comentário na issue perguntando se você pode trabalhar nela. Algo como: "Olá, posso
trabalhar nessa issue?".

Aguarde até que alguém atribua a issue a você. Uma vez atribuída, você pode prosseguir para a próxima
etapa.

Sinta-se à vontade para fazer qualquer pergunta na página da issue antes ou durante o processo de
desenvolvimento.

Ao começar a contribuir para o projeto, é recomendável que você pegue uma issue por vez. Isso ajuda a garantir que outras pessoas também tenham a oportunidade de colaborar e evita que recursos fiquem inativos por muito tempo.

### 3. Instale o Git

Certifique-se de ter o [Git instalado][install-git].

### 4. Faça um Fork do Projeto

[Faça um fork do repositório brutils][github-forking].

### 5. Clone o Seu Fork

[Clone][github-cloning] o seu fork localmente.

### 6. Crie um Novo Branch

Entre na pasta do brutils:

```bash
$ cd brutils-python
```

E crie um novo branch:

```bash
$ git checkout -b <issue_number>
```

### 7. Execute o brutils Localmente
## Instalação
### Requisitos

- [Python 3.7+][python]
- [Poetry][poetry]

Crie um [virtualenv][virtualenv] para o brutils e ative-o:

```shell
$ make shell
```

**Observação: Você precisa executar `make shell` toda vez que abrir uma nova janela ou aba do terminal.**

Instale as dependências:

```shell
$ make install
```

## Utilizando Localmente

Agora você pode usá-lo [da mesma forma descrita no arquivo README.md](/README.md#utilização).

## Testes

```shell
$ make test
```

### 8. Faça as Suas Alterações

Agora é a etapa em que você pode implementar as suas alterações no código.

É importante notar que documentamos o nosso código usando [docstrings][docstring-definition].
Módulos, classes, funções e métodos devem ser documentados. Suas alterações também devem ser bem
documentadas e refletir docstrings atualizadas, caso algum dos parâmetros tenha sido alterado para
um classe/atributo ou mesmo funções.

Todas as docstring devem estar em Inglês. Fique à vontade para utilizar o Google Tradutor caso
precise. Iremos sugerir mudanças na tradução se necessário, então não se preocupe com possíveis
erros de inglês.

Seguimos o padrão abaixo para manter consistência nas docstrings:

```python
class Example:
    """Explain the purpose of the class

    Attributes:
        x[dict]: Short explanation here
        y[type, optional]: Short explanation here

    """

    def __init__(self, x, y=None):
        self.x = x
        self.y = y

    def foobar(self, w):
        """Purpose if the function

        Args:
            w[str]: Short explanation here

        Returns:
            value[str]: Short explanation here

        """
        ...
        return value

```

Algo a se ter em mente ao documentar o código com docstrings é que você pode ignorar docstrings em
decoradores de propriedade e métodos mágicos.

### 9. Teste as Suas Alterações

#### Escreva Novos Testes

Certifique-se de ter criado os testes necessários para cada nova alteração que você fez.

#### Certifique-se de que Todos os Testes Passaram

Execute todos os testes com `make test` e certifique-se de que todos passaram.

**Os PRs não serão mesclados se houver algum teste faltando ou falhando.**

### 10. Faça o Commit e Envie as Suas Alterações

Faça o commit das alterações:

```bash
$ git commit -a -m "<commit_message>"
```

Push o seu commit para o GitHub:

```bash
$ git push --set-upstream origin <issue_number>
```

Crie a quantidade de alterações/commits que você precisa e os envie.

### 11. Adicione Entradas no CHANGELOG.md

[Adicione uma entrada no CHANGELOG.md][keep-a-changelog].

### 12. Crie um PR no GitHub

[Crie um PR no GitHub][github-creating-a-pr].

### 13. Atualize o Seu Branch se Necessário

[Certifique-se de que seu branch esteja atualizado com o main][github-sync-pr]

# Lançar uma Nova Versão

Aqui você encontrará como lançar uma nova versão em produção do brutils:

- [1. Criar um Release PR](#1-criar-um-release-pr)
- [2. Deploy via GitHub](#2-deploy-via-github)

### 1. Criar um Release PR

#### Atualizar a Versão da Biblioteca

Incremente o número da versão, seguindo o [Versionamento Semântico][semantic-versioning],
no arquivo `pyproject.toml`:

- https://github.com/brazilian-utils/brutils-python/blob/main/pyproject.toml#L3

#### Atualizar o CHANGELOG.md

Adicione um título para a nova versão com o novo número e a data atual, como
[neste exemplo](https://github.com/brazilian-utils/brutils-python/blob/main/CHANGELOG.md?plain=1#L9).

E adicione os links da versão, como [neste exemplo](https://github.com/brazilian-utils/brutils-python/blob/bc10b7242bd939cc445070f7e937e3ad187ff95a/CHANGELOG.md?plain=1#L33-L34)

#### Crie o PR

Crie um PR com o nome `Release v<versão>` contendo as duas alterações acima.

[Exemplo de Release PR](https://github.com/brazilian-utils/brutils-python/pull/128)

#### Faça o Merge do PR

Assim que o PR for aceito e passar em todas as verificações, faça o merge.

### 2. Deploy via GitHub

O lançamento da nova versão em produção é feita automaticamente quando uma
[nova release é criada][creating-releases] no GitHub.

- Preencha o campo `tag version` com: `v<versão>` (por exemplo, `v2.0.0`).
- Preencha o campo `release title` com o mesmo valor que a versão da tag (por exemplo, `v2.0.0`).
- Preencha o campo `release description` com o conteúdo copiado do arquivo CHANGELOG.md da seção de
versão correspondente.

Exemplos reais estão disponíveis em: https://github.com/brazilian-utils/brutils-python/releases

Quando o Deploy via GitHub for concluído, a nova versão também será lançada automaticamente no
[PyPI][brutils-on-pypi]. Baixe a nova versão do brutils do PyPI e teste se tudo está
funcionando conforme o esperado.

[brutils-issues]: https://github.com/brazilian-utils/brutils-python/issues
[brutils-on-pypi]: https://pypi.org/project/brutils/
[creating-releases]: https://docs.github.com/pt/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release
[docstring-definition]: https://www.python.org/dev/peps/pep-0257/#what-is-a-docstring
[github-cloning]: https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository
[github-creating-a-pr]: https://docs.github.com/pt/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request
[github-forking]: https://docs.github.com/pt/get-started/quickstart/contributing-to-projects
[github-join]: https://github.com/join
[github-sync-pr]: https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/keeping-your-pull-request-in-sync-with-the-base-branch
[install-git]: https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git
[keep-a-changelog]: https://keepachangelog.com/pt-BR/1.0.0/
[poetry]: https://python-poetry.org/docs/#installation
[python]: https://www.python.org/downloads/
[semantic-versioning]: https://semver.org/lang/pt-BR/
[virtualenv]: https://virtualenv.pypa.io/en/latest/
