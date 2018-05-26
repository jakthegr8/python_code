class Acount():
  maximum_balance = 300
  
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance
  
  def deposit(self, amount):
    print(self.balance + amount)
    print(self.maximum_balance)
    if (self.balance + amount) > self.maximum_balance:
      print('You reached the maximum deposit')
    else:
      self.balance =  self.balance + amount
    return self.balance
  
  def withdraw(self, amount):
    if self.balance >= amount:
      self.balance = self.balance - amount
    else:
      print('You don not have balance')
    return self.balance

  def __str__(self):
    return f'Owner: {self.owner} \nBalance: {self.balance}'


acount = Acount('Jose', 100)

print(acount.deposit(100))
print(acount.deposit(100))
print(str(acount))
print(acount.deposit(100))
print(acount.withdraw(100))
print(acount.withdraw(100))
print(acount.withdraw(100))
print(str(acount))
print(acount.withdraw(100))