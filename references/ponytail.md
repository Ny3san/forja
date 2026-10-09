# `/ponytail [lite|full|ultra]`

Aplique simplicidade deliberada somente à tarefa autorizada. O padrão é `full`.

## Escada

Pare no primeiro item que resolver por completo:

1. O requisito pode ser removido sem perder o resultado pedido?
2. O projeto já tem uma solução adequada?
3. A biblioteca padrão resolve?
4. A plataforma oferece um recurso nativo?
5. Uma dependência já instalada resolve?
6. Uma implementação direta e legível resolve?

Não troque segurança, validação, acessibilidade, tratamento de erro ou requisito explícito por menos linhas.

## Níveis

- `lite`: faça o pedido e cite uma alternativa menor quando ela for relevante.
- `full`: escolha a menor solução completa e explique apenas as decisões que afetam manutenção ou risco.
- `ultra`: questione requisitos dispensáveis e prefira remover antes de adicionar, sem descumprir o resultado confirmado pelo usuário.

Exemplo, para "adicione um cache às respostas da API":

- `lite`: o cache pedido, mais uma linha: "`functools.lru_cache` resolve isso sem classe própria, se você preferir."
- `full`: `@lru_cache(maxsize=1000)` na função de busca. Omitido: classe de cache própria.
- `ultra`: "Sem cache por enquanto: nada mostra que a busca é lenta. Quando mostrar, `@lru_cache` resolve."

Em correções, procure os chamadores antes de editar e resolva a causa comum. Lógica não trivial deixa uma verificação pequena, usando a infraestrutura existente ou a stdlib.

Marque um atalho conhecido somente quando o limite não estiver evidente no código:

```text
ponytail: <limite atual>; mudar para <alternativa> quando <gatilho observável>
```

Entregue primeiro o resultado. Termine com o que foi omitido e o risco restante, quando houver.
