from pydantic import BaseModel, EmailStr, Field, constr


class UserSchema(BaseModel):
    """
    Модель данных пользователя.

    Используется для описания структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.

    Содержит данные, необходимые для создания пользователя.
    """
    email: EmailStr
    password: constr(min_length=1, max_length=250)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
     Схема ответа после создания пользователя.

     Возвращает ответ с данными созданного пользователя.
     """
    user: UserSchema
