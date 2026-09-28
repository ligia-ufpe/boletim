---
titulo: "Formalizando o conhecimento matemático na era da IA"
autor: "Maria Eduarda Farias"
autor_url: "https://www.linkedin.com/in/maria-eduarda-farias-b6435327a/"
imagem: "https://images.unsplash.com/photo-1635372722656-389f87a941b7?auto=format&fit=crop&w=1200&q=70"
---

Por volta de 300 a.C., Euclides escreveu *Os Elementos*, uma coleção de 13 livros autocontidos sobre os fundamentos da geometria euclidiana. De modo semelhante, muitos trabalhos matemáticos iniciais podiam ser compreendidos integralmente a partir do próprio texto.

Com o tempo, os avanços começaram a se acumular e a área tornou-se cada vez mais complexa. Hoje, não é incomum encontrar artigos com centenas de páginas e dezenas de citações. O teorema da classificação dos grupos simples finitos, também conhecido como *O Teorema Enorme*, é um exemplo notável: um esforço colaborativo de cerca de 100 autores e dezenas de milhares de páginas, compreendido em sua totalidade por pouquíssimos matemáticos.

Nos últimos anos, a inteligência artificial começou a se inserir nesse cenário, transformando não apenas a forma como produzimos conhecimento, mas também como o validamos. Em uma palestra recente, Kevin Buzzard, professor no Imperial College London, destacou as limitações dos métodos tradicionais de documentar avanços matemáticos: informações-chave ausentes nos artigos, conhecidas apenas por especialistas, tendem a se perder com o tempo.

Sua estratégia para mitigar o problema é a Mathlib, uma biblioteca *open-source* escrita em Lean, um provador de teoremas que permite formalizar resultados matemáticos de modo que possam ser verificados por computador. Embora criada para garantir rigor e reprodutibilidade, a Mathlib vem se tornando uma aliada promissora das IAs generativas, que podem utilizá-la como uma base de conhecimento confiável para raciocinar matematicamente de forma mais precisa e verificável.

Atualmente, um dos grandes desafios dos LLMs é o das alucinações, pois eles frequentemente inventam informações ou cometem erros lógicos, especialmente em contextos matemáticos. Para avaliar suas capacidades, são usados benchmarks inspirados em olimpíadas de conhecimento, como o da MathArena, que testou diversos modelos na IMO 2025. O Gemini 2.5 Pro teve a melhor performance, com 31% de acertos, pontuação abaixo da necessária para uma medalha de bronze, mostrando o quanto ainda há espaço para avanços.

Surpreendentemente, o Seed-Prover, da ByteDance, alcançou a medalha de prata na mesma competição. O modelo combina um LLM voltado ao raciocínio matemático com um verificador formal em Lean. Portanto, integrar esses modelos a ferramentas como o *Lean* e sua Mathlib possibilita a construção de argumentos mais robustos, reduzindo erros e tornando-os mais confiáveis.

Ainda que essas tecnologias estejam longe de substituir matemáticos humanos, elas marcam um passo importante rumo a um futuro em que IAs atuam como copilotos na descoberta matemática, auxiliando na formalização de resultados, explorando novas ideias e assegurando a correção lógica de argumentos complexos.

**Fontes**

- [Kevin Buzzard - Where is Mathematics Going?](https://www.youtube.com/watch?v=K5w7VS2sxD0)
- [Mathlib Initiative](https://mathlib-initiative.org/)
- [MathArena - IMO Blogpost](https://matharena.ai/imo/)
