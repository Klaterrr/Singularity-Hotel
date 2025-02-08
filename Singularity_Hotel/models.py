from sqlalchemy import Date, Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import user
from .database import Base






class Hotel(Base):
  __tablename__ = "hotels"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  address = Column(String)
  phone = Column(String)
  total_budget = Column(Integer)
  monthly_expenses = Column(Integer)

  rooms = relationship("Room", back_populates="hotel")
  staffs = relationship("Staff", back_populates="hotel")

class Room(Base):
  __tablename__ = "rooms"

  id = Column(Integer, primary_key=True, index=True)
  hotel_id = Column(Integer, ForeignKey("hotels.id"))
  room_number = Column(Integer)
  type = Column(String)
  price = Column(DECIMAL)

  hotel = relationship("Hotel", back_populates="rooms")
  reservations = relationship("Reservation", back_populates="room")

class Guest(Base):
  __tablename__ = "guests"

  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String)
  last_name = Column(String)
  email = Column(String)
  phone = Column(String)

  reservations = relationship("Reservation", back_populates="guest")

class Staff(Base):
  __tablename__ = "staffs"

  id = Column(Integer, primary_key=True, index=True)
  first_name = Column(String)
  last_name = Column(String)
  position = Column(String)
  hotel_id = Column(Integer, ForeignKey("hotels.id"))
  salary = Column(Integer)

  hotel = relationship("Hotel", back_populates="staffs")
  administrators = relationship("User", back_populates="staff")

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  password = Column(String)
  email = Column(String)
  reserve_codes = Column(String)
  known_ips = Column(String)
  guest_id = Column(Integer, ForeignKey("guests.id"))

  guest = relationship("Guest", back_populates="users")
  

class Admin(Base):
  __tablename__ = "admins"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  staff_id = Column(Integer, ForeignKey("staffs.id"))
  hotel_id = Column(Integer, ForeignKey("hotels.id"))
  
  staff = relationship("Staff", back_populates="admins")
  hotel = relationship("Hotel", back_populates="admins")

class Reservation(Base):
  __tablename__ = "reservations"

  id = Column(Integer, primary_key=True, index=True)
  guest_id = Column(Integer, ForeignKey("guests.id"))
  room_id = Column(Integer, ForeignKey("rooms.id"))
  check_in_date = Column(Date)
  check_out_date = Column(Date)
  number_of_guests = Column(Integer)
  total_price = Column(DECIMAL)

  guest = relationship("Guest", back_populates="reservations")
  room = relationship("Room", back_populates="reservations")
  payments = relationship("Payment", back_populates="reservation")

class Payment(Base):
  __tablename__ = "payments"

  id = Column(Integer, primary_key=True, index=True)
  reservation_id = Column(Integer, ForeignKey("reservations.id"))
  amount = Column(DECIMAL)
  payment_date = Column(Date)
  payment_method = Column(String)

  reservation = relationship("Reservation", back_populates="payments")

class Inventory(Base):
  __tablename__ = "inventories"

  id = Column(Integer, primary_key=True, index=True)
  item_name = Column(String)
  quantity = Column(Integer)
  hotel_id = Column(Integer, ForeignKey("hotels.id"))
  cost = Column(Integer)

  hotel = relationship("Hotel")
