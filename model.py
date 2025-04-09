import decouple
from transformers import pipeline

model = decouple.config("MODEL_ID")

context = """
'Task 1: Is It a Bird? 300 Karma points

hello guys my name is nayan.

In this task, you will learn how to build your first machine-learning model that identifies whether an image consists of a bird, using Kaggle and Jupyter Notebook.

Check out: https://course.fast.ai/Lessons/lesson1.html

After completing this task, upload your notebook to GitHub and share the hosted GitHub repository URL in the #⁠ai channel using the hashtag #cl-ai-birdmodel to avail 300 karma points.'
"""

question = "What kind of advantage do I get when I complete this task?"  # True

# question = "How many karma do I get for completing this task?" # True

# question = "Where should I submit this task?" # False

# question = "who create this task?" # True

# question = "could you provide any resource for it?" # False

# question = "any reference for solve this task?" # False

# question = "what is karma?" # False

# question = "please provide any website for complete this task?" # False

# question = "tag i need to submit this problem" # True

# question = "which type domain is this" # False

# question = "which task is this?" # False

# question = "which task label?" # False

qa = pipeline("question-answering", model=model)

result = qa(question=question, context=context)
print(result["answer"])
