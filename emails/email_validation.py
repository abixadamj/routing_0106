def validate_my_email(email: str) -> bool:
    """testy emaila, jeśli któryś będzie błędny, zwracamy False"""
    from email_validator import validate_email, EmailNotValidError

    try:
        # Validate.
        valid = validate_email(email)

        # Update with the normalized form.
        email = valid.email
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        return False
    return True


