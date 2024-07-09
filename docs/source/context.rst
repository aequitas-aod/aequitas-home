Context and background
######################################################################

General Introduction
*********************

Artificial Intelligence (AI) systems are becoming increasingly pervasive in our daily lives, influencing decisions from hiring practices to loan approvals, as well as access to education and healthcare support. However, these systems are not immune to biases; in fact, they often reflect and can exacerbate societal inequalities. Once trained, a system that performs discriminatory actions can crystallize biases into automated, repeated behaviors on a large scale, thereby **amplifying** instances of **discrimination**.

**AI fairness** is a research field that addresses these issues by working to ensure that AI technologies are developed and deployed in an **equitable** way. The primary challenge in this domain is therefore to identify discriminatory behaviors, creating awareness among developers and users so that mitigation measures can be implemented.

The research field of AI fairness is very active today. Typically, there are two mainstream approaches:

* adopting a fair-by-design methodological approach during the design phase of an AI system, and
* measuring and mitigating discriminatory behaviors in existing systems.

 These two approaches are not mutually exclusive. Both approaches have a preliminary step, which is the **definition** of what **fairness** means in the context of the AI system's application.

::

What does it mean to be non-discriminatory in a decision?

First, it is important to emphasize that the selected fairness definition will align with a certain **policy** that is to be enforced in a specific context. This definition will then be integrated into the algorithm.

When we move from a natural language definition of fairness that considers legal and social aspects to a concept that is understandable by an AI system, we refer to it as **computational fairness**.

~ ~ ~
**NOTE**

**Computational fairness** refers to the practice of ensuring that algorithms and AI systems operate in a way that is equitable and free from bias. It involves **translating principles of fairness, which often encompass legal, ethical, and social dimensions, into precise, measurable criteria** that can be understood and enforced by computational systems.

In summary, computational fairness seeks to operationalize abstract fairness concepts into actionable, measurable practices within AI systems to ensure they are just and unbiased in their decision-making processes. This process typically includes:

* Defining fairness notions: establishing what fairness means within a specific context and translate it in computational terms
* Implementing fairness in algorithms: integrating fairness considerations into the design and functioning of AI systems
* Measuring and monitoring: continuously evaluating AI systems to ensure they meet fairness constraints. This includes using metrics to measure discrimination (see :ref:detection.rst)
* Mitigation strategies: applying techniques to address and reduce identified biases (see :ref:mitigation.rst)

~ ~ ~


The AEQUITAS project
*********************

* objectives and ambitions
* methodology
* impact
