# Modelo de AGENTS.md

Copie o bloco abaixo para `AGENTS.md` na raiz do projeto. Preencha **somente** com o que foi observado (em `/analisar`) ou escolhido (em `/create-project`).

## Como usar o modelo

- **Mantenha curto**, até cerca de 150 linhas. O arquivo entra no contexto do agente em toda sessão. Escreva só o que o agente não descobre lendo o código.
- **Remova seções que não se aplicam.** Um script pequeno precisa de 4 ou 5 delas.
- **Fato ou dedução.** Fato vem de um arquivo lido. Dedução leva `(inferido)`. Campo sem informação: "Não identificado, confirmar com o time".
- **Monorepo ou módulos grandes.** Crie um `AGENTS.md` menor dentro de cada pasta com as regras daquele módulo. A raiz fica com o que vale para todos.
- **Preferências pessoais** ficam num arquivo local (`AGENTS.local.md`), fora do Git.
- **Claude Code.** Crie um `CLAUDE.md` com uma linha, `@AGENTS.md`, para ele ler o mesmo arquivo.
- **Informação permanente que apareceu num prompt** (comando, convenção, decisão) pertence aqui. Se o usuário repete a mesma instrução, mova para cá.

---

```markdown
# AGENTS.md: diretrizes para agentes de IA

> Leia este arquivo inteiro antes de criar, alterar ou remover código.
> Gerado por [/analisar | /create-project] em [data]. Revise antes de tratar como fonte de verdade.

## 0. Como trabalhar
- Escreva o menor código que funciona. Reutilize antes de criar.
- Ordem: precisa existir? Já existe no projeto? Stdlib? Recurso nativo? Dependência instalada? Uma linha? Código mínimo.
- Sem abstração sem segundo uso real. Sem código "para o futuro".
- Atalho com teto conhecido leva `ponytail: <teto> e <caminho de melhoria>`.
- Entenda antes de mudar: leia os arquivos que a mudança toca.
- Mudança em vários arquivos, dependências ou configs: mostre um plano curto e espere aprovação.
- Verifique o trabalho com os comandos da seção 2. Itere até passar. Se não passar, reporte.
- Não simplifique validação de entrada, tratamento de erro que protege dados, segurança ou acessibilidade básica.

## 1. Contexto
- **Tipo:** [site | CLI | API | app web | biblioteca | script | monorepo]
- **Objetivo:** [uma frase]
- **Público:** [quem usa]
- **Stack:** [linguagem, framework, versões]
- **Banco e integrações:** [lista ou "Nenhum"]

## 2. Comandos oficiais
- Instalar: `[comando]`
- Executar: `[comando]`
- Testar: `[comando]`
- Lint e formatação: `[comando]`
- Build: `[comando]`

Use só estes. Não invente scripts.

## 3. Arquitetura
- **Camadas:** [ex.: interface, regras, dados | "arquivo único"]
- **Regra de dependência:** [ex.: interface não acessa dados diretamente]
- **Fluxo principal:** [entrada, processamento, saída, em poucas linhas]

## 4. Estrutura e onde colocar código novo
[árvore resumida com a função de cada pasta]

- Novo componente ou tela: `[caminho]`
- Nova regra de negócio: `[caminho]`
- Nova chamada externa: `[caminho]`
- Novo teste: `[caminho]`

## 5. Convenções
- **Arquivos:** [padrão observado]
- **Funções e variáveis:** [padrão observado]
- **Formatação:** [do .editorconfig e do formatador]
- **Imports e tipagem:** [alias, regras de tipos]

## 6. Estado e dados
- **Global:** [ferramenta ou "não usado"]
- **Local:** [quando usar]
- **Contratos e tipos:** [onde ficam]

## 7. Interface (se houver)
- Reutilize os componentes de `[caminho]` antes de criar outro.
- Toda tela assíncrona tem carregando, erro, vazio e sucesso.
- Formulário valida e mostra o erro perto do campo.
- HTML semântico, label em todo campo, navegação por teclado.
- Responsividade: [abordagem usada].

## 8. Segurança
- Segredo nunca entra no código. Use variável de ambiente.
- Variável nova entra no `.env.example` no mesmo commit.
- Valide toda entrada externa no ponto de entrada.
- Não registre senha, token ou dado pessoal em log.
- Consulta parametrizada. Nada de concatenar entrada em SQL ou shell.

## 9. Testes
- Regra de negócio nova tem ao menos um teste que falha se a regra quebrar.
- Ferramenta: [ex.: pytest, vitest, nenhuma].
- Fluxos críticos: [quais, se identificados].
- Não crie suíte nova sem pedido, a menos que o projeto já tenha uma.

## 10. Git
- Commits: [padrão observado | "Não identificado"]. Título até 50 caracteres; o corpo explica o porquê.
- Uma unidade lógica por commit.
- Não versione `.env`, dependências instaladas, builds nem arquivos de IDE pessoais.

## 11. Documentação
- Atualize o README quando mudar o jeito de rodar ou testar.
- Decisões de arquitetura: [caminho ou "Não identificado"].
- Escreva prosa direta: sem emoji, sem frase de efeito, sem adjetivo de vendas.

## 12. Proibido
- Reescrever o projeto sem pedido explícito.
- Adicionar dependência sem registrar o motivo.
- Alterar CI, build, variáveis de ambiente ou scripts de publicação sem autorização.
- Remover teste ou verificação para fazer o build passar.
- Criar camada, abstração ou arquivo sem uso atual.

## 13. Pendências conhecidas
| Severidade | Problema | Local | Ação recomendada |
|---|---|---|---|
| Crítico | ... | ... | ... |

> Não corrija estes itens por conta própria. Cada correção deve ser pedida.
> Em projeto criado com /create-project: "Nenhuma pendência na criação" e a lista do que foi pulado.
```
