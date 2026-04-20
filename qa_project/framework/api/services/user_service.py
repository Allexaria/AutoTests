from qa_project.framework.api.schemas import (
    AuthResponse,
    CreateAccountResponse,
    DeleteAccountResponse,
)


class UserService:
    def __init__(self, client):
        self.client = client

    def login(self, email, password):
        return self.client.post("/verifyLogin", data={"email": email, "password": password})

    def login_validated(self, email, password):
        response = self.login(email=email, password=password)
        return response, AuthResponse.model_validate(response.json())

    def login_without_email(self, password):
        return self.client.post("/verifyLogin", data={"password": password})

    def login_wrong_method(self, email, password):
        return self.client.delete("/verifyLogin", data={"email": email, "password": password})

    def create_account(self, user_data):
        return self.client.post("/createAccount", data=user_data)

    def create_account_validated(self, user_data):
        response = self.create_account(user_data)
        return response, CreateAccountResponse.model_validate(response.json())

    def update_account(self, user_data):
        return self.client.put("/updateAccount", data=user_data)

    def delete_account(self, email, password):
        return self.client.delete("/deleteAccount", data={"email": email, "password": password})

    def delete_account_validated(self, email, password):
        response = self.delete_account(email=email, password=password)
        return response, DeleteAccountResponse.model_validate(response.json())

    def get_user_detail_by_email(self, email):
        return self.client.get("/getUserDetailByEmail", params={"email": email})
