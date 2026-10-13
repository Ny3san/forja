# `/analisar [caminho]`

Diagnostique o projeto sem alterar arquivos. A escrita de `AGENTS.md` exige `--agents`.

## Escopo e segurança

- Sem `caminho`, use o diretório de trabalho. Se o caminho não existir ou não tiver sinais de projeto (manifesto, código-fonte, documentação), diga isso e pare.
- Leia, não execute. Não rode o código, os testes nem os scripts do projeto, a menos que o usuário peça. Nesse caso, rode só os comandos que o próprio projeto declara e informe o resultado.
- Não leia um `.env` real sem pedido explícito. Ao encontrar um segredo, registre o arquivo e a linha, nunca o valor.

## Opções

- `--rapido`: contexto, até cinco problemas prioritários e, se autorizado, `AGENTS.md`. Não percorra todos os pilares.
- `--agents` ou `--agents=root`: permite criar ou atualizar apenas o `AGENTS.md` da raiz.
- `--agents=modules`: permite também `AGENTS.md` nos módulos que tenham regras próprias. Não crie arquivos aninhados sem essa opção.

## Processo

1. Leia README, manifestos, scripts, configurações, `.env.example`, `.gitignore`, testes e CI.
2. Localize os pontos de entrada e siga de três a cinco fluxos representativos. Em monorepo ou projeto com vários serviços, comece pelos módulos de maior risco e declare a amostra.
3. Obtenha os comandos de instalar, executar, testar, lint e build dos arquivos do projeto, não da memória.
4. Avalie apenas os pilares aplicáveis de `boas-praticas.md`. Use `Bom`, `Parcial`, `Problemático`, `Não aplicável` ou `Não avaliado`.
5. Registre cada problema com evidência `arquivo:linha`, impacto, severidade e correção recomendada. Marque deduções com `(inferido)`.
6. Separe diagnóstico, recomendação e implementação. Não corrija o código durante a análise.
7. Pergunte somente o que os arquivos não respondem e que muda o diagnóstico. Entregue o que já foi possível concluir junto com a pergunta.

## Severidade

- **Crítico:** impede a execução, expõe segredo ou dado, ou pode causar perda de dados.
- **Alto:** bug provável, falha relevante de segurança ou bloqueio recorrente de evolução.
- **Médio:** prejudica manutenção, legibilidade ou teste sem quebrar o uso atual.
- **Baixo:** consistência ou conveniência com impacto limitado.

## Formato de um problema

```text
[Alto] Senha comparada em texto puro (pilar 13, Segurança)
Evidência: src/login.py:27
Impacto: um vazamento do banco expõe todas as senhas.
Correção: gravar e comparar um hash, por exemplo com `hashlib.scrypt`.
```

## `AGENTS.md`

Com `--agents`, use `agents-template.md` e registre apenas fatos específicos do projeto: comandos, mapa, invariantes, convenções não óbvias e armadilhas.

- Se o arquivo já existir, preserve as regras válidas e faça a menor atualização necessária.
- Se houver conflito de intenção, mostre o conflito e peça decisão antes de sobrescrever.
- Não copie políticas genéricas de engenharia para o arquivo.
- O Claude Code lê `CLAUDE.md`, não `AGENTS.md`. Se o projeto usa o Claude Code, sugira um `CLAUDE.md` com a linha `@AGENTS.md` (sem crases dentro do arquivo) e crie-o somente se o usuário pedir.

## Resposta

```text
Resumo: <o que é o projeto e o estado geral, em duas frases>

Problemas prioritários
1. <problema no formato acima>

Pilares: <tabela com pilar, status e evidência; omitida com --rapido>

Escopo: lido <...>; amostrado <...>; não lido <...> (motivo)

Próximos passos: <o que fazer agora e o que pode esperar>
Arquivos criados ou alterados: <lista, ou "nenhum">
```

Não dê nota numérica, salvo pedido explícito. Se pedirem nota, calcule somente sobre os pilares aplicáveis e explique o método.
