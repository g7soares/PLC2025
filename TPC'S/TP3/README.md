# TP2
Neste problema, o professor orientou-nos para fazer um pequeno conversor de *Markdown* para *HTML*

# Solução
Optei por fazer funções individuais para usar com o método *re.sub*, assim, para cada elemento de Markdown, criei:

## Funções de Conversão

### 1. **boldF(m)** - Negrito
Converte texto entre `**` para tags `<b>`:
- Input: `**texto**`
- Output: `<b>texto</b>`

### 2. **italicF(m)** - Itálico
Converte texto entre `*` para tags `<i>`:
- Input: `*texto*`
- Output: `<i>texto</i>`

### 3. **linkF(m)** - Links
Converte a sintaxe `[texto](url)` para tags `<a>`:
- Input: `[página da UC](http://www.uc.pt)`
- Output: `<a href="http://www.uc.pt">página da UC</a>`

### 4. **imageF(m)** - Imagens
Converte a sintaxe `![alt](url)` para tags `<img>`:
- Input: `![imagem dum coelho](http://www.coellho.com)`
- Output: `<img src="http://www.coellho.com" alt="imagem dum coelho"/>`

### 5. **headingF(m)** - Cabeçalhos
Converte cabeçalhos `#`, `##`, `###` para tags `<h1>`, `<h2>`, `<h3>`:
- Calcula o nível com `len(m.group(1))`
- Input: `## Subtítulo`
- Output: `<h2>Subtítulo</h2>`

### 6. **boldinitalic(m)** - Negrito dentro de Itálico
Converte texto entre `***` para tags `<b><i>`:
- Input: `***texto***`
- Output: `<b><i>texto</i></b>`
- Este caso deve ser processado **antes** do negrito e itálico simples para evitar conflitos

### 7. **numberedListF(m)** - Listas Numeradas
Converte listas numeradas para tags `<ol>` e `<li>`:
- Processa múltiplas linhas consecutivas iniciadas por `1.`, `2.`, etc.
- Remove a numeração original usando `re.sub(r'^\d+\.\s+', '', item)`
- Envolve cada item em tags `<li>`

## Função Principal: markdown_to_html(text)

A função `markdown_to_html` aplica todas as conversões na ordem correta:

1. **Listas numeradas** - Primeiro, pois são multi-linha
2. **Cabeçalhos** - Elementos de início de linha
3. **Imagens** - Antes dos links (ambos usam `[]()` mas imagens têm `!`)
4. **Links** - Após imagens
5. **Negrito e Itálico combinados** (`***texto***`) - Antes dos casos individuais
6. **Negrito** - Antes de itálico (para evitar conflitos)
7. **Itálico** - Por último

### Expressões Regulares Utilizadas:

- **Listas numeradas**: `r'(?:^\d+\.\s+.+$\n?)+'` - Captura blocos de linhas numeradas
- **Cabeçalhos**: `r'^(#{1,3})\s+(.+)$'` - Captura 1 a 3 `#` no início da linha
- **Imagens**: `r"!\[(.*?)\]\((.*?)\)"` - Captura `![texto](url)`
- **Links**: `r"\[(.*?)\]\((.*?)\)"` - Captura `[texto](url)`
- **Negrito e Itálico**: `r"\*\*\*(.*?)\*\*\*"` - Captura texto entre `***`
- **Negrito**: `r"\*\*(.*?)\*\*"` - Captura texto entre `**`
- **Itálico**: `r"\*(.*?)\*"` - Captura texto entre `*`

## Nota Importante
A ordem de processamento é crucial! 
- As **imagens** devem ser processadas antes dos **links**, pois ambos usam a sintaxe `[texto](url)`, mas as imagens têm um `!` no início.
- O caso **negrito dentro de itálico** (`***texto***`) deve ser processado antes dos casos simples de negrito e itálico para evitar que o regex capture incorretamente os asteriscos.