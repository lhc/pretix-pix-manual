import pytest

from pretix_pix_manual.payment import is_valid_pix_key


@pytest.mark.parametrize(
    "pix_key,is_valid",
    [
        ("some random string", False),
        ("123123123", False),
        ("b7517c20-2d67-4a42-a41e", False),
        ("email@example.com", True),  # E-mail address
        ("85899296000187", True),  # CNPJ
        ("01032624078", True),  # CPF
        ("b7517c20-2d67-4a42-a41e-cfa622d53ec4", True),  # Random key
    ],
)
def test_is_valid_pix_key(pix_key, is_valid):
    assert is_valid_pix_key(pix_key) == is_valid
