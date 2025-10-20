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
   * - :doc:`HR1 <usecase-hr1-adecco>`
     - Adecco
     - FDCGM + LLM Assessment
     - Fairness in CV screening & job matching
   * - :doc:`HR2 <usecase-hr2-akkodis>`
     - Akkodis
     - FDCGM + IFM + FaUCI
     - Fairness in AI-assisted recruitment
   * - :doc:`S1 <usecase-s1-child-neglect>`
     - IRCCS
     - PSSA + LLM-based Rule Extraction
     - Trustworthy AI for child neglect detection
   * - :doc:`S2 <usecase-s2-disadvantaged-students>`
     - Univ. of La Laguna
     - TAIRA + FRIA
     - Fairness in student performance prediction
   * - :doc:`HC1 <usecase-hc1-dermatology>`
     - IRCCS
     - FMM + Synthetic Data
     - Fairness in dermatological image diagnosis
   * - :doc:`HC2 <usecase-hc2-ecg>`
     - PRE
     - FOIM + Synthetic ECG
     - Fairness in biomedical signal interpretation

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



