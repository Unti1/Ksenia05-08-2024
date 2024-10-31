
def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance -= amount
            return balance
        else:
            return "Недостаточно средств"

    def get_balance():
        return balance

    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "get_balance": get_balance
        }

if __name__ == '__main__':
    account = create_account(1000)
    print("Баланс:", account['get_balance']())
    account['deposit'](500)
    print("Баланс:", account['get_balance']())
    print(account['withdraw'](2000))
    print(account['withdraw'](700))
    print("Баланс:", account['get_balance']())