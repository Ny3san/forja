# Forja

Forja é uma skill para agentes de código (Claude Code, Codex, Cursor e outros) que entrega código bem feito, simples e funcional, e prosa sem enchimento.

Ela tem seis comandos. Cada um resolve um problema diferente que aparece quando se trabalha com IA escrevendo código:

- O agente cria um projeto com estrutura demais e dependências que ninguém pediu.
- Você entra num projeto que não conhece e não sabe por onde começar.
- Seu prompt é vago, e o agente faz outra coisa.
- Um texto escrito por IA soa genérico e robótico.
- Você quer as regras do projeto registradas para os próximos agentes que mexerem nele.

A Forja trata cada um desses casos com um comando próprio.

## Comandos

| Comando | Para que serve | Escreve arquivos? |
|---|---|---|
| `/analisar [caminho]` | Avalia o projeto pelos 20 pilares de qualidade e gera um `AGENTS.md` com as diretrizes | Só o `AGENTS.md` |
| `/entender <pergunta>` | Responde perguntas sobre o código, incluindo o motivo histórico de cada decisão | Não |
| `/create-project <nome>` | Cria um projeto novo, enxuto e validado, numa pasta nova | Só na pasta nova |
| `/prompt <texto>` | Reescreve um prompt vago como um pedido claro para um agente de código | Não |
| `/humanizar <texto ou arquivo>` | Remove marcas de texto escrito por IA, sem mudar o que o texto diz | Só se receber um arquivo |
| `/ponytail [lite\|full\|ultra]` | Aplica a solução mais simples que funciona a qualquer tarefa de código | Conforme a tarefa |

Se você não usar o comando explicitamente, a skill escolhe pela intenção do pedido. "Melhora esse prompt" vai para `/prompt`. "Tira a cara de IA disso" vai para `/humanizar`. "Como funciona essa parte do código?" vai para `/entender`. Qualquer outra tarefa de código roda no modo `/ponytail full`.

## Instalação

A forma mais rápida é pelo Skills CLI, que instala a skill no diretório certo de cada agente:

```bash
# Instala para o agente que você usa, no projeto atual
npx skills add Ny3san/forja -a codex

# Instala para todos os seus projetos
npx skills add Ny3san/forja -g -a claude-code

# Instala para vários agentes de uma vez
npx skills add Ny3san/forja -g -a codex -a claude-code -a cursor

# Instala para todos os agentes suportados
npx skills add Ny3san/forja --agent '*' -g
```

`-g` instala no diretório do usuário, para valer em todos os projetos. Sem ele, a instalação fica só no projeto atual. Use `-y` para pular as perguntas.

Para verificar o que está instalado:

```bash
npx skills ls -a codex
```

Para atualizar depois de uma nova versão:

```bash
npx skills update
```

### Instalação manual

Se preferir não usar o CLI, copie a pasta `forja/` para o diretório de skills do seu agente:

| Agente | macOS e Linux | Windows |
|---|---|---|
| Codex | `~/.codex/skills/forja/` | `%USERPROFILE%\.codex\skills\forja\` |
| Claude Code | `~/.claude/skills/forja/` | `%USERPROFILE%\.claude\skills\forja\` |
| Cursor | `~/.cursor/skills/forja/` | `%USERPROFILE%\.cursor\skills\forja\` |

Reinicie o agente depois de copiar, para ele carregar a skill.

## Como usar

### Com Claude Code

Os comandos com barra funcionam direto no chat:

```text
/forja analisar este projeto
/forja create-project tarefas-cli --plano
/forja prompt "faz um login pro meu site"
```

### Com Codex e outros agentes

Peça pelo nome da skill e pelo comando:

```text
Use a skill forja, comando /analisar, no projeto atual.
```

Os agentes que lêem `AGENTS.md` (Codex, Cursor, Copilot e outros) seguem as regras do arquivo gerado pelo `/analisar` mesmo sem a skill instalada. Isso faz da Forja uma ferramenta de duas partes: a skill cria as diretrizes, e o arquivo as mantém valendo para qualquer agente que mexer no projeto.

## Exemplos

### Analisar um projeto desconhecido

```text
/forja analisar ./meu-projeto
```

A Forja lê o README, os manifestos de dependência, as configurações, os testes e o CI. Depois avalia os 20 pilares de qualidade, com status e nota de cada um, e lista os problemas por severidade: crítico, alto, médio e baixo. No fim, cria um `AGENTS.md` na raiz do projeto. Nada no código existente é alterado.

Se o projeto for grande, use o modo rápido, que gera só o contexto, os cinco problemas principais e o `AGENTS.md`:

```text
/forja analisar ./monorepo --rapido
```

### Entender o código antes de mexer

```text
/forja entender por que a função de cobrança recebe 15 argumentos
```

Em vez de uma busca de texto, a Forja procura onde a função é chamada, lê o `git log` e o `git blame` e segue as issues e PRs citadas nos commits. A resposta vem curta e com caminhos `arquivo:linha`. Quando não é possível confirmar algo, ela diz isso.

### Criar um projeto novo

```text
/forja create-project agenda-cli
```

Sem outras informações, a Forja escolhe a stack mais enxuta que atende ao objetivo, diz a escolha em uma linha e segue. Ela cria o `README.md`, o `AGENTS.md`, o `.gitignore`, o código de entrada e uma verificação executável, roda a instalação, os testes e o programa, e só então declara o projeto pronto. Se algum passo não puder ser validado, a resposta diz qual.

Para ver o plano antes de qualquer arquivo ser criado:

```text
/forja create-project agenda-cli --plano
```

### Melhorar um prompt

Entrada:

```text
faz um sistema de login pro meu site
```

Saída, em forma de molde:

```text
Objetivo: adicionar login com e-mail e senha ao site, com sessão persistente e logout.
Contexto: o site usa [PREENCHER: stack]. Usuários ficam em [PREENCHER: tabela ou arquivo]. Siga o AGENTS.md.
Restrições: senha sempre com hash, segredos em variável de ambiente, nenhuma biblioteca de autenticação nova sem aviso.
Antes de codar: leia as rotas e o modelo de usuário atuais e mostre um plano de até 10 linhas. Espere aprovação.
Pronto quando: um teste cobre cadastro, login correto, senha errada e logout, e a suíte passa. Itere até passar.
```

A Forja não inventa o que não sabe. Lacunas aparecem como `[PREENCHER]`, e a resposta lista o que você precisa completar. Prompt que já está bom volta quase igual, com a explicação de por que não precisa mudar.

### Tirar a cara de IA de um texto

```text
/forja humanizar README.md
```

Na versão padrão, a Forja altera só a prosa. Código, dados, frontmatter e links ficam como estão. Se você colar um texto seu como amostra de voz, ela segue o seu ritmo e o seu vocabulário. A resposta mostra a nota do texto antes e depois, em cinco dimensões: direto, ritmo, confiança, autenticidade e densidade.

### Escrever código enxuto

```text
/forja ponytail ultra adicionar cache para as respostas da API
```

No modo `ultra`, a resposta prioriza deletar antes de adicionar e questiona o próprio requisito. No modo `full`, que é o padrão, a solução usa a stdlib e o recurso nativo da plataforma antes de qualquer dependência:

```python
@lru_cache(maxsize=1000)
def buscar_usuario(id: int) -> dict:
    ...
# Pulado: classe de cache própria. Adicionar quando o lru_cache se mostrar insuficiente.
```

## Princípios

A Forja segue oito princípios em todos os comandos:

1. **Entender antes de mudar.** Ela lê os arquivos que a mudança toca e segue o fluxo real. A escada de decisão encurta a solução, nunca a leitura.
2. **Escada de decisão.** Antes de escrever código, a pergunta é: isso precisa existir? Já existe no projeto? A stdlib resolve? Um recurso nativo resolve? Uma dependência já instalada resolve? Cabe em uma linha? Só então vem o código mínimo.
3. **Sem abstração sem uso.** Nada de interface com uma implementação, fábrica para um produto, ou configuração de valor que nunca muda.
4. **Bug é causa raiz.** Antes de corrigir, a Forja procura todos os chamadores da função. Um guard na função compartilhada vale mais que um guard em cada caso.
5. **Atalho com teto é marcado.** Simplificações com limite conhecido levam um comentário `ponytail:` dizendo o limite e o caminho de melhoria.
6. **Verificar o próprio trabalho.** A Forja roda testes, build ou o programa e itera até passar, no máximo três rodadas. Se não passar, reporta a falha.
7. **Plano antes de mexer em código existente.** Em pasta nova, ela mostra o plano e segue. Em código existente que toca vários arquivos, dependências ou configurações, espera aprovação.
8. **Prosa limpa.** Textos que a Forja escreve para pessoas (README, commit, relatório, resposta no chat) evitam frases de efeito, palavras genéricas, emoji decorativo e travessão como conector universal.

### Quando não ser enxuto

Algumas coisas nunca são cortadas, mesmo com o modo `ultra`:

- Validação de entrada em pontos de confiança, como formulários, parâmetros de API e respostas externas.
- Tratamento de erro que impede perda de dados.
- Segurança: segredos, autenticação e permissões.
- Acessibilidade básica: labels, semântica HTML e navegação por teclado.
- Qualquer coisa que você tenha pedido explicitamente. Se você insistir na versão completa, a Forja faz sem discutir.

## Os 20 pilares

O `/analisar` usa 20 pilares de qualidade para avaliar um projeto. Eles estão detalhados em `references/boas-praticas.md`:

1. Objetivo e escopo
2. Arquitetura
3. Estrutura de pastas e arquivos
4. Fluxos do sistema
5. Modelagem de dados e contratos
6. Ambiente do VS Code
7. Legibilidade do código
8. Componentização
9. Gerenciamento de estado
10. UI, UX e design system
11. Acessibilidade e responsividade
12. Estados da interface e tratamento de erros
13. Segurança e privacidade
14. Testes
15. Desempenho e escalabilidade
16. Git e colaboração
17. Documentação
18. Configuração e dependências
19. CI/CD, deploy e observabilidade
20. Manutenção e evolução

Para cada pilar, a análise indica o status (Bom, Parcial, Problemático ou Não avaliado), a nota de 0 a 10 e a evidência. Sem evidência suficiente, o pilar fica como "Não avaliado", com o motivo. A Forja não dá nota alta sem evidência.

## O AGENTS.md gerado

O arquivo `AGENTS.md` é a parte que mais se beneficia da Forja no longo prazo. Ele fica na raiz do projeto e reúne o que um agente precisa saber antes de mexer no código:

- Contexto: tipo de projeto, objetivo, público, stack e integrações.
- Comandos oficiais de instalar, rodar, testar, formatar e buildar.
- Arquitetura e regra de dependência entre as camadas.
- Estrutura de pastas e onde colocar cada tipo de código novo.
- Convenções de nomes, formatação e tipagem.
- Regras de segurança, testes, commits e documentação.
- Lista do que é proibido fazer sem pedido.
- Pendências encontradas na análise, com severidade.

O arquivo é gerado só com o que foi observado no projeto. O que não puder ser confirmado é marcado como "Não identificado". Como o conteúdo entra no contexto do agente em toda sessão, o modelo pede que o arquivo tenha até cerca de 150 linhas. Em monorepos, cada módulo pode ter o próprio `AGENTS.md`.

Depois de gerado, revise o arquivo com o time antes de tratá-lo como fonte de verdade.

## Referências

A skill carrega cada arquivo de referência só quando o comando precisa dele:

| Arquivo | Conteúdo | Usado por |
|---|---|---|
| `references/boas-praticas.md` | Os 20 pilares e as regras gerais de código | `/analisar`, `/create-project` |
| `references/agents-template.md` | Modelo do `AGENTS.md` | `/analisar`, `/create-project` |
| `references/stacks-minimos.md` | Esqueletos mínimos por tipo de projeto | `/create-project` |
| `references/prompt-guide.md` | Lições de prompts, checklist e moldes | `/prompt` |
| `references/escrita-humana.md` | Padrões de texto escrito por IA e como corrigi-los | `/humanizar` |

Essa separação mantém a skill leve. O arquivo principal fica pequeno, e os detalhes entram no contexto só quando são necessários.

## Stacks suportadas pelo /create-project

O `/create-project` escolhe a menor stack que atende ao objetivo. A ordem vai do mais enxuto ao mais pesado:

1. **Site estático:** HTML, CSS e JavaScript puros, sem framework.
2. **Script ou CLI em Python:** stdlib, `argparse` e `unittest`.
3. **Script ou CLI em Node:** `node:util` e `node:test`.
4. **API HTTP:** stdlib do Python ou do Node, ou Flask e Express quando houver roteamento real.
5. **Frontend com framework:** React ou Vue com Vite.
6. **Persistência simples:** SQLite pela stdlib, com schema em arquivo versionado.

Se a escolha mudar a arquitetura de forma relevante, como login de usuários, pagamento ou vários inquilinos, a Forja pergunta antes de criar qualquer arquivo.

## Limitações

A Forja tem limites que vale conhecer antes de depender dela:

- **A análise depende dos arquivos disponíveis.** Sem acesso à produção, ao banco real ou ao histórico completo do Git, os pilares correspondentes ficam como "Não avaliado".
- **Não substitui revisão humana.** Não é uma auditoria de segurança formal, nem um teste de carga.
- **O `AGENTS.md` é um ponto de partida.** O time deve revisá-lo antes de usá-lo como referência.
- **Projetos grandes são amostrados.** A Forja prioriza os módulos críticos e informa o que não conseguiu ler por completo.
- **O `/create-project` cobre projetos pequenos e médios.** Escala, compliance e vários times pedem decisões de arquitetura tomadas por pessoas.
- **O `/prompt` não conhece o seu projeto além do que consegue ler.** Por isso ele deixa `[PREENCHER]` onde falta informação.
- **O `/humanizar` não garante passar em detectores de IA.** O objetivo é texto claro para leitores humanos. Ele não deve ser usado para esconder autoria onde a autoria precisa ser declarada.
- **Os comandos com barra são pensados para Claude Code.** Em outros agentes, peça pelo nome do comando, como no exemplo de uso.

## Perguntas frequentes

**A Forja executa comandos no meu computador?**
Sim, quando você pede. O `/create-project` instala dependências e roda testes e o programa, e o `/analisar` lê arquivos. Leia o `SKILL.md` antes de instalar, como faria com qualquer código de terceiros.

**Preciso de internet?**
Só para instalar a skill. Depois de instalada, os comandos rodam com os arquivos locais e com o que o agente já tem acesso.

**A Forja altera meu código existente?**
O `/analisar` não altera código. O `/entender` também não. O `/humanizar` altera só a prosa de arquivos que você indicar. O `/create-project` cria arquivos apenas numa pasta nova. Mudanças em código existente seguem o princípio de plano antes de implementar: a Forja mostra o que vai mudar e espera aprovação quando a mudança é grande.

**Funciona com linguagens além de Python, Node e JavaScript?**
A análise e o `/entender` funcionam com qualquer linguagem que o agente consiga ler. O `/create-project` tem esqueletos para as stacks listadas acima. Para outras linguagens, a Forja escolhe a stack mais enxuta que conhece e registra a escolha.

**Por que se chama Forja?**
Forjar é dar forma a algo sólido com o mínimo de material. É a ideia do projeto: código bem feito, sem excesso.

**Posso usar a Forja em projetos comerciais?**
Sim. A skill é distribuída sob licença MIT. As skills e os projetos de onde ela se inspirou também são MIT, como listado em Créditos.

**Como contribuo?**
Abra uma issue descrevendo o caso de uso ou a regra que faltou. Para mudanças no comportamento da skill, descreva o problema antes da solução. Pull requests são bem-vindos com um caso de teste ou um exemplo de antes e depois.

## Roteiro

Itens que ainda não estão prontos:

- Testes automatizados para cada comando, com entradas e saídas esperadas.
- Modo `/analisar --json`, para integrar a análise a pipelines de CI.
- Mais stacks no `/create-project`, incluindo Go e Rust com esqueletos mínimos.
- Exemplos reais de `AGENTS.md` gerados em projetos open source conhecidos.
- Versão em inglês da documentação e dos padrões de escrita.

## Créditos

A Forja junta ideias de outros projetos e as adapta ao português e ao fluxo de código:

- **ponytail** (github.com/DietrichGebert/ponytail, MIT): a escada de decisão, o princípio de deletar antes de adicionar e a marcação `ponytail:` para atalhos com teto conhecido.
- **humanizer** (github.com/blader/humanizer, MIT): os padrões de texto escrito por IA e a ideia de mostrar a versão antes e depois. A base é o guia "Signs of AI writing", da Wikipedia.
- **stop-slop** (github.com/hardikpandya/stop-slop, MIT): as regras de frase, o filtro de advérbios e voz passiva e a pontuação em cinco dimensões.
- **Palestra de Boris, da Anthropic**, sobre dicas práticas para o Claude Code: as lições que estruturam o `/prompt`, como começar pelas perguntas sobre o código, pedir um plano antes de codar e dar um jeito de verificar o resultado.

A Forja não é afiliada à Anthropic, à Vercel, à Wikipedia nem aos autores dos projetos citados. Os nomes são usados apenas para dar crédito às fontes.

## Estrutura do repositório

```text
forja/
├── SKILL.md                      # comandos, princípios e processos (carregado sempre)
├── README.md                     # esta documentação
├── LICENSE                       # MIT
└── references/                   # carregados sob demanda pelos comandos
    ├── boas-praticas.md          # 20 pilares e regras gerais de código
    ├── agents-template.md        # modelo do AGENTS.md
    ├── stacks-minimos.md         # esqueletos por tipo de projeto
    ├── prompt-guide.md           # método e moldes do /prompt
    └── escrita-humana.md         # padrões de texto escrito por IA
```

O `SKILL.md` fica na raiz do repositório, porque é o arquivo que o agente lê primeiro. O Skills CLI usa esse arquivo para reconhecer a skill. As referências ficam numa subpasta para que o contexto do agente não seja gasto com detalhes que a tarefa atual não usa.

## Desinstalação

Pelo Skills CLI:

```bash
npx skills remove --agent codex forja
```

Manualmente, apague a pasta `forja/` do diretório de skills do agente (veja a tabela de instalação manual). Os arquivos `AGENTS.md` que a Forja criou nos seus projetos não são removidos automaticamente: eles continuam valendo para os agentes que lerem o projeto, então apague-os só se quiser.

## Compatibilidade

| Agente | Skill instalada | Comandos com barra | Lê o AGENTS.md |
|---|---|---|---|
| Claude Code | Sim | Sim | Sim, com `CLAUDE.md` apontando para ele |
| Codex | Sim | Pelo nome do comando | Sim |
| Cursor | Sim | Pelo nome do comando | Sim |
| Outros agentes com Skills CLI | Sim | Pelo nome do comando | Depende do agente |

Os comandos com barra dependem de cada agente. Quando não funcionarem, use a forma em texto: "use a skill forja, comando /analisar".

## Licença

MIT. Veja o arquivo `LICENSE`.
