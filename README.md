# Automação de Testes Sauce Demo

Framework de automação web UI com Python 3.11+, Selenium, Pytest e Guará. Os testes seguem a arquitetura `Spec → Transaction → Page`, com cenários classificados como smoke, regression e end-to-end.

## Requisitos

- Python 3.11 ou superior
- Google Chrome instalado
- Acesso à internet para acessar `https://www.saucedemo.com`

## Configuração no Windows (PowerShell)

Na raiz deste projeto:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se a política local bloquear a ativação do ambiente virtual, execute `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` e use esse interpretador para rodar os testes.

## Configuração no Ubuntu/Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

O Selenium Manager procura e inicializa o driver compatível com o Chrome. A fixture cria um perfil temporário e isolado para cada teste e desativa o gerenciador de senhas e o alerta de vazamento do Chrome, evitando interferência da máquina do desenvolvedor. Em integração contínua, o navegador é executado em modo headless.

## Executar os testes

```bash
python -m pytest
python -m pytest -m smoke
python -m pytest -m regression
python -m pytest -m e2e
python -m pytest -k checkout
```

Para visualizar o navegador durante a execução local, não defina `HEADLESS=true`. Para forçar o modo headless localmente, defina essa variável como `true`.

## Relatórios

```bash
mkdir -p reports
python -m pytest --html=reports/report.html --self-contained-html --junitxml=reports/results.xml
```

No PowerShell, crie a pasta de saída antes de executar:

```powershell
New-Item -ItemType Directory -Force reports
python -m pytest --html=reports/report.html --self-contained-html --junitxml=reports/results.xml
```

O workflow em `.github/workflows/ci.yml` executa a validação de qualidade e a suíte apropriada ao evento: Smoke em pull requests, Regression em pushes para `main`, Smoke e Regression em releases publicadas e E2E diariamente. Também pode ser iniciado manualmente pela aba **Actions** do GitHub, quando as três suítes rodam em paralelo. Cada suíte publica os relatórios HTML, JUnit e screenshots de falhas como artefatos por 14 dias.

### Pipeline do GitHub Actions

A pipeline possui uma etapa de qualidade e suítes de teste independentes:

1. **Code quality**: executa Black, isort e Flake8.
2. **Smoke**: executa em pull requests e releases publicadas.
3. **Regression**: executa em pushes para `main` e releases publicadas.
4. **E2E**: executa diariamente às 06:00 UTC ou manualmente.

As suítes são executadas em jobs paralelos, em Chrome headless, somente depois da aprovação da qualidade. O workflow reutilizável `.github/workflows/test-suite.yml` mantém a instalação, execução e publicação dos relatórios consistentes entre elas. Em caso de falha de teste, a screenshot é incluída no relatório HTML e salva em `reports/screenshots/`.

Para usar a pipeline:

1. Publique este projeto em um repositório GitHub.
2. Faça push para `main` ou abra um pull request direcionado para `main`.
3. Acesse **Actions → CI** para acompanhar a execução e baixar os relatórios em **Artifacts**.
4. Para validar uma release, publique-a no GitHub; para E2E imediato, use **Run workflow**.

## Classificação dos cenários

| Marcador | Objetivo | Execução |
|---|---|---|
| `smoke` | Verificar rapidamente o acesso e o login essencial | `python -m pytest -m smoke` |
| `regression` | Validar comportamentos integrados de login, catálogo, carrinho e checkout | `python -m pytest -m regression` |
| `e2e` | Validar a jornada crítica de compra até a confirmação | `python -m pytest -m e2e` |

Marcadores funcionais adicionais permitem selecionar cenários por domínio: `login`, `cart`, `checkout`, `products` e `purchase`. O smoke valida login, adição de item ao carrinho e compra completa. A regressão cobre todos os cenários funcionais, incluindo credenciais inválidas, usuário bloqueado, operações e ordenação do carrinho, compra com múltiplos produtos, continuidade de compra, validações do checkout, logout, reset do carrinho e carrinho vazio. O e2e segue a matriz de classificação documentada em `docs/source/test_strategy.md`.

## Estrutura

```text
tests/
├── config/       # Configuração do ambiente
├── data/         # Dados estáticos dos cenários
├── fixtures/     # WebDriver e dados de teste
├── pages/        # Page Objects e interações com a interface
├── specs/
│   ├── smoke/
│   ├── regression/
│   └── e2e/
└── transactions/ # Fluxos de negócio reutilizáveis
```

## Navegação da documentação

A documentação técnica está em `docs/source/` e inclui arquitetura, padrões, criação de testes, Pages e Transactions, estratégia de logs, qualidade, troubleshooting e checklist de pull request. Consulte `docs/source/index.rst` para o índice.
