from locust import HttpUser, task, between


# Locust User class
class CouponUser(HttpUser):
    wait_time = between(1, 3)  # Time between consecutive tasks

    @task
    def view_coupon(self):
        # Simulate users accessing the coupon endpoint
        self.client.get(
            "/search_coupons/?csrfmiddlewaretoken=b3jN84b9zfWwsO4CjMgRAYLXyFpHtEi02OrhzXMU4gb7v9uuxYgeX64D5ParPmKJ&search_query=test"
        )
