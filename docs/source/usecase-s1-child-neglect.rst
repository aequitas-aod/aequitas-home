.. _s1-context:

Introduction and background
---------------------------
The Child Neglect use case addresses one of the most ethically and socially sensitive domains of AI: the identification of children potentially exposed to abuse or neglect. The overarching goal was to investigate whether AI could responsibly assist medical professionals in detecting patterns indicative of child abuse without replacing or undermining clinical judgment. Early in the analysis, AEQUITAS’ Zero-Question Methodology—which asks whether AI should be used at all—revealed that the available hospital dataset, despite containing valuable diagnostic information (notably the “NAP – Neglect and Abuse Pediatric” flag), was statistically limited and ethically sensitive. Rather than pursuing predictive classification, the project reoriented toward AI-supported knowledge extraction and decision support, using LLMs to derive structured rules from clinical manuals. These manuals describe symptoms, injury patterns, and professional protocols for handling suspected cases of maltreatment. The extracted rules were subsequently validated and compiled into a five-question digital checklist (NAP Checklist) designed to guide emergency doctors in recognising early warning signs of abuse. This use case therefore exemplifies AEQUITAS’ “Fairness-by-Design before AI design” principle: instead of automating moral judgment, the methodology channels AI into a trustworthy, assistive role that enhances transparency, traceability, and equity in clinical care. 

Fair-by-Design methodology: Prohibited Social Scoring Assessment (PSSA)
-----------------------------------------------------------------------

Methodology Overview
~~~~~~~~~~~~~~~~~~~~
The assessment followed the Prohibited Social Scoring Assessment (PSSA) methodology, grounded in the EU AI Act’s definition of social scoring as the “evaluation or classification of natural persons or groups of persons over a certain period of time based on their social behaviour or known, inferred or predicted personal or personality characteristics”. For the social scoring to be prohibited, it must meet one or both criteria:  

* detrimental or unfavourable treatment of certain natural persons or groups of persons in social contexts that are unrelated to the contexts in which the data was originally generated or collected;  

* detrimental or unfavourable treatment of certain natural persons or groups of persons that is unjustified or disproportionate to their social behaviour or its gravity;  

PSSA follows the structure of the AI Act definition, taking participants through a two-step process of 1) identifying whether their AI system uses/constitutes a form of social scoring and 2) assessing whether this social scoring meets the consequence requirements that would render the system classified as prohibited.  

To do so, the participants answered a series of reverse-engineered and interlocking questions intended to elicit less overt forms of social scoring and guide participants in dissecting which elements of the use case, if any, would be considered prohibited.   

The AEQUITAS use case of AI Assisted Identification of Child Abuse and Neglect in Hospitals was evaluated during this workshop. The AI system aims to detect and assess the risk of child abuse and neglect in the hospital context, whilst reducing bias and discrimination on the basis of ethnicity and socioeconomic background. The full report can be found in  (???????)

Key Findings
~~~~~~~~~~~~
Based on the available information, the AI system does not constitute a form of prohibited social scoring under the AI Act. The methodology helped guide this conclusion, though further technical detail would have enabled deeper analysis. 

Part 1: System Requirements 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The system appears to perform classification by flagging children as either at risk or not at risk of abuse. This classification relies on a flagging mechanism but lacks clear evidence of evaluation functions such as ranking or rating individuals. As there was limited information on how the system work it was hard to arrive at a definitive conclusion on whether it was ‘evaluating’ children and parents.  

Regarding the data used, participants identified that the system draws on medical data, including medical histories, which could involve known or inferred personal characteristics such as mental health. There was discussion around whether mental health diagnoses might be interpreted as personality related traits.  

Next, we considered whether the data used originated from social contexts unrelated to where it was originally collected. The AI system operates entirely within the hospital setting, using data collected for medical purposes. While some administrative data (e.g. zip codes) might indirectly indicate socioeconomic status, they are considered part of the protected medical record under GDPR. Ultimately, the participants concluded that while the AI system likely relies on personal or personality-related characteristics, it does not use data from unrelated social contexts and thus does not satisfy Point (i) of the prohibition criteria. 

Part 2: Consequence Requirements 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We examined whether the system leads to detrimental or unfavourable treatment under two conditions: 
* Point (i): Use in unrelated social contexts - We found that any action taken because of the AI system’s output would occur within the hospital setting, where the data was originally collected. Therefore, this condition is not met.  

* Point (ii): Unjustified or disproportionate treatment - We concluded that any resulting action, such as further investigation by medical professionals, would not be unjustified or disproportionate, given the gravity of child abuse as a social and medical issue. In fact, when a child is flagged as being at risk, it is likely to trigger proportionate and legally justified interventions, rather than arbitrary or excessive responses. 

Moreover, the types of contexts in which unjustified detrimental treatment is a concern (such as education, employment, law enforcement, housing, and migration) are those listed in Annex III and Annex I of the AI Act. The AEQUITAS use case does not affect individuals in these domains directly. Therefore, even if negative outcomes arise for parents (e.g., social services involvement), these outcomes are likely to be justified and proportionate, assuming the system’s flagging is accurate and responsibly used. 

Assessment of PSSA 
~~~~~~~~~~~~~~~~~~
The methodology was effective in structuring the assessment and aligning with the AI Act, but updates are needed to reflect the European Commission’s latest guidance. Participants flagged unclear terminology (e.g. "unfavourable" vs. "detrimental") and complex phrasing in some questions, suggesting a need for reordering and simplification. Lastly, better technical detail on the use case and a clearer explanation of the methodology’s purpose and structure would improve usability and relevance in future applications. 

Integration into the experimentation environment
------------------------------------------------

The main objective of the experiments was to transform expert clinical knowledge—scattered across lengthy hospital manuals and pediatric forensic guidelines—into a structured, auditable, and explainable tool to support medical decision-making. This process exemplifies AEQUITAS’ principle of Fairness-by-Design before model design: ensuring that ethical compliance, transparency, and human oversight are embedded before any algorithmic implementation. The technical work leveraged LLMs to automatically extract, formalise, and validate diagnostic rules from medical manuals used by pediatric departments to assess potential child neglect and abuse. The resulting knowledge base was translated into a five-question checklist (the NAP Checklist, where “NAP” stands for Neglect and Abuse Pediatric) designed to help emergency doctors recognise early indicators of risk. The checklist encapsulates five key diagnostic dimensions: 

* Consistency of injuries – evaluating whether explanations match observed lesions; 

* Delay in seeking medical care – assessing whether treatment was postponed without justification; 

* Signs of neglect – identifying malnutrition, poor hygiene, or insufficient supervision; 

* Inconsistent medical history – highlighting contradictions in patient or caregiver narratives; 

* Behavioural or relational anomalies – recognising unusual interactions between child and caregiver. 

Each dimension was derived from validated clinical protocols (e.g., ESCAPE and SCAN tools) and cross-checked with domain experts to ensure medical relevance and ethical soundness. 

**Experimental Phase**

1. **Manual Testing.** The checklist was first tested manually on a set of 35 anonymised emergency department cases, including 17 confirmed child neglect/abuse cases and 18 control cases. Each case was reviewed manually, and the checklist questions were answered independently by evaluators. The manual assessment demonstrated 100% recall (no false negatives) and an overall accuracy of approximately 89%, with only two false positives arising from ambiguous injury descriptions. These results confirmed the clinical reliability of the checklist as a high-sensitivity screening tool for supporting doctors during emergency evaluations. 

2. **Automated Testing with LLMs.** In a second phase, the team explored whether the same checklist could be automatically applied to unstructured clinical text using a Large Language Model (GPT-3.5-Turbo). The model was prompted to read anonymised patient records (over 21,000 admissions) and answer the five checklist questions with TRUE/FALSE outputs. Two experiments were performed: 

* A zero-shot setup, in which the model received only the instruction and checklist. 

* A few-shot setup, using five manually validated examples to improve contextual understanding. 

The automated model correctly identified most NAP-positive cases but tended to over-predict risk, generating a moderate number of false positives (around 5%). This behaviour was particularly evident in the fifth question, where the model inferred suspicion from emotional or ambiguous language in doctors’ notes. The few-shot setup improved precision, demonstrating that contextual examples can calibrate model judgment, though full automation remained ethically and operationally unsuitable. 

**Results and Ethical Validation.** The experiments confirmed that AI can enhance but not replace human clinical reasoning in detecting potential child neglect. The manually applied checklist achieved strong sensitivity with minimal false alarms, while automated testing showed the feasibility of natural language processing in triaging large volumes of textual data. However, results also revealed the moral and practical limits of automation: while LLMs can recognise relevant textual patterns, they lack the contextual and ethical awareness needed to interpret the complex human situations surrounding suspected abuse. The findings therefore reinforced the Fair-by-Design and IFM conclusions that human oversight and proportionality are indispensable in this domain. 

From an ethical perspective, the use case validated AEQUITAS’ pre-regulatory decision pathway. The PSSA methodology established that the system does not qualify as a prohibited form of social scoring, since it operates solely within the medical context and supports, rather than penalises, families. 

Key outcomes
~~~~~~~~~~~~
* Shift from prediction to assistance: The experiments demonstrated that fairness in AI for child protection depends on the system’s role—moving from autonomous prediction to explainable, assistive support. 

* High sensitivity, limited automation: The NAP Checklist achieved full recall and reliable accuracy, showing that explainable rules outperform black-box predictions in ethically constrained domains. 

* Human oversight as a design feature: Both manual and automated testing confirmed the necessity of medical supervision to interpret AI outputs responsibly. 

* Fairness embedded in purpose: The system aligns with AEQUITAS’ fairness objectives by ensuring that the AI’s impact is proportionate, justified, and directed toward safeguarding fundamental rights rather than ranking or penalising individuals. 

The experiments mark a significant milestone in applying AEQUITAS’ Fair-by-Design methodology to a socially critical healthcare use case. The work demonstrated how AI can be safely integrated into sensitive decision-making contexts when fairness principles are operationalised through governance, transparency, and participatory validation. By transforming clinical expertise into structured, explainable rules and rigorously testing them under human supervision, the use case provided a model for ethically compliant AI in child protection—one that strengthens professional judgment, respects human dignity, and upholds the principles of proportionality and justice embedded in the EU AI Act.

Learnings
---------
The use case provided one of the demonstrations of AEQUITAS’ ability to operationalise fairness, proportionality, and human oversight in an ethically constrained domain. By combining the PSSA, the experimentation, the case showed how AEQUITAS can guide the development of AI systems that strengthen human decision-making while avoiding unjustified or discriminatory automation. 

The first major learning emerged from the PSSA methodology, which clearly established the ethical and legal boundaries for AI use in child protection. The assessment confirmed that the system did not constitute prohibited social scoring under the EU AI Act, since it operates within the medical context and aims to safeguard children rather than evaluate or penalise them. This validation showed how AEQUITAS can help practitioners differentiate between legitimate clinical support systems and high-risk social scoring mechanisms, providing a pre-regulatory compliance path that ensures fundamental rights protection from the earliest design stages. 

The experimentation phase translated these conceptual insights into practical validation. The manual testing of the NAP Checklist achieved 100% recall and high accuracy, confirming that knowledge-based tools can reliably assist in risk detection when guided by expert rules. The LLM-based automated experiments further demonstrated that AI can effectively process large volumes of unstructured clinical data to support doctors, but that human supervision remains indispensable. This outcome reaffirmed AEQUITAS’ central tenet that AI in high-stakes environments should assist, not replace, human professionals. 

The ethical implications of these findings are significant. The project showed that fairness in child protection is not about equalising algorithmic outputs, but about ensuring just, transparent, and proportionate decision support that respects the vulnerability of the affected individuals. It also demonstrated that fairness must be designed into the purpose and function of the system—transforming AI from a predictive or punitive instrument into a trustworthy clinical assistant. 

In conclusion, the use case proved that AEQUITAS can deliver fairness assurance for AI systems operating in morally complex environments, where the stakes involve not only performance but also fundamental human rights. The project established a replicable blueprint for developing AI tools that are compliant by design, explainable by construction, and ethically defensible in deployment. It also demonstrated that the fair and trustworthy use of AI in child protection is possible—provided that technology remains firmly anchored in human judgment, social context, and respect for human dignity. 