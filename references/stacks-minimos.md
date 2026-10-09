# Escolha de stack para `/create-project`

Escolha a menor stack que atenda ao requisito e funcione no ambiente disponível. Respeite a linguagem ou ferramenta escolhida pelo usuário; simplicidade não autoriza trocar a tecnologia pedida.

## Ordem de decisão

1. **Documento ou site estático:** HTML e CSS; JavaScript apenas para comportamento necessário.
2. **Automação, script ou CLI:** biblioteca padrão da linguagem escolhida.
3. **Serviço HTTP:** recurso nativo ou microframework já escolhido quando roteamento, middleware ou as bibliotecas disponíveis justificarem.
4. **Interface reativa:** framework somente quando o estado e as interações excederem uma página simples; use o scaffold oficial da ferramenta escolhida e remova demonstrações.
5. **Persistência:** arquivo local para dados simples; SQLite para relações e consultas locais; servidor de banco apenas quando concorrência, operação ou requisito externo exigirem.

Não mantenha um catálogo fechado de frameworks ou versões. Confirme a versão instalada ou declarada no ambiente e use o comando oficial da ferramenta escolhida.

## Estrutura mínima

Todo projeto precisa apenas de:

- ponto de entrada e código necessário ao objetivo;
- `README.md` com instalar, executar e verificar;
- `.gitignore` e `.editorconfig` adequados;
- `AGENTS.md` com comandos e decisões específicas;
- teste ou verificação pequena para lógica não trivial;
- `.env.example` quando houver configuração externa.

Adicione pastas ou módulos quando houver responsabilidades distintas, não por modelo arquitetural antecipado.

## Dependências

- Prefira stdlib e recursos nativos quando forem suficientes.
- Use uma dependência que o projeto já adota antes de introduzir outra.
- Registre o motivo de uma dependência nova.
- Use o mecanismo de lock ou faixa de versão normal da ferramenta escolhida; não invente uma política universal de fixação de versões.

## Verificação por tipo

- **Site:** abra em um navegador, confira console, teclado e tamanhos relevantes. Sem navegador disponível, valide o HTML com a ferramenta que houver e declare no relatório que a verificação visual não foi feita.
- **CLI ou script:** execute ajuda, caminho principal e verificação da lógica.
- **API:** teste ao menos a rota principal, entrada inválida e formato de erro.
- **Interface reativa:** rode build e confira os estados que podem ocorrer no fluxo implementado.
- **Persistência:** valide criação, leitura e erro relevante com dados temporários.

Autenticação, pagamento, multi-tenant, processamento assíncrono e infraestrutura de produção exigem decisão do usuário antes da criação.
