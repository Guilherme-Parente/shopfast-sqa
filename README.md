# Mini-SQAP — ShopFast

## Contexto

Durante a Black Friday, a ShopFast aprovou pedidos com desconto sem validação de pagamento.

A falha foi estrutural:

* ausência de validação entre serviços
* falta de governança no pipeline
* decisão baseada em "achismo"

Impacto:

* prejuízo financeiro
* falha logística em escala
* quebra de adequação funcional (ISO 25010)

---

## Política de Qualidade (IEEE 730)

### Regra Imutável 01 — Consistência Financeira Obrigatória

Nenhum desconto pode ser aplicado sem pagamento autorizado.

**Enforcement (CI/CD):**

* Testes obrigatórios cobrindo:

  * pagamento aprovado → desconto permitido
  * pagamento recusado → erro obrigatório
* Cobertura mínima: 85% no domínio financeiro
* Falha em contrato Payment ↔ Order bloqueia deploy

---

### Regra Imutável 02 — Isolamento + Fail Fast

Regras críticas devem ser isoladas da interface e validar antes de executar.

**Enforcement (CI/CD):**

* Bloqueio se regra estiver em Controller/UI
* Obrigatoriedade de exceções de negócio
* Validação explícita antes de qualquer cálculo

---

## Matriz de Risco (PxI)

Risco: desconto aplicado sem pagamento

* Probabilidade: Alta
* Impacto: Muito Alto

Classificação: Risco Extremo

A ausência de governança permitiu falha sistêmica.

---

## Impacto no Change Failure Rate (DORA)

O SQA reduz falhas ao:

* antecipar validação (shift-left)
* bloquear builds inconsistentes
* eliminar decisões não verificadas

Resultado: redução do Change Failure Rate e aumento da confiabilidade.

---

## Sumário Executivo

Este Mini-SQAP implementa:

* regras imutáveis com enforcement automatizado
* validação financeira obrigatória
* isolamento de lógica crítica

O sistema deixa de ser reativo e passa a ser preventivo.

---

## Implementação

A lógica crítica foi isolada em `PricingService`, garantindo:

* validação obrigatória de pagamento
* validação de cupom
* fail fast em qualquer inconsistência
