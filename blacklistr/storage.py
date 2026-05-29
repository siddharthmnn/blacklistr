import json
from pathlib import Path
from datetime import datetime


CASES_DIR = Path("cases")


def save_case(data):
    CASES_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = CASES_DIR / f"case_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return filename
