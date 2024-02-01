import pytest, os
from api.models import Vocabulary

app_base_url = os.getenv("BASE_URL", "http://127.0.0.1:8000")
env = "Testing"

@pytest.fixture(scope="module")
def default_vocabularies():
    return [
        Vocabulary(
            name="Test 1",
            description="A test vocabulary.",
            short_name="test1",
            local_path=f'{app_base_url}/test1',
            base_uri="http://foo.bar/baz"
        )
    ]