from models.user import user


class Mentor(User):
    def __init__(self, name, surname, user_id, password):
        super().__init__(name, surname, user_id, password)

        User.add_user(self)
