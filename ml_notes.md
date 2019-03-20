## ML realted notes

### Basic
**Why batch normalization can't be used with dropout?**
Dropout cause variance shift when inferencing. This will crack down the BN layer, because the mean and variance for inferencing is calculated during training.
However, we don't do drop out when inferencing, thus cause this problem.

### Useful library
1. [Facebook wav2letter](https://code.fb.com/ai-research/wav2letter/)

### NLP 
1. [10 leads of NLP in 2018](http://ruder.io/10-exciting-ideas-of-2018-in-nlp/)
2. Knowledge Graph Embedding \[[paper](https://arxiv.org/pdf/1811.04588.pdf)\] \[[code](https://github.com/davidlvxin/TransC)\]
3. [Introduction to BERT](http://bangqu.com/hiA591.html)
4. [Strutured Attention Network](https://arxiv.org/abs/1702.00887)
5. [GPT2, Language model are unsupervised multitask learners](https://openai.com/blog/better-language-models/)

### Miscellaneous
1. [Thoughts on the BagNet Paper](https://blog.evjang.com/2019/02/bagnet.html)
2. [Interpretability of CNN](https://zhuanlan.zhihu.com/p/30074544)
3. [RT streaming anomaly dtection](https://towardsdatascience.com/real-time-streaming-and-anomaly-detection-pipeline-on-aws-cbd0bef6f20e)

### Papers
1. [What have deep net done for vision?](https://arxiv.org/pdf/1805.04025.pdf)
2. [Model based RL](https://medium.com/syncedreview/google-brain-simple-complete-model-based-reinforcement-learning-for-atari-b350a960921c)
3. [Adabound, an optimizer as fast as Adam, as good as SGD](https://github.com/Luolc/AdaBound)
