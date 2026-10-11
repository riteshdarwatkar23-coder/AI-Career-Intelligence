from pydantic import BaseModel, Field, field_validator


class Job(BaseModel):
    title: str = Field(min_length=1)
    company: str = Field(min_length=1)
    location: str = Field(min_length=1)

    @field_validator("title", "company", "location")
    @classmethod
    def reject_whitespace_only(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Field cannot contain only spaces")
        return value