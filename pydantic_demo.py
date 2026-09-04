from pydantic import BaseModel, EmailStr, Field


# ==========================================
# Ex - 1
# ==========================================
class Book(BaseModel):
    title: str
    author: str
    price: float
    pages: int


book_1 = Book(
    title="Subtle Art of Not Giving a #### !",
    author="Mark Manson",
    price="500",
    pages="500",
)

print(book_1)
print(type(book_1.price))
print("==========================================")


# ==========================================
# Ex - 2
# ==========================================


class Movie(BaseModel):
    name: str
    rating: float
    languages: list[str]


movie_1 = Movie(name="The Odyssey", rating="10.000", languages=["english", "hindi"])

print(movie_1)
print("==========================================")

# ==========================================
# Ex - 3
# ==========================================


class Employee(BaseModel):
    name: str
    salary: float = Field(gt=0)
    experience: int = Field(ge=0)
    email: EmailStr


# emp_1 = Employee(
#     name="Tyler", salary="250k", experience=2, email="tyler.durdern@live.com"
# )
emp_2 = Employee(
    name="Tyler", salary="250000", experience=2, email="tyler.durdern@live.com"
)

print(emp_2)
print("==========================================")

# ==========================================
# Ex - 4
# ==========================================


class Address(BaseModel):
    city: str
    state: str
    pincode: str = Field(max_length=6, min_length=6)


class Company(BaseModel):
    name: str
    founder: str
    address: Address


comp_1 = Company(
    name="NxtWave",
    founder="Costco",
    address={"city": "Hyderbad", "state": "TL", "pincode": "600014"},
)

print(comp_1)
print("==========================================")

# ==========================================
# Ex - 4
# ==========================================


class Order(BaseModel):
    order_id: int
    customer_name: str
    phone: str = Field(max_length=10, min_length=10)
    items: list[str]
    total_price: float = Field(gt=0)
    address: Address


order_1 = Order(
    order_id="1",
    customer_name="venkat",
    phone="9999999499",
    items=["socks", "pens", "plates"],
    total_price=900,
    address=Address(city="Hyd", state="TL", pincode="600014"),
)

print(order_1)
print("==========================================")
