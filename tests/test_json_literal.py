from json_literal import *


def test_values() -> None:
    import json_literal

    assert json_literal.null is None
    assert json_literal.true is True
    assert json_literal.false is False


def test_auto_load():
    assert null is None
    assert true is True
    assert false is False
