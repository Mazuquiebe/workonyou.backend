from rest_framework_simplejwt.exceptions import AuthenticationFailed, status, _


class InvalidCredentials(AuthenticationFailed):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _("Invalid credentials")
    default_code = "credentials_not_valid"


class RequiredFields(AuthenticationFailed):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _("username or email is required")
    default_code = "required_field"


class NotFound(AuthenticationFailed):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _("Not found")
    default_code = "not_found"