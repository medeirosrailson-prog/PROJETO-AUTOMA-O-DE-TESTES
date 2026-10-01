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
| Login com sucesso | Smoke | É uma verificação rápida de disponibilidade e acesso ao catálogo |
| Login com credenciais inválidas | Regression | Confirma a regra de rejeição e a mensagem de erro |
| Usuário bloqueado | Regression | Valida o bloqueio de uma conta específica |
| Compra de produto com sucesso | Smoke, Regression, E2E | É o fluxo crítico de negócio e percorre login, catálogo, carrinho e checkout até a confirmação |
| Adicionar item ao carrinho | Smoke, Regression, E2E | É uma etapa essencial da jornada de compra e valida a atualização do carrinho |
| Remover item do carrinho | Regression | Valida remoção e estado vazio |
| Ordenar produtos por preço crescente | Regression | Confirma a ordenação por preço |
| Ordenar produtos por nome | Regression | Confirma a ordenação alfabética |
| Continuar comprando após adicionar item | Regression | Valida a navegação de retorno ao catálogo |
| Checkout sem preencher dados | Regression | Valida obrigatoriedade do nome |
| Checkout parcial | Regression | Valida obrigatoriedade do CEP quando os demais campos estão preenchidos |
| Logout com sucesso | Regression, E2E | Confirma encerramento correto da jornada e da sessão |
| Resetar carrinho | Regression | Confirma que o estado do carrinho pode ser limpo |
| Acessar carrinho sem itens | Regression | Confirma o comportamento do carrinho vazio |

Os cenários estão implementados em `tests/specs/` e recebem os marcadores declarados em `pytest.ini`. Um cenário pode receber mais de um marcador se a estratégia do produto exigir; a categoria deve continuar refletindo custo, criticidade e escopo reais, não apenas o nome do fluxo.

## 4. Comandos

```bash
python -m pytest -m smoke
python -m pytest -m regression
python -m pytest -m e2e
python -m pytest
```

## 5. Política de execução

O workflow executa toda a suíte em pull requests e em pushes para `main`. Para repositórios maiores, pode-se executar smoke em cada pull request e reservar regressão/e2e para integração pós-merge ou release, monitorando duração, estabilidade e criticidade antes de alterar os gatilhos.
