from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.schema import validate_json_schema
from tools.fakers import get_random_email

public_user_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string"
)
create_user_response = public_user_client.create_user(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()

user_id = create_user_response.user.id

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_user_client = get_private_users_client(authentication_user)

get_user_response = private_user_client.get_user_api(user_id=user_id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)
