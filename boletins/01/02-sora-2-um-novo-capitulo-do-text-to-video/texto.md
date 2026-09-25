---
titulo: "Sora 2: um novo capítulo do text-to-video"
autor: "Rodrigo Rossiter"
autor_url: "https://www.linkedin.com/in/rodrigo-rossiter-a36b5227a"
---

Se você acompanha Generative AI, então já deve estar sabendo do [Sora 2](https://openai.com/index/sora-2/), o novo modelo text-to-video da OpenAI, que é capaz de gerar vídeos hiper-realistas com maior duração, coerência física e áudio sincronizado, permitindo narrativas multi-shot diretamente gerados pelo modelo.

[Analisando o modelo mais a fundo](https://skywork.ai/blog/behind-the-scenes-sora-2-technical-innovations-best-practices-2025/), percebe-se uma arquitetura híbrida, um diffusion–transformer, que processa vídeo por meio de patches espaço-temporais (tokens), o que traz ganhos claros na preservação de forma e na estabilidade temporal: objetos deformam-se menos e mantêm posicionamento e aparência mais consistentes ao longo dos frames. Para elevar ainda mais a qualidade, o sistema admite condicionamento multimodal (prompt, áudio e referência de imagem/estado). Contudo, o pipeline requer prompts bem-especificados, incluindo restrições físicas e de continuidade temporal, e devido às limitações de memória em clipes longos, as melhores práticas recomendam decompor a narrativa em cenas curtas e explicitar estados de cena entre cortes, além de aplicar etapas manuais de pós-processamento, como suavização de flicker, estabilização e harmonização de cor.

Na prática, isso quer dizer que com o avanço desse tipo de tecnologia, ideias viram vídeos em questões de minutos, assim fazendo com que pequenas equipes tenham direito a prototipagem visual e pré-visualizações mais acessíveis, coisa que antes, apenas aqueles com mais investimento teriam acesso.

Contudo, versões anteriores do Sora já mostraram [vieses problemáticos](https://www.wired.com/story/openai-sora-video-generator-bias/) (estereótipos de gênero, raça e capacidade) em investigações jornalísticas e estudos acadêmicos, além de haver preocupações a respeito de temas como deepfakes, direitos autorais e usos maliciosos. A OpenAI inclui medidas de segurança com suas políticas de usos e controles de proveniência, porém, pesquisadores mostram que muitas dessas medidas falharam na prática com sua primeira versão. Com isso, são feitas pesquisas que estudam [formas de mitigar esse problema](https://arxiv.org/pdf/2510.13202), como:

1. Aumento sintético e contrafactual de dados para equilibrar representações
2. Uso de geradores guiados por classificadores e filtragem por detectores de segurança
3. Marcação e revisão humana para controlar uso indevido

O lançamento do Sora 2 e seu feed social ampliam questões práticas: distribuição rápida de vídeos facilita prototipagem criativa, mas também exige moderação escalável contra deepfakes, violações de direitos e usos maliciosos, reforçando a necessidade de auditoria técnica contínua, políticas de consentimento e regulação.
