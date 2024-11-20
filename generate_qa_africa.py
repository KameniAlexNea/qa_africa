import os
import random
import uuid
from concurrent.futures import ThreadPoolExecutor
from glob import glob

from tqdm import tqdm
import ollama

from generator.prompts import *
from generator.utils import *

# from generator.gen_dataclass import *

print(os.getpid(), "Process PID")

k = 3
n_choice = 100

BASE_FOLDER = "QuestionsCameroon/Smollm3B"
N_QUESTION = 5

model_name = "qwen2.5:latest"


def make_predictions(example: str):
    try:
        messages = [
            {
                "role": "system",
                "content": system,
            },
            {
                "role": "user",
                "content": human.format().format(
                    N_QUESTION=N_QUESTION,
                    CONTEXT=example,
                    FORMAT=format_text,
                    SOURCE=folder,
                ),
            },
        ]
        name = str(uuid.uuid4()) + ".txt"
        name = os.path.join(BASE_FOLDER, folder, name)

        result = ollama.chat(
            model=model_name,
            messages=messages,
        )[
            "message"
        ]["content"]
        with open(name, "w") as file:
            file.write(f"<context>\n{example}\n<\context>\n\n")
            file.write(result)  # mode="json"
    except:
        print("Fails", example)


folders = glob("histoire_cameroun/*")

files = {os.path.basename(folder): get_dataset(folder) for folder in folders}

total = sum(len(i) for i in files.values())
sizes = {folder: len(i) / total for folder, i in files.items()}
sizes = {
    f: max(1, min(int(round(r * n_choice)), len(files[f]))) for f, r in sizes.items()
}

for folder in sizes:
    os.makedirs(
        os.path.join(
            BASE_FOLDER,
            folder,
        ),
        exist_ok=True,
    )

for folder, size in sizes.items():
    # texts = ["\n\n".join(random.sample(files[folder], k=k)) for _ in range(size)]
    pos = set([random.randint(0, len(files[folder])) for _ in range(size)])

    texts = ["\n\n".join(files[folder][i : i + k]) for i in pos]

    print(pos)
    print("\n\nStarting", folder)
    with ThreadPoolExecutor(max_workers=2) as executor:
        res = list(tqdm(executor.map(make_predictions, texts), total=len(texts)))
