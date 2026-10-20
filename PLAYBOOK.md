# Rotina de conteúdo · @marquinhosmilhas

Regras que a rotina diária segue para criar e agendar carrosséis. Definidas pelo Marquinhos em 11/10/2026.

## Volume

- **2 carrosséis por dia**, às **11h** e às **18h** (horário de Brasília), os picos da audiência no Metricool. Uma vez por semana, conferir os picos de novo (`getBestTimeToPostByNetwork`) e ajustar.
- Os carrosséis são criados sempre para o **dia seguinte**.

## Regra do eco

Todo conteúdo novo publicado no perfil (Reel, carrossel ou foto) ganha **pelo menos 1 carrossel com outra perspectiva sobre o mesmo tema** nos dias seguintes.

Ângulos possíveis: o erro mais comum, o passo a passo, a conta com números, mito x verdade, comparação (A ou B?), checklist para salvar, bastidor ou história pessoal, "o que ninguém te conta".

## Regra do fora da curva

Um post está **fora da curva** quando o alcance dele é **pelo menos 3 vezes a média** dos posts do mesmo tipo nos últimos 30 dias.

Post fora da curva ganha **de 3 a 5 carrosséis derivados**, espalhados pelos 5 dias seguintes, cada um com um ângulo diferente.

## Ordem da fila

1. Derivados de posts fora da curva
2. Ecos de posts novos
3. Temas do banco de ganchos e promoções de transferência em andamento

**Não fazer:** posts sobre feriados nem ganchos de pergunta genérica ("pra onde você iria?"). O Marquinhos vetou em 11/10/2026.

## Formato (o que funciona no nicho)

- Estilo **"print de tweet"**: gerado com `_base/gerar.py` (foto, "Marquinhos Milhas", @marquinhosmilhas, fundo branco).
- **Capa:** gancho forte em 1 ou 2 linhas, de preferência com número ou valor, e "arrasta pro lado".
- **De 5 a 7 lâminas**, uma ideia por lâmina, texto curto, emojis como marcadores (❌ ✅ 1️⃣ 💸).
- **Última lâmina:** `COMENTA: "PALAVRA"` + "📌 Salva".
- **Sem emoji de bandeira** (o Windows desenha como letras: "US", "EU"). Use 🗽 🐉 🗾 🛕.
- **Legenda curta:** uma frase + "Comenta PALAVRA…" + 4 hashtags.
- Referência: os posts do @matheustiburtino nesse estilo têm de 1 a 3,9 mil comentários.

## Reels de teste (relançamento)

- Manter sempre **gancho de preço na frente** (destino + valor em destaque nos 3 primeiros segundos). Em 19/10, o teste da China sem preço no gancho rendeu pouco.
- Zoom de impacto no 1º meio segundo; CTA "COMENTA MENTORIA" nos últimos segundos; legenda explica que a emissão é antiga.

## Honestidade

- Nunca inventar preço, rota, quantidade de milhas ou promoção. Valor ilustrativo leva a palavra "exemplo" na arte.
- Promoção só entra se for confirmada numa fonte do dia (site do programa ou notícia), com a data de validade.
- Não usar selo de verificado.

## Palavras-chave

- Cada carrossel tem uma palavra-chave no `COMENTA:`. Registrar em `palavras-chave.md` com a data e o que mandar no direct, para configurar a resposta automática.
- Em uso: `MILHAS` e `CONTA` (link do Voa Milha), além das que o Marquinhos já usa (ALERTA, ASSESSORIA, CONSULTORIA…).

## Aprovação

- Os posts são criados no Metricool como **rascunho**, já com data e hora. O Marquinhos revisa no app do Metricool e programa os que aprovar.
- Os primeiros da semana de 12/10 foram aprovados por ele na conversa e podem ir direto como agendados.

## Arquivos

- `carrosseis/<AAAA-MM-DD>-<tema>/NN.png`: as artes
- `roteiros/<AAAA-MM-DD>-<tema>.json`: o texto de cada lâmina, entrada do `gerar.py`
- `registro.md`: o que foi criado, de qual post veio e o link do Metricool
- As imagens vão para um repositório público separado do site, para o Metricool conseguir buscar.
