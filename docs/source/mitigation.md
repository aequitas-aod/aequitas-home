# AI Bias Mitigation

## What is Bias Mitigation?


Bias mitigation refers to the set of techniques and strategies used to reduce or
eliminate unjustified biases that can emerge in AI models. These biases can
arise from skewed training data, unbalanced algorithms, or other sources that
reflect human or structural prejudices.

### Why is it important?
Bias mitigation is crucial to ensure that AI systems are fair, inclusive, and
non-discriminatory, thereby promoting more accurate and just decisions in
applications ranging from hiring processes to medical diagnosis.

## Mitigation Approaches
Bias mitigation approaches in artificial intelligence refer to the various
strategies and techniques designed to reduce or eliminate biases within AI
models and their training processes.

These biases can arise from historical data, algorithmic structures, or even
unintentional human biases encoded in the data. By applying these approaches, we
can improve the fairness, accuracy, and inclusiveness of AI systems.

To mitigate the bias, it is possible to work through these three stages of model
development and apply specific methodologies for that stage:

### Pre-processing
Pre-processing approaches aim to modify the input data before it is used to
train AI models. The goal is to remove or reduce biases present in the raw data.
There are a variety of ways to do this, the most common being:
- **Data Reweighing**:
Assigns weights to tuples in the training dataset to make it discrimination-free
without modifying the labels. Weights are selected based on the distribution of
protected attributes or using optimization methods to minimize disparities
between groups. [[1]](#1)
- **Data Transformation**:
Applying techniques like normalization or encoding to reduce the impact of
biases in the data. [[2]](#2)
- **Anonymization**:
Removing or masking sensitive attributes (such as gender, ethnicity) to prevent
them from influencing the model.

### In-Processing
In-processing approaches focus on improving algorithms and training techniques
to prevent the introduction of bias during the model building phase.
There are a variety of ways to do this, the most common being:
- **Adversarial Regularization**:
Adding specific loss terms during training and use of an adversarial model
during training of the main model. The goal is to penalize the model when it
makes predictions based on sensitive attributes. [[3]](#3)
- **Fair Representation Learning**:
Learns data representations that are independent of sensitive attributes (e.g.,
gender, ethnicity). The goal is to find a latent representation that encodes the
data well but also obfuscates information about protected attributes, promoting
unbiased predictions. [[4]](#4)
- **Fairness Constraints Methods**:
Incorporates fairness constraints directly into the optimization process of the
learning algorithm. Examples include adding fairness metrics such as demographic
parity (equal probability of positive outcomes across groups) or equalized odds
(equal true positive and false positive rates across groups) as additional terms
in the loss function. [[5]](#5)

### Post-Processing
Post-processing approaches are applied after the model has been trained, aiming
to correct any biases present in the model’s predictions.

There are a variety of ways to do this, the most common being:
- **Equalized Odds Post-Processing**: The main goal of Equalized Odds is indeed
  to ensure that the model has similar True Positive Rate (TPR) and False
Positive Rate (FPR) rates among different groups. This is critical to prevent
the model from unfairly discriminating against certain groups. [[6]](#6)
- **Calibration**: Recalibrating predicted probabilities to ensure they are
  reliable and equitably distributed across various groups. [[7]](#7)
- **Reject Option Classification**: Giving the option to defer decisions when
  the model is uncertain, particularly in cases where predictions could be
unfair. This allows for human oversight in critical decisions, improving
fairness. [[8]](#8)

#### References
<a id="1">[1]</a>
F. Kamiran and T. Calders, “Data Preprocessing Techniques for Classification without Discrimination,” Knowledge and Information Systems, 2012

<a id="2">[2]</a>
F. P. Calmon, D. Wei, B. Vinzamuri, K. Natesan Ramamurthy, and K. R. Varshney. “Optimized Pre-Processing for Discrimination Prevention.” Conference on Neural Information Processing Systems, 2017

<a id="3">[3]</a>
B. H. Zhang, B. Lemoine, and M. Mitchell, “Mitigating Unwanted Biases with Adversarial Learning,” AAAI/ACM Conference on Artificial Intelligence, Ethics, and Society, 2018

<a id="4">[4]</a>
R. Zemel, Y. Wu, K. Swersky, T. Pitassi, and C. Dwork, “Learning Fair Representations.” International Conference on Machine Learning, 2013

<a id="5">[5]</a>
Muhammad Bilal Zafar and Isabel Valera and Manuel Gomez Rodriguez and Krishna P. Gummadi, "Fairness Constraints: Mechanisms for Fair Classification", 2017

<a id="6">[6]</a>
M. Hardt, E. Price, and N. Srebro, “Equality of Opportunity in Supervised Learning,” Conference on Neural Information Processing Systems, 2016

<a id="7">[7]</a>
G. Pleiss, M. Raghavan, F. Wu, J. Kleinberg, and K. Q. Weinberger, “On Fairness and Calibration,” Conference on Neural Information Processing Systems, 2017

<a id="8">[8]</a>
F. Kamiran, A. Karim, and X. Zhang, “Decision Theory for Discrimination-Aware Classification,” IEEE International Conference on Data Mining, 2012
