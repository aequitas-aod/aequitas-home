Innovative Techniques for AI Fairness
=================================================

In our continuous effort to enhance fairness and accuracy in AI systems, the AEQUITAS project has pioneered a suite of innovative techniques designed to detected and mitigate bias. These advanced techniques are embedded directly within our experimentation tool, providing users with powerful, accessible means to conduct experiments and refine processes. The list below details the cutting-edge techniques we have developed, each tailored to address specific challenges in bias detection and correction.

AI Bias Detection & Awareness
------

This section outlines our key contributions to bias detection and awareness, featuring cutting-edge research and methodologies that address the complex challenges posed by socio-technical decision-making environments. New tools for detection have been proposed as well as new metrics for bias evaluation. Each entry below details a significant advancement in the field, designed to refine how we assess, understand, and correct biases in AI applications.

* `Impact based fairness framework for socio-technical decision making <https://ceur-ws.org/Vol-3523/paper12.pdf>`_: This paper introduces the AEQUITAS Socio-Technical System Assessment tool, which evaluates the broader impact of AI-driven decisions on society. The tool aims to ensure that automated decisions contribute positively to social equity and cohesion.

* Generalization of existing SoA metrics

    * `Generalized Disparate Impact for Configurable Fairness Solutions in ML <https://proceedings.mlr.press/v202/giuliani23a/giuliani23a.pdf>`_: This paper introduces a new metric that enhances traditional metrics to better handle data attributes that vary continuously, providing a more detailed and accurate analysis.

    * `AI-fairness and equality of opportunity: a case study on educational achievement <https://ceur-ws.org/Vol-3808/paper17.pdf>`_: This paper introduces a new metric that Incorporates considerations of the social and legal context in the bias assessment, adapting detection techniques to be sensitive to changing regulations and cultural expectations.


* Exploitation of Explainable AI techniques for assessing fairness

    * `Hierarchical Knowledge Extraction from Opaque Machine Learning Predictors <https://link.springer.com/chapter/10.1007/978-3-031-80607-0_20>`_: This paper introduces novel techniques for symbolic knowledge extraction from a black box. This allows for a better understanding of undesired rules hidden in the algorithm.

    * `Achieving Complete Coverage with Hypercube-Based Symbolic Knowledge-Extraction Techniques <https://link.springer.com/chapter/10.1007/978-3-031-50396-2_10>`_: This paper introduces novel techniques for symbolic knowledge extraction from a black box. This allows for a better understanding of undesired rules hidden in the algorithm.

    * `Unmasking the Shadows: Leveraging Symbolic Knowledge Extraction to Discover Biases and Unfairness in Opaque Predictive Models <https://ceur-ws.org/Vol-3808/paper13.pdf>`_: This study examines the use of symbolic knowledge-extraction to identify biases in opaque predictive models by analyzing if-then rules. The approach is shown to effectively detect unfair decisions, aiding in the development of fairer, more transparent systems.


AI Bias Mitigation
------

The AEQUITAS project has led to the development of several innovative techniques aimed at mitigating AI bias and ensuring fairness in various domains. These advancements focus on incorporating fairness into the very structure of AI systems, ensuring not only immediate fairness but also long-term stability and adaptability.

* `FAiRDAS: Fairness-Aware Ranking as Dynamic Abstract System <https://ceur-ws.org/Vol-3523/paper5.pdf>`_: This study proposes an abstract dynamic system to ensure long-term fairness in AI-driven ranking and matchmaking systems. By modeling the evolution of fairness metrics over time, the approach helps analyze system behavior, interactions, and trade-offs, validated through Use case S2.

* `Ensuring Fairness Stability for Disentangling Social Inequality in Access to Education: the FAiRDAS General Method <https://www.ijcai.org/proceedings/2024/820>`_: This work introduces FAiRDAS, a framework for modeling long-term fairness in AI-based educational performance prediction, addressing issues of educational inequality. It provides a customizable solution to ensure fairness while maintaining the stability of mitigation actions over time, demonstrated with real-world data (S2). This is a more advanced and complete study on fairness in AIEd compared to the previous one.

* `Enforcing Fairness via Constraint Injection with FaUCI <https://ceur-ws.org/Vol-3808/paper8.pdf>`_: This work introduces FaUCI, a versatile framework for incorporating fairness constraints into neural networks, supporting a wide range of attribute types. It outperforms state-of-the-art in-processing fairness solutions in terms of effectiveness and efficiency across various fairness metrics.

* `Long-Term Fairness Strategies in Ranking with Continuous Sensitive Attributes <https://ceur-ws.org/Vol-3808/paper8.pdf>`_: This work addresses the gap in fairness research by proposing a methodology for ensuring long-term fairness in ranking systems with continuous sensitive attributes.

AI Fairness: Methodology and Formal Methods
------
In the AEQUITAS project, a key focus has been to develop comprehensive methodologies and formal methods for assessing and enforcing fairness throughout the AI lifecycle. The main contribution are the following.

* `Assessing and Enforcing Fairness in the AI Lifecycle <https://www.ijcai.org/proceedings/2023/0735.pdf>`_: This survey organizes the current state of research on fairness concepts and related bias-mitigation techniques across the AI lifecycle, and also highlights the gaps and challenges identified during its development. This set the foundation for the AEQUITAS methodology as well as the state of the art techniques included in the experimentation environment.

* `A geometric framework for fairness <https://ceur-ws.org/Vol-3523/paper9.pdf>`_: The paper presents the GEOmetric Framework for Fairness (GEOFFair), which provides an intuitive and rigorous approach to understanding fairness in machine learning. By representing fairness-related elements as vectors and sets, GEOFFair allows for visualizing mitigation techniques, constructing proofs, and exploring fairness properties like distances between fairness vectors and trade-offs between metrics.

Benchmarks and Synthetic Data Generation: different bias polarization
------
The AEQUITAS project has also made significant advances in the creation of benchmarks and the generation of synthetic data to explore and evaluate bias polarization in AI systems. These innovations are crucial for assessing the impact of various biases and ensuring that mitigation techniques perform effectively under different scenarios.

* `Generation of Clinical Skin Images with Pathology with Scarce Data <https://link.springer.com/chapter/10.1007/978-3-031-63592-2_5>`_: This research presents a Machine Learning (ML) technique to generate synthetic, realistic skin images for dermatology, addressing the challenge of limited training data for disease detection. By using just a few samples, the approach augments datasets and improves image classification tasks, demonstrated with data from Use case HC1.
