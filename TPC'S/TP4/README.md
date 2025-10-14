# TPC4 - Analisador Léxico para Linguagem de Query
Realizado por Gonçalo Soares a108393

## Descrição do Trabalho

Este trabalho consiste na implementação de um **analisador léxico** (lexer) para uma linguagem de query.

### Exemplo de Query Suportada

# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000

---

## Objetivos

- Implementar um analisador léxico capaz de reconhecer todos os tokens da linguagem
- Classificar cada token identificado (tipo, valor, linha, posição)
- Tratar comentários, strings com tags de idioma, e símbolos especiais
- Ignorar whitespace mantendo controlo de linhas

---

## Implementação

### Tokens Reconhecidos

O analisador identifica os seguintes tipos de tokens:

| Token | Descrição | Exemplo |
|-------|-----------|---------|
| `COMMENT` | Comentários (começam com `#`) | `# DBPedia: obras` |
| `SELECT` | Palavra-chave select | `select` |
| `WHERE` | Palavra-chave where | `where` |
| `LIMIT` | Palavra-chave LIMIT | `LIMIT` |
| `VARIABLE` | Variáveis (começam com `?`) | `?nome`, `?desc` |
| `PREFIX` | Prefixos com namespace | `dbo:MusicalArtist`, `foaf:name` |
| `STRING` | Strings entre aspas | `"Chuck Berry"` |
| `IDIOMA` | Tag de idioma | `@en`, `@pt` |
| `A` | Palavra especial 'a' | `a` |
| `LBRACE` | Chaveta esquerda | `{` |
| `RBRACE` | Chaveta direita | `}` |
| `DOT` | Ponto | `.` |
| `NUMBER` | Números inteiros | `1000` |
| `NEWLINE` | Quebra de linha | `\n` |
| `WHITESPACE` | Espaços, tabs | ` `, `\t` |

### Expressões Regulares Utilizadas

```python
dic = {
    'COMMENT':     r"\#.*",           
    'STRING':      r'"[^"]*"',              
    'IDIOMA':      r'@[a-zA-Z\-]+', 
    'SELECT':      r'select',        
    'WHERE':       r"where",
    'LIMIT':       r"LIMIT",
    'VARIABLE':    r"\?[a-zA-Z_][a-zA-Z0-9_]*",
    'PREFIX':      r"[a-zA-Z_][a-zA-Z0-9_]*:[a-zA-Z_][a-zA-Z0-9_]*",
    'A':           r"a", 
    'LBRACE':      r"\{",
    'RBRACE':      r"\}",
    'DOT':         r"\.",
    'NEWLINE':     r"\n",
    'NUMBER':      r"[0-9]+",
    'WHITESPACE':  r"[ \t\r]+",
}
```

### Algoritmo

1. **Combinação de Regex**: Todas as expressões regulares são combinadas usando grupos nomeados (`(?P<nome>padrão)`)
2. **Matching Sequencial**: `re.finditer()` encontra todos os matches sequencialmente
3. **Identificação de Tipo**: Através de `match.groupdict()` identifica-se qual grupo fez match
4. **Extração de Informação**: Para cada token captura-se:
   - **Tipo** do token
   - **Valor** 
   - **Linha** onde aparece
   - **Span** (posição inicial e final no input)
5. **Filtragem**: Comentários e whitespace são ignorados (exceto newlines para controlo de linha)

### Função Principal

```python
def tokenizer(input_string):
    tokens = []
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in dic.items())
    linha = 1
    
    for match in re.finditer(token_regex, input_string):
        groups = match.groupdict()
        for tipo, valor in groups.items():
            if valor is not None: 
                if tipo == "NEWLINE":
                    linha += 1
                elif tipo not in ('WHITESPACE', 'COMMENT'):
                    tokens.append((tipo, valor, linha, match.span()))
                break
    
    return tokens
```

---

## Estrutura de um Token

Cada token retornado é uma tupla com 4 elementos:

```python
(tipo, valor, linha, span)
```

**Exemplo:**
```python
('SELECT', 'select', 2, (32, 38))
('VARIABLE', '?nome', 2, (39, 44))
('STRING', '"Chuck Berry"', 4, (95, 108))
('IDIOMA', '@en', 4, (108, 111))
```

---
## Detalhes Técnicos

### Operador `[^"]` em Regex

O operador `^` dentro de `[]` significa **negação**:
- `[^"]` = qualquer caracter **exceto** aspas
- `"[^"]*"` = captura strings sem ser greedy (para na primeira aspas de fecho)

### Ordem de Prioridade

A ordem dos tokens no dicionário é importante:
1. `COMMENT` primeiro (para ignorar resto da linha)
2. `STRING` e `IDIOMA` antes de identificadores genéricos
3. Keywords antes de identificadores (para evitar que "select" seja reconhecido como PREFIX)

---
