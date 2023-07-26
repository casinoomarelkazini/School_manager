from locust import HttpUser, task, between

class OdooUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds between task execution

    @task
    def view_homepage(self):
        # Replace 'http://localhost:8069' with the URL of your Odoo app
        self.client.get("http://localhost:8069/web#action=355&model=school.student&view_type=list&cids=1&menu_id=227")

    @task
    def view_products(self):
        # Replace 'http://localhost:8069' with the URL of your Odoo app
        self.client.get("http://localhost:8069/web#action=357&model=school.teacher&view_type=list&cids=1&menu_id=227")

    @task
    def login(self):
        # Replace 'http://localhost:8069' with the URL of your Odoo app
        # Replace 'your_username' and 'your_password' with actual login credentials
        login_data = {
            "login": "odoo",
            "password": "odoo",
            "db": "odoo"  # Replace 'your_database' with your Odoo database name
        }
        self.client.post("http://localhost:8069/web/login", json=login_data)

    @task
    def add_to_cart(self):
        # Replace 'http://localhost:8069' with the URL of your Odoo app
        # Replace 123 with the product ID you want to add to the cart
        cart_data = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "route": "/shop/cart/update",
                "kwargs": {
                    "product_id": 123,
                    "add_qty": 1
                }
            }
        }
        self.client.post("http://localhost:8069/web#action=357&model=school.teacher&view_type=list&cids=1&menu_id=227/jsonrpc", json=cart_data)
