from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.adress import Address
from models.base import Base
from models.user import User

# Create an engine to connect to a SQLite database
engine = create_engine('sqlite:///example.sqlite', echo=True)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create some users and addresses
user1 = User(name='John Doe', email='john@example.com')
address1 = Address(country='Ukraine', street='123 Main St', city='Springfield', zip_code='12345', user=user1)
user1.addresses.append(address1)

user2 = User(name='Jane Smith', email='jane@example.com')
address2 = Address(country='Ukraine', street='456 Elm St', city='Riverside', zip_code='54321', user=user2)
user2.addresses.append(address2)

# Add the users and addresses to the session
session.add_all([user1, user2])
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(f"User: {user.name}, Email: {user.email}")
    for address in user.addresses:
        print(f"Address: {address.street}, {address.city}, {address.zip_code}")
