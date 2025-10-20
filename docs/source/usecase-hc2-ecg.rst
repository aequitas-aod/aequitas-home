.. _hc2-context:


Introduction and background
---------------------------
Since its discovery and invention in 1902 by Willem Einthoven, the electrocardiogram (ECG or EKG) has become the main staple of any diagnostic procedure in hospitals, whether the suspected diagnosis is directly related to cardiac symptoms or whether other symptoms may be at play. The main benefit of the ECG is that it enables non-invasive recording of the electrical activity of the heart, and visualizing or storing the heart’s beats in a format that can be read and interpreted by trained physicians. 

The interpretation is based on recognizing the various components of the so called PQRST complex that comprises a single heartbeat. The PQRST complex has been called as such ever since Einthoven’s description of the ECG signal. The sequence of waves is directly related to polarization and depolarization of the various structural parts of the heart and their role and position in the sequence of a single heartbeat. For instance, the R-wave is the largest because it represents the depolarization of all ventricles. Given its size it is easiest to detect and is typically used to determine the interbeat interval (the time between beats as visualized by the RR interval in Figure 1) which in turn is used to compute heart rate as the number of beats per minute. 

Although the general public typically only knows about the typical ECG shape as visualized in Figure 1, clinicians actually (typically) use 12 individual leads (ECG sensors) and track the progression of a specific wave over time across the leads to glean more information to support their diagnostic purpose. For instance, changes in the deflection of the P-wave on leads II and V1 are known to be indicative of hypertrophyError! Bookmark not defined.. 
(NON COMPLETA)

Known biases and unfairness  
~~~~~~~~~~~~~~~~~~~~~~~~~~~
That such relations between (changes in) ECG deflections and symptoms exist for many people is largely due to the DNA homogeneity of the human population: It has been estimated that only 0.1% of our DNA varies2. Despite that homogeneity, it has been observed that ECG morphology, for instance aspects like the duration and voltage of the QRS complex, varies between different ethnic populations3,4. Similarly, there is evidence that ECG abnormalities vary between ethnic populations. For instance, in the US it was observed that people with European ancestry have a higher prevalence of atrial fibrillation5 despite having lower risk factors than underrepresented ethnic groups6. 

Thus, on the one hand, the ECG and symptoms have large commonality over the human population but the ability to algorithmically detect deviations from the norm for certain subpopulations depends, on the other hand, on the availability of such data to train such an algorithm. This applies for the monitoring of ECG to detect these deviations from the norm as well as for diagnostic purposes where algorithms support clinicians in their diagnosis. This situation may result in bias in the monitoring or diagnostic algorithms.  

For instance, it is known that between the genders, considerable differences in cardiac disease exist: women have higher mortality, more symptoms, and higher rates of recurrence after ablation procedures against atrial fibrillation. Women present differently compared to men when suffering from myocardial infarction, and their bodies react to and process medication differently than males do7. When (AI) algorithms are trained on data that, for the majority, is based on measurements on males, such an algorithm may not respond properly to ECG data from women.  

Similarly, with the physiological changes in the body due to ageing, it is known that ECG signals are different between the younger and older population8 but there is a paucity of data from the younger population with a potential effect of biasing AI against younger people. Similar reasoning applies for comorbidities that have been shown to affect the ECG signal to some degree9: It is difficult to capture a sufficient amount of data for all possible combinations of comorbidities and symptomatic ECG traces. 

It is therefore important that (AI) algorithms for monitoring of running ECG and/or diagnosis of symptomatic ECG need to be trained on well-balanced data set ensuring fair and biasfree performance for all intended larger and smaller populations of hospital patients. For that reason, it is important for developers of algorithms for scoring and classifying ECG signals to have a diversity of data available to ensure that their algorithms can be readily used in a diverse range of scenarios without compromising on the efficacy of the algorithm to determine the correct outcome.  

Synthetic ECG
~~~~~~~~~~~~~
One way to deal with bias and unbalance in data is to use synthetic data to complement or replace the original data. For ECG, typically, one of three approaches is used: mathematical modeling, computer-vision techniques, or deep-learning approaches10. For this use case, we have developed a confidential algorithm to generate synthetic ECG traces to support the development of AI algorithms for ECG classification in all aspects. The ECG signal generator can create healthy/normal ECGs for multiple leads and add noise to the signal from a diverse range of sources to represent real-life scenarios involving faulty or misplaced ECG leads. Beyond the normal ECGs, the algorithm can also generate symptomatic ECGs with specific configurations to create signals with a range of type and severity of the symptoms. A sample of these synthetic ECGs has been made available to interested parties in the Aequitas consortium for further analysis. 

Fair-by-Design – Fair Output Interpretation Methodology
-------------------------------------------------------
Methodology Overview
~~~~~~~~~~~~~~~~~~~~
The assessment followed the Fair Output Interpretation Methodology (FOIM), which is grounded in EU AI Act’s Article 14 “Human Oversight”. The aim of FOIM is to have an interdisciplinary and a multi-stakeholder group assess the fairness of the AI system’s outputs within the context it will be used in. FOIM assists AI users and/or deployers in critically assessing the outputs of AI systems before actual deployment to ensure fair implementation. Given that AI systems are developed in diverse environments with various tasks in mind, it is paramount to address the technical, ethical, legal, and social constraints to fairness in AI model outputs.   

This methodology was tested in a workshop using the AEQUITAS use case of bias-aware prediction of ICU healthcare outcomes. The AI system predicts in-hospital mortality and ICU length of stay based on continuously monitored patient data, producing a score that informs clinical decision-making. The MIMIC-III dataset comprised over 53,000 ICU admissions from a Boston hospital between 2001 and 2012.  As the system has not yet been developed, the workshop used fictional scenarios based on assumed inputs and outputs. Participants evaluated these hypothetical cases to identify potentially biased outcomes, mirroring the kind of human oversight required in real clinical settings. The full report findings can be found in Appendix F.1. 

Key Findings
~~~~~~~~~~~~

Purpose identification 
^^^^^^^^^^^^^^^^^^^^^^
The AI use case was found to be a single and predictive purpose AI system, with the intended purposes of informing decisions, calculating a score, and ranking within the context of mortality and ICU stay for critical patients. 

Data Source & Representation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The MIMIC-III dataset was found to be unfit for the intended EU context due to its U.S. origin, limited ethnic representation, and healthcare-specific biases (e.g. practices linked to insurance incentives). These issues raised concerns about data representativeness and the risk of discriminatory outcomes if left unaddressed. 

Outcome evaluation
^^^^^^^^^^^^^^^^^^
To assess the success of the system’s outcomes, participants recommended evaluating its impact on diverse population groups. They proposed using a matrix that integrates social, legal, and medical perspectives into outcome evaluation. Trust by doctors was suggested as a possible success indicator, though it could be subjective. Transparency and user agency were also emphasised. Furthermore, when assessing whether historical or other forms of bias had been identified and addressed in the system’s design, it was found that historical biases had not been considered. Participants also flagged the absence of control features (e.g. a ‘stop’ function), concluding that deployment would be premature without these safeguards in place. 

Assessment of FOIM 
~~~~~~~~~~~~~~~~~~
The methodology was effective in assessing output fairness and aligned well with Article 14 of the EU AI Act, though several sections require clearer phrasing and refinement. Questions on Mode Confusion Bias were difficult to answer and should be further clarified. he Dunning-Kruger section raised concerns about sensitivity and potential defensiveness among doctors, suggesting a need for more careful wording to maintain engagement. Furthermore, clarification on Question 2 in terms of which experts were consulted could yield more insight into output interpretation. 


.. rubric:: References

.. [#] https://ecgwaves.com/topic/ecg-normal-p-wave-qrs-complex-st-segment-t-wave-j-point/

.. [#] L. B. Jorde, S. P. Wooding, Genetic variation, classification and ‘race’, Nature Genetics 36 (2004) S28–S33.

.. [#] I. A. Mansi, I. S. Nash, Ethnic differences in electrocardiographic intervals and axes, Journal of Electrocardiology 34 (2001) 303–307.doi:10.1054/jelc.2001.27453.

.. [#] E. W. Hancock, B. J. Deal, D. M. Mirvis, P. Okin, P. Kligfield, L. S. Gettes, Aha/accf/hrs recommendations for the standardization and interpretation of the electrocardiogram: Part v: Electrocardiogram changes associated with cardiac chamber hypertrophy: A scientific statement from the american heart association electrocardiography and arrhythmias committee, council on clinical cardiology; the american college of cardiology foundation; and the heart rhythm society, Circulation 119 (3 2009). doi:10.1161/CIRCULATIONAHA.108.191097.

.. [#] K. Hebert, H. C. Quevedo, L. Tamariz, A. Dias, D. L. Steen, R. A. Colombo, E. Franco, S. Neistein, L. M. Arcement, Prevalence of conduction’abnormalities in a systolic heart failure population by race, ethnicity, and gender, Ann Noninvasive Electrocardiol 17 (2012) 113–122.

.. [#] U. R. Essien, J. Kornej, A. E. Johnson, L. B. Schulson, E. J. Benjamin, J. W. Magnani, Social determinants of atrial fibrillation, Nature Reviews Cardiology 18 (2021) 763–773. doi:10.1038/s41569-021-00561-0.

.. [#] M. J. Legato, P. A. Johnshon, J. E. Manson, Consideration of sex differences in medicine to improve health care and patient outcomes. JAMA (2016) E1-E2.

.. [#] http://doi.org/10.1515/JBCPP.2011.017.

.. [#] https://pmc.ncbi.nlm.nih.gov/articles/PMC9267325/.

.. [#] https://www.sciencedirect.com/science/article/pii/S0010482524015385.
