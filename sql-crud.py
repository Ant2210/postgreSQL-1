from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from postgres_settings import postgres_settings1 as settings

# Executing the instruction from our localhost "chinook" db
db = create_engine(
    f"postgresql://{settings['user']}:{settings['pass']}@{settings['host']}:{settings['port']}/{settings['db']}"
)
base = declarative_base()


# Create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Instead of connecting to the database directly, we will ask for a session
# Create a new instance of the sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# Opens an actual session by calling the Session() subclass defined above
session = Session()

# Creating the database using the declarative_base subclass
base.metadata.create_all(db)

# Create records on our "Programmer" table
# ada_lovelace = Programmer(
#     first_name = "Ada",
#     last_name = "Lovelace",
#     gender = "F",
#     nationality = "British",
#     famous_for = "First Programmer"
# )

# alan_turing = Programmer(
#     first_name = "Alan",
#     last_name = "Turing",
#     gender = "M",
#     nationality = "British",
#     famous_for = "Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name = "Grace",
#     last_name = "Hopper",
#     gender = "F",
#     nationality = "American",
#     famous_for = "COBOL Language"
# )

# margaret_hamilton = Programmer(
#     first_name = "Margaret",
#     last_name = "Hamilton",
#     gender = "F",
#     nationality = "American",
#     famous_for = "Apollo 11"
# )

# bill_gates = Programmer(
#     first_name = "Bill",
#     last_name = "Gates",
#     gender = "M",
#     nationality = "American",
#     famous_for = "Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name = "Tim",
#     last_name = "Berners-Lee",
#     gender = "M",
#     nationality = "British",
#     famous_for = "World Wide Web"
# )

# ant_griffiths = Programmer( 
#     first_name="Ant",
#     last_name="Griffiths",
#     gender="M",
#     nationality="Welsh",
#     famous_for="Awesome",
# )

# add each instance of our programmers to our session
# session.add(ant_griffiths)

# # commit our session to the database
# session.commit()

# Updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# # commit our session to the database
# session.commit()

# Updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # Defensive programming
# if programmer is not None:
#     print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records found")

# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# Query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | ",
    )