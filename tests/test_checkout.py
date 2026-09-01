from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import BASE_URL


def test_complete_checkout(driver, wait):

    driver.get(BASE_URL)

    # Add product to cart
    products_page = ProductsPage(driver, wait)
    products_page.select_product("Samsung galaxy s6")
    products_page.add_to_cart()

    # Open cart
    cart_page = CartPage(driver, wait)
    cart_page.open_cart()

    # Open Place Order form
    checkout_page = CheckoutPage(driver, wait)
    checkout_page.open_place_order()

    # Enter customer details
    checkout_page.enter_order_details(
        "Vishal",
        "India",
        "Jabalpur",
        "4111111111111111",
        "09",
        "2026"
    )

    # Purchase
    checkout_page.purchase_order()

    # Verify confirmation
    confirmation = checkout_page.get_order_confirmation()

    assert confirmation == "Thank you for your purchase!"