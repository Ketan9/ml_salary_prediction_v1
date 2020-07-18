# to test if flask index functions working fine
from app import index
def test_index():
    assert index() == "Flask Index function works fine"

