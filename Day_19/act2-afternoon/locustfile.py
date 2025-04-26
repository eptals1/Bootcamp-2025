from locust import HttpUser, task

class MyUser(HttpUser):

    @task
    def inner(self):
        self.client.post("/patients-inner-join")

    
    @task
    def left(self):
        self.client.get("/patients-inner-join")

    @task
    def right(self):
        self.client.get("/patients-left-join")