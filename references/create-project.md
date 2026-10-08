# `/create-project <nome>`

Crie um projeto pequeno ou médio dentro de uma pasta nova. Não altere uma pasta existente e não inicialize Git, faça commit, publique ou implante sem pedido explícito.

## Antes de criar

- Se o destino existir e não estiver vazio, pare e peça outro caminho ou autorização específica.
- Extraia do pedido: objetivo, tipo de projeto, restrições e critério de pronto.
- Use `stacks-minimos.md` para escolher a menor stack compatível com os requisitos e com o ambiente disponível.
- Pergunte antes quando faltar uma decisão que altere arquitetura, dados, autenticação, pagamento, multi-tenant ou dependências relevantes.
- Com `--plano`, mostre o plano e espere aprovação. Sem a opção, siga após comunicar escolhas relevantes.

## Criar

Inclua somente o necessário para instalar, executar e verificar:

- código de entrada e módulos exigidos pelo objetivo;
- `README.md` curto com comandos confirmados;
- `.gitignore` e `.editorconfig` adequados;
- `.env.example` apenas quando houver configuração externa;
- `AGENTS.md` curto com fatos do projeto;
- uma verificação executável para lógica não trivial.

Não adicione CI, Docker, banco, autenticação, framework ou biblioteca sem requisito concreto.

## Validar

Execute os comandos documentados de instalação, teste ou verificação, build quando existir e uma execução mínima. Corrija enquanto houver uma hipótese nova e progresso observável. Se uma falha se repetir sem nova hipótese, pare e informe comando, saída relevante e o que não foi validado.

## Relatório

Informe stack e versões observadas, comandos para rodar e testar, arquivos criados, validações executadas e itens deliberadamente omitidos com o gatilho para adicioná-los.

