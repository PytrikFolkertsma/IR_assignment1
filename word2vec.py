import copy
import gensim
import logging
import pyndri
import pyndri.compat

word2vec_init = gensim.models.Word2Vec(
    size=300,  # Embedding size
    window=5,  # One-sided window size
    sg=True,  # Skip-gram.
    min_count=5,  # Minimum word frequency.
    sample=1e-3,  # Sub-sample threshold.
    hs=False,  # Hierarchical softmax.
    negative=10,  # Number of negative examples.
    iter=1,  # Number of iterations.
    workers=8,  # Number of workers.
)

with pyndri.open('index/') as index:
    print('Loading vocabulary.')
    dictionary = pyndri.extract_dictionary(index)
    sentences = pyndri.compat.IndriSentences(index, dictionary)

    print('Constructing word2vec vocabulary.')

    # Build vocab.
    word2vec_init.build_vocab(sentences, trim_rule=None)

    models = [word2vec_init]

    for epoch in range(1, 5 + 1):
        print('Epoch %d', epoch)

        model = copy.deepcopy(models[-1])
        model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)

        models.append(model)

    print('Trained models: %s', models)