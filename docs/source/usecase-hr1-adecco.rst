Context
============================
This case study analyzes a specific software used by the Adecco Group in the candidate selection process. The software supports the recruitment process by recommending the best candidates for a given job position and, conversely, suggesting the most suitable positions for candidates.

At the core of the software is a recommendation engine powered by AI, which extracts relevant information from candidates’ resumes and standardizes it against structured data stored in the internal database. By comparing the candidates' attributes with the requirements of the job position, the software generates a ranked list of candidates based on their compatibility. The results are then presented to the recruiter.

Following this, the shortlisted candidates are personally evaluated by the recruiters and, if deemed suitable, proposed to the relevant companies.

Additionally, the software provides access to a dataset composed of anonymized data, collected over a specific period (e.g., a snapshot of a single day’s operation). This dataset includes the matches proposed by the software, enriched with candidates’ information such as age, gender, geographic location, education, and the specific job positions requirements.

Goal
============================
The aim of this case study is to target the cognitive and structural bias that might be associated with existing assisted hiring systems. The analysis of the tool will make it possible to detect and assess possible biased outcomes resulting from the algorithm/software and the human expert in the selection of candidates.

Known biases and unfairness
---------------------------
In the context of the Adecco Group's use of automated recruiting software, particularly for Adecco Formazione, several biases and potential unfairness may arise. First, algorithmic bias can occur if the training data embedded in the software system is not representative of the diverse applicant pool, leading to skewed selection processes that favor certain demographics over others based on age, gender, geographic location, and educational background. Additionally, if the software disproportionately recommends candidates from specific regions or with certain educational credentials, it may inadvertently marginalize equally or more qualified candidates from other backgrounds.

Method
============================

AEQUITAS assessed the algorithm already in use for candidate selection. The algorithm assessment can be run both with synthetic data (suitably generated through the synthesizer of Task. 7.2) and through real data from Adecco Group (once possibly corrected by bias). The dimensions to be validated are 1) diagnosis of bias in algorithms 2) their reparation if needed. Further validation is related to the bias that may exist in the interpretation of results Accordingly, the algorithm outputs will be analysed in relation to the human decision to proceed with this validation.

ADECCO Data and Analysis
------------------------

Data Collection
^^^^^^^^^^^^^^^
The two datasets come from two matching algorithms: direct matching versus reverse matching.
The direct matching dataset contains the best 10 candidates for each job position.
The data are sorted by candidate identifier asc and match score desc.

The reverse matching dataset contains the best 5 offers (job positions published on Adecco website)
and the best 5 orders (job position managed internally without publishing on Adecco website) for each candidate.
The data are sorted by job identifier asc and match score desc.
Note that match rank is calculated for each job position type (orders vs offers).

Experimentation and results
-------------------------
Experiments conducted within the AEQUITAS framework and experimentation environment, leading to the best solution for ADECCO, can be found at the following links.

* `Preliminary Analysis <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Data_Analysis.pdf>`_

* `Data Pre-processing <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_preprocessing.pdf?rev=1.1>`_

* `Synthetic Data Generation via LLMs <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Synthetic_Data_Gen_Langchain.pdf?rev=1.1>`_

* `Bias Detection <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Bias_Detection.pdf>`_

* `Bias Mitigation <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Bias_Mitigation.pdf>`_
