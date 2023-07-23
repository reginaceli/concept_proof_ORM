import re

def check_valid_email(address):

    regex_check_email = re.compile(
        r"^\w+(?:[!#$%&'*+/=?^_`{|}~.-]\w+)*@\w+(?:[-._]\w+)*\.\w{2,}$", flags=re.M)

    is_valid = re.findall(regex_check_email, address)

    return bool(is_valid)


