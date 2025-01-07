Use Cases
#########

Domain: Recruitment
********************

Use case HR1: Bias-free recruiting system
=========================================

.. note::
   This is a placeholder text based on the (updated) original project proposal.

.. toctree::
   :maxdepth: 2

   usecase-hr1-adecco


Use case HR2: Job-matching recruiting tool
==========================================

.. toctree::
   :maxdepth: 2

   usecase-hr2-akkodis


Domain: Society and economics
*****************************

Use case S1: Identification of child neglect
============================================

.. toctree::
   :maxdepth: 2

   usecase-s1-child-neglect

Use case S2: Disadvantaged students
===================================

.. toctree::
   :maxdepth: 2

   usecase-s2-disadvantaged-students


Domain: Healthcare
******************

Use case HC1: Dermatology
=========================

.. toctree::
   :maxdepth: 2

   usecase-hc1-dermatology


Use case HC2: Synthetic ECG
===========================

.. note::
   This is a placeholder text based on the (updated) original project proposal.

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
