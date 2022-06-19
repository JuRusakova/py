import pytest
from fixture.application import Application

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

# function for parametrise all test functions
def pytest_generate_tests(metafunc):  # metafunc - info about all fixtures
    for fixture in metafunc.fixturenames:  # find your fixture
        if fixture.startswith("exel_"):
            testdata = load_from_exel(fixture[5:])  # load data from file(where name beginning after 5 symbols)
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])  # where, from, presentation


# import testdata from module
def load_from_exel(file):
    groups = []
    # path to file
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.xlsx")
    xl = CreateObject("Excel.Application")
    xl_book = xl.Workbooks.Open(file_path)
    book_list = xl_book.Worksheets("Лист1")
    for i in range(3):
        groups.append(book_list.Range(f"A{i + 1}").Value[()])
    xl.Quit()
    return groups