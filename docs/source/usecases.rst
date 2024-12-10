Use Cases
#########

Domain Recruitment
******************

* Use case name
* general description and introduction
* Dataset description & analysis
* Results

Bias-free recruiting system
===========================


Job-matching recruiting tool
============================

.. toctree::
   :maxdepth: 3

   usecase-hr2-akkodis


Domain Society and economics
****************************

Identification of child neglect
===============================

Context
-------

In the last decades, child abuse and neglect have seen soaring numbers. The broad adoption of electronic health records in clinical settings offers a new avenue for addressing this. Detecting and assessing risks of child abuse and neglect within hospital settings could prevent and reduce bias against ethnic and socioeconomic disadvantaged communities as well as raise the overall safety of children. There are two main factors that guide a doctor during the diagnosis: 1) the visit 2) the medical history (anamnesis). In the case of pediatric patients, the latter is even more delicate as it is the parent who interprets and reports the child's disease and represents the. child's rights. Furthermore, today's reality of migration flows and increasingly deficient parenting are the norms, make anamnesis ever more complex: language barriers, parenting skills, cultural differences all become accelerators of bias insertion in the entire process. It should also be noted that, in this process, the parent often uses many strategies of mystification, to avoid being seen as a potential abuser. Thus, hospitals' processes currently rely mainly on experts as cultural mediators for dealing with potential child abuse, who are not continuously available at the hospital, contributing to delays in diagnosis, affecting children and parents and elevating overall costs. An AI decision support system can only give concrete, effective and rapid help, if fair outcomes compliant with EGTAI are produced.

Goal
----

To develop an innovative AI system following AEQUITAS methodologies to detect and assess risk for child abuse and neglect within hospital settings, prioritizing the prevention and reduction of bias against ethnic and socioeconomic disadvantaged communities. The possibility of racial bias in AI systems reinforces our challenge of addressing racism through an AI system and finding the optimal form of human-machine collaboration.
.. toctree::
   :maxdepth: 3

Method
------
   usecase-s2-disadvantaged-students

Data from the AOUBO pediatric emergency room management system will be used to design a new AI system to support doctors in identifying "at-risk" cases given a specific medical history. This case study will benefit from the AEQUITAS socio-technical approach of including and assessing the often disadvantaged background of children and their parent(s). Being aware that the accompanying parent is in the vast majority of cases the mother that might be without a driving license, living in less serviced urban areas, or – in some cases – in need of her husband’s permission to move autonomously, is fundamental to have a full picture of the patient. This is a typical case where intersectionality does play a role as gender and race lines of inequality interact and multiply possible negative discriminatory effects. This relevant socio-economic background is crucial in 2 directions: 1. It is relevant when designing and developing the AI system in support of doctors’ decisions because it adds a novel layer of information upon which the decision is made and 2. It is relevant to doctors’ evaluation of the possible protocols. The technical solutions will avoid the risk of repeating, amplifying and contributing to gender stereotypes in the overall evaluation of patient history. The case study develop a predictive system from scratch, following methodologies and techniques (WP5) and comparing its results with those suggested by human experts to assess their fairness.

Domain: Healthcare
******************

* Use case name
* general description and introduction
* Dataset description & analysis
* Results

Dermatology
===========

Synthetic ECG
=============

Context
-------
Electrocardiograms (ECG) are the gold-standard in medicine for an overall and finegrained assessment of the condition of the heart. The deflections in the so-called PQRST complex that represents a single heartbeat are connected to the sequence of contractions of the heart muscle. Deviations in those deflections are directly tied to cardiovascular diseases like (ventricular) arrhythmia, myocarditis, myocardial fibrosis, or even inherited or acquired defects. Classification of ECG traces as symptomatic or normal is typically done by experts. AI Algorithms trained on existing data can be used to automate this process. However, these training data may suffer from various forms of bias which in turn are entrained into the resulting AI algorithm.
To prevent that the algorithm disadvantages particular groups by generating false positives or false negatives, we propose to investigate if and how such AI algorithms are affected by bias. To this end, we will determine whether bias exist(ed) in the original data sets and mitigate that bias by generating synthetic non-biased data. Additionally, instead of trying to remove bias from the data, we will try to deliberately introduce bias to determine if the algorithm can handle this bias and generalizes well. Developing methods to generate synthetic ECG data will be part of this process.

Goal
----

To build a bias-aware algorithm for the classification of ECG traces as normal or symptomatic.


Method
------

We will first investigate methods that are suited to generate synthetic ECG data with or without deliberately introduced bias. Once the ECG synthetic data, with one or more deliberately introduced (additional) biases is available, the data will be used to determine whether a Philips proprietary solution is sensitive to bias. This solution evaluates ECG traces to classify, beat by beat, whether the beats are normal or affected by disease. Due to bias in the original training data these evaluations can be biased as well. To this end, PRE will use the Aequitas experimentation platform on premises to validate this use case.
