import pytest
import cotd1

def test():
    assert cotd1.alphabet("hello world and practice makes perfect and hello world again") == ['again', 'and', 'hello', 'makes', 'perfect', 'practice', 'world']