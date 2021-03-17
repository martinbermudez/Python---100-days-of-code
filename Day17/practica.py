class Usuario:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def seguir(self, user):
        user.followers += 1
        self.following += 1

user_1 = Usuario("002","juan carlos")
user_2 = Usuario("001", "martin")

user_1.seguir(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
