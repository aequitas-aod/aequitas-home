AI fairness in the AI system lifecycle: the holistic AEQUITAS approach
######################################################################

There is a need for a more holistic approach to fair AI, that includes technical
steps, sociological activities, legal compliance measures and understanding, and
ethical considerations.  Addressing the need for AI systems free from
discrimination requires a multidisciplinary approach that combines social,
legal, and technical perspectives.  Despite significant advancements in research
and technical solutions, a gap remains between socio-legal and technical
approaches.

Introduction
************

**Fair-by-design methodology** refers to an approach in the field of AI where
fairness considerations are integrated into the AI lifecycle from the outset.
This methodology aims to ensure that AI systems are *fairly designed*,
addressing potential biases or discrimination (according to a particular
definition of fairness) during the design and development phase rather than
attempting to rectify them after deployment.

Fair-by-design methodologies emphasize proactive measures to mitigate biases and
promote fairness, such as using diverse and representative datasets,
implementing fairness-aware algorithms, and incorporating transparency and
accountability mechanisms into AI systems.

We address this complex problem by proposing a **meta-methodology** -- namely,
:ref:`FairBridge<FairBridge: Converting Legal and Social Principles into AI 
Fairness Techniques>` -- offering a reference for defining AI fairness
methodologies that integrate all three perspectives (social, legal, and
technical ones).  The meta-methodology utilizes a questionnaire-based system
where socio-legal and technical domain experts iteratively refine questions and
responses, supported by automation.

Fair-by-design Approaches
*************************

The design of fair AI approaches involves a detailed analysis of
the entire lifecycle of an AI system, as considering the non-discrimination
aspects of an AI system requires constant actions and monitoring at every phase
of the AI lifecycle. The analysis of the AI lifecycle and its relation to
fairness actions begins with the analysis of the lifecycle itself from two
different perspectives: i) the socio-legal perspective, and ii) the technical
perspective.

The key takeaways are that there are significant gaps between these
perspectives:

* The technical point of view focuses on a narrower – and more limited – AI
  lifecycle compared to the broader social and legal perspective.  
* It is very rare for technical solutions to cover the entire AI lifecycle,
  because its narrower definition compared to its socio/legal counterpart. 
* Technical methods typically intervene at very specific phases.

Albeit there are significant differences from the socio/legal/ethical lens and
the technical one, the core phases of the AI life cycle are shared by both
perspectives: there is a clear identification of the necessity of carefully
considering how data has been sampled (collected or generated), analyzing
whether it contains any kind of bias, and studying how it has to be processed
not to introduce further bias. Both perspectives also place careful emphasis on
how AI algorithms should be evaluated for fairness.

More details the overview over the different perspectives and current gaps can
be found in the following subsections:

* :ref:`Technical Lens<Technical Lens>`
* :ref:`Social, Legal and Ethical Technical Lens`
* :ref:`Bridging the Gap`

Merging the gap between these perspectives is a crucial aspect of a
fair-by-design methodology. :ref:`FairBridge<FairBridge: Converting Legal and
Social Principles into AI Fairness Techniques>` addresses this precise challenge.


Social, Legal and Ethical Technical Lens
========================================

There is no such thing as a consolidated method for fair-by-design AI.  We are
transitioning from an industrial society to an "AI society", driven by two key
forces: stratification and association, representing vertical and horizontal
movements. Existing social divisions and inequalities persist, but new forms are
emerging as social structures, economic relations, and computational systems
intersect. Understanding these contextualized features of AI is crucial to avoid
the *abstraction error* often made in computer science, which overlooks social
context.

* A very relevant notion is that of **situated knowledge** underlying knowledge
  production and the power relations among relevant stakeholders.
* Revealing ML’s social world is key to understand the emergence of bias and
  discrimination in the ML algorithms and models themselves.

Since AI-systems have spread in both public and private sectors, discussion
about algorithmic fairness has arisen. Fairness usually relates to the intent of
achieving a larger, mainly social, overarching goal, such as ‘fair’ hiring,
welfare service delivery, and lending. One important claim to a fair-by-design
social methodology is about the choices and assumptions that are made in the
design process, which could and should be more inclusive.

To diagnose and mitigate biases in AI, it is important to differentiate between
individual and group-level fairness. Individual fairness means that
similar individuals should be treated similarly, and group fairness means that
the outcomes of an AI system should not vary if the population is split into
groups (e.g., by protected attributes). An important strand of literature seeks
to implement mathematical fairness metrics to assess a model’s impartiality
towards subgroups.  Different statistical fairness metrics lead to varying ways
to assess bias in a AI system. 

Fairness Social Perspective
---------------------------

The first action is to understand technology through a socio-technical lens that
sustains the acknowledgment of mutual influences between technical and social
structures. This passage is required to highlight the culture of and modes of
knowledge production in computer science that betrayed the social goals the
field was trying to achieve.

**Distributive fairness** refers to the fairness of the *outcomes (aims)* of
decision making, while **procedural fairness** refers to the fairness of the
*decision-making processes (means)* that lead to the outcomes. 

Technology is the result of a process of social construction with the
contribution of a variety of stakeholders.

::

    Is fairness distributive or procedural? Should it be a socially constructed
    notion?

* **Disparate impact** happens when members of a marginalized class are
  negatively affected more than others when using a formally neutral policy or
  rule. 

    * It is unintentional or indirect discrimination. 

* **Disparate treatment** refers to the situation where an individual is
  intentionally treated differently based on their membership of a marginalized
  class.

* Neither disparate impact nor disparate treatment aim exclusively at
  distributive fairness

    * More sophisticated notions are required → procedural fairness.

The sociological and legal domains are still in the process of converging toward
a unified methodology for fair-by-design AI, albeit strong effort is currently
being invested - consider for instance the European AI Act. Technological
solutions are consequently not sufficiently regulated (or there are not sufficient
incentives towards fairness), nor the legal and social contexts are sufficiently
stable to provide unequivocal guidelines that could be applied by technicians
without guidance from legal/social experts.

Fairness Legal Perspective
--------------------------

The legal relevance of AI was reflected in the EU Ethics Guidelines for
Trustworthy AI (EGTAI), as one of the 3 pillars upon which trustworthy AI rests.
AI systems do not operate in a lawless world. A number of legally binding rules
at European, national and international levels already apply or are relevant to
the development, deployment and use of AI systems today. Legal sources include,
but are not limited to: EU primary law (the Treaties of the European Union and
its Charter of Fundamental Rights), EU secondary law (such as the General Data
Protection Regulation, the Product Liability Directive, the Regulation on the
Free Flow of Non-Personal Data, anti-discrimination Directives, consumer law and
Safety and Health at Work Directives), the UN Human Rights treaties and the
Council of Europe conventions (such as the European Convention on Human Rights),
and numerous EU Member State laws. Besides horizontally applicable rules,
various domain-specific rules exist that apply to particular AI applications
(such as for instance the Medical Device Regulation in the healthcare sector).

Moreover, recent regulatory developments around AI are laying down technical,
social, ethical (and general legal) fairness notions in specific legal
requirements. The EU AI Act is bound to set technical (design) requirements for
high-risk AI systems to ensure the protection of fundamental rights (such as the
right to non-discrimination), by demanding for example (that):

* High-risk AI systems undergo a fundamental right, identification and
  impact assessment (proposed).
* (...) elimination or reduction of risks as far as possible through adequate
  design and development; (art. 9 (4) (a) AI Act)A.
* Training, validation and testing data sets [of high-risk AI] shall be
  relevant, representative, free of errors and complete. They shall have the
  appropriate statistical properties, including, where applicable, as regards
  the persons or groups of persons on which the high-risk AI system is intended
  to be used (art. 10 (3) AI Act).
* High-risk AI systems shall be designed and developed in such a way, including
  with appropriate human-machine interface tools, that they can be effectively
  overseen by natural persons during the period in which the AI system is in use
  (art. 14 (1) AI Act).
* High-risk AI systems shall be designed and developed in such a way that they
  achieve, in the light of their intended purpose, an appropriate level of
  accuracy robustness and cybersecurity, and perform consistently in those
  respects throughout their lifecycle (art 15 (1) AI Act).

Despite all of this, legal methodologies for AI fairness-by-design are scarce
and often limited to one phase of the lifecycle or one particular regulation.
Often these methodologies lack clear guidance regarding which assessment element
is relevant at which stage of the AI-lifecycle and who should be involved when
and how. As we have seen that unfairness or bias can creep in at all stages of
the AI-lifecycle, a more targeted legal methodology is necessary, especially
with regard to the upcoming AI Act that holds numerous requirements and
obligations directed at different stages of the AI lifecycle.

Technical Lens
==============

There is a dearth of fair-by-design methodologies tackled from the
engineering/technology perspective. Technological approaches mostly focus on
specific phases of the AI lifecycle (e.g., data collection, training of models,
evaluation of results, etc.). 

AI outside of the ML subfield is extremely underrepresented, and this is
especially true from the technological point of view. This is a limitation:

* There are many AI algorithms that do not fall into the ML categories whose
  impact to society and economy is non-negligible and whose behavior can be
  influenced by various biases. 

* We recommend researchers and practitioners to start increasing their
  attentions to other AI domains as well.

.. image:: img/AI_lifecycle_tech.png
  :width: 300
  :alt: AI Lifecycle - Technical Perspective

Technological methods to enforce fairness in ML are typically subdivided
according to the phase in the AI lifecycle in which they can be applied. A broad
classification is the following:

* **Pre-processing techniques** approach the problem by removing the underlying
  discrimination from the data prior to modelling. This is argued in the
  literature to be the most flexible phase of repairing bias in the pipeline, as
  it makes no assumptions with respect to the choice of applied modelling
  technique. The methods, that modify the training data are at odds with
  policies like GDPR’s right to an explanation, potentially introducing new
  biases. Sufficient knowledge of the data and veracity assumptions are
  required.  
* **In-processing techniques** modify the traditional learning algorithms to
  account for fairness during the model training phase. They require a higher
  technological effort and integration with standard ML libraries to avoid
  porting challenges.  
* **Post-processing** is a set of methods that can be run on the output scores
  of the classifier as a post-training processing step to make decisions fairer.
  The accuracy is suboptimal when compared to “equally fair” classifiers and
  could be the case that test-time access to protected attributes is needed,
  which may not be legally permissible.

For a detailed survey on technical methods for enhancing fairness of AI
approaches, we refer to the recent paper from `[Calegari et al.]
<https://cora.ucc.ie/items/f5e86ca6-3848-4e92-9e04-23a26d445b1c>`_.

Technological methodologies tend to adopt a reductionist approach, aiming at
decomposing complex problems into a series of (hopefully easier) sub-problems.
Under this solution paradigm, it is more “natural” to devise approaches that
focus on specific fairness-related aspects, such as bias detection or
mitigation, rather than to create holistic approaches encompassing the entire
design process. This is compounded by the fact that a fair-by-design methodology
can hardly be founded on merely technological grounds: a fair-by-design approach
should encompass several aspects (e.g., dataset creation, data sampling,
algorithmic choices, output evaluation, etc.) that should involve human-mediated
elements, and thus cannot be entirely decoupled from sociological, economical,
cultural and legal subtexts.

Bridging the Gap
================

Considering the entire AI system lifecycle is fundamental when assessing
fairness and mitigating bias in AI systems:

* It allows for a comprehensive understanding of how bias can infiltrate at
  various stages, from data collection and model training to deployment and
  impact assessment.  
* By examining the entirety of the process, we can identify and address
  potential biases more effectively, ensuring fairness across all stages of
  development and implementation.

The analysis of the socio/legal and technological lenses revealed how there is
still a non-negligible distance between the two areas.  It is very rare for
technical solutions to cover the entire AI lifecycle, because its narrower
definition compared to its socio/legal counterpart. More commonly, technical
methods intervene at very specific phases.

The interplay between sociological/legal and technological perspectives is still
in its infancy: engineering solutions tend to adopt excessively reductionistic
approaches (discarding the big picture) while sociological/legal varied
indications and suggestions struggle to coalesce into a set of well-defined and
actionable guidelines which can be actually applied

Other gaps between the technological and legal perspectives stem from the
relative lack of (effective) communication between legal experts (and
lawmakers), ethicists and social scientists on the one hand, and technical
experts (i.e., the developers of AI systems) on the other.

* The socio/legal approaches tend to provide broader requirements and
  guidelines, refraining from defining how fairness should be measured in
  practice.
* The technical approaches typically start with the aim of defining fairness
  metrics, requiring:

    * a definition of the fairness notions from social, legal, ethical and
      technical perspectives;
    * a quantitative mechanism to measure them (if possible).
* Fairness notions vary by context and stakeholder, requiring different actions
  to achieve. They can be measured quantitatively using fairness metrics, but
  this leads to numerous metrics each capturing different aspects of fairness.


Summarizing:

* There is a clear gap in current fair-by-design practice. 
* The integration of social, legal, ethical, and technological
  perspectives presents two challenges: complexity and interdisciplinarity. 
* Each perspective operates within its own framework:

    * Social, legal, and ethical perspectives focus on human behavior, ethical
      principles designed for digitalization, and regulation, while
      technological perspectives prioritize efficiency, functionality, and
      innovation. 
    * Bridging these perspectives requires interdisciplinary collaboration. 
    * This is compounded by cultural and contextual differences, which are
      crucial from the legal point of view.

* Divergent priorities: technological perspectives often prioritize performance
  and scalability, whereas social and legal considerations emphasize
  accountability, equity and the protection of (fundamental)
  rights, democracy, and the rule of law.
* Pace of change: technology evolves rapidly, outpacing the ability of social,
  ethical and legal frameworks to adapt. This misalignment leads to regulatory
  gaps and ethical dilemmas.  
* Lack of common vocabulary and/or conceptual framework: each discipline has its
  own vocabulary and ‘language’ and concepts whilst quite often referring to the
  same elements or objectives. Mapping and matching these diverging vocabulary
  and concepts are a lengthy but crucial process. 


FairBridge: Converting Legal and Social Principles into AI Fairness Techniques
******************************************************************************

Modern computational systems are becoming increasingly complex, impactful, and
pervasive, mostly due to the ever-increasing capabilities of AI technologies.
As AI grows in autonomy and performance, it also becomes more widespread in
applications that directly affect human lives, such as healthcare, justice,
education, finance, etc.  AI-powered systems tend to absorb, reproduce, and
sometimes even amplify, the biases present in the data they are trained on, or
in the people who design them.

To mitigate this issue, recent efforts in AI-fairness research have been
focusing on either:

* developing statistical algorithms for detecting and mitigating biases,
* defining guidelines and best practices for ensuring fairness in \ac{AI}
  systems.

We propose a **meta-methodology** for fairness engineering, consisting of a
*stable* set of core principles and an *evolvable* pool of practices for
steering end users towards a deeper understanding of the problem/domain they are
dealing with, and for guiding their decision-making. The meta-methodology
should then be reified into a guidelines-provisioning software system whose
capabilities and degree of automation can be incrementally improved, as
prescribed by the meta-methodology itself.

::

    We propose developing the Fair-by-Design via an incremental approach,
    starting from an initial version to be repeatedly refined.

The Meta-Methodology
====================

Fairness notions vary by context and stakeholders, requiring different
activities for fulfilment. Legal and social perspectives on fairness are
case-dependent, interpreted differently, and influenced by social and
institutional factors; setting thresholds for what is fair or unfair.  Current
Fair-by-Design practices have a clear gap due to the challenges of complexity
and interdisciplinarity in integrating multiple perspectives. These insights can
be summarized as follows:

* Fair-by-Design approaches require the collaboration of an interdisciplinary
  team;
* Fair-by-Design methodology should be tailored according to the context.

For this purpose, we propose a meta-methodology rather than a single
methodology; we want to provide tools for **building fair methodologies**.  Both
socio-legal and technical experts shall operate this tool.

Practical attempt to build a Fair-by-Design methodology should keep into account
the following desiderata:

* the methodology should consider the cultural context and the domain in which
  the \ac{AI} system is going to be applied;
* the methodology should adapt to any change in the cultural context as it
  evolves;
* the methodology should assist experts in the activity of translating the
  social, legal, and ethical requirements into technical requirements but
  without replacing the human decision-maker;
* the methodology should account for pre-existing datasets and algorithms as the
  basis for the fair AI system to be developed.

Such a reiterated approach is paramount to ensure that the resulting
methodologies are kept up-to-date as the contexts evolves. In practice, we want
to provide a tool (the meta-methodology) to build and adjust Fair-by-Design
methodologies for AI. This degree of separation is important as while the
fairness methodology depends on the context and needs to be tailored to its
specific domain, the meta-methodology can instead be general and shared across
different social and legal contexts.

::

    We require a Fair-by-Design methodology to be based on a Questions/Answers
    (Q/A) mechanism
    
The questions and their admissible answers should be designed to deepen
decision-makers understanding of the problem and the domain they are dealing
with, and to make them aware of any relevant issues concerning their application
scenario ---hence guiding their decisions accordingly. For this reason, the
questions and answers should be designed by experts in law, sociology,
statistics, and computer science.

.. image:: img/fairbridge_overview.png
  :width: 600
  :alt: FairBridge Methodology Overview

Actors Types
============

FairBridge is intended to be used by *organizations* whose goal is to develop
fair AI algorithms.  These algorithms are assumed to be eventually composed into
AI systems, and these systems are expected to be used by some *end-users*.

* For instance, end users could be private individuals or companies as well as
  public institutions or civil society organizations willing to use the final
  AI system.
* End-users may also include "affectees", i.e., people affected by (subjected
  to) the decision of an AI system being used by somebody else% ---e.g.,
  job applicants, or welfare recipients.

End-users are *not* the actual users of FairBridge.  The actual users are the
*members* of the organizations who are responsible for developing the AI
systems.  These members are divided into two categories:

* **Business users** are responsible for any decision concerning the target
  AI system. They should be in the position of making decisions. In
  particular, they are the ones who should answer the questions. For this
  reason, they should have sufficient background knowledge to understand the
  questions and the admissible answers, or know who to ask for help when this is
  not the case.
* **Technical users** are responsible for the actual implementation of the AI
  system, following the decisions taken by the business users.  In practice,
  they are software developers, data scientists, and so on, hence they possess
  adequate technological expertise to develop AI systems.

The Q/A mechanism should include questions aimed at identifying the
stakeholders, in such a way their existence and views can be included in any
fairness-assessment and enforcing action.  A similar argument holds for the
*potential* end-users of the target AI system, whose profile should be
identified and taken into account by the Q/A mechanism as early as possible.

Questions/Answers Flow
======================

The Q/A mechanism is the core of the FairBridge system, and it is the main tool
by which the meta-methodology is reified into a practical software system.  It
involves a set of *relevant* questions and their *admissible* answers, plus a
partial ordering relation, which defines the order in which the questions should
be asked to the business users.  The answer to a question may impact which and
how many questions are asked later on to the same business user.

.. image:: img/qa-graph-path.png
  :width: 600
  :alt: Graphical depiction of the Q/A mechanism

Even if the graph is the same for all business users, each business user may
follow a different path, depending on their particular use case, domain, goals,
and constraints.  In other words, the graph represents the whole set of
questions and answers, and their ordering, while the path represents the subset
of questions and answers that are shown to one particular business user.  The
Q/A graph is designed, filled, and refined by experts, as prescribed by the
meta-methodology. Conversely, Q/A paths are constructed by business users and
technical users and they are tailored to the specific needs of the organization
they belong to.


AI fairness Methodology
***********************

* building blocks “clickable”
* for each building block link to the guidelines
* Development & Evaluation link to the tech
