from pathlib import Path
from datetime import datetime

NOTES_DIR = Path("storage/notes")

NOTES_DIR.mkdir(
    parents=True,
    exist_ok=True
)

def create_note(content):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = NOTES_DIR / f"note_{timestamp}.txt"

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    return f"Nota salva em {filename.name}"

def list_notes():

    files = sorted(NOTES_DIR.glob("*.txt"))

    if not files:
        return "Nenhuma nota encontrada."

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