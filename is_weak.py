def is_weak(password):
    if password.isdigit() and len(password) >= 4:
        is_ascending = all(
            int(password[i + 1]) == (int(password[i]) + 1) % 10
            for i in range(len(password) - 1)
        )
        if is_ascending:
            return True

    if password.isdigit() and len(password) >= 4:
        is_descending = all(
            int(password[i + 1]) == (int(password[i]) - 1) % 10
            for i in range(len(password) - 1)
        )
        if is_descending:
            return True

    if len(set(password)) <= 2:
        return True

    return False