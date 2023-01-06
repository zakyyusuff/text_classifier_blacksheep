
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, IntEnum
from typing import List
from uuid import UUID

class Type_of_df(Enum):
    v1 = 'type'
    v2 = 'text'


@dataclass
class TextClassifier:
    v1: str
    v2: str

