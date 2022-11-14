# 1. py.test - This command is used to execute all tests
# 2. py.test -v : This command is used to execute our tests and
#               also will include the information fer tests explicitly where
#               it will tell wheather it passed or failed.
# 3. py.test -s : This command is used to show logs after execution.
# py.test -k car -v -s
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_my_very_firstProgramm():
    message = "Hello World"
    assert "ju" in message

@pytest.mark.smoke
@pytest.mark.xfail
def test_my_very_firstProgramm():
    msg = "Hello World"
    assert "Hello World" == msg
    print(msg)
