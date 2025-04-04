import pytest

@pytest.fixture()
def before_after():
    print('\nПредусловие')
    yield
    print('\nПостусловие')


def test_demo (before_after):
    assert 1 == 1

def test_demo2 (before_after):
    assert 2 == 1


