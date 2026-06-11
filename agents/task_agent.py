from pathlib import Path
from datetime import datetime

TASKS_DIR = Path("storage/tasks")

TASKS_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def create_task(content):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = TASKS_DIR / f"task_{timestamp}.txt"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return f"Tarefa salva em {filename.name}"

def list_tasks():

    files = sorted(TASKS_DIR.glob("*.txt"))

    if not files:
        return "Nenhuma tarefa encontrada."

    result = []

    for index, file in enumerate(files, start=1):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            content = f.read().strip()

        result.append(
            f"{index}. {content}"
        )

    return "\n".join(result)

