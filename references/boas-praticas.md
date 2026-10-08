# Boas práticas: checklist dos 20 pilares

Use este arquivo em `/analisar` (para avaliar cada pilar) e em `/create-project` (para não esquecer o básico). Cada pilar tem o que verificar e uma regra prática.

## Os 20 pilares

| # | Pilar | Verificar | Regra prática |
|---|---|---|---|
| 1 | Objetivo e escopo | README diz o que o projeto faz e para quem | Uma frase de objetivo no topo do README |
| 2 | Arquitetura | Camadas claras, dependências em uma direção, sem ciclos | Interface não acessa dados direto; regra de negócio não importa interface |
| 3 | Estrutura de pastas | Agrupamento lógico, nomes consistentes, sem lixo | Agrupe por domínio quando passar de 3 áreas; nada de `copia`, `old`, `teste2` |
| 4 | Fluxos do sistema | Caminho de uma ação, do início ao fim, é rastreável | Consegue apontar o arquivo de entrada e cada passo sem adivinhar |
| 5 | Modelagem e contratos | Tipos ou schemas definidos; contratos de API documentados ou tipados | Um lugar único para os tipos de dados compartilhados |
| 6 | Ambiente do VS Code | `.editorconfig`, formatação, extensões recomendadas | `.editorconfig` e formatador configurados são o mínimo |
| 7 | Legibilidade | Nomes claros, funções curtas, lint configurado | Função que não cabe na tela geralmente faz duas coisas |
| 8 | Componentização | Módulos reutilizáveis, sem lógica duplicada | Duplicou pela segunda vez? Extraia. Antes disso, não |
| 9 | Gerenciamento de estado | Estado local vs global definido; sem cópia duplicada | Estado vive onde é usado; global só quando compartilhado de verdade |
| 10 | UI, UX e design system | Componentes base, tokens de cor e espaçamento, consistência | Reutilize componentes existentes antes de criar um novo |
| 11 | Acessibilidade e responsividade | HTML semântico, labels, contraste, teclado, breakpoints | Botão é `<button>`, link é `<a>`; todo campo tem label |
| 12 | Estados e erros | Loading, erro, vazio e sucesso tratados; erro de API tratado | Nenhum `catch` silencioso; toda tela assíncrona tem os quatro estados |
| 13 | Segurança e privacidade | Sem segredos no código, validação de entrada, permissões | Entrada externa é suspeita até ser validada |
| 14 | Testes | Unitários para regra, integração para fluxo crítico | Ao menos um teste para a lógica não trivial |
| 15 | Desempenho e escalabilidade | Consultas eficientes, carregamento sob demanda, sem gargalo óbvio | Meça antes de otimizar; corrija o que é óbvio (consulta em loop, lista sem paginação) |
| 16 | Git e colaboração | `.gitignore`, convenção de commits, branches | Um commit por unidade lógica; título com até 50 caracteres |
| 17 | Documentação | README com setup e execução; decisões relevantes registradas | README responde: o que é, como roda, como testa |
| 18 | Configuração e dependências | `.env.example`, lockfile, dependências sem uso | Variável nova entra no `.env.example` no mesmo commit |
| 19 | CI/CD, deploy e observabilidade | Pipeline de lint, teste e build; logs úteis | CI roda os mesmos comandos que o desenvolvedor roda |
| 20 | Manutenção e evolução | Facilidade de adicionar funcionalidade; dívida identificada | Dívida conhecida vem marcada (`ponytail:` ou `TODO` com motivo) |

## Regras gerais de código

**Organização**
- Uma responsabilidade por função, uma por arquivo quando o arquivo cresce.
- Reutilize antes de criar: procure helpers existentes com busca no projeto.
- Nomes seguem o padrão já usado no projeto. Se não houver padrão, use o da linguagem.

**Erros**
- Não engula exceções. Trate, propague ou registre com contexto.
- Mensagens de erro dizem o que aconteceu e o que fazer, sem expor detalhes internos ao usuário final.

**Segurança**
- Segredos entram por variável de ambiente. Nunca no código, nunca em commit.
- Valide entrada externa no ponto de entrada (formulário, rota, parâmetro, arquivo).
- Não logue senhas, tokens, dados pessoais ou chaves.
- Use consulta parametrizada; nunca concatene entrada em SQL ou comando de shell.

**Interface**
- Toda tela com dados assíncronos tem: carregando, erro (com ação de tentar de novo), vazio (com orientação) e sucesso.
- Formulário valida e mostra o erro perto do campo, não só no topo.
- Funciona com teclado e leitor de tela. Contraste mínimo de 4.5:1 para texto normal.

**Testes**
- Lógica de negócio nova: ao menos um teste que falha se a regra quebrar.
- Teste deve ser rápido e não depender de rede ou de relógio real sem controle.

**Git**
- Título do commit: `tipo: descrição` em até 50 caracteres. Corpo explica o porquê.
- Não commite `.env`, `node_modules`, `dist`, `__pycache__`, arquivos de IDE pessoais.

**Dependências**
- Antes de adicionar: a stdlib resolve? Algo já instalado resolve? Se não, registre o motivo.
- Versões pinadas por lockfile. Remova dependência que não é importada.

**Simplicidade (ponytail)**
- Menos código, menos arquivos, menos camadas. Abstração só quando houver o segundo uso real.
- Simplificação com teto conhecido: comente com `ponytail:` dizendo o teto e o caminho de melhoria.

**Prosa e prompts**
- README, commit, comentário e relatório seguem `escrita-humana.md`: o ponto primeiro, sem enchimento, sem emoji decorativo.
- Instrução repetida em prompts (comando, convenção, decisão) vira linha no `AGENTS.md`.
- Tarefa grande para um agente começa por um plano e termina numa verificação executável (ver `prompt-guide.md`).
