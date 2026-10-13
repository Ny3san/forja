# AGENTS.md

> Revisado em 2026-10-08.

## Contexto
- Objetivo: skill para agentes de código com seis comandos (analisar, entender, create-project, prompt, humanizar, ponytail).
- Conteúdo: Markdown em português do Brasil. O único código é o validador em `dev/tests/`.
- Stack: Python 3 com a biblioteca padrão. Sem dependências.

## Comandos
- Testar: `python3 -m unittest discover -s dev/tests -t dev/tests -v`

## Mapa do projeto
- `SKILL.md`: descoberta, roteamento, opções, permissões e regras compartilhadas. É a fonte da verdade.
- `references/<comando>.md`: procedimento de cada comando.
- `references/boas-praticas.md`, `agents-template.md`, `stacks-minimos.md`, `prompt-guide.md`, `escrita-humana.md`: guias carregados sob demanda.
- `dev/tests/test_forja.py`: validador de coerência. Fica fora da skill de propósito: não é instrução para o agente.
- `.github/workflows/test.yml`: roda o validador a cada push e pull request.
- `NOTICE`: avisos de copyright dos projetos MIT que a Forja adapta. Todo projeto creditado no README precisa de um aviso aqui.
- `CLAUDE.md`: uma linha, `@AGENTS.md`, para o Claude Code ler este arquivo.

## Invariantes
- `SKILL.md` fica abaixo de 500 linhas. Detalhe de comando vai para `references/`.
- Comando novo exige uma linha na tabela de `SKILL.md`, `references/<comando>.md` e uma linha no README.
- Opção nova exige uma entrada no `argument-hint`, na tabela de opções, na referência que a implementa e no README.
- A coluna "Escrita permitida" é um limite de segurança. Mudá-la exige aprovação do mantenedor.
- A prosa de todos os arquivos segue `references/escrita-humana.md`. O validador confere vocabulário, travessão, emoji e advérbios.

## Convenções
- Sem emoji, sem travessão como conector, sem negrito decorativo.
- Exemplos são originais. Os fictícios dizem que são ilustração.
- Dentro de tabelas, escreva `\|` para uma barra vertical dentro de crases.

## Verificação
- Antes de concluir qualquer mudança, rode o comando de teste acima e confirme que não há falhas.

## Armadilhas
- `escrita-humana.md` cita as palavras vetadas, então o validador a isenta do filtro de vocabulário. Ao acrescentar uma palavra à linha "Palavras de IA", acrescente a raiz dela em `BANNED_STEMS`, em `dev/tests/test_forja.py`.
- O README lista a estrutura do repositório. Criar ou remover um arquivo visível exige atualizar a árvore.
