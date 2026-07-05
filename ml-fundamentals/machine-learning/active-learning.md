* Draft: 2021-02-16 (Tue)

# Active Learning

## Active learning in education

> * **Active learning** is any approach to instruction in which all students are asked to engage in the **learning** process. 
>   * **Active learning** stands in contrast to "traditional" modes of instruction in which students are passive recipients of knowledge from an expert.
>
> Source: [Active Learning | Center for Educational Innovation](https://cei.umn.edu/active-learning#:~:text=Active learning is any approach,of knowledge from an expert.)
>
> * **Active learning** is "a method of learning in which students are actively or experientially involved in the learning process and where there are different levels of active learning, depending on student involvement."
>
> Source: [Active learning](https://en.wikipedia.org/wiki/Active_learning), Wikipedia

## Active learning in machine learning

According to [Active learning machine learning: What it is and how it works](https://algorithmia.com/blog/active-learning-machine-learning), 2020-09-27, Algorithmia



> **What is active learning?**
>
> * Active learning is 
>   * the subset of machine learning in which 
>   * a learning algorithm can query a user interactively to label data with the desired outputs.
> * Active learning is all about labeling data dynamically and incrementally during the training phase 
>   * so that the algorithm can identify what label would be the most beneficial for it to learn from.
>
> * Active learning is closer to traditional supervised learning.
>
> * It is a type of semi-supervised learning,
>   * meaning models are trained using both labeled and unlabeled data.
>   * The idea behind semi-supervised learning is that labeling just a small sample of data might result in the same accuracy or better than fully labeled training data. 
>   * The only challenge is determining what that sample is.
>
> **Three categories of active learning**
>
> * Stream-based selective sampling
> * Pool-based sampling
> * Membership query synthesis
>
> **How does active learning work?**
>
> * Basically, the decision of whether or not to query each specific label 
>   * depends on whether the gain from querying the label is greater than the cost of obtaining that information.
>   * This decision making, in practice, can take a few different forms based on the data scientist’s budget limit and other factors.
>
> **(More on) What is active learning?**
>
> * In active learning, the algorithm proactively selects the subset of examples to be labeled next from the pool of unlabeled data.
>
> * Therefore, active learners are allowed to 
>
>   * interactively pose queries during the training stage. 
>   * These queries are usually in the form of unlabeled data instances and the request is to a human annotator to label the instance. 
>   * This makes active learning part of the human-in-the-loop paradigm, where it is one of the most powerful examples of success.
>
> * The fundamental belief behind the active learner algorithm concept is that 
>
>   * an ML algorithm could potentially reach a higher level of accuracy
>   * while using a smaller number of training labels
>   * if it were allowed to choose the data it wants to learn from
>
>   

