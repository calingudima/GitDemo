import pytest
#this file will contian fixtures to intruct before and after the execution
# to use fixtures we need to create methods

@pytest.fixture(scope="class")
def setup():
    print("This print statement will get executed first")
    yield
    print("This statement will be executed last")



# EXTREMELY helpful for cross/browsing testing

@pytest.fixture(params=[("Firstname : Hakim", "Lastname : Bekkour", "Balance : $50000"),
                        ("Firstname : Yulia", "Lastname : Melnyk", "Balance : -$1000")])
def data_sets(request):
    return request.param