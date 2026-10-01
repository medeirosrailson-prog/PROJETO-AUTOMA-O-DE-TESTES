# Troubleshooting

# Sumário

1. Introdução  
1.1 Objetivo  
1.2 Escopo  
2. Abordagem Geral de Troubleshooting  
3. Passo a Passo para Depuração de Testes Automatizados  
3.1 Identificar o erro  
3.2 Reproduzir o problema  
3.3 Isolar a causa  
3.4 Validar hipóteses  
3.5 Corrigir e validar  
4. Depuração com print  
4.1 Quando utilizar  
4.2 Exemplos práticos  
5. Depuração com breakpoint()  
5.1 Como utilizar  
5.2 Execução interativa  
5.3 Exemplos práticos  
6. Arquivos relevantes para investigação  
7. Ferramentas úteis para depuração  
8. Boas práticas de depuração  
9. Checklist de investigação  
10. Referências e Links Úteis  

# 1. Introdução

## 1.1 Objetivo

Este documento define um processo padronizado para identificação, análise e correção de falhas em testes automatizados utilizando Python, Selenium, Pytest e o framework Guará.

## 1.2 Escopo

Aplica-se a depuração de:

- Testes falhando
- Problemas de execução
- Erros em Transactions ou Pages
- Problemas com dados de teste
- Falhas de configuração

# 2. Abordagem Geral de Troubleshooting

A depuração deve seguir uma abordagem estruturada:

1. Identificar o erro
2. Reproduzir o problema
3. Isolar a causa
4. Validar hipóteses
5. Corrigir
6. Confirmar a solução

# 3. Passo a Passo para Depuração de Testes Automatizados

## 3.1 Identificar o erro

Executar os testes e analisar o output:

```bash
pytest -v
````

Avaliar:

* Mensagem de erro
* Stack trace
* Arquivo e linha da falha

## 3.2 Reproduzir o problema

Executar apenas o teste com erro:

```bash
pytest tests/specs/test_login.py -v
```

Garantir que o erro é reproduzível.

## 3.3 Isolar a causa

Verificar em qual camada o erro ocorre:

* Test (Spec)
* Transaction
* Page
* Dados
* Configuração

## 3.4 Validar hipóteses

Checar:

* Localizadores inválidos
* Dados incorretos
* Timeout de elementos
* Problemas de carregamento da página

## 3.5 Corrigir e validar

Após ajustar:

```bash
pytest -v
```

Confirmar que o erro não ocorre mais.

# 4. Depuração com print

## 4.1 Quando utilizar

* Verificar valores de variáveis
* Confirmar execução de passos
* Inspecionar dados de entrada

## 4.2 Exemplos práticos

No Test:

```python
def test_login(driver, login_data):
    print(login_data)
```

Na Transaction:

```python
def do(self, url, user, password):
    print("URL:", url)
    print("User:", user)
```

Na Page:

```python
def login(self, user, password):
    print("Preenchendo usuário:", user)
```

# 5. Depuração com breakpoint()

## 5.1 Como utilizar

Inserir no ponto desejado:

```python
breakpoint()
```

## 5.2 Execução interativa

Executar o teste normalmente:

```bash
pytest -v
```

O Python entrará em modo interativo.

Comandos úteis:

| Comando    | Descrição          |
| ---------- | ------------------ |
| n          | Próxima linha      |
| s          | Entrar na função   |
| c          | Continuar execução |
| p variável | Exibir valor       |
| q          | Sair               |

## 5.3 Exemplos práticos

```python
def do(self, url, user, password):
    breakpoint()
    self._driver.get(url)
```

Analisar:

```python
p url
p user
```

# 6. Arquivos relevantes para investigação

Os seguintes arquivos são fontes importantes de diagnóstico:

| Arquivo                                | Responsabilidade              |
| -------------------------------------- | ----------------------------- |
| tests/config/settings.py               | Configuração geral do projeto |
| tests/fixtures/driver.py               | Inicialização do WebDriver    |
| tests/fixtures/data\_fixture.py        | Dados de teste                |
| tests/data/data\_loader.py             | Carregamento de dados         |
| tests/docs/patterns.md                 | Padrões do framework          |
| tests/docs/architecture.md             | Arquitetura do framework      |
| tests/assertions/custom\_assertions.py | Regras de validação           |
| tests/pages/base\_page.py              | Métodos base de interação     |
| pytest.ini                             | Configuração do Pytest        |

# 7. Ferramentas úteis para depuração

## Pytest verbose

```bash
pytest -v
```

## Execução de teste específico

```bash
pytest caminho/do/teste.py
```

## Execução com logs detalhados

```bash
pytest -s
```

## VSCode Debugger

* Usar breakpoints visuais
* Executar modo debug
* Inspecionar variáveis

## Logs do Selenium

Verificar console do navegador e erros de DOM.

## DevTools (Browser)

* Inspecionar elementos
* Validar seletores
* Verificar tempo de carregamento

# 8. Boas práticas de depuração

* Sempre isolar o problema antes de corrigir
* Evitar alterações sem entender a causa
* Validar localizadores no DevTools
* Usar logs de forma controlada
* Remover prints após correção
* Utilizar breakpoint apenas durante análise
* Garantir que testes são determinísticos

# 9. Checklist de investigação

* O erro é reproduzível?
* O localizador está correto?
* O elemento está disponível no momento da interação?
* Os dados estão corretos?
* A Transaction está funcionando isoladamente?
* Existe timeout ou sincronização incorreta?
* O driver foi inicializado corretamente?
* A URL está correta?
* Existe dependência entre testes?

# 10. Referências e Links Úteis

* Selenium WebDriver Documentation: <https://www.selenium.dev/documentation/>
* Pytest Documentation: <https://docs.pytest.org>
* Python Debugging: <https://docs.python.org/3/library/pdb.html>
* Guará Framework: <https://guara.readthedocs.io/en/latest/>
* Chrome DevTools: <https://developer.chrome.com/docs/devtools/>

# Troubleshooting

## Sumário

1. Preparar a investigação
2. Diagnosticar falhas comuns
3. Depurar com logs, `print` e breakpoint
4. Arquivos úteis
5. Ferramentas
6. Referências

## 1. Preparar a investigação

1. Ative o ambiente virtual e confirme `python --version` (Python 3.11+).
2. Reproduza somente o teste que falhou, por exemplo: `python -m pytest -k checkout -vv`.
3. Leia a mensagem e o traceback completos. Diferencie falha de assertion, timeout, localização de elemento, inicialização do Chrome e erro de rede.
4. Repita a execução antes de alterar o teste. Uma falha intermitente pode indicar sincronização, dependência externa ou estado compartilhado.
5. Verifique os relatórios em `reports/` quando a execução tiver sido iniciada com as opções de relatório do README.

## 2. Diagnosticar falhas comuns

### Elemento não encontrado ou timeout

1. Confirme a URL atual e o estado esperado da página.
2. Inspecione o elemento no navegador e atualize o seletor na Page correspondente.
3. Prefira IDs, atributos `data-test` e condições explícitas em `BasePage`.
4. Não aumente o timeout nem adicione `sleep` sem evidência de que o carregamento realmente demora mais.

### Falha ao iniciar o Chrome

1. Confirme que o Chrome está instalado e inicia manualmente.
2. Atualize Selenium com `python -m pip install --upgrade selenium`.
3. Deixe o Selenium Manager resolver o driver; remova drivers locais obsoletos do `PATH` se houver conflito.
4. Em Linux/CI, confirme o uso de `CI=true` para ativar headless e os argumentos necessários ao container.

### Alerta de senha do Google Password Manager

O aviso é do navegador, não do formulário de checkout do Sauce Demo. Use um perfil efêmero do WebDriver e não salve credenciais pessoais no navegador de automação. A fixture deste projeto desativa o serviço de preenchimento/salvamento de senhas do Chrome; as credenciais públicas de demonstração ficam apenas nos dados de teste. Não tente contornar um alerta de segurança aceitando-o via Selenium nem use senhas pessoais ou reais.

### Falha após mudança de interface

1. Localize a interação na Page Object correspondente.
2. Atualize seletor ou ação apenas na Page, mantendo assertions no teste.
3. Execute os testes da funcionalidade e depois a suíte completa.

## 3. Depurar com logs, `print` e breakpoint

Para inspecionar um valor temporariamente, adicione `print(driver.current_url)` ou `print(driver.title)` no ponto relevante. Execute com `-s` para exibir a saída:

```bash
python -m pytest -k checkout -vv -s
```

Para pausar a execução, adicione `breakpoint()` no teste, na Transaction ou na Page durante a investigação:

```python
breakpoint()
```

Execute o teste isolado e use os comandos do depurador Python, como `n` (próxima linha), `s` (entrar na chamada), `p variavel` (inspecionar valor) e `c` (continuar). Remova os pontos de interrupção e prints temporários antes de enviar o pull request. Para o depurador integrado do VS Code, crie uma configuração Python de pytest que execute um teste específico e use breakpoints no editor.

## 4. Arquivos úteis

| Arquivo | Informação |
|---|---|
| `pytest.ini` | Diretórios de descoberta e marcadores |
| `pyproject.toml`, `.flake8`, `tox.ini` | Formatação, imports, lint e execução local |
| `tests/config/settings.py` | URL e timeout configuráveis |
| `tests/fixtures/driver.py` | Opções e ciclo de vida do Chrome |
| `tests/pages/` | Seletores e ações da interface |
| `tests/transactions/` | Fluxos de negócio |
| `tests/specs/` | Cenários e assertions |
| `.github/workflows/` | Execução e coleta de relatórios no CI |

Consulte também `architecture.md`, `patterns.md`, `how_to_create_test.md`, `how_to_create_page.md`, `how_to_create_transaction.md` e `pr_checklist.md`.

## 5. Ferramentas

- DevTools do Chrome: inspecionar DOM, atributos, console e requisições.
- VS Code: depurador Python com breakpoints e terminal integrado.
- Pytest: `-k`, `-m`, `-vv`, `-s` e `--tb=long` para isolar e entender falhas.
- Selenium: `driver.current_url`, `driver.title` e inspeção explícita do estado do elemento.
- Relatórios Pytest HTML/JUnit publicados pelo GitHub Actions como artefatos.

## 6. Referências

- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Documentação do Pytest](https://docs.pytest.org/)
- [Tutorial do Guará](https://guara.readthedocs.io/en/latest/TUTORIAL_TESTING.html)
- [Depurador Python](https://docs.python.org/3/library/pdb.html)
