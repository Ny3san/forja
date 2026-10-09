# Checklist dos 20 pilares

Use em `/analisar` para avaliar somente o que se aplica ao projeto. Em `/create-project`, consulte apenas os pilares ligados ao produto criado.

## Status

- **Bom:** a evidência observada atende ao contexto atual.
- **Parcial:** existe, mas deixa uma lacuna concreta.
- **Problemático:** há defeito, risco ou ausência necessária.
- **Não aplicável:** o pilar não pertence a este tipo de projeto.
- **Não avaliado:** faltou acesso ou evidência; informe o motivo.

Não dê nota numérica por padrão. Se o usuário pedir, pontue de 0 a 10 somente os pilares aplicáveis e avaliados, apresente a fórmula da média e mantenha riscos críticos fora da compensação matemática.

## Pilares

| # | Pilar | Evidência a procurar | Aplicabilidade |
|---|---|---|---|
| 1 | Objetivo e escopo | README, descrição do pacote, fluxos entregues | Todos |
| 2 | Arquitetura | Pontos de entrada, dependências, limites entre módulos | Projetos com mais de uma responsabilidade |
| 3 | Estrutura | Agrupamento, nomes, arquivos abandonados | Todos |
| 4 | Fluxos | Caminhos completos da entrada à saída | Todos |
| 5 | Modelagem e contratos | Tipos, schemas, formatos de API e dados | Quando há dados compartilhados ou externos |
| 6 | Ambiente de desenvolvimento | Comandos, editorconfig, formatador | Quando há colaboração ou tooling |
| 7 | Legibilidade | Nomes, coesão, complexidade localizada | Todos |
| 8 | Reuso | Duplicação real e componentes compartilhados | Quando há segundo uso concreto |
| 9 | Estado | Fonte de verdade e sincronização | Aplicações com estado mutável |
| 10 | UI e consistência visual | Componentes, tokens, padrões de interação | Interfaces visuais |
| 11 | Acessibilidade e responsividade | Semântica, labels, teclado, contraste, layouts | Interfaces para usuários |
| 12 | Estados e erros | Falhas possíveis, mensagens e recuperação | Operações que podem falhar ou esperar |
| 13 | Segurança e privacidade | Entradas, permissões, segredos e dados sensíveis | Conforme fronteiras e dados do sistema |
| 14 | Testes | Regras críticas e regressões cobertas | Quando há comportamento verificável |
| 15 | Desempenho e escala | Medições, consultas, volume e gargalos evidentes | Conforme carga e requisitos conhecidos |
| 16 | Git e colaboração | Ignore, histórico e fluxo do time | Repositórios colaborativos |
| 17 | Documentação | Instalação, execução, uso e decisões não óbvias | Conforme público e manutenção |
| 18 | Configuração e dependências | Lockfile, variáveis, dependências usadas | Quando existem dependências ou configuração externa |
| 19 | Entrega e observabilidade | CI, deploy, logs, métricas e recuperação | Software implantado ou operado |
| 20 | Manutenção | Acoplamento, pontos frágeis e dívida conhecida | Todos |

## Como registrar um problema

Para cada achado, informe:

1. pilar e status;
2. evidência em `arquivo:linha`. Para a ausência de algo (por exemplo, sem testes), a evidência é a busca feita: onde procurou e o que não achou;
3. impacto observável;
4. severidade;
5. menor correção suficiente.

O formato de um problema está em `analisar.md`.

Não marque como problema a ausência de uma prática que o projeto não precisa. Não recomende framework, camada, teste, documento ou pipeline apenas para preencher o checklist.
