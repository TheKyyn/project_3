from locust import HttpUser, task, between

class BigDataTestUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def get_data(self):
        self.client.get("/data?category=example")

    @task(1)
    def add_data(self):
        self.client.post("/data", json={"data_value": "Test Value", "category": "Test Category"})
