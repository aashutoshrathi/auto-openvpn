import pytest
import openvpn.makeIt as mk

def test_account():
    fake = mk.login("akkad")
    assert(fake == "test")
