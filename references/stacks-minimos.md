# Stacks mínimas para /create-project

Escolha a menor stack que atende ao objetivo. A ordem abaixo vai do mais enxuto ao mais pesado. Só suba um degrau se o requisito exigir.

## Regra de escolha
1. Dá para resolver com HTML, CSS e JS puros? Site estático.
2. Dá para resolver com um script na stdlib da linguagem? Script ou CLI.
3. Precisa receber requisições HTTP? API com a stdlib ou um micro-framework.
4. Precisa de interface reativa com muitos estados? Framework de frontend (React ou Vue com Vite).
5. Precisa de persistência com consultas? Banco pequeno (SQLite) antes de servidor de banco.

Se a escolha mudar a arquitetura de forma relevante (login de usuários, pagamento, multi-tenant), pergunte antes.

---

## A. Site estático
Arquivos: `index.html`, `styles.css`, `main.js` (só se houver comportamento), `README.md`, `AGENTS.md`, `.gitignore`, `.editorconfig`.
- HTML semântico, `<label>` em todo campo, `<button>` para ações.
- CSS com variáveis para cor e espaçamento. Mobile first com `min-width` nas media queries.
- Sem framework, sem bundler, sem dependência.
- Validação: abrir no navegador e conferir o console sem erros. Se houver lint de HTML, rodar.
- Como rodar: `python -m http.server 8000` ou abrir o arquivo.

## B. Script ou CLI (Python)
Arquivos: `main.py` (ou `<nome>.py`), `test_<nome>.py` se houver lógica, `README.md`, `AGENTS.md`, `.gitignore`, `.editorconfig`.
- Use `argparse` para argumentos. Sem Click ou Typer se o uso for simples.
- Separe a lógica em funções puras e o `if __name__ == "__main__":` como ponto de entrada.
- Verificação: `python -m pytest` se pytest estiver instalado; senão `python test_<nome>.py` com `assert`s e `unittest`, que é da stdlib.
- Dependências: nenhuma se possível. Se houver, `requirements.txt` com versões fixadas.
- Como rodar: `python main.py --help`.

## B2. Script ou CLI (Node)
Arquivos: `index.js`, `package.json` (com `"type": "module"` e script `start`), `README.md`, `AGENTS.md`, `.gitignore`, `.editorconfig`.
- Node tem `node:test` e `node:util` (parseArgs) na própria plataforma.
- Verificação: `node --test` com um arquivo `*.test.js`.
- Como rodar: `node index.js --help`.

## C. API HTTP
Arquivos: `app.py` ou `server.js`, `test_api.py` ou `*.test.js`, `README.md`, `AGENTS.md`, `.env.example`, `.gitignore`, `.editorconfig`.
- Com a stdlib: `http.server` (Python) ou `node:http`. Serve para protótipo e ferramenta interna.
- Com micro-framework: Flask (Python) ou Express (Node) quando houver roteamento e middleware reais.
- Validação de entrada em cada rota, no início. Resposta de erro sempre em JSON com status correto.
- Verificação: um teste que chama a rota principal e confere status e corpo.
- Como rodar: comando documentado no README; a porta vem de variável de ambiente com valor padrão.

## D. Frontend com framework
Arquivos mínimos: gerado pelo `npm create vite@latest` (template escolhido), depois apagar o que não é usado (logos, CSS de exemplo, componentes de demonstração).
- Um componente por arquivo, em `src/components/`. Estado local primeiro; global só se compartilhado.
- Cada chamada assíncrona com loading, erro e vazio.
- Verificação: `npm run build` e `npm run lint` (se configurado) e `npm test` com Vitest se houver lógica.
- Não adicione biblioteca de UI, roteamento ou estado global sem necessidade concreta. Registre no `AGENTS.md` o motivo de cada uma.

## E. Persistência simples
- SQLite pela stdlib do Python (`sqlite3`) ou `node:sqlite` quando disponível. Sem ORM para poucas tabelas.
- Schema em um arquivo `schema.sql` versionado.
- Consulta sempre parametrizada.

---

## Checklist comum a todas as stacks
- [ ] `README.md` com instalar, rodar e testar.
- [ ] `AGENTS.md` preenchido.
- [ ] `.gitignore` adequado (dependências, builds, `.env`, caches da linguagem).
- [ ] `.editorconfig` com indentação e fim de linha.
- [ ] `.env.example` se houver configuração externa.
- [ ] Uma verificação executável para lógica não trivial.
- [ ] Os comandos do README foram executados e funcionaram.
