.. _use-cases-overview:

Use Cases Overview
#########
The validation of the AEQUITAS Framework was conducted through **six real-world use cases** spanning the domains of **Recruitment, Society and economics, and Healthcare**.  
Each use case applied one or more *Fair-by-Design* methodologies, together with socio-technical modelling (IFM), experimental validation, and synthetic data testing.  

Collectively, they demonstrate the **transferability, robustness, and legal-technical coherence** of the AEQUITAS approach across different AI contexts.

Together, these six use cases validate AEQUITAS as a **comprehensive Fair-by-Design framework** capable of aligning AI development with the principles of **fairness, transparency, and accountability** across sectors.

.. list-table:: Usecases
   :header-rows: 1
   :class: blue-header

   * - **Domain**
     - **Organisation**
     - **Methodology**
     - **Focus**
     - **Preliminary Tests & Experimenter Reports**
   * - :doc:`HR1 <usecase-hr1-adecco>`
     - Adecco
     - FDCGM + LLM Assessment
     - Fairness in CV screening & job matching
     - `HR1 folder <https://github.com/aequitas-aod/aequitas-doc/tree/main/usecase-hr1-adecco>`_
   * - :doc:`HR2 <usecase-hr2-akkodis>`
     - Akkodis
     - FDCGM + IFM + FaUCI
     - Fairness in AI-assisted recruitment
     - `HR2 folder <https://github.com/aequitas-aod/aequitas-doc/tree/main/usecase-hr2-akkodis>`_
   * - :doc:`S1 <usecase-s1-child-neglect>`
     - IRCCS
     - PSSA + LLM-based Rule Extraction
     - Trustworthy AI for child neglect detection
     -
   * - :doc:`S2 <usecase-s2-disadvantaged-students>`
     - Univ. of La Laguna
     - TAIRA + FRIA
     - Fairness in student performance prediction
     - `S2 folder <https://github.com/aequitas-aod/aequitas-doc/tree/main/usecase-s2-disadvantaged-students>`_
   * - :doc:`HC1 <usecase-hc1-dermatology>`
     - IRCCS
     - FMM + Synthetic Data
     - Fairness in dermatological image diagnosis
     - `HC1 folder <https://github.com/aequitas-aod/aequitas-doc/tree/main/usecase-hc1-dermatology>`_
   * - :doc:`HC2 <usecase-hc2-ecg>`
     - PRE
     - FOIM + Synthetic ECG
     - Fairness in biomedical signal interpretation
     -

Domain Recruitment
***********

Use case HR1: Bias free AI assisted recruiting system
=====================================================
Tested the FDCGM methodology on a job-matching AI system and extended the evaluation to *LLM-based screening tools*, showing AEQUITAS’ adaptability to emerging generative AI contexts.

.. toctree::
   :maxdepth: 1

   usecase-hr1-adecco

Use case HR2: Assess and repair job-matching AI-assisted recruiting tool to mitigate gender and other bias
==========================================================================================================
  Analysed bias in AI-assisted candidate screening and validated the *Fair Data Collection, Governance and Management (FDCGM)* methodology in combination with *Information Flow Modelling (IFM)* and the *FaUCI* intersectional fairness algorithm.

.. toctree::
   :maxdepth: 1

   usecase-hr2-akkodis

Domain Society and economics
***********


Use case S1: AI assisted identification of child abuse and neglect in hospital with implications for socio-economic disadvantaged and racial bias reduction
================================================================================================================================================================

  Applied the *Prohibited Social Scoring Assessment (PSSA)* to identify the ethical and legal limits for AI deployment in child protection.  
  Used *LLM-based knowledge extraction* from clinical manuals to design a validated, non-predictive support tool — demonstrating responsible non-use of AI.

.. toctree::
   :maxdepth: 1

   usecase-s1-child-neglect

Use case S2: Unfair Inequality in Education
===========================================  
  Assessed fairness in predictive models for student performance.  
  The case combined *TAIRA* (Trustworthy AI Readiness Assessment) and *FRIA* (Fundamental Rights Impact Assessment) with *IFM*, introducing a new fairness metric — *Conditional Demographic Disparities (CDD)*.

.. toctree::
   :maxdepth: 1
   usecase-s2-disadvantaged-students

Domain Healthcare
***********

Use case HC1: AI assisted identification of dermatological disease for diversity and inclusion in dermatology
=====================================================================================================================

Employed the *Fair Model Methodology (FMM)* to assess bias in skin disease prediction and leveraged *synthetic data* to address underrepresentation of darker skin tones.

.. toctree::
   :maxdepth: 1
     
   usecase-hc1-dermatology

Use case HC2: Bias-aware prediction of ECG healthcare outcomes
==============================================================

Applied the *Fair Output Interpretation Methodology (FOIM)* to ensure fairness in AI interpretation of ECG signals, with synthetic data for controlled demographic imbalance.

.. toctree::
   :maxdepth: 1

   usecase-hc2-ecg

Discussion
***********
The validation of the AEQUITAS Framework across six heterogeneous use cases —spanning human resources, education, and healthcare— has demonstrated its capacity to transform the abstract concept of fairness into a practical, measurable, and auditable design principle. Through the integration of legal, ethical, socio-technical, and technical perspectives, AEQUITAS proved that fairness can be operationalized not only as a retrospective check but as a continuous process embedded throughout the AI lifecycle. 

Methodological Coherence 
========================

Each component of the AEQUITAS Framework —Fair-by-Design (FbD) methodologies, Information Flow Modelling (IFM), and the Controlled Experimentation Environment— contributed complementary insights, creating a coherent fairness assurance pipeline: 

* The FbD methodologies (TAIRA, FRIA, PSSA, FMM, FDCGM) provided structured processes, drafted with input from the project’s civil activists and society organizations and associations, to translate the normative and legal language of the EU AI Act and the Charter of Fundamental Rights into concrete assessment steps. They guided developers, lawyers, and domain experts in articulating fairness requirements, identifying protected attributes, and defining proportionality criteria. 

* Information Flow Modelling (IFM) expanded this reflection to the socio-technical level. It revealed how bias and responsibility are distributed among data, algorithms, and human actors. IFM confirmed that fairness must be understood as a system property and is not limited to datasets or code but extends to decision pathways, feedback loops, and organizational practices. 

* The Controlled Experimentation Environment provided quantitative validation and technical stress testing. Through fairness metrics (Statistical Parity Difference, Disparate Impact, Equalized Odds Ratio, Demographic Parity Ratio, and Conditional Demographic Disparity), it enabled the measurement, comparison, and documentation of fairness outcomes before and after mitigation. 

This integration created a closed methodological loop: FbD methodologies identified fairness risks, IFM contextualized them within human workflows, and the Controlled Experimentation Environment translated them into measurable indicators. Together, they produced reproducible, compliance-ready evidence in line with forthcoming AI Act conformity assessments. 

Cross-Domain Insights  
=====================
The six use cases validated AEQUITAS in three distinct regulatory and operational contexts: 

**HR Domain** (Akkodis, Adecco): Fairness challenges emerged from biased historical data and opaque recommendation systems. AEQUITAS demonstrated how FbD and IFM could expose structural inequalities (e.g., gender, age, nationality) and guide mitigation through pre-processing (Correlation Remover), in-processing (Adversarial Debiasing, FaUCI), and interpretability. The Controlled Experimentation Environment showed measurable fairness gains while maintaining model performance, proving that equity and accuracy are not mutually exclusive. 

**Social Domain** (Education, Child Neglect): These use cases tested AEQUITAS at the intersection of ethics and fundamental rights. In Disadvantaged Students, the introduction of Conditional Demographic Disparity (CDD) and the residualization method provided fairness measures aligned with socio-economic contexts, linking AI fairness to social justice. In Child Neglect, AEQUITAS validated that fairness sometimes means refraining from prediction: the PSSA and experimentation proved that responsible AI can take the form of explainable knowledge support rather than autonomous classification. 

**Healthcare Domain** (Dermatology, ECG): AEQUITAS validated fairness methodologies in clinical decision support. Through Fair Model Methodology (FMM) and diffusion-based synthetic data augmentation, the framework addressed representational bias in medical imaging (light-skin dominance) and demographic imbalance in biomedical signals. Results confirmed that fairness-aware data generation can substantially reduce group disparities without compromising diagnostic accuracy, provided it is grounded in transparent design and human oversight. 

Across all domains, AEQUITAS demonstrated adaptability: from numerical data to textual records and medical images, from traditional ML models to generative architectures. This cross-sector validation highlights the framework’s potential as a universal fairness assurance toolkit for high-risk AI systems. 

Technical and Ethical Learnings 
===============================
The project produced several cross-cutting learnings relevant to both developers and policymakers: 

* Fairness is contextual and multidimensional. 

* Fairness cannot be defined solely in statistical terms; it depends on social context, legal norms, and human interpretation. Metrics like CDD and FairRateCDD extended conventional fairness evaluation by conditioning on socio-economic and contextual variables, making fairness measurable within relevant contexts. 

* Data governance is foundational. 

* Across use cases, the greatest source of unfairness originated upstream from, for instance, biased, incomplete, or non-representative datasets. Technical mitigation can only compensate to a point; sustainable fairness requires robust data collection, documentation, and validation processes. 

* Human oversight is not optional. 

* Whether in recruitment, education, or healthcare, AEQUITAS confirmed that human review is essential for ensuring proportionality and accountability. Fairness-by-design implies not just better models but also clear governance protocols, training for users, and monitoring mechanisms to prevent automation bias. 

* Synthetic data is a fairness enabler although the stress testing with polarized data how that synthetic data cannot address all bias issues. 

* Generative models such as diffusion networks improved representation and fairness metrics in under-sampled groups. However, stress testing showed that fairness gains plateau when minority representation falls below a structural threshold (~5% of the dataset). This finding underscores the need for data diversity by design rather than reliance on synthetic augmentation alone. 

* Fairness must extend beyond compliance. 

AEQUITAS moved the fairness debate from compliance to capability-building: enabling organizations to work on the governance, quality, and transparency of (historic) data, and systematically test, reason about, and document fairness decisions throughout the AI lifecycle. This supports continuous assurance rather than one-off audits. 

Validation of AEQUITAS as a Pre-Regulatory Instrument 
=====================================================
The experiments collectively demonstrated that AEQUITAS functions as a pre-regulatory sandbox: a safe environment for exploring the fairness boundaries of AI systems before deployment. By combining socio-legal and technical analysis, the framework enables: 

* Early identification of potential non-compliance with the AI Act’s fairness and fundamental rights provisions. 

* Iterative testing of mitigation strategies in controlled conditions. 

* Generation of traceable documentation (datasets, bias reports, fairness logs) ready for conformity assessment. 

* The framework’s modularity also allows alignment with other regulatory and strategic initiatives, including EUSAIR for regulatory sandboxes and IT4LIA AI Factory for fairness testing infrastructures. Integrating AEQUITAS within these ecosystems would ensure sustained operational use beyond the project’s lifetime and accelerate its Technology Readiness Level (TRL) toward adoption by industry and policymakers. 

Overall Impact 
==============
AEQUITAS has provided empirical proof that trustworthy, fair, and legally aligned AI is achievable through a multi-layer methodology that bridges ethics, law, and engineering. 

Its main impacts include: 

* A validated fairness assurance framework that covers the entire AI lifecycle. 

* A library of tested metrics and mitigation techniques applicable across sectors. 

* A set of real-world use cases serving as reference implementations for regulatory sandboxes. 

* A demonstrated link between AI fairness and societal fairness, connecting algorithmic metrics to social equity outcomes. 

Through these achievements, AEQUITAS established itself as a cornerstone for the European vision of Human-Centric AI: an approach that not only mitigates harm but actively advances justice, accountability, and inclusion in algorithmic systems. 

The AEQUITAS project has shown that fairness is not an abstract or unattainable goal but an actionable engineering and governance task. By embedding fairness considerations into every stage of AI design, from data governance to socio-technical deployment, AEQUITAS has turned compliance into capability and ethics into infrastructure. The validation across six use cases demonstrated that fairness can be tested, quantified, and improved without sacrificing performance, provided that it is framed as a cross-disciplinary responsibility shared by developers, policymakers, civil society organizations, activists, and domain experts.  

AEQUITAS thus leaves behind not only a validated framework but also a methodological legacy: a blueprint for how Europe can operationalize the principles of trustworthy AI through practical, evidence-based, and context-aware innovation. 

Conclusions
***********
The validation activities conducted across six use cases have confirmed the effectiveness, flexibility, and cross-domain applicability of the AEQUITAS Framework as a practical instrument for implementing fairness-by-design in Artificial Intelligence. By integrating ethical, legal, socio-technical, and technical perspectives, AEQUITAS demonstrated that fairness can be transformed from an abstract principle into a measurable and auditable socio-technical engineering process. 

Through the combined use of Fair-by-Design methodologies (TAIRA, FRIA, PSSA, FMM, FDCGM), Information Flow Modelling (IFM), and the Controlled Experimentation Environment, AEQUITAS provided a structured path for identifying, analyzing, and mitigating bias throughout the AI lifecycle. This multidisciplinary approach proved essential in addressing both algorithmic and systemic unfairness, ensuring alignment with the EU AI Act, the Charter of Fundamental Rights, and broader societal expectations of transparency and accountability. 

Across all domains —Human Resources, Social, and Healthcare— AEQUITAS demonstrated that fairness is achievable without compromising performance. The experiments confirmed that responsible data governance, contextual fairness metrics, and targeted mitigation strategies can significantly reduce discrimination while maintaining model accuracy and trustworthiness. Moreover, the use of synthetic data generation and stress testing established new frontiers for fairness assessment, revealing both the potential and the boundaries of algorithmic mitigation. 

The project also validated AEQUITAS as a pre-regulatory sandbox, providing organizations with a controlled environment to test compliance, document fairness decisions, and build readiness for future conformity assessments under the AI Act. 

In conclusion, AEQUITAS has delivered a comprehensive fairness assurance framework that unites theory and practice. It leaves a methodological legacy for Europe’s vision of trustworthy, human-centric AI—one that embeds fairness into the very architecture of technology design. By turning ethical principles into actionable tools, AEQUITAS provides a blueprint for building AI systems that are not only intelligent but also just, transparent, and aligned with fundamental human values. 