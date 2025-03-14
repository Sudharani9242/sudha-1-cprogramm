class sudha:
  def __init__(self):
    self.public_var = "I'm very talented"
    self.__private_var = "I'm good girl"
  def show_private(self):
    print(self.__private_var)
Affu = sudha() 
print(Affu.public_var)
Affu.show_private()
