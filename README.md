# Forja

Forja é uma skill para agentes de código que reúne seis fluxos: diagnosticar projetos, explicar código, criar projetos mínimos, melhorar prompts, revisar prosa e reduzir complexidade desnecessária.

## Comandos

| Comando | Resultado | Escrita permitida |
|---|---|---|
| `/analisar [caminho]` | Diagnóstico baseado em evidências | Nenhuma por padrão |
| `/analisar [caminho] --agents` | Diagnóstico e `AGENTS.md` na raiz | Somente o arquivo autorizado |
| `/entender <pergunta>` | Explicação do código e do histórico disponível | Nenhuma |
| `/create-project <nome>` | Projeto mínimo e validado em pasta nova | Somente na pasta nova |
| `/prompt <texto>` | Prompt técnico revisado | Nenhuma |
| `/humanizar <texto ou arquivo>` | Prosa revisada sem alterar fatos | Somente o arquivo indicado |
| `/ponytail [lite\|full\|ultra]` | Menor solução completa para a tarefa | Conforme a tarefa autorizada |

A skill pode reconhecer intenções claras, como “explique este fluxo” ou “melhore este prompt”. `/ponytail` não é o modo automático de toda tarefa de código; ele entra quando for pedido ou quando o problema for complexidade desnecessária.

## Instalação

Pelo Skills CLI:

```bash
npx skills add Ny3san/forja -a codex
npx skills add Ny3san/forja -g -a claude-code
```

Use `-g` para instalar para o usuário. Para atualizar:

```bash
npx skills update
```

Na instalação manual, copie este repositório para a pasta de skills do agente:

| Agente | macOS e Linux | Windows |
|---|---|---|
| Codex | `~/.codex/skills/forja/` | `%USERPROFILE%\.codex\skills\forja\` |
| Claude Code | `~/.claude/skills/forja/` | `%USERPROFILE%\.claude\skills\forja\` |
| Cursor | `~/.cursor/skills/forja/` | `%USERPROFILE%\.cursor\skills\forja\` |

Reinicie o agente depois da cópia.

## Uso

Em ferramentas com comandos de skill:

```text
/forja analisar ./meu-projeto
/forja analisar ./meu-projeto --agents
/forja create-project agenda-cli --plano
/forja prompt "corrige o login"
```

Em outros agentes:

```text
Use a skill forja, comando /entender: como o pedido atravessa esta API?
```

### Analisar sem alterar

```text
/forja analisar ./meu-projeto
```

A análise lê os arquivos relevantes, segue fluxos representativos e classifica apenas os pilares aplicáveis como `Bom`, `Parcial`, `Problemático`, `Não aplicável` ou `Não avaliado`. Cada problema deve apontar uma evidência `arquivo:linha`. Nota numérica só aparece quando solicitada.

Para autorizar um arquivo de contexto na raiz:

```text
/forja analisar ./meu-projeto --agents
```

Em monorepo, `--agents=modules` também permite arquivos nos módulos que tenham regras locais. Sem essa opção, a Forja não cria arquivos aninhados.

### Entender o código

```text
/forja entender por que a função de cobrança recebe 15 argumentos
```

A Forja procura chamadores, instanciações e o fluxo dos dados. Em perguntas históricas, consulta `git log`, `git blame` e referências disponíveis a issues ou PRs. A resposta separa fatos, inferências e o que não pôde ser confirmado.

### Criar um projeto

```text
/forja create-project agenda-cli
```

A Forja escolhe a menor stack compatível com o pedido e o ambiente, cria apenas os arquivos necessários e executa a verificação documentada. Ela não inicializa Git, faz commit, publica ou implanta sem pedido explícito.

`--plano` mostra o plano e espera aprovação antes de criar arquivos. Mesmo sem a opção, uma decisão sobre arquitetura, dados, autenticação, pagamento, multi-tenant ou dependência relevante exige confirmação.

### Melhorar um prompt

```text
/forja prompt "faz um login pro meu site"
```

O resultado preserva a intenção, consulta o projeto quando disponível e deixa lacunas como `[PREENCHER: ...]`. Um plano com aprovação só entra quando existe decisão arquitetural, risco, ambiguidade relevante ou expansão de escopo.

### Revisar prosa

```text
/forja humanizar README.md
```

A Forja altera somente a prosa do arquivo indicado. Código, dados, frontmatter, links, fatos e voz legítima do autor são preservados. A resposta padrão traz o texto final e até três mudanças úteis.

Use `--diagnostico` para receber sinais encontrados, crítica e a avaliação heurística nas dimensões direto, ritmo, confiança, autenticidade e densidade.

### Reduzir complexidade

```text
/forja ponytail full adicionar cache para as respostas da API
```

- `lite`: executa o pedido e aponta uma alternativa menor quando relevante.
- `full`: escolhe a menor solução completa.
- `ultra`: questiona requisitos dispensáveis e prefere remover antes de adicionar.

Nenhum nível corta segurança, validação, acessibilidade, tratamento de erro que protege dados ou requisito confirmado pelo usuário.

## Princípios

- Ler o fluxo real antes de mudar código.
- Reutilizar o projeto, a stdlib, a plataforma e as dependências instaladas antes de criar algo.
- Corrigir a causa compartilhada de um bug quando ela existir.
- Não criar abstrações ou opções para usos hipotéticos.
- Verificar pelo mecanismo real do projeto.
- Continuar enquanto houver progresso; parar e reportar quando a mesma falha se repetir sem uma hipótese nova.
- Pedir aprovação por impacto e risco, não pela quantidade de arquivos.
- Não transformar análise em autorização para corrigir, versionar ou publicar.

## Estrutura

```text
forja/
├── SKILL.md
├── README.md
├── LICENSE
└── references/
    ├── analisar.md
    ├── entender.md
    ├── create-project.md
    ├── prompt.md
    ├── humanizar.md
    ├── ponytail.md
    ├── boas-praticas.md
    ├── agents-template.md
    ├── stacks-minimos.md
    ├── prompt-guide.md
    └── escrita-humana.md
```

O `SKILL.md` contém apenas descoberta, roteamento, permissões e regras compartilhadas. Cada comando carrega sua referência e os guias de que realmente precisa.

## Limitações

- A análise depende dos arquivos acessíveis e não substitui auditoria formal, teste de carga ou observação de produção.
- Projetos grandes podem ser amostrados; a resposta deve declarar o recorte.
- O `AGENTS.md` gerado precisa de revisão do time antes de virar fonte de verdade.
- `/create-project` cobre projetos pequenos e médios; decisões de escala, compliance e operação exigem contexto humano.
- `/humanizar` melhora a leitura, mas não promete enganar detectores nem esconder autoria.

## Créditos

- [ponytail](https://github.com/DietrichGebert/ponytail), MIT: simplicidade deliberada e atalhos com limite explícito.
- [humanizer](https://github.com/blader/humanizer), MIT: sinais recorrentes de prosa gerada por IA.
- [stop-slop](https://github.com/hardikpandya/stop-slop), MIT: revisão de ritmo e preenchimento verbal.
- Palestra de Boris, da Anthropic: contexto, planejamento proporcional e verificação em prompts para agentes.

A Forja não é afiliada aos projetos ou organizações citados.

## Licença

MIT. Veja `LICENSE`.
