.. _s1-context:

Context
-------

In the last decades, child abuse and neglect have seen soaring numbers. The broad adoption of electronic health records in clinical settings offers a new avenue for addressing this. Detecting and assessing risks of child abuse and neglect within hospital settings could prevent and reduce bias against ethnic and socioeconomic disadvantaged communities as well as raise the overall safety of children. There are two main factors that guide a doctor during the diagnosis: 1) the visit 2) the medical history (anamnesis). In the case of pediatric patients, the latter is even more delicate as it is the parent who interprets and reports the child's disease and represents the. child's rights. Furthermore, today's reality of migration flows and increasingly deficient parenting are the norms, make anamnesis ever more complex: language barriers, parenting skills, cultural differences all become accelerators of bias insertion in the entire process. It should also be noted that, in this process, the parent often uses many strategies of mystification, to avoid being seen as a potential abuser. Thus, hospitals' processes currently rely mainly on experts as cultural mediators for dealing with potential child abuse, who are not continuously available at the hospital, contributing to delays in diagnosis, affecting children and parents and elevating overall costs. An AI decision support system can only give concrete, effective and rapid help, if fair outcomes compliant with EGTAI are produced.

.. _s1-goal:

Goal
----

To develop an innovative AI system following AEQUITAS methodologies to detect and assess risk for child abuse and neglect within hospital settings, prioritizing the prevention and reduction of bias against ethnic and socioeconomic disadvantaged communities. The possibility of racial bias in AI systems reinforces our challenge of addressing racism through an AI system and finding the optimal form of human-machine collaboration.

.. _s1-known:

Known biases and unfairness
^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the context of leveraging AI to detect and assess risks of child abuse and neglect within hospital settings, several state-of-the-art AI biases are noteworthy. The integration of AI in healthcare, especially in sensitive areas such as pediatric anamnesis, introduces complex ethical challenges. Key among these is the potential for racial and socioeconomic biases, which can arise from skewed training data that does not adequately represent diverse populations. This can lead to discriminatory outcomes against ethnic minorities and economically disadvantaged groups, exacerbating existing disparities in healthcare.

Moreover, language barriers and cultural differences present in scenarios influenced by migration and varied parenting norms can further complicate the effectiveness of AI systems. These factors may lead AI algorithms to misinterpret or overlook crucial contextual information provided during medical histories, thus risking inaccurate assessments. The reliance on parents' accounts can also lead to biased data input, as some parents might downplay or misrepresent symptoms and situations due to fear of stigmatization or legal repercussions.

.. _s1-method:

Method
------

Data from the AOUBO pediatric emergency room management system will be used to design a new AI system to support doctors in identifying "at-risk" cases given a specific medical history. This case study will benefit from the AEQUITAS socio-technical approach of including and assessing the often disadvantaged background of children and their parent(s). Being aware that the accompanying parent is in the vast majority of cases the mother that might be without a driving license, living in less serviced urban areas, or – in some cases – in need of her husband’s permission to move autonomously, is fundamental to have a full picture of the patient. This is a typical case where intersectionality does play a role as gender and race lines of inequality interact and multiply possible negative discriminatory effects. This relevant socio-economic background is crucial in 2 directions: 1. It is relevant when designing and developing the AI system in support of doctors’ decisions because it adds a novel layer of information upon which the decision is made and 2. It is relevant to doctors’ evaluation of the possible protocols. The technical solutions will avoid the risk of repeating, amplifying and contributing to gender stereotypes in the overall evaluation of patient history. The case study develop a predictive system from scratch, following methodologies and techniques (WP5) and comparing its results with those suggested by human experts to assess their fairness.

.. _s1-exp:

Experimentation and results
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   The experiments for this use case have become more challenging as they progressed due to data scarcity in the scenario. Drawing meaningful conclusions from such a limited dataset would be ethically unacceptable and pose significant risks. Therefore, the exercises being currently conducted on this use case are related to: 1) the application of the TAIRA methodology, including the Question-0 methodology; 2) experimentation with GenAI for the automatic translation of the "notebooks containing guidelines for the identification of abuse and mistreatment" owned by the hospital.
