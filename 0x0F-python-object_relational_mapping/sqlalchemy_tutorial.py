#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///example.db', echo=False)
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "orm_tutorial"), pool_pre_ping=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(100))
    nickname = Column(String(50))
    
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

User.__table__
# print(User.__repr__(User))
Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

new_user1 = User(name='Johnkennedy', fullname='Johnkennedy Umeh', nickname='Johnkenzzy')
new_user2 = User(name='Chukwudum', fullname='Chukwudum Umeh', nickname='Chuks')
session.add(new_user1)
# session.add(new_user2)
# print(new_user1.__repr__)
# print(new_user1.id)
# our_user = session.query(User).filter_by(name='Johnkennedy').first()
# our_user = session.query(User).filter_by(name='Chukwudum').first()
session.add_all([
    User(name='Wendy', fullname='Wendy Williams', nickname='Windy'),
    User(name='Mary', fullname='Mary Contrary', nickname='Mary'),
    User(name='Fred', fullname='Fred Flintstone', nickname='Freddy')])
session.add(new_user2)

print("-----")
print(session.new)

print("-----")
for user in session.query(User).order_by(User.name).all():
    print("{}, {}, {}". format(user.name, user.fullname, user.nickname))

print("-----")
our_user = session.query(User).filter_by(name='Wendy').first()
our_user.fullname = 'Wendy Nkemaknam'
print(session.dirty)
session.commit()
print(our_user.fullname)

for instance in session.query(User).order_by(User.id):
    print(instance.id, ": ", instance.name, instance.fullname)

session.close()
