from langchain.pydantic_v1 import Field, BaseModel


class Property(BaseModel):
    """A single property consisting of key and value"""

    key: str = Field(..., description="key")
    value: str = Field(..., description="value")
