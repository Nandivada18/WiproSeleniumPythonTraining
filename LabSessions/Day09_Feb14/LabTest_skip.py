import pytest
import sys

#1.Skipped Featured not implemented
@pytest.mark.skip(reason = "Feature not implemented yet")
def test_feature():
    print()

#2. Runs only on linux
@pytest.mark.skipif(sys.platform != "linux",reason = "Runs only on Linux")
def test_linux():
    print()

#3.checks on API health endpoint if status = 200 skip the test
import requests

def test_api():
    response = requests.get("https://videogamedb.uk:443/api/v2/videogame")
    #If API is not healthy then skip dynamically
    if response.status_code != 200:
        pytest.skip(f"API not healthy. Status code: {response.status_code}")
    #If healthy so continue validation
    assert response.status_code == 200