from faker import Faker

fake = Faker()


def create_user():
    return {
        "name": fake.first_name(),
        "email": fake.unique.email(),
        "password": fake.password(),
        "title": fake.random_element(elements=("Mr", "Mrs", "Miss")),
        "birth_date": str(fake.random_int(min=1, max=28)),
        "birth_month": fake.month_name(),
        "birth_year": str(fake.random_int(min=1950, max=2005)),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "company": fake.company(),
        "address1": fake.street_address(),
        "address2": fake.secondary_address(),
        "country": fake.country(),
        "zipcode": fake.postcode(),
        "state": fake.state(),
        "city": fake.city(),
        "mobile_number": fake.phone_number(),
    }
