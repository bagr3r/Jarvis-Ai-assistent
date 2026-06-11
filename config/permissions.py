from pathlib import  Path

WORKSPACE = Path("./storage").resolve()

BLOCKED_OPERATIONS = [
    "delete",
    "move",
    "rename"
]