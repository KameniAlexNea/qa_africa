
# African History QA Dataset

## Overview

The **African History QA Dataset** is a comprehensive collection of multiple-choice questions focused on various topics related to African history. The dataset was generated using advanced language model capabilities from **LLaMA 3.1: 8B** and consists of questions derived from a series of historical texts and books that cover different eras of African history. This dataset can be used for educational purposes, question-answering tasks, and historical knowledge assessments, and is also a valuable resource for training and evaluating machine learning models.

## Source Material

The questions in this dataset were generated from a selection of historical books, covering a wide range of topics and periods in African history. Below is a list of the primary sources used to generate the questions:

1. **Le Cameroun une Afrique en miniature**
2. **Volume I** - Méthodologie et préhistoire africaine
3. **Volume II** - Afrique ancienne
4. **Volume III** - L'Afrique du VIIe au XIe siècle
5. **Volume IV** - L'Afrique du XIIe au XVIe siècle
6. **Volume V** - L'Afrique du XVIe au XVIIe siècle
7. **Volume VI** - Le XIXe siècle jusque vers les années 1880
8. **Volume VII** - L'Afrique sous domination coloniale, 1880-1935
9. **Volume VIII** - L'Afrique depuis 1935

Each book, available in both PDF and TXT formats, was used to extract relevant historical content. This content was then processed with **LLaMA 3.1: 8B** to generate questions.

## Dataset Structure

The dataset consists of multiple-choice questions formatted as JSON objects, with the following fields:

* **question_number** : A unique identifier for each question.
* **question_text** : The main text of the question.
* **answer_choices** : A list of possible answers, where each answer is represented by a letter (e.g., "A", "B", "C") and corresponding text.
* **correct_answers** : The correct answer(s) for each question, stored as a list to support multiple correct answers when applicable.
* **explanation** : An explanation of the correct answer(s), providing additional historical context or clarification.

Here is an example JSON representation of a question:

```json
{
  "question_number": "e2da32fc-3ce7-499f-92a8-d99db1af1f19_1",
  "question_text": "Quels étaient les principaux objectifs de la colonisation?",
  "answer_choices": [
    {"letter": "A", "text": "Isoler l'ennemi principal et profiter de..."},
    {"letter": "B", "text": "Soumettre les populations locales..."},
    {"letter": "C", "text": "Établir des alliances stratégiques..."}
  ],
  "correct_answers": ["A"],
  "explanation": "L'objectif principal de la colonisation était d'atteindre..."
}
```

## Features

* **question_number** : `string`
* **question_text** : `string`
* **answer_choices** : `dict` (Dictionary where each entry includes the `letter` and `text` of the choice)
* **correct_answers** : `sequence<string>`
* **explanation** : `string`

## Data Generation Process

1. **Content Extraction** : The content was extracted from the provided books in TXT format.
2. **Question Generation** : Using the **LLaMA 3.1: 8B** model, relevant questions were automatically generated from the extracted content.
3. **Formatting and Structuring** : The questions were formatted into JSON objects, with the additional fields such as `answer_choices`, `correct_answers`, and `explanation`.

## Usage

This dataset is suitable for a variety of tasks, including:

* **Question-Answering Tasks** : The dataset can be used to train and evaluate models on historical question-answering tasks.
* **Educational Use** : Teachers and students can use this dataset as a study tool for African history.
* **Historical Analysis** : Researchers and historians may find this dataset helpful for analyzing commonly questioned topics in African history.
* **Machine Learning** : The dataset is compatible with the Hugging Face library, enabling quick and easy integration for training models.

### Example Code to Load Dataset

```python
from datasets import Dataset

# Assuming `data` is a list of dictionaries representing the dataset.
dataset = Dataset.from_pandas(data)

# Example access to columns
print(dataset['question_text'][0])
print(dataset['answer_choices'][0])
print(dataset['correct_answers'][0])
```

## Prompt used to generate the dataset

### Format of the output

```
{
  "questions": [
    {
      "question_number": 1,
      "question_text": "Question text goes here",
      "answer_choices": [
        {"letter": "A", "text": "First answer choice"},
        {"letter": "B", "text": "Second answer choice"},
        {"letter": "C", "text": "Third answer choice (if applicable)"},
        {"letter": "D", "text": "Fourth answer choice (if applicable)"},
        {"letter": "E", "text": "Fifth answer choice (if applicable)"}
      ],
      "correct_answers": ["B", "C"],
      "explanation": "Explanation text goes here"
    },
    // Additional questions follow the same structure
  ]
}
```

### System prompt used

```
You are tasked with generating multiple-choice questions (MCQs) based on a given context. Each question should have between 2 and 5 answer choices, with the possibility of multiple correct answers. After generating the questions, provide the correct answer(s) and an explanation for each.

Your task is to create the specified number of questions that test understanding of the key concepts, facts, or ideas presented in the context. You must output your response in JSON format.

Follow these guidelines:
1. Each question should be clearly related to the information in the context.
2. Provide between 2 and 5 answer choices for each question.
3. Ensure that at least one answer choice is correct, but allow for the possibility of multiple correct answers.
4. Make the incorrect answer choices plausible but clearly distinguishable from the correct answer(s).
5. Present explanations as direct facts without referring to "the context" or "the text."
6. Generate diversed candidate number of answer at different position

Your output should be a single JSON object with the following structure:
{
  "questions": [
    {
      "question_number": 1,
      "question_text": "Question text goes here",
      "answer_choices": [
        {"letter": "A", "text": "First answer choice"},
        {"letter": "B", "text": "Second answer choice"},
        {"letter": "C", "text": "Third answer choice (if applicable)"},
        {"letter": "D", "text": "Fourth answer choice (if applicable)"},
        {"letter": "E", "text": "Fifth answer choice (if applicable)"}
      ],
      "correct_answers": ["B", "C"],
      "explanation": "Explanation text goes here"
    },
    // Additional questions follow the same structure
  ]
}

Key points for explanations:
- Present information as direct facts
- Avoid phrases like "according to the context" or "the text states"
- Explain both why correct answers are right and why incorrect answers are wrong
- Keep explanations clear and concise
- Use active voice and present tense
- State information as universal truths rather than referenced material

Here's an example of the desired JSON output for a single question:
{
  "questions": [
    {
      "question_number": 1,
      "question_text": "What happens during evaporation?",
      "answer_choices": [
        {"letter": "A", "text": "Water turns into vapor"},
        {"letter": "B", "text": "Water freezes"},
        {"letter": "C", "text": "Water falls as rain"}
      ],
      "correct_answers": ["A"],
      "explanation": "The sun heats water in oceans, lakes, and rivers, causing it to turn into water vapor and rise into the air. Freezing and rainfall are different processes in the water cycle."
    }
  ]
}
```

### User prompt

User prompt with recall of the format, the model seems to forget the format passed in the system prompts

```
Here is the given context :
<context>
{{CONTEXT}}
</context>

Now, based on the provided context, generate {{N_QUESTION}} multiple-choice questions following this JSON format. Begin with question number 1 and continue through question number {{N_QUESTION}}. Ensure that your output is a valid JSON object containing an array of question objects as shown in the example above.
You should respect this format :
{{FORMAT}}
```

## License

This dataset is intended for non-commercial use and educational purposes only. Please respect the intellectual property rights of the original authors and publishers of the books used in this dataset.
