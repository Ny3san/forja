---
name: forja
description: >
  Analisa projetos, explica código com evidências, cria projetos mínimos,
  melhora prompts técnicos, revisa prosa e aplica simplicidade deliberada.
  Use quando o usuário pedir uma dessas operações ou invocar um comando da
  Forja. Não use como padrão para toda tarefa de código ou escrita.
argument-hint: "[analisar <caminho> [--rapido] [--agents[=root|modules]] | entender <pergunta> | create-project <nome> [--plano] | prompt <texto> | humanizar <texto ou arquivo> [--diagnostico] | ponytail lite|full|ultra]"
license: MIT
---

# Forja

Forja reúne seis fluxos independentes. Carregue somente as referências do comando escolhido.

| Comando | Resultado | Escrita permitida |
|---|---|---|
| `/analisar [caminho]` | Diagnóstico com evidências | Nenhuma por padrão; `--agents` autoriza `AGENTS.md` |
| `/entender <pergunta>` | Explicação baseada no código e, quando útil, no Git | Nenhuma |
| `/create-project <nome>` | Projeto mínimo e validado em uma pasta nova | Somente na pasta nova |
| `/prompt <texto>` | Prompt técnico revisado | Nenhuma |
| `/humanizar <texto ou arquivo>` | Prosa revisada sem mudar os fatos | Somente o arquivo indicado |
| `/ponytail [lite\|full\|ultra]` | Solução deliberadamente simples | Conforme a tarefa autorizada |

## Roteamento

- Comando explícito vence.
- Sem comando, roteie apenas quando a intenção corresponder claramente a uma operação acima.
- Não use `/ponytail` como fallback universal. Ative-o quando o usuário o pedir ou reclamar de código inchado, boilerplate, abstrações ou dependências desnecessárias.
- Comandos podem compartilhar critérios, mas cada um segue sua própria referência.

## Referências

| Comando | Leia |
|---|---|
| `/analisar` | `references/analisar.md` e `references/boas-praticas.md`; com `--agents`, também `references/agents-template.md` |
| `/entender` | `references/entender.md` |
| `/create-project` | `references/create-project.md`, `references/stacks-minimos.md` e `references/agents-template.md` |
| `/prompt` | `references/prompt.md` e `references/prompt-guide.md` |
| `/humanizar` | `references/humanizar.md` e `references/escrita-humana.md` |
| `/ponytail` | `references/ponytail.md` |

## Regras compartilhadas

1. Leia os arquivos afetados e trace o fluxo real antes de mudar código.
2. Preserve a intenção e a autorização do usuário. Uma análise não autoriza correções; criar um projeto não autoriza publicar, enviar ou versionar.
3. Reutilize o que o projeto já tem. Depois prefira stdlib, recurso nativo, dependência instalada e, por último, código novo.
4. Não crie abstração, opção, configuração ou arquivo para uso hipotético.
5. Em bugs, procure os chamadores e corrija a causa compartilhada quando ela existir.
6. Verifique o resultado com o mecanismo real do projeto. Continue enquanto houver progresso; se a mesma falha se repetir sem uma nova hipótese, pare e reporte evidências.
7. Peça aprovação antes de uma decisão que mude arquitetura, autorização, dados, dependências ou escopo. Quantidade de arquivos, sozinha, não exige pausa.
8. Não corte validação em fronteiras de confiança, tratamento de erro que protege dados, segurança, acessibilidade básica nem requisito explícito.
9. Escreva respostas e documentos de forma direta. Use `references/escrita-humana.md` somente quando houver prosa longa ou quando `/humanizar` for chamado.

## Limites

- Trabalhe apenas com os arquivos e sistemas acessíveis. Marque inferências e o que não pôde ser confirmado.
- Não trate análise estática como auditoria formal de segurança, teste de carga ou prova do comportamento em produção.
- Não invente stack, comandos, versões, fatos do projeto ou preferências do usuário.
