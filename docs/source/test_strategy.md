# Estratégia de classificação dos testes

## 1. Objetivo

Classificar os cenários para equilibrar feedback rápido durante a integração, cobertura de regressão e validação das jornadas completas de maior risco.

## 2. Critérios

| Categoria | Critério de inclusão | Momento recomendado |
|---|---|---|
| Smoke | Fluxo curto que confirma que a aplicação está acessível e uma capacidade essencial funciona | Pull request e integração frequente |
| Regression | Comportamento específico de uma funcionalidade integrada, incluindo casos negativos e limites | Validação de alterações e entrega |
| E2E | Jornada crítica atravessando várias funcionalidades até um resultado de negócio | Validação de release |

## 3. Cenários classificados

| Cenário | Categoria | Motivo |
|---|---|---|
| Login com sucesso | Smoke, Regression, E2E | É pré-requisito para os fluxos autenticados e confirma acesso ao catálogo |
| Login com credenciais inválidas | Regression | Confirma a regra de rejeição e a mensagem de erro |
| Usuário bloqueado | Regression | Valida o bloqueio de uma conta específica |
| Compra de produto com sucesso | Smoke, Regression, E2E | É o fluxo crítico de negócio e percorre login, catálogo, carrinho e checkout até a confirmação |
| Adicionar item ao carrinho | Smoke, Regression, E2E | É uma etapa essencial da jornada de compra e valida a atualização do carrinho |
| Remover item do carrinho | Regression | Valida remoção e estado vazio |
| Adicionar múltiplos produtos ao carrinho | Regression | Confirma que mais de um produto distinto permanece no carrinho |
| Ordenar produtos por preço crescente | Regression | Confirma a ordenação por preço |
| Ordenar produtos por nome | Regression | Confirma a ordenação alfabética |
| Continuar comprando após adicionar item | Regression | Valida a navegação de retorno ao catálogo |
| Checkout sem preencher dados | Regression | Valida obrigatoriedade do nome |
| Checkout parcial | Regression | Valida obrigatoriedade do CEP quando os demais campos estão preenchidos |
| Logout com sucesso | Regression, E2E | Confirma encerramento correto da sessão |
| Resetar carrinho | Regression | Confirma que o estado do carrinho pode ser limpo |
| Acessar carrinho sem itens | Regression | Confirma o comportamento do carrinho vazio |

Os 15 cenários estão implementados em `tests/specs/` e recebem os marcadores declarados em `pytest.ini`. Marcadores funcionais adicionais (`login`, `cart`, `checkout`, `products` e `purchase`) permitem selecionar áreas específicas. Um cenário pode receber mais de um marcador conforme sua criticidade e a classificação acordada.

## 4. Comandos

```bash
python -m pytest -m smoke
python -m pytest -m regression
python -m pytest -m e2e
python -m pytest
```

## 5. Política de execução

| Evento | Suíte |
|---|---|
| Pull request para `main` | Smoke |
| Push para `main` | Regression |
| Publicação de release | Smoke e Regression |
| Agendamento diário, 06:00 UTC | E2E |
| Execução manual | Smoke, Regression e E2E em paralelo |

O workflow executa as suítes em jobs paralelos após a aprovação da qualidade do código, compartilhando as etapas de execução por meio de `.github/workflows/test-suite.yml`. Falhas nos testes geram screenshot PNG em `reports/screenshots/`, vinculada também ao relatório HTML; os relatórios são publicados como artefatos do GitHub Actions.
