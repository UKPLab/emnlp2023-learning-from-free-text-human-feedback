# Learning From Free-Text Human Feedback – Collect New Datasets Or Extend Existing Ones?
This repository provides the code for our paper _Learning From Free-Text Human Feedback – Collect New Datasets Or Extend Existing Ones?_. It is an experimental software and is published for the sole purpose of giving additional background details on the publication. This is a cleaned-up and condensed version of what was used to conduct the experiments in the paper (please get in touch if you find errors).

## Citation
Please reference our work as follows:

```
@inproceedings{petrak-etal-2023-learning,
    title = "Learning From Free-Text Human Feedback {--} Collect New Datasets Or Extend Existing Ones?",
    author = "Petrak, Dominic and Moosavi, Nafise and Tian, Ye and Rozanov, Nikolai and Gurevych, Iryna",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.1011",
    doi = "10.18653/v1/2023.emnlp-main.1011",
    pages = "16259--16279",    
}
```

## Project Descriptions

Learning from free-text human feedback is essential for dialog systems, but annotated data is scarce and usually covers only a small fraction of error types known in conversational AI. Instead of collecting and annotating new datasets from scratch, recent advances in synthetic dialog generation could be used to augment existing dialog datasets with the necessary annotations. However, to assess the feasibility of such an effort, it is important to know the types and frequency of free-text human feedback included in these datasets. 

In this work, we investigate this question for a variety of commonly used dialog datasets, including MultiWoZ, SGD, BABI, PersonaChat, Wizards-of-Wikipedia, and the human-bot split of the Self-Feeding Chatbot. Using our observations, we derive new taxonomies for the annotation of free-text human feedback in dialogs and investigate the impact of including such data in response generation for three SOTA language generation models, including GPT-2, LLAMA, and Flan-T5. Our findings provide new insights into the composition of the datasets examined, including error types, user response types, and the relations between them

## How To

This repository consists of two sub-directories, __code__ and __data__. The first one contains all scripts related to our automatic filtering approach. The second one contains the annotated data. Please refer to the READMEs in both sub-directories for instructions.

## Contact Persons

Dominic Petrak (<petrak@ukp.informatik.tu-darmstadt.de>)
  
## Links

[UKP Lab Homepage](https://www.ukp.tu-darmstadt.de/) | [TU Darmstadt Website](https://www.tu-darmstadt.de/index.en.jsp)

