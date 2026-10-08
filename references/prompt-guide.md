# Guia de prompts (base do /prompt)

Fonte: palestra de Boris, da Anthropic, sobre dicas práticas para usar o Claude Code. As lições valem para qualquer agente de código. Este guia as transforma em critérios para diagnosticar e reescrever um prompt.

Conteúdo: 1. As 8 lições · 2. Checklist de diagnóstico · 3. Molde · 4. Moldes por tipo de tarefa · 5. Tamanho da tarefa · 6. Onde cada informação mora · 7. Exemplos · 8. O que evitar

---

## 1. As 8 lições

| # | Lição | Por que funciona | O que fazer no prompt |
|---|---|---|---|
| 1 | **Comece entendendo.** Perguntas sobre o código antes de editar. | Mostra o que o agente consegue sozinho e onde precisa de ajuda. | Em área desconhecida, abra com "leia X e explique como funciona hoje". |
| 2 | **Seja específico, como com outro engenheiro.** | O agente decide melhor com detalhes do que com um desejo vago. | Troque "melhore" por o resultado, o lugar e o motivo. Prompts mais longos e falados funcionam bem. |
| 3 | **Peça um plano antes do código.** | Uma funcionalidade grande pedida de uma vez às vezes sai certa, às vezes sai outra coisa. O plano barato evita retrabalho caro. | "Antes de escrever código, faça um plano e espere minha aprovação." Não precisa de modo especial. |
| 4 | **Dê contexto.** Arquivos, decisões de arquitetura, comandos, estilo, histórico do Git, issues. | Quanto mais contexto, melhores as decisões. | Cite os arquivos (`@caminho`), aponte a issue ou o commit, diga a restrição e o motivo. |
| 5 | **Apresente as ferramentas.** CLIs e servidores MCP do time. | O agente encadeia as ferramentas sozinho se souber que existem. | "Use `<cli>` e veja `--help` para os comandos." Não ensine o encadeamento passo a passo. |
| 6 | **Dê um jeito de verificar e iterar.** Testes, screenshot, simulador. | Com feedback, duas ou três rodadas chegam perto do perfeito. Sem ele, o agente declara pronto no escuro. | Termine com "pronto quando `<comando ou checagem>`; itere até passar". |
| 7 | **Confie no que o modelo já sabe.** Git, formato de commit, convenções do repo. | Explicar o óbvio gasta contexto e não melhora o resultado. | "Faça commit, push e abra um PR" basta. O agente lê o histórico para achar o formato. |
| 8 | **Corrija cedo e só o trecho errado.** | Interromper no meio custa menos que refazer tudo. | Peça confirmação nos pontos de decisão. Se 19 de 20 linhas servem, peça para trocar uma. |

---

## 2. Checklist de diagnóstico

Marque cada item como ok, fraco ou ausente.

| Item | Pergunta | Se faltar |
|---|---|---|
| Resultado | Dá para saber, ao ler, como fica o mundo quando a tarefa termina? | Reescreva como resultado ("o usuário consegue X"), não como método. |
| Contexto | O agente sabe onde mexer e por que isso importa? | Adicione arquivos, stack, issue ou a conversa que originou o pedido. |
| Restrições | Está claro o que não fazer e quais padrões seguir? | Adicione "siga o AGENTS.md" e as proibições, com o motivo de cada uma. |
| Verificação | Existe um comando ou checagem que prova que funcionou? | Adicione "pronto quando..." e peça para iterar até passar. |
| Tamanho | Cabe num plano de até uns 10 passos? | Quebre em etapas (seção 5). |
| Plano | Tarefa de vários arquivos ou ambígua pede aprovação antes de editar? | Adicione "mostre um plano e espere minha aprovação". |
| Lugar da informação | Algo permanente (comandos, convenções) está preso no prompt? | Sugira mover para o `AGENTS.md` (seção 6). |

Dois ou mais itens ausentes: o prompt precisa de reescrita. Um item fraco: ajuste e explique. Todos ok: devolva igual e diga por quê.

---

## 3. Molde

Remova a linha que não se aplica. Um prompt pequeno continua pequeno.

```
Objetivo: <resultado esperado, em 1 ou 2 frases>
Contexto: <onde mora, arquivos @, stack, por que isso é necessário>
Restrições: <o que não mexer, padrões a seguir, e o motivo>
Antes de codar: leia <arquivos> e me mostre um plano curto. Espere minha aprovação.
Pronto quando: <comando de teste, build ou checagem visual>. Itere até passar.
Entrega: <o que reportar; commit ou PR, se quiser>
```

---

## 4. Moldes por tipo de tarefa

| Tipo | Mínimo necessário |
|---|---|
| **Pergunta sobre código** | A pergunta, o trecho ou área, e se quer o porquê histórico (peça `git log` e `git blame`). Sem plano, sem verificação. |
| **Mudança pequena** | Objetivo, arquivo, restrição. Sem plano; verificação em uma linha. |
| **Funcionalidade** | Todas as linhas do molde. Plano com aprovação. |
| **Bug** | Esperado, atual, como reproduzir. Peça a causa raiz e a lista de chamadores antes de editar. Verificação: um teste que falha antes e passa depois. |
| **Projeto novo** | Objetivo, tipo, stack ou "a mais enxuta", critério de pronto. Pode usar `/create-project`. |
| **Interface a partir de um mock** | Imagem do mock, ferramenta de screenshot e "compare e itere até ficar igual". |

---

## 5. Tamanho da tarefa

- Mais de uns 10 passos, ou mais de um módulo independente: quebre em etapas, cada uma com seu critério de pronto.
- Etapas independentes podem rodar em paralelo, em sessões ou checkouts separados.
- Pedido gigante de uma vez ("implemente o sistema inteiro") vira: etapa 1 plano e esqueleto, etapa 2 núcleo com testes, etapa 3 bordas.
- Na dúvida, comece pelo plano. É a etapa mais barata de corrigir.

---

## 6. Onde cada informação mora

| A informação é... | Vai para... |
|---|---|
| Só desta tarefa | O prompt |
| Permanente e do time (comandos, convenções, arquivos centrais, decisões de arquitetura) | `AGENTS.md` do projeto, curto |
| Específica de uma pasta | `AGENTS.md` dentro da pasta |
| Preferência pessoal | Arquivo local fora do Git (`AGENTS.local.md` ou `CLAUDE.local.md`, no `.gitignore`) |
| Um fluxo repetido (rotular issues, revisar PR) | Um comando reutilizável da ferramenta |
| Segredo | Variável de ambiente, nunca no prompt |

Pergunte, para cada dado: quem precisa dele, sempre ou só às vezes, time inteiro ou só eu? Contexto longo demais gasta a janela do agente e rende pouco.

---

## 7. Exemplos

### Exemplo 1: pedido vago

**Antes**
```
Faz um sistema de login pro meu site.
```

**Depois**
```
Objetivo: adicionar login com e-mail e senha ao site, com sessão persistente e logout.
Contexto: o site usa [PREENCHER: stack, ex.: Express + SQLite]. Usuários ficam em [PREENCHER: tabela ou arquivo]. Siga o AGENTS.md.
Restrições: senha sempre com hash (bcrypt ou argon2), segredos em variável de ambiente, nenhuma biblioteca de autenticação nova sem me avisar.
Antes de codar: leia as rotas e o modelo de usuário atuais e me mostre um plano de até 10 linhas. Espere minha aprovação.
Pronto quando: um teste cobre cadastro, login correto, login com senha errada e logout, e `npm test` passa. Itere até passar.
Entrega: liste os arquivos alterados e o que ficou de fora.
```

**O que mudou:** resultado e escopo explícitos; restrições de segurança com motivo; plano antes de codar; verificação executável; lacunas marcadas em vez de inventadas.

### Exemplo 2: bug

**Antes**
```
O botão de salvar não funciona.
```

**Depois**
```
Objetivo: corrigir o botão "Salvar" do formulário de perfil, que não grava as alterações.
Contexto: acontece em [PREENCHER: tela ou URL]. Esperado: gravar e mostrar "Salvo". Atual: [PREENCHER: nada acontece, ou erro no console?].
Antes de editar: ache a causa raiz e liste todos os chamadores da função envolvida. Me diga a causa antes de corrigir.
Pronto quando: um teste reproduz a falha, falha antes da correção e passa depois, e a suíte inteira passa.
```

**O que mudou:** sintoma virou esperado versus atual; pede causa raiz antes de editar; verificação em dois tempos.

### Exemplo 3: já está bom

**Antes**
```
Faça commit das mudanças, dê push e abra um PR.
```

**Depois:** igual. O repositório e o histórico do Git já dizem ao agente o formato do commit e do PR. Acrescentar instruções só gastaria contexto.

---

## 8. O que evitar

- Frases de efeito ("seja o melhor engenheiro do mundo", "pense muito bem", letras maiúsculas gritando). Não substituem contexto.
- Regra sem motivo. Com o motivo, o agente aplica nos casos de borda que você não previu.
- Ensinar o que o agente já sabe (como usar o Git, como estruturar um commit).
- Detalhar o encadeamento de ferramentas. Diga que a ferramenta existe e onde está o `--help`.
- Inflar prompt pequeno com seções vazias.
- Pedir tudo de uma vez quando há mais de uma etapa independente.
- Inventar fatos do projeto para preencher o molde. Lacuna fica como `[PREENCHER]`.
