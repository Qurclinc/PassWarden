def validate_password(passwd):
    if len(passwd) < 6:
        return (False, "Ошибка регистрации", "Пароль слишком короткий")
    if passwd.lower() == passwd or passwd.upper() == passwd:
        return (False, "Ошибка регистрации", "Пароль должен содержать буквы верхнего и нижнего регистра")
    if passwd.isdigit():
        return (False, "Ошибка регистрации", "Пароль должен содержать хотя бы одну цифру")
    if passwd.isalpha():
        return (False, "Ошибка регистрации", "Пароль должен содержать хотя бы одну букву")
    if " " in passwd:
        return (False, "Ошибка регистрации", "Пароль не должен содержать пробельные символы")
    return (True,)