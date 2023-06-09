import pytest
from tests.constants import FILE_PATH
from player.core import load


@pytest.mark.unit
def test_load_positive_len_list():
    assert len(load(FILE_PATH)) == 3



@pytest.mark.unit
def test_load_positive_start_str():
    assert load(FILE_PATH)[0][0] == "b"
