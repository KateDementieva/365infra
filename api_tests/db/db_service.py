class UsersDbService:
    def __init__(self, session): # 1
        self.session = session # 2

    def get_activity(self, name):
        self.session.execute('SELECT active FROM users WHERE name=?', (name,))
        return self.session.fetchone()

    def add_user(self, name, active):
        self.session.execute('INSERT INTO users VALUES (?, ?)', (name, active))
        self.session.connection.commit()