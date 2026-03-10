from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdNabuStore:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_search_and_add_to_cart(self):

        driver = self.driver

        # Open website
        driver.get("https://adnabuteststore.myshopify.com")

        # Search product
        search_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("T-shirt")
        search_box.submit()

        # Select first product
        product = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item"))
        )
        product.click()

        # Add product to cart
        add_to_cart = self.wait.until(
            EC.element_to_be_clickable((By.NAME, "add"))
        )
        add_to_cart.click()

        # Verify cart page
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/cart']"))
        )

        assert cart_icon.is_displayed()

    def teardown_method(self):
        self.driver.quit()
