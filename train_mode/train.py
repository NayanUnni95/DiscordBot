from transformers import (
    AutoTokenizer,
    AutoModelForQuestionAnswering,
    TrainingArguments,
    Trainer,
)
from datasets import Dataset

context = """
Task 1: Is It a Bird? 300 Karma points

hello guys my name is nayan.

In this task, you will learn how to build your first machine-learning model that identifies whether an image consists of a bird, using Kaggle and Jupyter Notebook.

Check out: https://course.fast.ai/Lessons/lesson1.html

After completing this task, upload your notebook to GitHub and share the hosted GitHub repository URL in the #⁠ai channel using the hashtag #cl-ai-birdmodel to avail 300 karma points.
"""

examples = [
    {
        "question": "What kind of advantage do I get when I complete this task?",
        "context": context,
        "answers": {"text": ["300 karma points"], "answer_start": [27]},
    },
    {
        "question": "How many karma do I get for completing this task?",
        "context": context,
        "answers": {"text": ["300 karma points"], "answer_start": [27]},
    },
    {
        "question": "Where should I submit this task?",
        "context": context,
        "answers": {"text": ["#⁠ai channel"], "answer_start": [276]},
    },
    {
        "question": "Tag I need to submit this problem?",
        "context": context,
        "answers": {"text": ["#cl-ai-birdmodel"], "answer_start": [316]},
    },
]

dataset = Dataset.from_list(examples)

model_checkpoint = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)


def preprocess(example):
    return tokenizer(
        example["question"],
        example["context"],
        truncation=True,
        padding="max_length",
        max_length=384,
        return_offsets_mapping=True,
    )


tokenized_dataset = dataset.map(preprocess)


model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)

training_args = TrainingArguments(
    output_dir="./qa-model",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    evaluation_strategy="no",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
)

trainer = Trainer(model=model, args=training_args, train_dataset=tokenized_dataset)

trainer.train()

trainer.save_model("./my_finetuned_qa_model")
tokenizer.save_pretrained("./my_finetuned_qa_model")
