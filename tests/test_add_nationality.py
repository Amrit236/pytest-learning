import pytest
from playwright.sync_api import Page

def add_nationality(name):
    if not name:
        raise ValueError("Name is required")
    return f"{name} added successfully"



from nationality import add_nationality


def test_add_nationality_success():
    result = add_nationality("Canadian")
    assert result == "Canadian added successfully"


def test_add_nationality_empty():
    with pytest.raises(ValueError):
        add_nationality("")
