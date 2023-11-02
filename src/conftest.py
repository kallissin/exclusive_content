from pytest import fixture
from uuid import uuid4
from datetime import datetime


@fixture
def fixture_content():
    return {
        "content_id": uuid4(),
        "category": "PYTHON",
        "title": "Instalando Python",
        "content": """pip install python""",
        "created_at": datetime.utcnow(),
        "updated_at": None,
    }