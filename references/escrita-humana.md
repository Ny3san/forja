# Escrita humana: filtro contra marcas de IA (base do /humanizar)

Fontes: **humanizer** (github.com/blader/humanizer, MIT, baseado em "Signs of AI writing", da Wikipedia) e **stop-slop** (github.com/hardikpandya/stop-slop, MIT). Os padrões foram condensados e adaptados ao português. Os exemplos são originais.

Conteúdo: 1. Por que o texto de IA soa assim · 2. Os 5 sinais mais fortes · 3. Padrões por grupo · 4. Verificações rápidas · 5. Nota · 6. Texto de projeto (README, commit, comentário) · 7. Exemplos

---

## 1. Por que o texto de IA soa assim

Um modelo de linguagem escolhe o que vem a seguir de um jeito que serve para o maior número possível de leitores e assuntos. Uma pessoa escolhe para um leitor e um assunto. Todo sinal abaixo é essa escolha padrão: a frase que anuncia importância em vez de dar um fato, o ritmo aplicado por regra, o fato comum vestido de decisivo, o resto de conversa de chat, a resposta que explica o que o leitor já sabe.

O alvo é o leitor humano. Passar em detector de IA não é objetivo.

---

## 2. Os 5 sinais mais fortes

Um único caso já justifica a edição.

| # | Sinal | Exemplo | Correção |
|---|---|---|---|
| 1 | **Não é X, é Y** | "Não é só um recurso, é uma mudança de jogo." | Diga Y direto. |
| 2 | **Fecho de uma linha** | "Pense nisso." depois de cada seção | Corte, ou funda numa afirmação específica. |
| 3 | **Máxima que soa profunda** | "No fundo, o que importa é a confiança." | Troque pela afirmação concreta. |
| 4 | **Preparação teatral** | "Vamos mergulhar.", "Sendo sincero?" | Comece pelo ponto. |
| 5 | **Discutir com ninguém** | "Não estou dizendo que X, mas...", "Uma abordagem tentadora seria..." | Remova a objeção ou a opção que ninguém levantou. |

---

## 3. Padrões por grupo

Os marcados com (fraco) só contam quando vários aparecem no mesmo trecho, porque um escritor cuidadoso pode usar qualquer um deles de propósito.

### A. Encenar em vez de afirmar

| Padrão | Exemplo | Correção |
|---|---|---|
| Fragmentos dramáticos | "Sem prior. Sem nostalgia." | Junte numa afirmação específica. |
| Fecho que repete ou explica o exemplo | "Isso mostra a importância de..." | Corte. |
| "O que acontece é que..." / "A verdade é que..." | Abertura que só prepara a frase | Diga a frase. |
| Narrador distante | "Ninguém projetou isso assim." | Ponha o leitor ou a pessoa na cena. |
| Metacomentário | "No restante deste texto, veremos..." | Apague. |

### B. Ritmo por regra

| Padrão | Exemplo | Correção |
|---|---|---|
| Tríades forçadas | "inovação, inspiração e insights" | Use quantos itens o sentido pede. |
| Frases começando igual | "Ela notou... Ela anotou... Ela arquivou..." | Junte ou mude o sujeito. |
| Frases do mesmo tamanho em sequência | Três frases de 12 palavras | Quebre uma. |
| Travessão como conector universal (fraco) | "a empresa — não o time — mas isso continua —" | Ponto, vírgula, dois-pontos ou parênteses. Mantenha só se a amostra de voz do autor usa. |
| Qualificadores empilhados (fraco) | "poderia talvez ser argumentado" | Fique só com o que a fonte sustenta. |
| Voz passiva e sujeito sumido (fraco) | "Nenhuma configuração é necessária." | Nomeie quem faz. |
| Advérbios de enfeite | "realmente", "simplesmente", "absolutamente" | Corte. |
| Extremos preguiçosos | "todo", "sempre", "nunca" sem ser literal | Diga o recorte real. |

### C. Inflação e autoridade emprestada

| Padrão | Exemplo | Correção |
|---|---|---|
| Palavras de IA | robusto, holístico, alavancar, sinergia, ecossistema, jornada, panorama, cenário atual, mergulhar, desvendar, crucial, transformador, de ponta | Palavra simples. |
| Significância inflada | "marca um momento decisivo", "o futuro é promissor" | Mantenha o fato, derrube o peso. Termine no último fato concreto. |
| Conexão vaga | "associado à liderança de", "em conexão com" | Diga a relação que a fonte dá. |
| Gerúndio de adorno | "simbolizando... refletindo... evidenciando..." | Mantenha só o que a fonte sustenta. |
| Linguagem de vendas | "localizado no coração de uma região deslumbrante" | Diga o que a coisa é. |
| Autoridade emprestada | "Especialistas acreditam...", "citado em grandes veículos" | Nomeie a fonte e o que ela disse, ou remova. |
| Fugir de "é" e "tem" | "configura-se como", "apresenta", "conta com" | "é", "tem". |
| Frases de preenchimento | "é importante ressaltar que", "vale destacar", "em suma", "nos dias de hoje" | Corte. |

### D. Formatação por regra

| Padrão | Exemplo | Correção |
|---|---|---|
| Negrito decorativo | "**KPIs**, **OKRs**" | Tire o negrito. Lista rotulada com negrito vira prosa. |
| Título decorativo | "🚀 Fase de Lançamento:", "A decisão, em uma tela" | Caixa de frase, sem emoji nem seta; diga o que a seção contém. |
| Aspas curvas (fraco) | “o projeto” | Aspas retas. |
| Emoji de enfeite | ✨🚀 | Remova. |

### E. Sobras do chat e do rascunho

| Padrão | Exemplo | Correção |
|---|---|---|
| Resíduo de chatbot | "Ótima pergunta!", "Espero ter ajudado!" | Tire a embalagem e fique com o conteúdo. |
| Aviso de limite de conhecimento | "Embora os detalhes sejam limitados..." | Diga o que a fonte mostra ou remova a frase. |
| Título repetido na primeira frase | "## Desempenho" seguido de "O desempenho importa." | Deixe o título trabalhar. |
| Escrever sobre o documento, não o assunto | "Esta função foi adicionada para substituir...", "A tabela abaixo compara..." | Descreva o assunto. A história da mudança vai no commit. |

### F. Escrever para o leitor errado

| Padrão | Exemplo | Correção |
|---|---|---|
| Reexplicar o que o leitor já sabe | Resposta que refaz o diagnóstico antes da decisão | Comece pela decisão. Diagnóstico e prova ficam para depois. |

---

## 4. Verificações rápidas

Antes de entregar prosa:

- Há advérbio de enfeite? Corte.
- Há voz passiva? Ache o ator e faça dele o sujeito.
- Algo inanimado faz verbo humano ("a decisão emerge")? Nomeie a pessoa.
- Há abertura que só prepara ("o que acontece é que")? Corte.
- Há "não é X, é Y"? Diga Y.
- Três frases seguidas com o mesmo tamanho? Quebre uma.
- O parágrafo termina em frase de efeito? Varie o fecho.
- Há travessão? Troque, salvo se a voz do autor o usa.
- Há afirmação vaga ("as implicações são significativas")? Nomeie a implicação.
- Soa como frase de citação? Reescreva.

---

## 5. Nota

Dê de 1 a 10 em cada dimensão, antes e depois. Abaixo de 35 de 50, revise de novo.

| Dimensão | Pergunta |
|---|---|
| Direto | Afirma ou anuncia? |
| Ritmo | Varia ou marca compasso? |
| Confiança | Respeita a inteligência do leitor? |
| Autenticidade | Soa como gente? |
| Densidade | Dá para cortar algo? |

---

## 6. Texto de projeto

| Onde | Regra |
|---|---|
| **README** | Diga o que é, como instalar, rodar e testar. Sem apresentação de vendas. |
| **Mensagem de commit** | `tipo: descrição` com até 50 caracteres, no imperativo ou presente, sem emoji. O corpo explica o porquê. |
| **Comentário de código** | Explique a razão, não o óbvio. "Incrementa i" não ajuda. Histórico da mudança vai no commit, não no comentário. |
| **Mensagem de erro** | Diga o que aconteceu e o que fazer. Sem "Ops!" e sem detalhe interno exposto ao usuário final. |
| **Relatório da Forja** | Resultado primeiro, evidência depois. Sem resumo do que acabou de ser dito. |
| **AGENTS.md** | Imperativo e curto. Mesmas regras de enchimento; sem preocupação com voz. |

Não altere o que o texto afirma. Nome, número, data, citação e fonte vêm do original ou do autor.

---

## 7. Exemplos

### README

**Antes**
> 🚀 Bem-vindo ao ToDoPro! Nossa solução robusta e inovadora revoluciona a forma como você gerencia tarefas. Não é apenas uma lista de tarefas, é um verdadeiro ecossistema de produtividade. Vamos mergulhar!

**Depois**
> ToDoPro é um app de linha de comando para gerenciar tarefas. Ele guarda tudo num arquivo JSON local. Instale com `pip install todopro` e rode `todopro add "comprar pão"`.

O "depois" assume que o projeto confirma esses fatos. Se não confirmar, os dados faltantes viram `[PREENCHER]`.

### Commit

**Antes**
> ✨ feat: Implementa uma robusta solução de cache para otimizar significativamente o desempenho do sistema!

**Depois**
> feat: cacheia a busca de usuários por 5 minutos
>
> A tela de equipe chamava a busca a cada renderização. O cache reduz as chamadas repetidas.

### Resposta no chat

**Antes**
> Ótima pergunta! Vale destacar que existem diversas abordagens possíveis. Em suma, a melhor escolha depende do seu contexto.

**Depois**
> Use `sqlite3` da stdlib. Você tem uma tabela e um usuário, e um servidor de banco só adicionaria manutenção.
