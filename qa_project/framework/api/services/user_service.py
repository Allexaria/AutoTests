class UserService:
    def __init__(self, client):
        self.client = client

    def login(self, email, password):
        return self.client.post("/verifyLogin", data={"email": email, "password": password})

    def login_without_email(self, password):
        return self.client.post("/verifyLogin", data={"password": password})

    def login_wrong_method(self, email, password):
        return self.client.delete("/verifyLogin", data={"email": email, "password": password})

    def create_account(self, user_data):
        return self.client.post("/createAccount", data=user_data)

    def update_account(self, user_data):
        return self.client.put("/updateAccount", data=user_data)

    def delete_account(self, email, password):
        return self.client.delete("/deleteAccount", data={"email": email, "password": password})

    def get_user_detail_by_email(self, email):
        return self.client.get("/getUserDetailByEmail", params={"email": email})
