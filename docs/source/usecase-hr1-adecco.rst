Context
============================
This case study is based on the analysis of specific an existing software used in the Adecco Group for the outsourcing of candidates, particularly those related to Adecco Formazione. The software in use at the Adecco Group covers the recruiting process from the collection of job applications to the screening through an automatized extraction of suitable candidates’ profiles that are then analysed in person by the recruiters and eventually outsourced at the relevant companies. Throughout the software, it is possible to access a dataset in the form of aggregated data, selected over a specific period of time (i.e., one year) with age, gender, geographic location, education and other characteristics of candidates and the job matching proposed by the software and the selection performed by the human.

Goal
============================
The aim of this case study is to target the cognitive and structural bias that might be associated with existing assisted hiring systems. The analysis of the tool will make it possible to detect and assess possible biased outcomes resulting from the algorithm/software and the human expert in the selection of candidates.

Known biases and unfairness
-------------------------
In the context of the Adecco Group's use of automated recruiting software, particularly for Adecco Formazione, several biases and potential unfairness may arise. First, algorithmic bias can occur if the training data embedded in the software system is not representative of the diverse applicant pool, leading to skewed selection processes that favor certain demographics over others based on age, gender, geographic location, and educational background. Additionally, if the software disproportionately recommends candidates from specific regions or with certain educational credentials, it may inadvertently marginalize equally or more qualified candidates from other backgrounds.

Method
============================

AEQUITAS assessed the algorithm already in use for candidate selection. The algorithm assessment can be run both with synthetic data (suitably generated through the synthesizer of Task. 7.2) and through real data from Adecco Group (once possibly corrected by bias). The dimensions to be validated are 1) diagnosis of bias in algorithms 2) their reparation if needed. Further validation is related to the bias that may exist in the interpretation of results Accordingly, the algorithm outputs will be analysed in relation to the human decision to proceed with this validation.

ADECCO Data and Analysis
-------------------------

Data Collection
^^^^^^^^^^^^^^^

Dataset Structure and Pre-Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Experimentation and results
-------------------------
Experiments conducted within the AEQUITAS framework and experimentation environment, leading to the best solution for ADECCO, can be found at the following links.

* `Preliminary Analysis <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Data_Analysis.pdf>`_

* `Data Pre-processing <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_preprocessing.pdf?rev=1.1>`_

* `Synthetic Data Generation via LLMs <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Synthetic_Data_Gen_Langchain.pdf?rev=1.1>`_

* `Bias Detection <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Bias_Detection.pdf>`_

* `Bias Mitigation <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Bias_Mitigation.pdf>`_

* `Bias Full Experimentation Pipeline within AEQUITAS <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ADECCO_Full_Experimentation_Pipeline.pdf>`_
