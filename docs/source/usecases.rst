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

The subject of fairness in the hiring process is crucial to guarantee a diverse workforce that evenly represents all demographics. Assessing the absence of biases in a set of data collected from a real-world example, can not only help immediately a company improve their hiring processes and polices, but also create fair sources for future AI training [1]_. Therefore, this use case, by providing a set of data collected during the candidate selection process of a large engineering company in Italy, is aiming to contribute to these objectives, allowing to create a bias free AI assisted recruiting system.

The Akkodis use case focuses on the analysis of the dataset created during the company’s recruitment process. This dataset contains information about all candidates and employees that went through the hiring process, including profiles imported from external databases, such as the ones provided by universities.

The information collected for each candidate includes data related to the candidate’s demographic identity (such as gender and age), geographical location (such as region of residence), if they are part of a protected category according to the state’s laws, work and study background, technical skills, their current status inside the company, and results of the evaluations they received during the hiring process.

This way we are able to represent and analyze the actual state of the profiles taken into consideration by a large engineering company in Italy to evaluate and improve the fairness of the recruitment process in the STEM field.

Use case description
--------------------

The process of finding new candidates in line with the current available positions in the company is complex and involves many steps performed by different professional profiles, spanning from HR representatives, throughout commercial staff (BM), to technical experts.

This process guarantees an efficient selection, evaluating a candidate from different perspectives and taking into consideration their full value as a possible employee.

However, as much as involving different points of view throughout the process can help create a fair environment, it can also lead to an increase in cognitive biases that may manifest in each different step.

By analyzing this dataset, we aim to identify and possibly correct any bias introduced during the hiring process. As it will provide an overview of the data uncovering patterns that may indicate unfairness, such as disparities in candidate evaluation based on gender, age, or other sensitive categories.

The way the dataset is structured (an entry for each step of the candidate’s hiring process) will also provide insights on where these improper patterns are actually occurring in the hiring process, rising awareness on cognitive biases and promoting more objective decision making.

Eventually, our goal is to improve the fairness and inclusivity of the hiring environment, ensuring that all candidates are evaluated based on their skills and potential rather than extraneous factors.

Recruitment Process
^^^^^^^^^^^^^^^^^^^

The Akkodis recruitment process is composed of several phases:

#. Initial phase:

    * Client contacts the company with a specific need.

    * The Commercial staff (the Business Managers team) identify a client's need as an opportunity the company may pursue to increase the technical staff.

#. Requirements analysis:

    * Understand the type of professional roles needed.

#. Search phase:

    * Search for a possible candidate in major search engines and professional social networks such as Monster, LinkedIn, AlmaLaurea (to name a few), as well as the database of spontaneous applications collected on the Akkodis website and internal referrals from colleagues.

    * First round of quick telephone interviews conducted by our HR or recruiters. These interviews aim to determine the candidates' actual availability for an introductory interview.

#. Introductory interview (HR):

    * Interview to determine/confirm the candidate's characteristics, delve into their professional background, and understand their economic aspirations.

#. Technical Interview (Internal Technical Expert):

    * Interview conducted by an internal expert or someone with relevant skills, or an internal resource already allocated at the client's site. Candidates who successfully pass this initial technical evaluation ideally undergo a qualification meeting at the client's site.

#. Qualification Meeting (Client):

    * Second technical evaluation reviewed by the client and usually limited to a small number of candidates. Note that not necessarily both the technical interview and QM take place; often, only the latter is conducted.

#. Hiring phase:

    * The client ultimately determines the suitability of the consultant to be hired.

    * In turnkey projects the QM is absent, and only the technical interview is conducted.

#. Onboarding phase:

    * Set of administrative and technical procedures necessary to prepare the new resource's entry into the company.

Known biases and unfairness
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The primary factor that introduces unfairness in this type of recruitment process is the cognitive bias of the people involved. Cognitive biases can lead to subjective judgments that may exclude valuable candidates due to incorrect preconceived notions about specific demographic groups. These biases can manifest at various stages of the process, from the initial search phase to the final hiring decision.

In particular, as it was observed even in recent studies [2]_,despite the continuous efforts by companies to promote the advantages of a diverse workforce, these types of biases can still present themselves. Taking into account the nature of the data features of the use case’s dataset, the most affected categories are gender, age, country of origin, and protected category. Any of these factors may lead the recruiter to believe that a candidate is more or less fit for a position without considering their actual skills.

By assessing the fairness of the dataset, the company will be able to raise awareness among all stakeholders about the potential for bias and its implications. Additionally, the company will be able to take corrective actions where necessary.

Akkodis Data and Analysis
-------------------------

Data Collection
^^^^^^^^^^^^^^^

As it was described in the previous chapter, the Akkodis dataset [3]_ contains data collected during the company’s recruitment process, precisely from the year 2019 to year 2023.

The data are inserted into the Akkodis system by the TA team when looking for potential candidates. More data relating to a specific candidate is added during each phase of the hiring process to fill in information about the interview’s outcome.

The dataset was then created by exporting in an analyzable format the data present on the Akkodis system.

Dataset Structure and Pre-Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The dataset consists of 40 columns and 21,377 entries.

The data has been carefully anonymized. In particular, the name (and the surname) of each candidate has been replaced with a hash code (ID), and names of previous companies where the candidate worked have been removed. Furthermore, the field Citizenship was removed as it presented a high risk of re-identification.

No other pre-processing steps were applied to data. Further details of the data and analysis can be found here: :ref:`Akkodis`.

.. rubric:: References

.. [1] S. Barocas, M. Hardt and A. Narayanan, "Fairness and Machine Learning: Limitations and Opportunities," MIT Press, 2023, pp. 232-261.

.. [2] C. Calluso and G. Devetag, "Discrimination in the hiring process - state of the art and implications for policymakers," Equality, Diversity and Inclusion: An International Journal, 2024.

.. [3] Akkodis, "Dataset_2.0_Akkodis.xlsx," Aequitas Consortium Repository, Available under permission, 2024.



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

Method
------

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
