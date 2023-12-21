from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///C:/Users/User/PycharmProjects/Elf/data.db', echo=True)

Base = declarative_base()


class Dog(Base):
    __tablename__ = "Dogs"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    breed = Column(String)
    owner = Column(String)

    def __repr__(self):
        return f"<Dog(name='{self.name}', age='{self.age}', breed='{self.breed}', owner='{self.owner}')>"


Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

dog1 = Dog(name="Sweety", age=8, breed="Toy Terrier", owner="May")
dog2 = Dog(name="May", age=1, breed="Chihuahua", owner="John")
dog3 = Dog(name="Rain", age=3, breed="dachshund", owner="Rich")

session.add(dog1)
session.add(dog2)
session.add(dog3)

session.commit()

users = session.query(Dog).all()
for dog in users:
    print(dog)