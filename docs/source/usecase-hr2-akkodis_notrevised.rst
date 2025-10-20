.. _hr2-context:

Introduction and background
---------------------------

The Akkodis use case focuses on the analysis of the dataset created during the company’s recruitment process. This dataset contains information about all candidates and employees who went through the hiring process, including profiles imported from external databases, such as the ones provided by universities.  

The information collected for each candidate includes data related to the candidate’s demographic identity (such as gender and age), geographical location (such as region of residence), if they are part of a protected category according to the state’s laws, work and study background, technical skills, their current status inside the company, and results of the evaluations they received during the hiring process.   

This way we are able to represent and analyze the actual state of the profiles taken into consideration by a large engineering company in Italy to evaluate and improve the fairness of the recruitment process in the STEM field. 

The process of finding new candidates to fill current available positions in the company is complex and involves multiple steps performed by different professional profiles, spanning from HR representatives to commercial staff (BM) and technical experts.  

This process guarantees an efficient selection, evaluating a candidate from different perspectives and taking into consideration their full value as a possible employee. 

However, as much as involving different points of view throughout the process can help create a fair environment, it can also lead to an increase in cognitive biases that may manifest in each different step. 

By analyzing this dataset, we aim to identify and possibly correct any bias introduced during the hiring process. As it will provide an overview of the data uncovering patterns that may indicate unfairness, such as disparities in candidate evaluation based on gender, age, or other sensitive categories. 

The way the dataset is structured (an entry for each step of the candidate’s hiring process) will also provide insights on where these improper patterns are actually occurring in the hiring process, rising awareness on cognitive biases and promoting more objective decision making. 

Eventually, our goal is to improve the fairness and inclusivity of the hiring environment, ensuring that all candidates are evaluated based on their skills and potential rather than extraneous factors. 

.. _hr2-senstive features:

Sensitive features
~~~~~~~~~~~~~~~~~~

In the context of AI fairness, it is crucial to identify and understand sensitive features within a dataset that may lead to biased outcomes or discrimination against certain groups. Some of the features in the AKKODIS dataset are included in this category. 

Below are listed the sensitive features present in the dataset: 

* **Age Range**: Age can be a sensitive factor as it may lead to age discrimination. 

* **Sex**: Gender identification is a critical sensitive feature that can influence hiring decisions and outcomes. 

* **Protected Category**: This explicitly indicates whether a candidate falls into a legally protected category, which is essential for fairness considerations. 

* **Residence**: The candidate's place of residence may introduce biases based on geographic location or socioeconomic status. 

* **Other Sensitive Features**: In addition to the above, there are other sensitive features not explicitly listed in the dataset that could impact biases. These might include factors such as ethnicity, disability status, educational background, and socioeconomic indicators. It is important to consider these additional features, as they can also contribute to systemic biases in hiring and affect the overall fairness of the recruitment process. 

These features should be closely monitored and analyzed to mitigate any potential biases in the AI systems used for recruitment, ensuring a fair and equitable hiring process. 

Known biases and unfairness  
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we look at our recruitment database, it’s clear that cognitive biases are affecting our hiring process, and we need to think about the ethical issues this raises for both candidates and our organization. 

* **Cognitive Bias in Evaluation**: We’ve noticed that the people involved in hiring often have different views, which can lead to inconsistent evaluations of candidates. For example, if our evaluators have unconscious biases that favor male candidates, this can put equally qualified female candidates at a disadvantage. Research shows that women in STEM fields often face these kinds of biases, which can impact their evaluations and hiring results. 

For instance, our data shows that male candidates tend to get higher scores in technical assessments, even when their qualifications are similar to those of female candidates. This suggests that there may be a bias in how evaluators see male versus female candidates, which could limit our efforts to create a diverse workforce and reinforce gender imbalances in our organization. 

* **Fairness in Decision-Making**: It’s important for us to ensure fairness in our AI-driven recruitment. Our project will look at how different factors, like candidate demographics and evaluation criteria, can lead to biased outcomes. For example, if age is a big factor in our hiring decisions, it might unfairly disadvantage younger or older candidates, which would reduce the diversity of our workforce. 

* **Transparency and Accountability**: To build trust with candidates and ensure accountability in our hiring practices, we need to be clear about how we identify and address biases in our recruitment process. By documenting our evaluation methods and sharing what we learn from our data analysis, we can create a culture of transparency and accountability. This is in line with the principles of the Aequitas project, which focuses on fairness in hiring. 

.. _hr2-context:

Fair-by-Design – Fair Data Collection, Governance and Management methodology 
----------------------------------------------------------------------------

Methodology Overview
~~~~~~~~~~~~~~~~~~~~

The Fair Data Governance and Management Methodology was developed to assess datasets used in high-risk AI systems in regard to fairness, representativeness, and compliance with the EU AI Act. This methodology translates legal obligations from the AI Act into practical, structured questions designed to guide multi-stakeholder assessments of training, testing, and validation datasets. It consists of two parts: 

Dataset level assessment: Overview of the entire dataset 

Data features level assessment: Evaluation of specific data features, conducted in three sub-parts: (a) identifying relevant information, (b) assessing potential bias/unfairness, and (c) documenting findings and proposing mitigations. 

The methodology was tested across three working sessions in collaboration with a hiring company using an AI tool to match candidates to job roles. The dataset comprised candidate information accumulated over five years from various sources. Participants were drawn from technical, legal, and socio-technical backgrounds and contributed to the evaluation through guided exercises and open discussion. The full report of the workshop can be found in Appendix B.2 while the key findings and methodological validation are summarised below. 

.. _hr2-method:

Key Findings
~~~~~~~~~~~~

Session 1: Dataset Overview and Scoping 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The session revealed that the dataset was not originally designed for AI system training but repurposed from historical recruitment records. This raised concerns about relevance, representativeness, and compliance with Article 10.2(d) of the AI Act. 

Participants identified inconsistent data collection practices and variability in mandatory fields, especially across national contexts. 

Subjective traits (e.g. "dynamism", "maturity") were inconsistently assessed using different scales, introducing non-uniform evaluation standards. Participants highlighted fairness concerns related to this inconsistency and to the potential amplification of location-based and gender biases. 

Statistical representation emerged as a central issue, especially around whether datasets should mirror existing labour market inequalities or aim to correct them. Participants diverged on the inclusion of protected characteristics. Some saw it as necessary for mitigating bias, while others warned of reinforcing stereotypes. 

Error handling practices revealed a tendency toward data maximisation (using as much data as possible) rather than data optimisation (using the right data), and the dataset included duplicates that inflated perceived volume and introduced systemic bias. 

Session 2: Feature Level Analysis
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Session 2 involved assessing two features "sex” and "candidate state". Overall, participants found that some legal concepts (e.g. Article 10.4’s “geographical, contextual, behavioural, or functional settings”) were difficult to apply at the feature level. Evaluating such criteria at the dataset level was seen as more appropriate. Terminological ambiguity in the AI Act hindered granular analysis. The results from the feature analysis were as follows: 

Part A: Sex  

Relevance: Debates echoed previous sessions. Some saw “sex” as essential for measuring bias; others argued it was irrelevant and posed legal risks. No consensus emerged, but all agreed its inclusion must be justified by the system’s purpose. 

Scale: The binary male/female classification was found to be exclusionary and potentially discriminatory. 

Volume: The dataset contained 22% female and 78% male entries, a distribution likely to introduce bias. 

Type of Data Feature: Recognized as both special-category data under the GDPR and a protected characteristic under the ECFR, "sex" poses direct fairness and legality concerns. 

Statistical Properties and Representativeness: Participants disagreed on whether to mirror real labor demographics or promote balanced representation (e.g. 50/50 gender split). The idea of using synthetic data was proposed but left unresolved. The issue of distribution shift was also flagged in relation to cross-border deployment. 

Part B: Candidate State 

Relevance: Participants agreed it was legally and functionally appropriate, as it served as the AI tool’s target variable. However, the binary label (“hired” vs. “not hired”) excluded candidates still in process and risked introducing inaccuracy. 

 

Session 3: Feature Level Analysis 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Session 3 continued and finished the evaluation of the "candidate state" feature.  The feature "dynamism" was also assessed. 

Part B: Candidate State  

Relevance: Though relevant, “candidate state” was flagged as a potential proxy for bias. If correlated with demographic data, it could reveal discriminatory patterns or even compromise anonymity. Some suggested it should not be used as a target variable. 

Volume: The dataset’s high dimensionality combined with medium volume raised concerns about model robustness. 

Statistical Properties and Representativeness: The distribution showed most hired candidates were Italian, with very few from countries like Egypt or Morocco, suggesting systemic exclusion risks. 

Part C: Dynamism: 

Relevance: Participants disagreed on how and when “dynamism” was measured. While it could help match candidate profiles to roles, its subjectivity and collection method (interview-based ratings) posed serious fairness concerns. 

Proxy for Bias: As with “sex,” dynamism was flagged as a potential carrier of gender and cultural stereotypes, e.g. assumptions that men are more dynamic. Participants warned of the risks in clients using arbitrary trait thresholds (e.g. “must have a dynamism score of 4”). 

Statistical Properties and Representativeness: Many entries lacked dynamism scores, reinforcing concerns about sampling inconsistencies raised in Session 1. 

Assessment of FDCGM 
~~~~~~~~~~~~~~~~~~~


Participants identified several areas of improvement. Firstly, there was a need for greater clarity in translating complex legal concepts from the EU AI Act into practical and implementable principles, as many participants lacked the legal background to interpret the mandates. Secondly, several questions designed for individual data features were better suited to dataset-level analysis. Terminology from the AI Act (e.g., “appropriate statistical properties”) was seen as too abstract and difficult to translate into actionable evaluation criteria. Additionally, differences in legal and technical understanding hindered consistent interpretation across disciplines. 
Participants recommended clearer guidance on legal concepts, structuring questions by development phase, and better support for interdisciplinary dialogue. 

Actions taken as a follow-up 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Akkodis has implemented rigorous procedures to ensure the quality, consistency, and ethical integrity of the dataset used for HR analytics. In collaboration with the University of Bologna, appropriate preprocessing techniques were applied to harmonize heterogeneous data sources, manage sensitive attributes, and support bias-aware modeling practices. These steps were essential in preparing the dataset for reliable analysis and in maintaining its representativeness. 

Handling of variables such as candidate state, gender, and residence was guided by methodological considerations and aligned with established best practices. Sensitive features were addressed through preprocessing and modeling-stage interventions, ensuring compliance with ethical standards and emerging regulatory frameworks, including the European Union’s proposed AI Act. 

Future data collection efforts will prioritize improvements in consistency and inclusiveness, particularly regarding the classification of gender and the completeness of residence information. Adjustments to subjective feature encoding may also be considered to enhance interpretability and reduce potential bias. 

These actions reflect a broader commitment to developing AI systems for HR that uphold principles of fairness, transparency, and non-discrimination, thereby contributing to the creation of trustworthy and socially responsible technological solutions. 

.. _hr2-exp:

Socio-technical analysis using IFM 
----------------------------------

Introduction to IFM
~~~~~~~~~~~~~~~~~~~
The Information Flow Model (IFM) is a structured methodology for analysing socio-technical decision systems by modelling how information is created, transformed, filtered, and used across both human and technical components. IFM represents decision-making processes as a directed graph of information sites and channels, which makes it possible to trace how outcomes are formed, where biases may be introduced, and how these propagate to affect stakeholders. Originally developed as part of AEQUITAS for AI Act compliance and fairness assessment, IFM provides a unified lens through which technical operations (datasets, models, algorithms) and social processes (human evaluations, organisational routines) can be jointly examined. In this report, we apply IFM to the Akkodis use case to complement the FDCGM methodology: while FDCGM assessed the fairness of the dataset itself, IFM focuses on how decisions and potential biases emerge in the end-to-end socio-technical recruitment chain. Together, the two methodologies validate different AEQUITAS blocks and illustrate how fairness-by-design requires both data-level and process-level perspectives. 

Socio-Technical Context
^^^^^^^^^^^^^^^^^^^^^^^

The use case examines a real-world recruitment process carried out by Akkodis in cooperation with a long-term client organisation. Recruitment is a multi-actor chain involving: 

A Business Manager (BM) who maintains direct contact with the client and interprets staffing needs. 

Talent Acquisition (TA) staff, who search and screen candidates through multiple channels and perform initial evaluations. 

The BM or technical consultants, who perform technical assessments. 

The Client, who conducts the final qualification interviews. 

Candidates are scored on several soft-skill dimensions and technical requirements, with feedback loops between client, BM, and TA shaping the process over time. This structure makes the process highly relational: while it allows tailoring to client needs, it also creates potential bias channels through informal interpretation, repeated client influence, and relationship-driven sourcing. 

Method
^^^^^^

The six-step IFM methodology was applied to model this process. The analysis began with interviews of two Talent Acquisition staff. Each interview was independently translated into Step 1 sketches of the information flow. These sketches were then iteratively refined, integrated, and analysed through Steps 2–5 of the IFM methodology. Because the use case owners also provided a well-structured database of historical recruitment logs, it was possible to pair the IFM model with a quantitative dataset analysis, creating a rare opportunity to validate IFM’s descriptive model against empirical outcomes. 

Stakeholder aims: Akkodis stakeholders expressed concern that human bias could affect recruitment decisions. They sought to use IFM to identify potential bias pathways and to determine what corrective measures might be taken. They also expressed interest in exploring AI tools in the future, but their immediate aim was to better understand the fairness of their existing human-driven recruitment system. 

Validation aims: For AEQUITAS, this use case represented an important corner-case for IFM, as it is a purely socio-technical process without active AI components. Demonstrating that IFM can meaningfully capture bias risks in a human-only decision process is therefore a key validation outcome. 

The case also tested the boundaries of the current IFM framework. The relational, feedback-driven nature of recruitment creates dynamic feedback loops (e.g. client preferences influencing BM and TA behaviour). The current IFM formalism does not fully support such dynamic properties. Nevertheless, the analysis applied IFM to model these dynamics in a static way, providing valuable insight into both the strengths and current limitations of the methodology. Finally, because detailed recruitment logs were available, the analysis provided an opportunity to contrast IFM findings with dataset-based statistical analysis, thereby validating IFM not only as a qualitative socio-technical model but as a bridge between process modelling and empirical data analysis. 


IFM Socio-Technical Graph 
~~~~~~~~~~~~~~~~~~~~~~~~~
 

Figure 2. IFM Model of the recruitment process showing two orthogonal sub-models. 

The sourcing process (upper, Figure 2) involves a request from the Client to the BM, who carries the request further to the TA who searches for candidates using several channels. The screening process (lower) is initiated by the TA by a cold call. Interested and suitable candidates are invited to an interview with the BM. Finally, the BM delivers final candidates to the Client for a qualification interview. Each lettered channel is described in Table 3. 

Table 3. The table describes channels (a)-(g) in the IFM from Figure 3. 

IFM Analysis 
~~~~~~~~~~~~

Bias Analysis 
^^^^^^^^^^^^^
The bias annotations in Table 3.4.1 result from applying Step 4 of the IFM methodology to the recruitment process model. Each channel was assessed based on interview data and structural analysis to identify plausible sources of bias introduced through the type of transformation each channel represents. Given that this is a fully social system with human actors many steps are either interpretation heavy abstraction steps or interpretation heavy filtering steps.  

In some transitions, reported standard procedures were noted as potential mitigations. Notable feedback dynamics were also noted as potential biases. Taken together, the bias and mitigations presented in the table highlights where in the process potential deviations and unexpected behaviors may arise and how they can propagate downstream. Since channels are related to actors and semantic stages, the biases can also be related to process stages and responsibility.  

Impact Analysis
^^^^^^^^^^^^^^^

In this section, we analyze whether the IFM constructed for the use case allows for discriminatory or fairness-relevant impacts to arise, and through which pathways these might propagate. We here distinguish between local bias and downstream impact: only biases that affect final decisions (C6) are considered realized impacts.  

We will focus on four classes of potential discriminatory outcomes: 

O1: Discrimination related to protected groups. Candidates could be filtered due to informal, subjective traits (e.g., gender, accent, ethnicty) unrelated to job criteria. 

O2: Geographic or socioeconomic discrimination. Candidates from distant or lower-status regions could be indirectly penalized. 

(O3): Reinforcement of Client-driven discrimination. Effects of a possibly discriminatory client on the candidates through direct selection at the final stage or through feedback effects. 

(O4): Reinforcement of Recruiter-driving discrimination. Discriminatory effects created or reinforced through relationship-based hiring patterns. 

The outcomes O3 and O4 partially overlap with O1 and O2 but since they are particular in their mechanism and effect we treat them as separate. In this analysis (O3) and (O4) partly go outside the scope of this version if IFM, they are included in attempt to test the limits of the current IFM version but the result is more speculative than O1 and O2. 

With regards to O1, the filtering steps in channels (e) and (f), particularly during cold calls and interviews, rely heavily on TA and BM interpretation. Although TA staff reported using structured methods for evaluation, interpretation bias remains a risk, especially in evaluating soft skills, language, or perceived motivation. These filter-steps ultimately determine which candidates are passed to the business manager and client. Without safeguards or double-checks, informal impressions and biases may disproportionately affect candidates from different linguistic, cultural, or communication backgrounds. This is also a channel for discrimination based directly on gender and ethnicity. 

It is possible that the proprietary structured methodology used in these interviews counteract or mitigate such subjective effects. We have not seen this methodology so we can’t make any statements on it, but structurally it holds a possible mitigating role. 

Even if the cold call and interview would themselves have mitigating methodology, the choice on who to call and the choice on which candidates to present to the client both include the possibility of causing O1-type outcomes unless mitigating factors unknown to us are present. 

For O2, the interview stage (f) includes consideration of logistical fit, such as travel time or willingness to relocate. These factors may systematically disadvantage candidates from outside urban centers or from lower-income areas. This can introduce regionally correlated, structural bias, even when the candidate is otherwise qualified. Since no mitigative mechanism was reported here, the path from (f) to (g) may carry such effects unchallenged into the final client decision leading to location based discrimination. 

Both (O3) and (O4) regards dynamic properties (reinforcement loops and feedback effects). The current IFM theoretical framework has known limits in this area – the analysis was still done on these effects in order to gather data for further IFM development capable of handling these dynamics. This means the analysis below is more speculative than the above O1 and O2 analysis. 

Despite these effects not being properly covered in full dynamics, the examples below still demonstrate how the current framework still is able to model them indirectly as static properties. 

(O3) represents potential Client-driven discrimination through feedback loops. This recruitment setting is heavily relational, the client’s preferences are not expressed only at the final selection stage (g), but are also through a feedback loop involving the BM and the TA. Over time, the feedback loop will give the BM an intuitive sense of "what kind of candidate the client wants," and the TA in turn adapts their own filtering and shortlisting strategies to align with this internalized expectation. 

Crucially, this is not always an explicit instruction. Instead, it emerges through reinforced relational dynamics — the BM wants to meet the client’s expectations and the TA wants to meet the BM’s expectations. This form of implicit alignment creates the risk for a structural bias channel: client preferences become culturally encoded without the need for any explicit biased criteria. 

The impact is that certain types of candidates, those perceived as more in line with the client's culture or past selections, are favored from early filtering stages onward. This effect bypasses or precedes explicit client selection: even if the client claims neutrality, the system as a whole has already adjusted to their presumed preferences. Over time, it can result in the reinforcement of cultural homogeneity, without any actor explicitly intending or acknowledging discriminatory practice. 

This potential effect is modeled in the IFM by the transitions (a) and (b), where BM and TA understanding (BMR and TAR) are shaped in part by this feedback on how well previous candidates were received. Such feedback effects were mentioned several times in interviews. Import to note here is that while this structural risk is shown to be present, this does not mean the discriminatory impact is present, just that the risk is present for it to be. 

The outcome (O4) concerns how previous experience with specific candidates (or candidate types) shapes sourcing and evaluation decisions in future recruitment cycles. Candidates who have previously reached a certain stage (C3, C4, or even C6) are not just stored in the database noting that stage, they also persist in the TA’s memory and professional trust network. 

This relational client pool becomes a powerful informal sourcing channel. When a new position opens, recruiters may begin by revisiting known quantities, those who performed well previously, or at least made it to later stages. While this can certainly increase efficiency, it can also lead to a feedback loop of structural favoritism: the more times a candidate has been considered or hired, the more likely they are to be considered again. Importantly, this practice can also potentially work to enshrine a particular candidate archetype, as those who were successful before become the template for future shortlisting, having effects of the same kind as Historical Bias in machine learning. These effects can seem benign but can, if unchecked, work to uphold stereotypes and structural bias, even in a wholly social system without automated components. 

This effect is primarily embedded in the sourcing channels, but implicit bias and stereotypes can affect the cold call step via TAR. This effect only becomes structurally significant through its long-term effect on how the sourcing channels and TA decisions are applied, but theoretically bias can accumulate over time, even if each individual decision appears justified.  

Dataset analysis
~~~~~~~~~~~~~~~~
Summary 

The IFM analysis highlights the nuanced and relational structure of the recruitment process. Key findings include structurally embedded risks of bias linked to informal interpretation, regional disadvantage, and client-internalised preferences. The IFM framework was able to capture these potential pathways and demonstrate how even wholly human decision systems can give rise to long-term structural bias. The quantitative analysis of recruitment logs supported the IFM-based hypotheses by identifying the stages of the process most likely to exhibit bias. While IFM on its own shows potential for bias and discrimination but not its empirical manifestation or direction, the quantitative analysis clarified these details. Results revealed clear gender-related dynamics, with female candidates progressing at higher rates, particularly in the BM interview and client qualification stages. This effect remained robust across different study fields, including both male-dominated and female-dominated disciplines. However, an intersectional perspective showed that this favourable treatment was not evenly distributed: non-Italian candidates were markedly disadvantaged and, in several subgroups, gender dynamics were reversed. These findings confirm the presence of complex, context-sensitive patterns of inclusion and exclusion that would be difficult to detect without combining socio-technical and quantitative approaches. 

Suggestions
~~~~~~~~~~~
Investigate in more depth the hiring rates of non-Italian candidates. Although the causes of the observed disparities are not yet clear, their magnitude justifies further examination. 

Further explore the apparent favourable treatment of women, which may be influenced by contextual or external factors not captured in this analysis. 

Expand the recruitment database to enable systematic logging and continuous monitoring of bias metrics, providing a stronger basis for tracking fairness over time and evaluating the effectiveness of mitigations. 

Review and adapt internal guidance and policies to ensure that early candidate selection (e.g. cold calls) and the handover between BM and client are conducted in a structured and bias-resistant manner.

Validation reflections
~~~~~~~~~~~~~~~~~~~~~~

This use case validates the IFM framework’s ability to uncover subtle, structural dynamics in a purely human system. The modeling tools available were sufficient to capture most of the structures, although admittedly lacking in the feedback-loop dynamics. 

While IFM successfully identified key structural risks, to fully capture the dynamic nature of feedback and social learning requires further development on IFM base theory.  

Such developments are underway to allow for modeling iterative or adaptive behavior, but none of these extensions were used here.  

The paired quantitative study showcases that IFM is not merely a modeling tool but fully a bridge between holistic socio-technical scope and quantitative and technical analysis.  

Integration into the experimentation environment
------------------------------------------------

To complement the fairness assessment conducted through the FDCGM methodology and the IFM socio-technical graph, the Akkodis use case was also validated within the AEQUITAS Experimentation Environment. This phase aimed to operationalise the key fairness concerns identified during the legal/ethical evaluation and socio-technical analysis by translating them into measurable outcomes using fairness metrics and mitigation algorithms. In direct continuity with the methodological phase, the experimentation selected age and sex as protected features, reflecting the risks highlighted in the FDCGM workshops regarding representativeness and compliance with Article 10 of the AI Act. Similarly, the experimentation explicitly targeted gender-related disparities, which the IFM analysis had identified as most likely to arise in evaluation-heavy steps (cold calls, interviews, BM/Client filtering). 

Metrics
~~~~~~~

In line with these risks, the following fairness metrics were applied before and after mitigation: 

Statistical Parity Difference (SPD): to detect disparities in positive outcomes across protected groups. 

Disparate Impact (DI): to assess proportional treatment between advantaged and disadvantaged groups. 

Equalized Odds Ratio (EOR): to evaluate whether error rates were balanced across groups. 

Demographic Parity Ratio (DPR): to measure the overall parity of selection outcomes irrespective of qualifications. 

These metrics were chosen to mirror the bias pathways flagged by the IFM (e.g., interpretation-heavy filtering, regional disadvantages) and the representativeness issues raised by FDCGM (skewed sex distribution, binary classification). 

Mitigation strategies
~~~~~~~~~~~~~~~~~~~~~

Two classical mitigation techniques were tested: 

Correlation Remover (pre-processing): reducing linear correlations between sensitive attributes and features, thereby addressing structural imbalances in the dataset flagged during FDCGM. 

Prejudice Remover (in-processing): adding fairness constraints into the learning objective, directly tackling cognitive bias risks identified through IFM in evaluation stages. 

The Prejudice Remover proved particularly effective, improving fairness metrics such as SPD and EOR, and reducing disparities between male and female predictions. However, consistent with FDCGM findings, this came with a fairness–accuracy trade-off, where small reductions in accuracy accompanied gains in fairness. 

Novel Intersectional Mitigation (FaUCI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To go beyond binary categories and to address intersectional risks repeatedly raised in both FDCGM (protected category × gender) and IFM (gender bias interacting with nationality/region), experimentation deployed FaUCI (Fairness under Constrained Injection), a novel AEQUITAS-developed algorithm. FaUCI enabled the explicit specification of fairness constraints across multiple overlapping sensitive attributes (e.g., gender × age × nationality), ensuring that intersectionally disadvantaged groups were not overlooked. In this use case, FaUCI successfully mitigated compounded disparities while maintaining model usability, demonstrating a significant methodological advance over classical techniques. 

The introduction of FaUCI within the experimentation environment directly addressed the intersectional disparities revealed by the IFM analysis. While IFM had shown that apparent gender favourability in later recruitment stages was not evenly distributed—particularly reversing for non-Italian candidates—FaUCI provided a concrete algorithmic solution to this problem. By allowing fairness constraints to be applied simultaneously across multiple overlapping attributes (e.g., gender × nationality × age), FaUCI operationalised the IFM insight that bias often emerges at the intersections rather than within single categories. Its application in the Akkodis case confirmed that intersectional fairness cannot be achieved through classical mitigation strategies alone, but requires dedicated methods capable of protecting subgroups most vulnerable to compounded disadvantage. 

Key outcomes
~~~~~~~~~~~~
The experimentation phase generated findings that directly reinforced and extended the methodological and IFM analyses: 

Binary gender representation, already critiqued in FDCGM workshops, was confirmed as a limitation in experimentation, underlining the need for non-binary inclusive modelling approaches. 

Data balancing strategies (e.g., resampling), proposed in FDCGM as remedies to skewed distributions, were validated in practice as essential pre-processing steps. 

Fairness–performance trade-offs, discussed in both workshops and IFM sessions, were observed empirically during mitigation experiments. 

Intersectional fairness, identified as a blind spot in both FDCGM and IFM, required a dedicated solution (FaUCI) to ensure equitable outcomes. 

In summary, the Experimentation Environment operationalised the concerns raised in both the FDCGM methodology and the IFM socio-technical model, demonstrating how AEQUITAS integrates normative analysis and empirical testing into a unified Fair-by-Design lifecycle. By validating classical and novel fairness interventions on the Akkodis dataset, the experimentation phase provided concrete evidence that socio-technical risks identified upstream can be systematically measured, mitigated, and monitored downstream. 

Use of suntetic data
--------------------
To complement the experimentation with real recruitment data, the AEQUITAS Synthetic Data Generator was employed to stress test the FaUCI algorithm, which had emerged as the most effective fairness mitigation strategy in the Akkodis use case. The aim of this phase was not only to validate FaUCI under realistic conditions but also to explore its “breaking points”—the thresholds where compounded biases become too severe for even advanced mitigation to fully correct. Synthetic datasets were generated by deliberately amplifying structural imbalances already observed in the historical data, such as underrepresentation of female candidates, skewed age distributions, and nationality-based disparities. By systematically varying these proportions, we created controlled scenarios that allowed us to test how robust FaUCI remained when confronted with extreme or adversarial bias conditions. The results showed that FaUCI maintained its ability to enforce fairness constraints across gender × age × nationality subgroups even under moderate skew. However, when imbalance reached extreme levels—for example, when minority subgroups represented less than 5% of the overall dataset—performance degraded. In such cases, FaUCI was still able to reduce disparities compared to baseline models, but fairness metrics like Statistical Parity Difference and Equalized Odds Ratio plateaued, indicating that mitigation alone could not compensate for the absence of meaningful subgroup representation in the data. 

This stress-testing exercise confirmed two key insights. First, FaUCI is a robust tool for intersectional fairness mitigation in recruitment settings, outperforming classical methods under both realistic and stressed conditions. Second, there are hard limits to algorithmic mitigation: when data imbalance becomes too extreme, fairness cannot be guaranteed without first addressing representational gaps at the data collection stage. These findings underscore the need for a combined strategy of data governance and algorithmic fairness, as envisaged by AEQUITAS, to ensure that fairness interventions remain effective across both normal and adverse scenarios. 


Learnings
---------
The collaboration with Akkodis provided the  opportunity to validate the AEQUITAS framework across its three main analytical pillars—dataset-level assessment (FDCGM), socio-technical modelling (IFM), and empirical experimentation with synthetic stress-testing. Taken together, these exercises produced a comprehensive picture of the fairness challenges and opportunities within AI-assisted recruitment. 

From the FDCGM workshops, Akkodis gained critical insight into the structural imbalances of its recruitment dataset. Sensitive attributes such as sex, age, and nationality were found to be unevenly represented, and subjective traits (e.g., “dynamism”) were assessed in inconsistent ways. These findings highlighted that latent biases are often embedded not only in overt demographic variables but also in how features are defined, collected, and coded. 

The IFM socio-technical analysis extended this perspective by mapping how information flows through the human-driven recruitment process. It revealed that potential bias does not only stem from datasets but is also introduced through interpretation-heavy filtering steps, regional considerations, and client feedback loops. Importantly, the IFM uncovered intersectional risks: while women appeared to fare better overall in later stages, this effect reversed for non-Italian candidates, demonstrating how compounded disadvantages may remain invisible without an intersectional lens. 

The experimentation environment then operationalised these findings, translating abstract fairness concerns into measurable metrics and corrective strategies. Metrics such as Statistical Parity Difference, Disparate Impact, and Equalized Odds Ratio were applied to quantify disparities, while mitigation algorithms like Correlation Remover and Prejudice Remover showed the fairness–accuracy trade-off in practice. The novel FaUCI algorithm directly addressed the intersectional bias patterns revealed by the IFM, demonstrating how advanced in-processing methods can protect subgroups at the intersection of multiple sensitive attributes. Stress-testing with synthetic data further confirmed FaUCI’s robustness, while also showing its limits: when minority groups are reduced to extremely small proportions, no algorithm can fully guarantee fairness without improving the underlying representativeness of the data. 

The overall outcome of these three exercises is twofold. First, Akkodis has developed a heightened awareness of the latent biases in its recruitment processes, ranging from dataset composition and subjective evaluation criteria to socio-technical dynamics and intersectional risks. Second, and most importantly, the validation confirmed that algorithmic fairness is achievable when technical mitigation is aligned with the socio-technical context. The FaUCI algorithm, developed within AEQUITAS and rigorously tested against the recruitment dataset, the IFM socio-technical model, and synthetic stress scenarios, provides Akkodis with an AI component that can be responsibly deployed in future recruitment systems. By explicitly protecting intersectionally disadvantaged groups, FaUCI moves beyond classical mitigation methods and ensures that fairness requirements are embedded by design. 

Looking ahead, Akkodis’ strategic priorities will include: 

Enhancing data collection protocols to ensure inputs are objective, representative, and inclusive. 

Conducting iterative assessments of recruitment datasets using AEQUITAS methodologies and metrics to track improvements over time. 

Exploring AI-based recruitment solutions leveraging the validated FaUCI algorithm, embedding equity from the outset and ensuring alignment with the EU AI Act. 

Through this process, Akkodis has gained both the technical insight and organisational capacity required to align with emerging ethical and regulatory standards. Most importantly, it now possesses a tested and validated fairness-aware algorithm that can serve as the cornerstone for building a recruitment environment that is both inclusive and trustworthy.

Design Process History - A Transparent Approach
-----------------------------------------------
In the following sections we show a list of preliminary experiments (on various areas) that we have conducted to refine the design of the experimenter. We show this history of our tentetives for the sake of increasing the transparency of the design process.

* `Preliminary Analysis <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/AKKODIS_Data_Analysis.pdf>`_

* `Synthetic Data Generation via LLMs <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/AKKODIS_Synthetic_Data_Gen_Langchain.pdf?rev=1.1>`_

* `Synthetic Data Generation via SDV <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/AKKODIS_Synthetic_Data_Gen_sdv.pdf?rev=1.1>`_

* `Bias Detection <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/AKKODIS_Bias_Detection.pdf>`_

* `Full Experimentation Pipeline within AEQUITAS <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/AKKODIS_Full_Experimentation_Pipeline.pdf>`_

