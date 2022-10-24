from app import hello_world

def test_index():
    assert hello_world() == 'Hello'