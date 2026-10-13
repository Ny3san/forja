# `/create-project <nome>`

Crie um projeto pequeno ou médio dentro de uma pasta nova. Não altere uma pasta existente e não inicialize Git, faça commit, publique ou implante sem pedido explícito.

## Antes de criar

- O destino é `./<nome>`, a partir do diretório de trabalho, salvo se o usuário informar outro caminho. Se o nome estiver vazio ou tiver `/`, `\` ou `..`, peça outro.
- Se o destino existir e não estiver vazio, pare e peça outro caminho ou uma autorização específica.
- Extraia do pedido: objetivo, tipo de projeto, restrições e critério de pronto.
- Use `stacks-minimos.md` para escolher a menor stack compatível com os requisitos e com o ambiente. Confirme que o runtime existe (por exemplo, `python3 --version`). Se não existir, diga isso e proponha a stack disponível; não instale runtimes sem autorização.
- Pergunte antes quando faltar uma decisão que altere arquitetura, dados, autenticação, pagamento, multi-tenant ou dependências de produção.
- Com `--plano`, mostre o plano e espere aprovação. Sem a opção, siga depois de comunicar as escolhas relevantes.

## Criar

Inclua somente o necessário para instalar, executar e verificar:

- código de entrada e módulos exigidos pelo objetivo;
- `README.md` curto com comandos confirmados e a versão do runtime em que a validação rodou. Não declare uma faixa de versões que você não testou;
- `.gitignore` e `.editorconfig` adequados;
- `.env.example` apenas quando houver configuração externa;
- `AGENTS.md` curto com fatos do projeto;
- uma verificação executável para lógica não trivial.

Não adicione CI, Docker, banco, autenticação, framework ou biblioteca sem requisito concreto.

## Validar

Instalar dependências executa código de terceiros. Declare os pacotes antes de instalar, instale dentro do projeto (ambiente virtual ou `node_modules`) e não use instalação global.

Execute os comandos documentados de instalação, teste ou verificação, o build quando existir e uma execução mínima. Siga a regra de verificação do `SKILL.md`: cada nova tentativa precisa de uma hipótese nova, e três tentativas sem sucesso encerram o trabalho com um relatório.

## Relatório

```text
Stack: <linguagem e versões observadas>
Rodar: <comando>
Testar: <comando>
Arquivos criados: <lista>
Validado: <comandos executados e resultado>
Não validado: <o que ficou de fora e por quê>
Omitido de propósito: <item> (adicionar quando <gatilho>)
```
