import secrets


def create_new(lenght, characters):
    """Генерация пароля длиной lenght из строки characters"""
    return "".join(secrets.choice(characters) for _ in range(lenght))
