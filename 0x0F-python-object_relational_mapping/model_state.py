"""Defines the State class and creates the Base instance
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state in the database.

    This class represents a state in the database,links to the 'states' table
    and defines two columns: 'id' and 'name'.

    Attributes:
        id (int): The unique id of the state.
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # This code will only run when the script is executed directly
    pass  # You can add any additional code to be executed here if needed
