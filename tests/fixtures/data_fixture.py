import json
from pathlib import Path

import pytest

DATA_DIRECTORY = Path(__file__).resolve().parents[1] / "data"


def _load_json(filename: str) -> dict:
    path = DATA_DIRECTORY / filename
    with path.open(encoding="utf-8") as data_file:
        return json.load(data_file)


@pytest.fixture
def login_data() -> dict:
    return _load_json("login_data.json")


@pytest.fixture
def checkout_data() -> dict:
    return _load_json("checkout_data.json")
