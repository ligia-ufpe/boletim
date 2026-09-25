---
titulo: "Título"
autor: "Fulano"
coluna_convidado: true
pendente: true
minibio: "Minibio de Fulano"
---

Imagine que você treinou uma IA para diagnosticar doenças com 99% de precisão em um hospital de Londres. Se você levar esse modelo para um hospital em Singapura, sem ajustes, ele provavelmente falhará silenciosamente, mantendo uma confiança arrogante em diagnósticos errados.

Para combater essa "superconfiança", pesquisadores desenvolveram a Conformal Prediction (CP). Diferente das redes neurais comuns, a CP não entrega apenas um resultado, mas um conjunto de possibilidades com uma garantia matemática de acerto (ex: "tenho 95% de certeza que a resposta está aqui"). Os fundamentos dessa área foram estabelecidos na obra clássica "Algorithmic Learning in a Random World" por Vovk, Gammerman e Shafer [1], e popularizados recentemente por guias acessíveis como o de Angelopoulos e Bates [2].

Porém, a CP clássica tem um calcanhar de Aquiles: ela assume que os dados de amanhã serão estatisticamente idênticos aos de ontem. Mas no mundo real, ocorre o Distribution Shift (mudança de distribuição). Câmeras mudam, o clima muda, as populações mudam.

É neste cenário que se insere o WQLCP, apresentado no workshop do CVPR 2025. No artigo "WQLCP: Weighted Adaptive Conformal Prediction for Robust Uncertainty Quantification Under Distribution Shifts" [3], propomos uma evolução necessária: a calibração consciente do teste.

Enquanto métodos anteriores tentavam apenas escalar a incerteza, o WQLCP utiliza a perda de reconstrução de um VAE para "sentir" o quão estranhos são os novos dados de teste (mesmo sem rótulos). Com base nisso, o algoritmo repondera matematicamente a importância dos exemplos de calibração, ajustando dinamicamente o limiar de confiança. Isso permite manter a segurança da predição mesmo quando o cenário muda drasticamente, marcando um passo importante para sistemas autônomos verdadeiramente robustos.
