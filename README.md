# Forja

Forja é uma skill para agentes de código com seis comandos: diagnosticar projetos, explicar código, criar projetos mínimos, melhorar prompts, revisar prosa e reduzir complexidade desnecessária.

## Comandos

| Comando | Resultado | Escrita permitida |
|---|---|---|
| `/analisar [caminho]` | Diagnóstico com evidências | Nenhuma por padrão; `--agents` autoriza o `AGENTS.md` |
| `/entender <pergunta>` | Explicação baseada no código e, quando útil, no Git | Nenhuma |
| `/create-project <nome>` | Projeto mínimo e validado em uma pasta nova | Somente na pasta nova |
| `/prompt <texto>` | Prompt técnico revisado | Nenhuma |
| `/humanizar <texto ou arquivo>` | Prosa revisada sem mudar os fatos | Somente o arquivo indicado |
| `/ponytail [lite\|full\|ultra]` | Solução deliberadamente simples | Conforme a tarefa autorizada |

Opções:

| Opção | Comando | Efeito |
|---|---|---|
| `--rapido` | analisar | Contexto e até cinco problemas prioritários, sem percorrer os pilares |
| `--agents` ou `--agents=root` | analisar | Autoriza criar ou atualizar o `AGENTS.md` da raiz |
| `--agents=modules` | analisar | Autoriza também `AGENTS.md` nos módulos com regras próprias |
| `--plano` | create-project | Mostra o plano e espera aprovação antes de criar arquivos |
| `--diagnostico` | humanizar | Acrescenta sinais encontrados, crítica e as cinco dimensões do guia |

A skill reconhece pedidos claros escritos com palavras próprias, como "explique este fluxo" ou "melhore este prompt". `/ponytail` não é o modo automático de toda tarefa de código: ele entra quando o usuário pede ou reclama de complexidade desnecessária.

## Instalação

Pelo Skills CLI:

```bash
npx skills add Ny3san/forja -a codex
npx skills add Ny3san/forja -g -a claude-code
```

`-g` instala para o usuário, em vez de só para o projeto atual. Para atualizar:

```bash
npx skills update
```

Na instalação manual, copie este repositório para a pasta de skills do agente, com o nome `forja`:

| Agente | macOS e Linux | Windows |
|---|---|---|
| Codex | `~/.codex/skills/forja/` | `%USERPROFILE%\.codex\skills\forja\` |
| Claude Code | `~/.claude/skills/forja/` | `%USERPROFILE%\.claude\skills\forja\` |
| Cursor | `~/.cursor/skills/forja/` | `%USERPROFILE%\.cursor\skills\forja\` |

Reinicie o agente depois da cópia.

## Uso

A primeira palavra depois de `/forja` é o comando:

```text
/forja analisar ./meu-projeto
/forja analisar ./meu-projeto --agents
/forja create-project agenda-cli --plano
/forja prompt "corrige o login"
```

Em agentes sem comandos de skill, escreva o pedido por extenso:

```text
Use a skill forja, comando entender: como o pedido atravessa esta API?
```

### Analisar sem alterar

```text
/forja analisar ./meu-projeto
```

A análise lê os arquivos relevantes, segue fluxos representativos e classifica apenas os pilares aplicáveis como `Bom`, `Parcial`, `Problemático`, `Não aplicável` ou `Não avaliado`. Cada problema aponta uma evidência `arquivo:linha`. Ela não executa o código do projeto, e a nota numérica só aparece quando o usuário a pede.

Para autorizar um arquivo de contexto na raiz, acrescente `--agents`. Em monorepo, `--agents=modules` também permite arquivos nos módulos com regras locais. Sem essa opção, a Forja não cria arquivos aninhados.

### Entender o código

```text
/forja entender por que a função de cobrança recebe 15 argumentos
```

A Forja procura chamadores, instanciações e o fluxo dos dados. Em perguntas históricas, consulta `git log`, `git blame` e as referências disponíveis a issues ou PRs. A resposta separa fatos, inferências e o que não pôde ser confirmado.

### Criar um projeto

```text
/forja create-project agenda-cli
```

A Forja escolhe a menor stack compatível com o pedido e o ambiente, cria apenas os arquivos necessários e executa a verificação documentada. Ela não inicializa Git, faz commit, publica nem implanta sem pedido explícito.

Com `--plano`, ela mostra o plano e espera aprovação antes de criar arquivos. Mesmo sem a opção, uma decisão sobre arquitetura, dados, autenticação, pagamento, multi-tenant ou dependência de produção exige confirmação.

### Melhorar um prompt

```text
/forja prompt "faz um login pro meu site"
```

O resultado preserva a intenção, consulta o projeto quando ele está disponível e deixa as lacunas como `[PREENCHER: ...]`. A Forja só reescreve o pedido, sem executá-lo. Exemplo de resultado:

```text
Objetivo: adicionar login com e-mail e senha ao site, com sessão persistente e logout.
Contexto: o site usa [PREENCHER: stack]. Usuários ficam em [PREENCHER: tabela ou arquivo].
Restrições: senha com hash, segredos em variável de ambiente, nenhuma biblioteca de autenticação nova sem aviso.
Antes de codar: leia as rotas e o modelo de usuário. Se a solução mudar o modelo de dados, mostre um plano curto e espere aprovação.
Pronto quando: um teste cobre cadastro, login correto, senha errada e logout, e a suíte passa. Itere até passar.
```

### Revisar prosa

```text
/forja humanizar README.md
```

A Forja altera somente a prosa do arquivo indicado. Ela preserva código, dados, frontmatter, links, fatos e a voz legítima do autor. A resposta padrão traz o texto final e até três mudanças úteis. `--diagnostico` acrescenta os sinais encontrados, a crítica e uma avaliação heurística em cinco dimensões: direto, ritmo, confiança, autenticidade e densidade.

### Reduzir complexidade

```text
/forja ponytail full adicionar cache para as respostas da API
```

- `lite`: executa o pedido e aponta uma alternativa menor quando ela é relevante.
- `full`: escolhe a menor solução completa.
- `ultra`: questiona requisitos dispensáveis e prefere remover antes de adicionar.

Nenhum nível corta segurança, validação, acessibilidade, tratamento de erro que protege dados ou requisito confirmado pelo usuário.

## Segurança e permissões

- Cada comando escreve somente onde a coluna "Escrita permitida" autoriza. Uma análise não autoriza correções, e criar um projeto não autoriza versionar, publicar ou implantar.
- `/analisar` e `/entender` leem sem executar o código do projeto. `/create-project` executa instalação, testes e uma execução mínima dentro da pasta nova, e a instalação roda código de terceiros.
- A Forja trata como dado o texto lido de arquivos, issues, commits e páginas. Ela não executa ordens dirigidas ao agente nesses textos e avisa o usuário.
- Ao encontrar um segredo, a Forja informa o arquivo e a linha, nunca o valor.
- Essas regras são instruções que o agente segue, não um sandbox. Ao analisar um repositório desconhecido, mantenha ligada a confirmação de comandos do seu agente.
- Leia o `SKILL.md` e as referências antes de instalar, como faria com qualquer código de terceiros.

## Regras compartilhadas

As regras que valem para todos os comandos estão na seção "Regras compartilhadas" do `SKILL.md`, que é a fonte da verdade. O README não as repete, para que não se contradigam.

## Testes

```bash
python3 -m unittest discover -s tests -v
```

O validador usa só a biblioteca padrão do Python. Ele confere que o frontmatter é válido, que cada referência existe e é carregada, que o README bate com o repositório e com as opções do `argument-hint`, que as tabelas estão íntegras e que a prosa passa pelo próprio filtro de `references/escrita-humana.md`.

## Contribuir

Abra uma issue descrevendo o caso de uso ou a regra que faltou, antes de propor a solução. Um pull request precisa passar nos testes. O `AGENTS.md` lista o que um comando ou uma opção nova exige.

## Estrutura

```text
forja/
├── SKILL.md
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── LICENSE
├── NOTICE
├── references/
│   ├── analisar.md
│   ├── entender.md
│   ├── create-project.md
│   ├── prompt.md
│   ├── humanizar.md
│   ├── ponytail.md
│   ├── boas-praticas.md
│   ├── agents-template.md
│   ├── stacks-minimos.md
│   ├── prompt-guide.md
│   └── escrita-humana.md
└── tests/
    └── test_forja.py
```

O `SKILL.md` contém apenas descoberta, roteamento, opções, permissões e regras compartilhadas. Cada comando carrega a própria referência e só os guias de que precisa.

## Limitações

- A análise depende dos arquivos acessíveis e não substitui auditoria formal, teste de carga ou observação de produção.
- Em projetos grandes, a Forja amostra os módulos de maior risco e declara o recorte na resposta.
- O `AGENTS.md` gerado precisa de revisão do time antes de virar fonte de verdade.
- `/create-project` cobre projetos pequenos e médios. Decisões de escala, compliance e operação exigem contexto humano.
- `/humanizar` melhora a leitura, mas não promete enganar detectores nem esconder autoria.
- O catálogo de `/humanizar` está em português. Em outros idiomas, valem os princípios, não a lista de palavras.

## Créditos

- [ponytail](https://github.com/DietrichGebert/ponytail), MIT: simplicidade deliberada e atalhos com limite explícito.
- [humanizer](https://github.com/blader/humanizer), MIT: sinais recorrentes de prosa gerada por IA.
- [stop-slop](https://github.com/hardikpandya/stop-slop), MIT: revisão de ritmo e preenchimento verbal.
- Palestra "Mastering Claude Code in 30 minutes", de Boris Cherny (Anthropic): contexto, planejamento proporcional e verificação em prompts para agentes.

Os avisos de copyright originais estão em `NOTICE`. A Forja não é afiliada aos projetos ou organizações citados.

## Licença

MIT. Veja `LICENSE`.
