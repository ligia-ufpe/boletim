---
titulo: "Entenda a Causa Real das Alucinações da IA"
autor: "João Victor Lopes"
autor_url: "https://www.linkedin.com/in/joão-victor-lopess"
imagem: "https://images.unsplash.com/photo-1731321094457-fc652112214b?auto=format&fit=crop&w=1200&q=70"
fonte: "https://openai.com/pt-BR/index/why-language-models-hallucinate/"
---

Se você usa IAs como o **ChatGPT** ou **Gemini**, provavelmente já se deparou com uma 'alucinação': uma resposta que soa perfeita, mas é falsa. Um advogado que usou a IA para pesquisar casos e recebeu citações de processos que nunca existiram é um exemplo famoso disso. Esse fenômeno, onde a IA gera respostas plausíveis mas factualmente incorretas, é o que chamamos de **"alucinação"**. Mas por que isso acontece?

Recentemente, a OpenAI publicou um [artigo](https://openai.com/pt-BR/index/why-language-models-hallucinate/) que joga uma nova luz sobre o problema. A resposta, surpreendentemente, não está apenas nos dados de treinamento, mas na própria "educação" desses modelos. Pense nos modelos de linguagem como alunos brilhantes se preparando para uma prova muito difícil. Durante o treinamento e, principalmente, nas avaliações (os *benchmarks*), eles aprendem que é melhor arriscar um palpite do que deixar uma questão em branco. O sistema de notas atual da maioria das avaliações de IA recompensa um palpite correto da mesma forma que uma resposta sabida, enquanto admitir "eu não sei" resulta em nota zero. Essa dinâmica cria um incentivo perverso: na dúvida, adivinhe. O resultado é um modelo que, para maximizar sua pontuação, prefere gerar uma resposta que *parece* correta a admitir incerteza.

Essa pressão estatística para sempre dar uma resposta é a raiz do problema. Não se trata de um "bug" misterioso, mas de uma consequência natural de como otimizamos essas tecnologias. A solução proposta? Mudar a forma de avaliar. Precisamos criar sistemas que penalizem mais os erros ditos com confiança e que, de alguma forma, recompensem a honestidade intelectual da máquina em admitir quando não sabe a resposta. Essa é uma das formas em que vamos poder ter sistemas de IA mais confiáveis e seguros.
