from typing import TypedDict

from playwright.sync_api import Playwright
import pytest
from typing import TypedDict 


class User(TypedDict):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict   



@pytest.mark.api
def test_post_user(playwright: Playwright):
    request=playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com/")

    respose=request.post("users", data={
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    })
