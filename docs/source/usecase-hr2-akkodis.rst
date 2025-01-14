Context
============================

The subject of fairness in the hiring process is crucial to guarantee a diverse workforce that evenly represents all demographics. Assessing the absence of biases in a set of data collected from a real-world example, can not only help immediately a company improve their hiring processes and polices, but also create fair sources for future AI training [1]_. Therefore, this use case, by providing a set of data collected during the candidate selection process of a large engineering company in Italy, is aiming to contribute to these objectives, allowing to create a bias free AI assisted recruiting system.

The Akkodis use case focuses on the analysis of the dataset created during the company’s recruitment process. This dataset contains information about all candidates and employees that went through the hiring process, including profiles imported from external databases, such as the ones provided by universities.

The information collected for each candidate includes data related to the candidate’s demographic identity (such as gender and age), geographical location (such as region of residence), if they are part of a protected category according to the state’s laws, work and study background, technical skills, their current status inside the company, and results of the evaluations they received during the hiring process.

This way we are able to represent and analyze the actual state of the profiles taken into consideration by a large engineering company in Italy to evaluate and improve the fairness of the recruitment process in the STEM field.

Goal
============================

The process of finding new candidates in line with the current available positions in the company is complex and involves many steps performed by different professional profiles, spanning from HR representatives, throughout commercial staff (BM), to technical experts.

This process guarantees an efficient selection, evaluating a candidate from different perspectives and taking into consideration their full value as a possible employee.

However, as much as involving different points of view throughout the process can help create a fair environment, it can also lead to an increase in cognitive biases that may manifest in each different step.

By analyzing this dataset, we aim to identify and possibly correct any bias introduced during the hiring process. As it will provide an overview of the data uncovering patterns that may indicate unfairness, such as disparities in candidate evaluation based on gender, age, or other sensitive categories.

The way the dataset is structured (an entry for each step of the candidate’s hiring process) will also provide insights on where these improper patterns are actually occurring in the hiring process, rising awareness on cognitive biases and promoting more objective decision making.

Eventually, our goal is to improve the fairness and inclusivity of the hiring environment, ensuring that all candidates are evaluated based on their skills and potential rather than extraneous factors.

Recruitment Process
-------------------------

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
-------------------------

The primary factor that introduces unfairness in this type of recruitment process is the cognitive bias of the people involved. Cognitive biases can lead to subjective judgments that may exclude valuable candidates due to incorrect preconceived notions about specific demographic groups. These biases can manifest at various stages of the process, from the initial search phase to the final hiring decision.

In particular, as it was observed even in recent studies [2]_,despite the continuous efforts by companies to promote the advantages of a diverse workforce, these types of biases can still present themselves. Taking into account the nature of the data features of the use case’s dataset, the most affected categories are gender, age, country of origin, and protected category. Any of these factors may lead the recruiter to believe that a candidate is more or less fit for a position without considering their actual skills.

By assessing the fairness of the dataset, the company will be able to raise awareness among all stakeholders about the potential for bias and its implications. Additionally, the company will be able to take corrective actions where necessary.

Method
============================

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

Experimentation and results
-------------------------
Experiments conducted within the AEQUITAS framework and experimentation environment, leading to the best solution for AKKODIS, can be found here.


.. rubric:: References

.. [1] S. Barocas, M. Hardt and A. Narayanan, "Fairness and Machine Learning: Limitations and Opportunities," MIT Press, 2023, pp. 232-261.

.. [2] C. Calluso and G. Devetag, "Discrimination in the hiring process - state of the art and implications for policymakers," Equality, Diversity and Inclusion: An International Journal, 2024.

.. [3] Akkodis, "Dataset_2.0_Akkodis.xlsx," Aequitas Consortium Repository, Available under permission, 2024.
