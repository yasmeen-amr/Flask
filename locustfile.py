from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def add_to_cart(self):
        # Simulate adding a product to the cart by sending a POST request
        response = self.client.post('/cart/add', json={"product_id": 1, "quantity": 1})

        # Check if the request was successful (status code 201)
        if response.status_code == 201:
            self.environment.events.request_success.fire(request_type="POST", name="/cart/add", response_time=response.elapsed.total_seconds(), response_length=len(response.content))
        else:
            self.environment.events.request_failure.fire(request_type="POST", name="/cart/add", response_time=response.elapsed.total_seconds(), exception=None, response_length=0)

    # Add more tasks to simulate different user behaviors
