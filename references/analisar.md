# `/analisar [caminho]`

Diagnostique o projeto sem alterar arquivos. A escrita de `AGENTS.md` exige `--agents`.

## Opções

- `--rapido`: contexto, até cinco problemas prioritários e, se autorizado, `AGENTS.md`; não percorra todos os pilares.
- `--agents` ou `--agents=root`: permite criar ou atualizar apenas o `AGENTS.md` da raiz.
- `--agents=modules`: permite também `AGENTS.md` nos módulos que tenham regras próprias. Não crie arquivos aninhados sem essa opção.

## Processo

1. Leia README, manifestos, scripts, configurações, `.env.example`, `.gitignore`, testes e CI. Nunca leia `.env` real sem necessidade explícita.
2. Localize os pontos de entrada e siga de três a cinco fluxos representativos. Em projeto grande, priorize módulos críticos e informe a amostra.
3. Obtenha comandos de instalar, executar, testar, lint e build dos arquivos do projeto, não da memória.
4. Avalie apenas os pilares aplicáveis de `boas-praticas.md`. Use `Bom`, `Parcial`, `Problemático`, `Não aplicável` ou `Não avaliado`.
5. Para cada problema, informe evidência `arquivo:linha`, impacto, severidade e correção recomendada. Marque deduções com `(inferido)`.
6. Separe diagnóstico, recomendação e implementação. Não corrija o código durante a análise.

## Severidade

- **Crítico:** impede execução, expõe segredo ou dado, ou pode causar perda de dados.
- **Alto:** bug provável, falha relevante de segurança ou bloqueio recorrente de evolução.
- **Médio:** prejudica manutenção, legibilidade ou teste sem quebrar o uso atual.
- **Baixo:** consistência ou conveniência com impacto limitado.

## `AGENTS.md`

Com `--agents`, use `agents-template.md` e registre apenas fatos específicos do projeto: comandos, mapa, invariantes, convenções não óbvias e armadilhas.

- Se já existir, preserve regras válidas e faça a menor atualização necessária.
- Se houver conflito de intenção, mostre o conflito e peça decisão antes de sobrescrever.
- Não copie políticas genéricas de engenharia para o arquivo.

## Resposta

Comece pelos problemas prioritários. Liste escopo lido e não lido, evidências, ações recomendadas e arquivos criados ou alterados. Não dê nota numérica, salvo pedido explícito. Se pedirem nota, calcule somente sobre pilares aplicáveis e explique o método.

