class User:
    def __init__(self, firstname, lastname, user_name, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.user_name = user_name
        self.email = self.firstname + '.' + self.lastname + '@gmail.com'
        self.password = password


class Order(User):
    def __init__(self, order_id, order_name, order_type, user_name):
        self.order_id = order_id
        self.order_name = order_name
        self.order_type = order_type
        self.user_name = user_name

    def get_dict(self):
        return {
            'order_id': self.order_id,
            'order_name': self.order_name,
            'order_type': self.order_type,
            'user_name': self.user_name
        }
