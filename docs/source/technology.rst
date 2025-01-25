Introduction
----------------------

In today's complex and rapidly changing technological landscape, the widespread adoption of AI-based decision support systems across various sectors demands attention to the prevention and mitigation of inequalities and intersectional discrimination that can arise. Building trust in these systems requires domain experts and stakeholders to have confidence in their decisions.
The objective of AEQUITAS is to develop an experimentation environment to address and tackle the multiple manifestations of bias and unfairness of AI by proposing a controlled experimentation environment for AI developers. Thus, AEQUITAS is a set of tools to carefully assess AI fairness and isolated settings in which Socio-technical systems (STS) are tested, evaluated, and refined to identify and mitigate potential existing bias sources. This type of environment is essential for conducting experiments to assess the performance and behaviour of AI models under various conditions enabling fair and compliant AI systems. It enables developers to make informed decisions about how to improve their AI systems, understand their limitations, and optimize their functionality.
On the other hand, creating and managing a cohesive enterprise architecture is undeniably intricate due to the involvement of diverse individuals with varying backgrounds who use different notations and express a consistent set of interests and activities to be part of the requirements specification. To effectively communicate information about different architecture domains, architecture views serve as an ideal mechanism. In essence, a view is a component of an Architecture Description that focuses on a specific set of related concerns and is customized for stakeholders.

Architectural Overview
----------------------
Creating the architecture in a large project like AEQUITAS imposes several challenges.
To overcome these, the 4+1 View Model designed by Philippe Kruchten has been adapted to specify the architecture view of the solution offered by AEQUITAS.

From a viewpoint perspective, those that were taken in consideration when building the project's architecture are the following:

* **Business viewpoint**: where the different stakeholders and the context are identified and discussed, and the fairness-related concepts and their relationships are described in detail.
* **Use case viewpoint**: Main representative use cases (data sharing, manipulation and use of datasets, upload to the AI on Demand platform) are described and users are categorised into two main groups, the *Business User (BU)* and the *Technical User (TU)*. The BU takes business and fairness-related decisions and translates them into requirements while the TU  develops AI tools which comply with those requirements.
* **System viewpoint**: this view describes the platform architecture from a logical perspective and includes a set of containers that fit all the project requirements.


Use Case view
~~~~~~~~~~~~~~


This section outlines the expected AEQUITAS usage. This is the central view for capturing different usage expectations and needs. In essence, it encompasses how AEQUITAS supports the different detection and mitigation of existing bias activities in an AI system.
A central part of this view consists in identifying the system's users and the activities they are expected to be performed.

Users
^^^^^^

Understanding the diverse set of users in AEQUITAS is crucial to tailoring the system. Users of AEQUITAS can be categorized into various types based on their roles, responsibilities, and interactions with the system. Here are the types of users of the system:

* **The Technical User (TU)**: any user with coding capability, who may either have or lack knowledge about fairness, but for sure they have a basic understanding of machine learning.
* **The Business User (BU)**: any user with legal, social, ethical, or management capability and responsibility, hence in charge of taking decisions.

AEQUITAS Primary Use Scenario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

AEQUITAS has the main goal to create an environment where users implementing AI technology can assess its validity with regard fairness and impact to people. For this purpose, AEQUITAS shall support the following activities:

* the BU can take business and fairness related decisions and translate them into requirements for the TU
* the TU can develop AI tools which comply with those requirements, and present results effectively to the BU

Thus, AEQUITAS must be seen as the place where BU needs and TU solutions converge.

AEQUITAS Secondary Use Scenarios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The secondary use cases satisfy needs such as:

1. allowing data exchanges between AEQUITAS users for further experimentation.
2. allowing interactions with the system manipulate and visualise data
3. allowing a user to interact with the AI on Demand platform: in this case a user shall be able to both push and pull from AI on Demand
