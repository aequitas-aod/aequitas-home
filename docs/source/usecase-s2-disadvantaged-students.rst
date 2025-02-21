.. _s2-context:

Context
-------

Academic performance in primary school is a good predictor of an individual's future income
and well-being [#]_. Anticipating low academic performance levels is relevant to implementing
corrective policies at early ages, and anticipating high academic performance is also relevant to
applying incentive mechanisms to achieve excellence [#]_.

To achieve this, it is necessary to have good predictive models, in terms of accuracy. However,
it is equally important for these models to generate fair predictions [#]_. This means they should
provide consistent predictions across different groups, ensuring no disparity in awarding
excellence prizes to students regardless of their social background or their parents' educational
levels. To achieve this, it is essential to have models that ensure fairness in their predictions.

This use case exploits an extensive dataset covering students from Las Palmas de Gran Canaria and Santa Cruz de Tenerife provinces, Canary Islands, Spain. This dataset extends beyond basic student information, encompassing data on their families, teachers, and academic achievements. While the raw data primarily consisted of questionnaire responses, we propose a refined dataset that has been preprocessed to ease training AI algorithms specifically designed to address challenging tasks, such as improving student performance and reducing drop-off rates. This focus on educational equality and fairness allows researchers to develop and test AI solutions that promote equal opportunities within the educational system.

The Agencia Canaria de Calidad Universitaria y Evaluación Educativa (ACCUEE)3 is a public institution in the Canary Islands, which aims to monitor the quality of education services in the region. To serve this purpose, it collects data concerning students, curricula, and schools.

Concerning students, collected data includes information on their academic performance in Mathematics, Spanish Language (local native language), and English, plus questionnaire responses from students, families, teachers, and school principals, which attempt to capture the socio-economic and cultural background of the students, as well as the situations of their schools. The data is collected from students in the 3rd and 6th grades of primary education, and in the 4th grade of secondary education. The collection process was repeated over four academic years, from 2015–16 to 2018–19.

We believe the dataset may be exploited to ease the life of students—hence improving the overall quality of the education system. The goal would be to identify the key predictors of academic performance, with a focus on factors that may lead to poor performance or drop-off. Identifying these factors is a fundamental step towards developing interventions that can help students in need— hence promoting fair access to education and ultimately enhancing student success. Intervention here may include: personalized academic support such as tutoring and mentoring, academic counselling to help students develop effective study habits, allocation of essential educational resources on a per-need basis, remedial coursework or enrichment programs to strengthen skills.

.. _s2-goal:

Goal
----
To link the outcomes of predictive models and their degree of bias to the socioeconomic concept of inequality of opportunities [#]_ reflected in the data and real life. Inequality of opportunity in educational achievement is measured as the inequality that is explained by factors that are beyond the control of the individual, such as the socioeconomic status of the parents, the cultural environment at home, the immigrant status, the state of health at birth, the neighborhood of birth, etc. (in the terminology of the AI-fairness literature these are the sensitive variables).

In particular, we analyze how the existence of certain sensitive variables (referred to as
circumstances in economics) that explain a relevant percentage of the inequality in educational
achievement are the cause of generating unfair predictions, as long as they influence the predictive
models directly or indirectly (i.e., through other predictors).

.. _s2-known:

Known biases and unfairness
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Halo Effect**: From teachers towards students, inferring skills, abilities, or attributes of a person based on a first impression (e.g., socioeconomic background, race, gender, etc.). Specifically, when marking is based on behaviours or characteristics of a student unrelated to the elements to be assessed within a subject.

#. **Confirmation Bias**: Both by teachers and students. The tendency to give rigor and truthfulness to data, ideas, or reasoning that align with what we believe to be true. Conversely, ignoring data, ideas, or explanations that cast doubt on our beliefs.

#. **Status Quo Bias**: Resistance to educational innovation by teachers. Preferring the environment and situation to remain stable. More value is placed on potential losses from change or innovation than on potential future gains.

#. **Sampling Bias**: Some specific students could not attend to school the day of the assessments, or they do not answer the questionnaires. Usually, these students come from more disadvantaged contexts, implying samples with underrepresentation of lower-class households or low performer students.

#. **Selection Bias**: Students and teachers are not randomly assigned to schools. Conversely, more motivated parents and teachers select better schools, generating self-selection problems (endogeneity). Then, schools’ value-added can be biased because better performance can be driven by the presence of better students and teachers.

.. _s2-method:

Method
------

.. _s2-data:

Data Collection
^^^^^^^^^^^^^^^
The raw data collected by the ACCUEE comes in tabular form. The table comes with 83,857 rows and 554 columns. Each row refers to a single student at a given grade and academic year. Primary education data for the A.Y. 2015–16 and 2018–19 is gathered through a comprehensive census over the entire population. For other grades and academic years, the data is collected through sampling. Longitudinal data is also included: students in 3rd grade (primary school) during A.Y. 2015–16 are sampled again in their 6th grade.

The columns of the table represent relevant features collected for each student. Overall, the 555 columns represent features from six categories: (i) identifiers (8 columns): various sorts of identifiers involving the student (e.g., at the school or ACCUEE level), and their academic situation (school, grade, academic year); (ii) performance features (6 columns), containing the student’s scores in Mathematics, Spanish Language, and English; (iii) students’ answers (154 columns) to a questionnaire concerning their own experiences with the school system (including but not limited to their access to resources, their relationship with teachers, their satisfaction level, etc.); (iv) principals’ answers (138 columns) to a questionnaire concerning the school the student is enrolled into; (v) families’ answers (91 columns) to a questionnaire concerning the socio-economic conditions of the student; (vi) teachers’ answers (158 columns) to a questionnaire concerning their workload, satisfaction, and methodology.

Questionnaires were standardized; consequently, the features obtained from them are either categorical or numerical. However, the data is not clean as missing values are present, and they are not evenly distributed across the features. Given the high dimensionality of the dataset, preprocessing is necessary to make it more manageable and suitable for the tasks we intend to address.

Dataset Structure and Pre-Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The dataset has been released and is publicly available, increasing the fairness benchmarks in the field. It can be found here: https://zenodo.org/records/11171863.

For more information about the data and preprocessing, see https://zenodo.org/records/11171863 and https://ceur-ws.org/Vol-3808/paper17.pdf.


.. _s2-exp:

Experimentation and results
---------------------------
Experiments conducted within the AEQUITAS framework and experimentation environment, leading to the best solution for ULL, can be found here:

* `Preliminary Analysis <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ULL-Preliminary%20Analysis.pdf?rev=1.1>`_

* `Pre-processing Mitigation <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ULL-Pre-processing%20Mitigation.pdf?rev=1.1>`_

* `In-processing Mitigation <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/ULL-In-processing%20Mitigation.pdf?rev=1.1>`_

.. rubric:: References

.. [#] Diener, E., Diener, M., & Diener, C. (1995). Factors predicting the subjective well-being of nations. Journal of personality and social psychology, 69(5), 851.

.. [#] Ladd, H. (Ed.). (2011). Holding schools accountable: Performance-based reform in education. Brookings Institution Press.

.. [#] Yu, R., Li, Q., Fischer, C., Doroudi, S., & Xu, D. (2020). Towards Accurate and Fair Prediction of College Success: Evaluating Different Sources of Student Data. International educational data mining society.

.. [#] Sewell, W. H. (1971). Inequality of opportunity for higher education. American Sociological Review, 36(5), 793-809.
