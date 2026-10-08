from dataclasses import dataclass
from enum import Enum

class Priority(Enum):
  High = 3
  Medium = 2
  Low = 1
@dataclass
class Task:
  id:int
  priority:Priority
  heading:str
  status: bool = False