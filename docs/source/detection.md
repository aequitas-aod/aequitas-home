## Introduction

### What is Bias Detection?

Bias detection in AI refers to the process of identifying and understanding biases that may exist within artificial intelligence systems and can lead to harmful decisions affecting individuals. The detection of bias relies on the use of fairness metrics that take into account the impact of a person's sensitive attributes on the outcomes of a system. Sensitive attributes change depending on the use-case under consideration and the features related to the involved individuals. Just a few examples of sensitive attributes might be gender, ethnicity, education level and the socio-economic status.

### Why is Bias Detection important?

With the growing impact of machine learning systems in domains protected by anti-discrimination law, it is crucial to develop techniques for algorithmically measuring fairness.

## Detection Approaches

From an algorithmic point of view, several detection approaches exist because there is no single fairness metric capable of effectively quantifying a machine learning system's bias in any context. The only solution is to carefully study the use case at hand and pick the most suitable fairness metric(s) to detect the bias depending on the adverse effects that need to be identified and mitigated. Within the same context it could definitely happen that different fairness metrics paint contradicting pictures regarding a model's outcomes. Some metrics might show that the system is biased while some might not. This is why it is essential to clearly understand what each fairness metric measures when it is used in practice.

As a brief introduction, we follow [(Verma, 2018)](#bibliography) to present some of the existing fairness metrics. These approaches can be categorized according to what information, relative to the data and the model's output, they use to quantify the existing bias.

### Notation

* **G**: sensitive attribute that shouldn't impact how a model makes its decisions
* **X**: non-sensitive attributes describing an individual
* **Y**: in classification settings, it is the ground truth label assigned to an individual  
* **S**: the predicted probability for a certain class
* **d**: the predicted class for an individual; it is usually derived from $S$ meaning that $d = 1$ when $S$ is above a certain threshold. Depending on the context, a model's decision, the predicted class for a specific individual, can either be good (*i.e.* associated to a positive outcome or set of consequences) or bad. From now on $d = 1$ will refer to the positive predicted class while $d = 0$ will refer to the negative predicted class.

For simplicity, when defining the presented fairness metrics, we will assume that the sensitive attribute $G$ is the gender attribute and its possible values are two: *male*, often abbreviated as $m$, and *female*, referred to as *f*.

### Definitions based on predicted outcome

#### Statistical parity (SP)

First introduced in [(Dwork, 2012)](#bibliography), statistical parity states that subjects belonging to groups identified by specific values of a sensitive attribute should have the same probability of being assigned to the positive predicted outcome. Mathematically:

$$P(d = 1|G = m) = P(d = 1|G = f)$$

In this case, the sensitive attribute $G$ represents an individual's gender and $m$ and $f$ are its possible values ("male" and "female" respectively).

#### Conditional Statistical Parity

The metric proposed by [(Corbett-Davies, 2017)](#bibliography) extends the previous one by allowing to condition on a specific subset of attributes to affect the outcome. The formula becomes:

$$P(d = 1|G = m, L = l)= P(d = 1|G = f, L = l)$$

In words, SP is computed only taking into consideration those individuals for whom the attribute $L$ has value $l$.

### Definitions Based on Predicted and Actual Outcomes

#### Predictive parity

A model satisfies the definition proposed by [(Chouldechova, 2016)](#bibliography) if individuals have equal PPV (Positive Predictive Value) regardless of the sensitive group they belong to. PPV is defined as $P(Y=1|d=1)$, the probability of a subject with a positive predictive value to belong to the positive class. Formally, Predictive Parity is given by:

$$P(Y=1|d=1, G=m) = P(Y=1|d=1, G=f)$$

#### False Positive Error Rate Balance

As the name suggests, this metric ([Chouldechova, 2016](#bibliography)) is satisfied when the protected and unprotected groups have equal false positive rate (FPR). FPR is the probability of a subject belonging to the negative class (*i.e.* the class associated with a "bad" outcome for its members) to be assigned a positive predictive value, $P(d = 1|Y = 0)$. The formal definition for the False Positive Error Rate Balance metric is:

$$P(d = 1|Y = 0,G = m) = P(d = 1|Y = 0,G = f )$$

#### False Negative Error Rate Balance

This metric (see [Chouldechova, 2016](#bibliography)) is also known as Equal Opportunity in the AI fairness literature. A classifier satisfies Equal Opportunity if subjects have equal false negative rates FNR across sensitive groups. FNR is the probability of an individual in the positive class to have a negative predicted value, $P(d = 0|Y = 1)$. The formula for the False Negative Error Rate Balance is:

$$P(d = 0|Y = 1,G = m) = P(d = 0|Y = 1,G = f )$$

Note that, mathematically, if a classifier with equal FNRs will also have equal TPR:

$$P(d = 1|Y = 1,G = m) = P(d = 1|Y = 1,G = f )$$

#### Equalized Odds

This definition ([Hardt, 2016](#bibliography)) combines the previous two meaning that for a classifier to satisfy Equalized Odds it is necessary that both the protected and the unprotected groups have equal TPR and FNR. Formally:

$$P(d = 1|Y = i,G = m) = P(d=1|Y=i,G=f), i \in \\{ 0,1 \\}$$

### Definitions Based on Predicted Probabilities and Actual Outcome

#### Test-fairness

This fairness metric ([Chouldechova, 2016](#bibliography)) is also knows as calibration in the fairness literature. A classifier satisfies this definition if for any predicted probability score $S$, subjects have equal probability to truly belong to the positive class independent of the sensitive group they belong to. In formulas this becomes:

$$P(Y = 1|S = s,G = m) = P(Y = 1|S = s,G = f )$$

#### Balance for positive class

Balance for the positive class ([Kleinberg, 2017](#bibliography)) is achieved if subjects constituting the positive class from all sensitive groups have equal average predicted probability score S. In our example used so far to present these metrics, this translates to:

$$E(S |Y = 1, G = m) = E(S |Y = 1, G = f )$$

#### Balance for negative class

Balance for the negative class in analogous to Balance for the negative class with the only exception that subjects belonging to the negative class are considered instead. Mathematically:

$$E(S|Y = 0,G = m) = E(S|Y = 0,G = f )$$

### Similarity-based measures

All the previously defined metrics specifically focus only on the sensitive attributes and end up ignoring all the remaining features $X$. This way of treating individuals might still be unfair if "similar individuals must be treated similarly", regardless of their sensitive attributes.

This is where similarity based fairness metrics come in.

#### Causal discrimination

A classifier satisfies causal discrimination ([Galhotra, 2017](#bibliography)) if any two subjects with the exact set of attributes $X$ are assigned the same label:

$$(X_{f} =X_{m} \land G_{f} \neq G_{m}) \implies d_{f} = d_{m}$$

#### Fairness through unawareness

To satisfy the definition proposed by [Kusner, 2017](#bibliography) it is sufficient that no sensitive attributes are *explicitly* used in the decision making progress. This also means that the classification outcome should be the same for those subjects that have the same attributes $X$: $Xi = Xj → di = dj$

### Causal Reasoning

Causal reasoning is based on the notion of causal graph: a directed, acyclic graph with nodes representing attributes of an individual and edges representing relationships between the attributes. Relationships between attributes and their influence on the model's outcome is captured by a set of equations which are further used to estimate the effects of the sensitive attributes (*i.e.* exactly what all fairness metrics do) and build algorithms that can mitigate the existing bias.

#### Counterfactual fairness

According to [Kusner, 2017](#bibliography) a causal graph is counterfactually fair if the predicted outcome $d$ in the graph does not depend on a descendant of the protected attribute $G$.

**Note**: The presented metrics are just a small subset of the existing ones. The reader is encouraged to read Verma's paper while keeping in mind that it was published in 2018. The other referenced papers allow to dive deeper in the technicalities and details that are out of the scope of this simple primer on AI bias detection.

## Bibliography

1. <a name="item1"></a>Verma, S. (2018). *Fairness Definitions Explained*. ACM.
2. <a name="item2"></a>Dwork, C. (2012). *Fairness Through Awareness*. ACM.
3. <a name="item3"></a>Corbett-Davies, S. (2017). *Algorithmic Decision Making and the Cost of Fairness*. ACM.
4. <a name="item4"></a>Chouldechova, A. (2016). *Fair prediction with disparate impact: A study of bias in recidivism prediction instruments*.
5. <a name="item5"></a>Hardt, M. (2016). *Equality of Opportunity in Supervised Learning*.
6. <a name="item6"></a>Kleinberg, J. (2017). *Inherent Trade-Offs in the Fair Determination of Risk Scores*. Schloss Dagstuhl - Leibniz-Zentrum für Informatik.
7. <a name="item7"></a>Galhotra, S. (2017). *Fairness testing: testing software for discrimination*. ACM.
8. <a name="item7"></a>Kusner, M. (2017). *Counterfactual Fairness*.
