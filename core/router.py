from agents.note_agent import create_note, list_notes
from agents.task_agent import create_task, list_tasks
from core.logger import write_log


def process_command(command):

    write_log(command)

    text = command.lower()

    if text == "listar notas":
        return list_notes()

    elif text == "listar tarefas":
        return list_tasks()

    if text.startswith("criar nota"):

        content = (
            command
            .lower()
            .replace("criar nota", "")
            .strip()
        )

        return create_note(content)

    elif text.startswith("criar tarefa"):

        content = (
            command
            .lower()
            .replace("criar tarefa", "")
            .strip()
        )

        return create_task(content)

    return (
        "Não entendi o comando. "
        "Tente usar 'nota' ou 'tarefa'."
    )