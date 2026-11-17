import pytest
from playwright.sync_api import expect
@pytest.fixture
def logged_in_page(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    return page
def test_add_to_cart(logged_in_page):
    page = logged_in_page
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator("[data-test=\"inventory-item\"]")).to_have_count(2)
    page.locator("[data-test=\"checkout\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("wrong_password")
    page.locator("[data-test=\"password\"]").press("Enter")
    expect(page.locator("[data-test=\"error\"]")).to_have_text("Epic sadface: Username and password do not match any user in this service")
    expect(page).to_have_url("https://www.saucedemo.com/")