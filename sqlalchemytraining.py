from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# connection to existing database
engine = create_engine('postgresql+psycopg2://postgres:#iamAfrica@localhost/employeedata')
# reflect the database tables from the database schema to python objects
Base = automap_base()
# reflect the tables from the existing database schema into python orm models
Base.prepare(engine,reflect = True)
#  The line assigns the existing employees table(reflected from the database) to a python class Employee
# The tables can be accessed through the classes
Employee = Base.classes.employees
# Create a session to manage the connection
Session = sessionmaker(bind = engine)
session = Session()
#  query all the employees
employees = session.query(Employee).all()
#  loop through and print the employee
for employee in employees :
    print(f"ID: {employee.employeeid}, firstname: {employee.firstname}, lastname: {employee.lastname}, Email:{employee.email},City:{employee.city}")