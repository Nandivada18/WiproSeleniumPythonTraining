import pytest

#request  - pytest object that contains information about
#who is calling the fixture and with what data

@pytest.fixture(params=["chrome","Firefox"])
def browser(request):
    print("Current browser:", request.param)
    return request.param

def test_browser(browser):
    assert browser in ["chrome","Firefox"]