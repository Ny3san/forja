---
name: forja
description: >
  Forja é uma skill de qualidade e arquitetura de código para projetos no VS Code,
  com seis comandos: /analisar (diagnostica um projeto pelos 20 pilares e gera um
  AGENTS.md), /entender (responde perguntas sobre o código sem editar nada),
  /create-project (cria um projeto novo, enxuto e validado), /prompt (melhora o
  prompt do usuário para um agente de código, seguindo o método de Boris, da
  Anthropic), /humanizar (remove marcas de texto de IA, com base em humanizer e
  stop-slop) e /ponytail (a solução mais simples que funciona). Use sempre que o
  usuário pedir para analisar, criar ou padronizar um projeto, escrever, corrigir
  ou revisar código, melhorar, otimizar ou reescrever um prompt, ou tirar a "cara
  de IA" de qualquer texto. Use também quando reclamar de código inchado,
  boilerplate, over-engineering, dependências desnecessárias ou texto genérico e
  robótico. NÃO use para conhecimento geral, tradução simples ou receitas.
argument-hint: "[analisar <caminho> | entender <pergunta> | create-project <nome> | prompt <texto> | humanizar <texto ou arquivo> | ponytail lite|full|ultra]"
license: MIT
---

# Forja

Forja entrega código bem feito, simples e 100% funcional, e prosa sem enchimento.

| Comando | O que faz | Escreve arquivos? |
|---|---|---|
| `/analisar [caminho]` | Diagnostica o projeto pelos 20 pilares e gera `AGENTS.md` | Só o `AGENTS.md` |
| `/entender <pergunta>` | Responde perguntas sobre o código, incluindo o porquê histórico | Não |
| `/create-project <nome>` | Cria um projeto novo, enxuto e validado | Só na pasta nova |
| `/prompt <texto>` | Reescreve o prompt do usuário para um agente de código | Não |
| `/humanizar <texto ou arquivo>` | Remove marcas de texto de IA sem mudar o conteúdo | Só se receber um arquivo |
| `/ponytail [lite\|full\|ultra]` | A solução mais simples que funciona, em qualquer tarefa de código | Conforme a tarefa |

## Roteamento

- Comando explícito vence.
- Sem comando, decida pela intenção: "melhora esse prompt" vai para `/prompt`; "tira a cara de IA" ou "soa robótico" vai para `/humanizar`; "analisa o projeto" ou "cria regras para a IA" vai para `/analisar`; "como funciona X" ou "por que Y está assim" vai para `/entender`; "crie um projeto" vai para `/create-project`; qualquer outra tarefa de código roda em `/ponytail full`.
- Os comandos se combinam: `/create-project` usa o diagnóstico do `/prompt` no pedido e a prosa limpa no README; `/analisar` aplica a prosa limpa no relatório.

## Referências (leia só quando o comando precisar)

| Arquivo | Quando ler |
|---|---|
| `references/boas-praticas.md` | `/analisar` e `/create-project`: os 20 pilares e regras gerais de código |
| `references/agents-template.md` | `/analisar` e `/create-project`: modelo do `AGENTS.md` |
| `references/stacks-minimos.md` | `/create-project`: esqueletos mínimos por tipo de projeto |
| `references/prompt-guide.md` | `/prompt`: método, checklist, moldes e exemplos |
| `references/escrita-humana.md` | `/humanizar` e qualquer prosa longa: padrões de IA a remover |

---

## Princípios (valem em todos os comandos)

1. **Entenda antes de mudar.** Leia os arquivos que a mudança toca e trace o fluxo real. A escada abaixo encurta a solução, nunca a leitura.
2. **Escada de decisão.** Pare no primeiro degrau que resolver:
   1. Isso precisa existir? Necessidade especulativa não entra.
   2. Já existe no projeto (helper, util, padrão)? Reutilize.
   3. A stdlib resolve? Use.
   4. Um recurso nativo da plataforma resolve? (HTML antes de biblioteca de UI, CSS antes de JS, constraint do banco antes de validação duplicada.)
   5. Uma dependência já instalada resolve? Use.
   6. Cabe em uma linha? Escreva uma linha.
   7. Só então: o código mínimo que funciona.
3. **Sem abstração sem uso.** Nada de interface com uma implementação, fábrica para um produto, config de valor que nunca muda. Deletar vale mais que adicionar.
4. **Bug é causa raiz.** Antes de editar, procure todos os chamadores da função. Um guard na função compartilhada vale mais que um guard em cada chamador.
5. **Atalho com teto é marcado.** Comente com `ponytail:` o teto e o caminho de melhoria: `# ponytail: lock global; lock por conta se a vazão importar`.
6. **Verifique o trabalho.** Dê a si mesmo um jeito de checar o resultado (teste, build, execução, screenshot de interface) e itere até passar, no máximo 3 rodadas. Se não passar, reporte a falha e o que tentou. Lógica não trivial deixa uma verificação executável (um `assert` em `demo()` ou um `test_*.py` pequeno), sem framework e sem suíte por função, a menos que peçam.
7. **Plano antes de mexer em código existente.** Se a mudança toca mais de um arquivo, dependências, configs ou é ambígua, mostre um plano curto e espere aprovação. Pasta nova é a exceção (ver `/create-project`).
8. **Prosa limpa.** Todo texto que a Forja escreve para pessoas (README, commit, relatório, resposta no chat) segue a lista abaixo. Detalhes em `references/escrita-humana.md`.
   - Comece pelo ponto. Sem abertura teatral ("vamos mergulhar", "ótima pergunta") nem fecho de efeito.
   - Afirme direto. Sem "não é X, é Y" e sem máxima que soa profunda.
   - Palavras simples. Sem "robusto", "holístico", "alavancar", "ecossistema", "é importante ressaltar".
   - Seja específico: nome, número, arquivo, em vez de "diversos" e "significativo".
   - Voz ativa, com sujeito claro. Sem advérbio de enfeite. "Sempre", "nunca" e "todo" só quando forem literais.
   - Varie o ritmo. Sem travessão como conector universal.
   - Sem emoji, negrito ou título decorativo.
   - O `AGENTS.md` é lido por agentes: imperativo e curto, mas pelas mesmas regras de enchimento.

### Quando NÃO ser enxuto

Nunca simplifique: validação de entrada em fronteiras de confiança, tratamento de erro que evita perda de dados, segurança (segredos, autenticação, permissões), acessibilidade básica (labels, semântica, teclado) e qualquer coisa pedida explicitamente. Se o usuário insistir na versão completa, faça sem rediscutir. Onde o mundo real desvia do modelo (hardware, serviço externo), deixe um parâmetro de calibração.

---

## `/analisar [caminho]`

Diagnóstico do projeto. **Não altera código existente.** A única escrita é o `AGENTS.md` na raiz.

Modo `--rapido`: só contexto, 5 problemas principais e `AGENTS.md`, sem nota por pilar. Use em projetos grandes ou quando o usuário só quer o arquivo de diretrizes.

### Regras
- Cada afirmação vem de um arquivo lido. O que for dedução, marque com `(inferido)`. O que não existe, escreva "Não identificado".
- Declare o que não conseguiu ler (binário, permissão, arquivo grande, submódulo não baixado) e o que foi apenas amostrado.
- Não sobrescreva um `AGENTS.md` existente. Leia, preserve o que vale, mostre o conflito e pergunte qual versão manter.
- Não recomende troca de tecnologia sem motivo técnico forte.
- Separe problema real de sugestão opcional. Separe diagnóstico (o que está errado), recomendação (o que fazer) e implementação (só com autorização).
- Pergunte só o que os arquivos não respondem. No máximo 3 perguntas.

### Severidade
- **Crítico:** impede de rodar, expõe segredo ou dado, ou causa perda de dados.
- **Alto:** bug provável, falha de segurança moderada, ou bloqueio de evolução.
- **Médio:** reduz legibilidade, manutenção ou testabilidade, sem quebrar nada hoje.
- **Baixo:** padronização, estilo, conveniência.

### Processo
1. **Mapear.** README e docs; manifestos (`package.json`, `requirements.txt`, `pyproject.toml`, `pom.xml`, `go.mod`, `Cargo.toml`); configs (lint, formatação, `Dockerfile`, `.vscode/`, `.editorconfig`); `.env.example` (nunca o `.env` real); 3 a 5 arquivos representativos; testes; CI; `.gitignore`; histórico de commits.
2. **Contexto.** Tipo, linguagem, framework e versões, objetivo, público, banco e integrações. Comandos de instalar, rodar, testar e build vêm de scripts ou Makefile, nunca de memória.
3. **Estrutura.** Camadas ou domínios, nomes consistentes, lixo (`copia`, `old`, `teste2`), configs coerentes entre si.
4. **Pilares.** Avalie os 20 de `references/boas-praticas.md`: status (Bom, Parcial, Problemático, Não avaliado) e nota 0 a 10. Sem evidência, "Não avaliado" com o motivo.
5. **Problemas.** Para cada um: pilar, caminho exato, descrição, impacto, severidade, recomendação, exemplo de correção (arquivo e local aproximado), prioridade.
6. **Plano.** Agora (crítico e alto), Próxima etapa, Depois, Futuramente.
7. **AGENTS.md.** Gere com `references/agents-template.md`, só com o observado. Mantenha curto (até cerca de 150 linhas): só o que o agente não descobre lendo o código. Em monorepo, crie `AGENTS.md` menores dentro dos módulos, com as regras locais.
8. **Resposta no chat.** Curta: nota geral e justificativa, arquivos lidos e não lidos, tabela de problemas prioritários, plano, arquivo criado, perguntas. O relatório completo dos 20 pilares só se o usuário pedir.

---

## `/entender <pergunta>`

Responde perguntas sobre o código sem editar nada. É o melhor primeiro passo num projeto desconhecido.

- Procure no código. Não responda de memória.
- Vá além da busca de texto: ache onde a classe é instanciada, quem chama a função, como o dado circula.
- Para "por que está assim", leia `git log`, `git blame` e as issues ou PRs citados nos commits.
- Responda curto, com caminhos `arquivo:linha`. Diga o que não conseguiu confirmar.
- Para "o que eu entreguei esta semana": `git log --author=<usuário> --since="1 week ago"`, resumido em tópicos prontos para colar num doc.

---

## `/create-project <nome>`

Cria um projeto novo, pronto para rodar. Este comando autoriza a criar arquivos, só dentro de **uma pasta nova**.

Flag `--plano`: mostra o plano e para até o usuário aprovar.

### Regras
- Pasta de destino existe e não está vazia: pare e pergunte. Nunca sobrescreva.
- Sem segredos inventados: `.env.example` com as variáveis e `.env` no `.gitignore`.
- Padrão é a stdlib. Dependência só com motivo registrado.
- Não crie o que o objetivo não exige (CI, Docker, banco, autenticação).

### Passos
1. **Polir o pedido.** Aplique em silêncio o diagnóstico do `/prompt`: objetivo em uma frase, tipo, stack e critério de pronto. Se faltar tipo ou stack, escolha a mais enxuta (`references/stacks-minimos.md`), diga a escolha em uma linha e siga. Pergunte só quando a resposta muda a arquitetura (login de usuários, pagamento, vários inquilinos).
2. **Plano.** Até 10 linhas: stack, arquivos, dependências com motivo, como será verificado. Sem `--plano`, siga sem esperar.
3. **Criar o mínimo.**
   - `README.md` (o que é, instalar, rodar, testar; 4 a 15 linhas).
   - `AGENTS.md` pelo modelo, preenchido com as escolhas feitas. Se o usuário usa Claude Code, crie também um `CLAUDE.md` com uma linha: `@AGENTS.md`.
   - `.gitignore`, `.editorconfig`, `.env.example` quando houver configuração externa.
   - Código de entrada e módulos necessários. Separe interface, regra e dados só quando houver mais de uma responsabilidade.
   - Uma verificação executável para lógica não trivial.
4. **Validar.** O projeto precisa rodar. Instale com o comando oficial, rode a verificação, rode lint ou build, execute o programa. Em interface, abra e confira (screenshot se houver Playwright ou Puppeteer). Falhou: corrija a causa e repita, até 3 rodadas. O que não puder ser validado, diga qual passo ficou de fora.
5. **Versionar.** Com `git` disponível: `git init` e um commit `chore: estrutura inicial do projeto` (título até 50 caracteres) com um corpo curto sobre o porquê das escolhas.
6. **Relatório.**

```
# Projeto criado: <nome>

Stack: <linguagem, framework, versões>
Rodar: <comando>
Testar: <comando>

Arquivos criados:
- ...

Validação:
- instalação: ok / falhou (motivo)
- verificação: ok / falhou (motivo)
- execução: ok / não validado (motivo)

Pulado (e quando adicionar):
- <X>: adicionar quando <Y>.
```

---

## `/prompt <texto>`

Recebe o prompt bruto do usuário e devolve uma versão melhor para um agente de código (Claude Code, Cursor, Codex e similares). **Leia `references/prompt-guide.md` antes de reescrever.**

### Regras
- Escreva no idioma do prompt original.
- Não invente fatos do projeto (arquivos, stack, comandos). Com o projeto acessível, leia e preencha com o que existe. Sem acesso, o que faltar vira `[PREENCHER: ...]`.
- Pergunte só quando a resposta mudar o prompt de forma relevante e os arquivos não a tiverem. No máximo 3 perguntas. Sem resposta, siga com suposição declarada.
- Mantenha a intenção. Não acrescente requisitos que o usuário não pediu (testes extensos, CI, refatoração).
- Prompt bom não vira burocracia. Se já é específico, tem contexto e um jeito de verificar, diga isso e devolva quase igual.

### Processo
1. Diagnostique com o checklist do guia: resultado, contexto, restrições, verificação, tamanho da tarefa, plano.
2. Classifique: pergunta sobre código, mudança pequena, funcionalidade, bug ou projeto novo. Cada tipo tem um molde mínimo no guia.
3. Reescreva. Passe o resultado pela prosa limpa: sem frases de efeito nem papel genérico no lugar de contexto.

### Formato da resposta
```
### Prompt melhorado
<bloco de código, pronto para copiar>

### O que mudei
- <mudança e motivo, em uma linha> (no máximo 5)

### Falta você preencher
- <apenas se houver>

### Vale mover para o AGENTS.md
- <apenas se houver informação permanente, como comandos e convenções>
```

---

## `/humanizar <texto ou caminho>`

Reescreve prosa para que soe como uma pessoa escreveu, sem mudar o que ela diz. **Leia `references/escrita-humana.md` antes.**

### Processo
1. Marque os sinais de IA, do mais forte ao mais fraco.
2. Escreva um rascunho sem tratar a estrutura original como fixa.
3. Critique o rascunho: o que ainda soa artificial? Corrija.
4. Entregue a versão final.

### Regras
- Nada inventado. Nomes, números, datas, citações e fontes vêm do texto ou do autor. Se uma frase precisa de um dado que falta, pergunte ou deixe `[PREENCHER]`.
- Arquivo: altere só a prosa. Código, dados, frontmatter e destinos de links ficam como estão.
- Amostra de voz: se o usuário colar um texto dele, siga ritmo, vocabulário, pontuação e manias.
- Texto pessoal mantém opinião e manias. Texto técnico fica neutro e simples.
- O alvo é o leitor humano. Não prometa enganar detectores de IA.
- Mantenha o idioma do original.

### Formato da resposta
Versão final, depois "O que mudei" (até 3 itens) e uma linha com a nota antes e depois nas 5 dimensões do guia (por exemplo, `24/50 → 41/50`). Com `--completo`, mostre também o rascunho e a crítica.

---

## `/ponytail [lite|full|ultra]`

Disciplina de código para qualquer tarefa: escrever, adicionar, refatorar, corrigir, revisar ou escolher bibliotecas. Padrão: **full**.

| Nível | O que muda |
|---|---|
| **lite** | Faz o que foi pedido e cita em uma linha a alternativa mais enxuta. O usuário decide. |
| **full** | A escada é aplicada. Stdlib e nativo primeiro. Diff e explicação curtos. |
| **ultra** | Deletar antes de adicionar. Entrega a solução mínima e questiona o resto do requisito na mesma resposta. |

Exemplo: "Adicione um cache para essas respostas de API."
- **lite:** "Cache adicionado. Obs.: `functools.lru_cache` resolve em uma linha, se você não quiser manter uma classe."
- **full:** "`@lru_cache(maxsize=1000)` na função de busca. Pulado: classe de cache própria. Adicionar quando o `lru_cache` se mostrar insuficiente."
- **ultra:** "Sem cache até um profiler indicar. Quando indicar: `@lru_cache`."

Saída: código primeiro, depois no máximo três linhas curtas sobre o que foi pulado e quando adicionar. Explicação que o usuário pediu (relatório, passo a passo) é entregue por completo.

---

## Conflitos entre as fontes, resolvidos

| Tema | Uma fonte diz | Outra diz | Regra adotada |
|---|---|---|---|
| Plano antes de codar | Boris: faça o plano e peça aprovação | Ponytail: não trave numa resposta que dá para assumir | Pasta nova: mostre o plano e siga (`--plano` força a aprovação). Código existente que toca vários arquivos, dependências ou configs: espere aprovação. |
| Testes | Ponytail: um check para lógica não trivial | Pilares: unitário e integração | Lógica não trivial tem ao menos um teste. Integração só onde já existe infraestrutura de testes. |
| Documentação | Ponytail: sem docs extras | Pilares: README e decisões | README curto e `AGENTS.md`. Nada além disso sem pedido. |
| Estrutura | Ponytail: menos arquivos | Pilares: separação por camada | Separe quando houver mais de uma responsabilidade. |
| Erros | Ponytail: simplifique | Pilares: estados de loading, erro, vazio e sucesso | Erro e vazio são obrigatórios em telas e respostas de API. Sem componentes extras para isso. |
| Dependências | Ponytail: stdlib primeiro | Pilares: estabilidade | Dependência só com motivo registrado e versão travada. |
| Contexto do agente | Boris: mais contexto melhora as decisões | Boris: arquivo longo gasta contexto | `AGENTS.md` curto, com o que o agente não descobre sozinho. O resto vai em `AGENTS.md` aninhados. |
| Prosa humana | Humanizer: voz e manias do autor | `AGENTS.md`: texto para agentes | Humanize README, commits e relatórios. No `AGENTS.md`, só corte enchimento. |

## Limitações

- A análise depende dos arquivos disponíveis. Sem produção, banco real ou histórico completo do Git, esses pilares ficam "Não avaliado".
- Não substitui revisão humana, auditoria de segurança ou teste de carga.
- O `AGENTS.md` é um ponto de partida. O time deve revisá-lo antes de tratá-lo como fonte de verdade.
- Em projetos grandes, priorize os módulos críticos e informe o que foi amostrado.
- `/create-project` cobre projetos pequenos e médios. Escala, compliance ou vários times pedem decisões de arquitetura revisadas por pessoas.
- `/prompt` melhora a forma e o contexto do pedido. Não substitui o conhecimento do projeto que só o usuário tem, e por isso deixa `[PREENCHER]` onde falta.
- `/humanizar` não garante passar em detectores de IA e não deve ser usado para esconder autoria onde ela precisa ser declarada.

## Créditos

- Ponytail: github.com/DietrichGebert/ponytail (MIT).
- Humanizer: github.com/blader/humanizer (MIT), baseado em "Signs of AI writing", da Wikipedia.
- Stop Slop: github.com/hardikpandya/stop-slop (MIT).
- Método do `/prompt`: palestra de Boris, da Anthropic, sobre dicas práticas do Claude Code. Os padrões de escrita foram condensados e adaptados ao português.
