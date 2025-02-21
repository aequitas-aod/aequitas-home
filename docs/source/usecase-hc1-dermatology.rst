.. _hc1-context:

Context
-------

There are many areas where AI can assist dermatological experts, such as computer-aided detection/diagnosis, disease prediction, image segmentation, etc. [18]_. The most successful AI applications to dermatology involve processing images and making automated decisions based on images of skin patches, e.g., distinguishing between images portraying healthy skin from images containing dermatological conditions [28]_.

Dermatology is among the areas which can benefit from data-driven models, as the first step of identifying skin diseases typically consists of visual inspection (possibly followed by further analyses) and AI approaches are well-suited to classify images—if provided with sufficient training data.

One of the greatest success stories of AI is image classification and image manipulation, in particular through data-driven approaches such as ML and Deep Learning (DL) [4]_. Computer vision boosted by DL has been employed in a variety of medical contexts, including dermatology, covering several tasks from disease classification using clinical images to disease classification using dermatopathology images [3]_ [5]_ [10]_. One of the biggest limitations of the widespread adoption of DL techniques is their data-hungry nature. Generally speaking, DL models base their success on the availability of large, annotated data sets, e.g., thousands of different images containing various examples of healthy skin and dermatological diseases.

AI can also come to the rescue to remove this obstacle, as in recent years, great strides have been made toward synthetic medical image generation through DL approaches [29]_ [26]_, in particular using DL models such as Variational Autoencoders (VAEs), Generative Adversarial Networks (GANs) and Diffusion Models [7]_. However, the majority of these data augmentation techniques –with few exceptions, e.g.,
[2]_ [9]_ – do not target skin images, but rather focus on MR images, PET, CT scans, radiography, etc [17]_. Instead, synthetic generation of clinical skin images with pathology aims at generating realistic and diverse images depicting various skin conditions and pathological patterns [15]_ [20]_. The goal is to capture the complexity and visual characteristics of different skin conditions, including dermatological diseases, lesions, and abnormalities [1]_.

To achieve this, researchers employ various strategies, including the incorporation of domain knowledge, data augmentation techniques, and conditioning methods that guide the generation process based on additional information or attributes. Existing approaches in the field have predominantly relied on the utilization of GANs or VAEs. These methods have proven to be effective in generating high-quality samples and learning latent representations. However, they tend to require several thousand training images to learn the features of skin with and without pathological conditions. In this paper, we circumvent this issue and propose to generate realistic skin images with a diffusion model and with a very scarce training set, i.e., a few hundred pictures. We validate our approach using real images taken from a public hospital in Italy (IRCCS Azienda OspedalieroUniversitaria Di Bologna); the code used to implement the approach and run the experiments is publicly available (https://github.com/aequitas-aod/experiment-gen-skin-images). To the best of our knowledge, there are very few approaches in the literature that employ diffusion models in this context and demonstrate their suitability even with a very small training set.

.. _hc1-goal:

Goal
----
The goal of this use case is to develop a synthetic image generator that can generate synthetic images of skin with pathologies in a way that captures the complexity and visual characteristics of different skin conditions, including dermatological disease, lesions, and abnormalities [1]_.

.. _hc1-method:

Method
------

Data, Analysis, Pre-processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raw data
""""""""

The initial raw dataset comprises a collection of 2495 images, belonging to 187 different medical cases, captured by doctors in hospitals using cameras or mobile phone cameras. Each photograph focuses on a specific patient, with the corresponding label indicating the diagnosed skin disease for that individual. At this stage, the data is in an unprocessed and sensitive format, frequently encompassing personal details, including identifiable facial features or recognizable characteristics. Additionally, although the photos primarily capture a specific body part related to the patient’s condition, they frequently include extraneous background elements or foreground clutter that are unrelated to the main focus. Considering these factors, an initial round of data refinement was necessary, primarily focusing on data cleaning, which involved removing irrelevant regions such as background elements from numerous photos, and ensuring data anonymization. The initial step of the data refinement process involved a manual labeling procedure, consisting of the following steps:

– Patch extraction: for each image, multiple patches of varying sizes were extracted. The guiding principle for this procedure was to extract patches that were relevant, specifically targeting the largest skin-only patch that contained a significant portion of diseased skin. Throughout this process, special care was taken to exclude personally identifiable regions of the body, including facial features and other sensitive areas like skin marks.

– Mask labelling: for each of the previously extracted patches, a binary mask was created. The purpose is to indicate which areas of the skin within the patch exhibited the presence of the disease.

Fixed-size patches generation
"""""""""""""""""""""""""""""

Although the data has undergone significant cleaning, its variable-sized nature prevents its direct utilization by ML models. As a result, a second round of refinement was implemented, this time employing an automatic approach. The primary objective at this stage is to extract fixedsize patches from the existing variable-sized ones, ensuring that diseased skin regions are adequately represented.

Coloured mask generation
""""""""""""""""""""""""

Even after implementing the aforementioned refinement steps, a significant portion of the extracted patches still exhibited undesirable properties, such as poor lighting or blurriness. To address this, an automatic filtering process was applied to eliminate patches with low contrast, common features of both poorly exposed and blurry images. For each of these patches, a binary mask was generated based on the provided labelling. However, inspired by the approach presented in [9]_, we extract a coloured mask as well. This coloured mask was obtained by filling the 0 and 1 regions of the binary mask with the dominant colour found in the corresponding part of the original image. Following these procedures, a total of 8,204 patches were successfully extracted from the initial set of 284 variable-sized images. However, 1,118 patches were discarded due to inadequate contrast. Despite these refinement steps, the dataset cannot be considered entirely clean. Upon closer examination, it was observed that a significant number of images still suffered from poor exposure, and the quality of the masks was often suboptimal. These factors must be taken into account when applying any type of model to this dataset.


For more information, please refer to https://link.springer.com/chapter/10.1007/978-3-031-63592-2_5.

.. _hc1-exp:

Experimentation and results
---------------------------

Experiments conducted within the AEQUITAS framework and experimentation environment, leading to the best solution for HC1, can be found at the following links.

* `Bias Detection <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/HC1_Bias_Detection.pdf>`_

* `Full Experimentation Pipeline within AEQUITAS <https://apice.unibo.it/xwiki/bin/download/Aequitas/Deliverables/HC1_Full_Experimentation_Pipeline.pdf?rev=1.1>`_

.. rubric:: References

.. [1] Barhoumi,W.,Khelifa,A.:Skinlesionimageretrievalusingtransferlearning-based approach for query-driven distance recommendation. Computers in Biology and Medicine 137, 104,825 (2021)
.. [2] Bhadula, S., Sharma, S., Juyal, P., Kulshrestha, C.: Machine learning algorithms based skin disease detection. International Journal of Innovative Technology and Exploring Engineering (IJITEE) 9(2), 4044–4049 (2019)
.. [3] Brinker, T.J., Hekler, A., Utikal, J.S., Grabe, N., Schadendorf, D., Klode, J., Berk- ing, C., Steeb, T., Enk, A.H., Von Kalle, C.: Skin cancer classification using convolutional neural networks: systematic review. Journal of medical Internet research 20(10), e11,936 (2018)
.. [4] Chai, J., Zeng, H., Li, A., Ngai, E.W.: Deep learning in computer vision: A critical review of emerging techniques and application scenarios. Machine Learning with Applications 6, 100,134 (2021)
.. [5] Chan, S., Reddy, V., Myers, B., Thibodeaux, Q., Brownstone, N., Liao, W.: Ma- chine learning in dermatology: current applications, opportunities, and limitations. Dermatology and therapy 10, 365–386 (2020)
.. [7] Chlap, P., Min, H., Vandenberg, N., Dowling, J., Holloway, L., Haworth, A.: A review of medical image data augmentation techniques for deep learning applications. Journal of Medical Imaging and Radiation Oncology 65(5), 545–563 (2021)
.. [9] Ghorbani, A., Natarajan, V., Coz, D., Liu, Y.: Dermgan: Synthetic generation of clinical skin images with pathology (2019)
.. [10] Göç̧eri, E.: Convolutional neural network based desktop applications to classify dermatological diseases. In: 2020 IEEE 4th International Conference on Image Processing, Applications and Systems (IPAS), pp. 138–143. IEEE (2020)
.. [15] Jaworek-Korjakowska, J., Yap, M.H., Bhattacharjee, D., Kleczek, P., Brodzicki, A., Gorgon, M.: Deep neural networks and advanced computer vision algorithms in the early diagnosis of skin diseases. In: State of the Art in Neural Networks and Their Applications, pp. 47–81. Elsevier (2023)
.. [17] Kebaili, A., Lapuyade-Lahorgue, J., Ruan, S.: Deep learning approaches for data augmentation in medical imaging: A review. Journal of Imaging 9(4), 81 (2023)
.. [18] Kim, M., Yun, J., Cho, Y., Shin, K., Jang, R., Bae, H.j., Kim, N.: Deep learning in medical imaging. Neurospine 16(4), 657 (2019)
.. [20] Li, Z., Koban, K.C., Schenck, T.L., Giunta, R.E., Li, Q., Sun, Y.: Artificial intelligence in dermatology image analysis: current developments and future trends. Journal of Clinical Medicine 11(22), 6826 (2022)
.. [26] Thambawita, V., Salehi, P., Sheshkal, S.A., Hicks, S.A., Hammer, H.L., Parasa, S., Lange, T.d., Halvorsen, P., Riegler, M.A.: Singan-seg: Synthetic training data generation for medical image segmentation. PloS one 17(5), e0267,976 (2022)
.. [28] Wells, A., Patel, S., Lee, J.B., Motaparthi, K.: Artificial intelligence in dermatopathology: Diagnosis, education, and research. Journal of Cutaneous Pathology 48(8), 1061–1068 (2021)
.. [29] Wen,Y.,Chen,L.,Deng,Y.,Zhou,C.:Rethinkingpre-trainingonmedicalimaging. Journal of Visual Communication and Image Representation 78, 103,145 (2021)
