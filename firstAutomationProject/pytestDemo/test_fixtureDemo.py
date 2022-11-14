# import pytest
#
#
# @pytest.fixture()
# def setup():
#     print("This print statement will get executed first")
#     yield
#     print("This statement will be executed last")


def test_fixture_first_program():
    print("This statement will be executed as part of fixture")
