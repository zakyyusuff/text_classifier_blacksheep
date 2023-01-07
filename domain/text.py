from blacksheep.server.openapi.v3 import OpenAPIHandler
from app import *
from openapidocs.v3 import Info
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, IntEnum
from typing import List
from uuid import UUID


# docs = OpenAPIHandler(info=Info(title="Example API", version="0.0.1"))
# docs.bind_app(app)

class Type_of_df(Enum):
    v1 = 'type'
    v2 = 'text'


@dataclass
class TextClassifier:
    v1: str
    v2: str

