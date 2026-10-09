# Modelo de `AGENTS.md`

Use somente em `/create-project` ou em `/analisar --agents`. O arquivo deve conter fatos e decisões específicas que um agente não descobre com facilidade lendo o código.

O agente lê este arquivo em toda sessão. Mantenha-o em até cerca de 150 linhas: o excesso dilui as regras que importam.

Remova seções vazias. Não copie políticas genéricas de segurança, Git, testes ou estilo. Em monorepo, a raiz contém regras comuns; arquivos de módulo existem apenas com `--agents=modules` e registram diferenças locais.

```markdown
# AGENTS.md

> Revisado em [data]. Confirme informações marcadas como inferidas.

## Contexto
- Objetivo: [uma frase]
- Usuários: [quem usa]
- Stack e versões: [observadas nos manifestos]
- Integrações: [serviços e bancos relevantes]

## Comandos
- Instalar: `[comando confirmado]`
- Executar: `[comando confirmado]`
- Testar: `[comando confirmado]`
- Lint/formatar: `[comando confirmado]`
- Build: `[comando confirmado]`

Omita comandos inexistentes. Não invente scripts.

## Mapa do projeto
- `[caminho]`: [responsabilidade]
- `[caminho]`: [responsabilidade]

## Arquitetura e invariantes
- [limite entre módulos ou direção de dependência]
- [regra de domínio que não pode ser quebrada]
- [fluxo central resumido]

## Convenções locais
- [convenção não imposta automaticamente pelas ferramentas]
- [onde colocar cada tipo relevante de código ou teste]

## Verificação
- Antes de concluir: `[menor conjunto de comandos suficiente]`
- Fluxos críticos: [lista confirmada]

## Fronteiras externas
- [entrada que exige validação específica]
- [segredo, permissão ou dado sensível e como o projeto o trata]
- [serviço externo e comportamento de falha]

## Armadilhas conhecidas
- [limite, dívida ou comportamento surpreendente com caminho]
```

Se um dado não puder ser confirmado e ainda for útil, marque `(inferido)` e diga como confirmá-lo. Não use “Não identificado” para preencher campos dispensáveis; remova o campo.

O Claude Code lê `CLAUDE.md`, não `AGENTS.md`. Para ligar os dois, o `CLAUDE.md` pode conter apenas a linha `@AGENTS.md`, escrita sem crases dentro do arquivo: o Claude Code ignora imports dentro de crases.
