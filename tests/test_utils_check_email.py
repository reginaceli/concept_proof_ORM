import pytest
from player.utils.email import check_valid_email

@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["example-indeed@strange-example.com",
    "firstname.lastname@example.com",
    "email@subdomain.example.co",
    "example@s.example",
    "1234567890@example.com"]
    )
def test_positive_valid_email(address):
    """Test validates as email address

    valid
    example-indeed@strange-example.com
    firstname.lastname@example.com
    email@subdomain.example.co
    example@s.example
    1234567890@example.com
    """

    assert check_valid_email(address) is True



@pytest.mark.unit
@pytest.mark.parametrize(
    "address",
    ["<email@example.com>",
    "email.example.com",
    "email@example@example-com",
    "this is\allowed@example.com"]
    )
def test_negative_valid_email(address):
    """Test validates as email address

    invalid
    <email@example.com>
    email.example.com
    email@example@example.com
    this is\allowed@example.com
    """

    assert check_valid_email(address) is False
