# AdNabu QA Assignment – Test Cases

## Feature 1: Product Search

### TC01 – Search for a valid product (Positive)
Steps:
1. Open AdNabuTestStore website
2. Enter "T-shirt" in search bar
3. Click Search

Expected Result:
Relevant products related to "T-shirt" should be displayed.

---

### TC02 – Search for a non-existing product (Negative)
Steps:
1. Open website
2. Enter "abcd1234xyz"
3. Click Search

Expected Result:
System should display message such as "No products found".

---

### TC03 – Search with empty input (Edge Case)
Steps:
1. Open website
2. Leave search field empty
3. Click Search

Expected Result:
System should either show all products or prompt user to enter search keyword.

---

## Feature 2: Add to Cart

### TC04 – Add product to cart successfully (Positive)
Steps:
1. Search for a product
2. Select any available product
3. Click "Add to Cart"

Expected Result:
Product should be added to the shopping cart successfully.

---

### TC05 – Add out-of-stock product (Negative)
Steps:
1. Open a product which is out of stock
2. Click "Add to Cart"

Expected Result:
System should prevent adding the product and display "Out of stock".

---

### TC06 – Add multiple quantities of a product (Edge Case)
Steps:
1. Open a product
2. Increase quantity to 3
3. Click "Add to Cart"

Expected Result:
Cart should show the product with quantity = 3.
