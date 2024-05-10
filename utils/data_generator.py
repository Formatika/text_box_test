from faker import Faker


def generate_fake_email():
    return Faker().email()


def generate_name():
    return Faker().name()


def generate_address():
    fake = Faker()
    street_number = fake.building_number()
    street_name = fake.street_name()
    city = fake.city()
    state = fake.state_abbr()
    zip_code = fake.zipcode()
    address = f"{street_number} {street_name}, {city}, {state} {zip_code}"
    return address
