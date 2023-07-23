import pytest
from player.utils.generate_pass import generate_password

@pytest.mark.unit
def test_positive_length_password():
    """Test len for generation a random password by size default"""

    assert  len((generate_password(8)))== 8


@pytest.mark.unit
def test_positive_set_unique_password():
    """Test ensures an unique password for list of passwords"""

    passwords = []
    for _ in range(100):
        passwords.append(generate_password(8))

    # print(passwords)
    assert len(set(passwords)) == 100
