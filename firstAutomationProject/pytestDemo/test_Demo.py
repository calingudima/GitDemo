import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureDemo:

    #@pytest.mark.smoke
    def test_my_very_first_car(self):
        print("aaaaa")

    #@pytest.mark.smoke
    def test_my_very_firstProgramm(self):
        print("bbbbbb")

    def test_my_very_second_car(self):
        print("ccccc")

    def test_my_very_firstProgramm2(self):
        print("ddddd")

    def test_my_very_firstProgramm3(self):
        print("eeeee")

    def test_my_very_firstProgramm4(self):
        print("fffff")



