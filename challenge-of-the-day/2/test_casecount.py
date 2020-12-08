import pytest
import casecount

def test():
    assert str(casecount.case("Hello world!")) == "UPPER 1\nLOWER 9"