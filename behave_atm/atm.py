class InsufficientFundsError(Exception):
    pass


class InvalidPINError(Exception):
    pass


class AccountLockedError(Exception):
    pass


class ATM:
    def __init__(self, initial_balance=0, pin="1234", daily_limit=8000):
        self.balance = int(initial_balance)
        self.pin = pin
        self.transaction_history = []
        self.failed_attempts = 0
        self.locked = False
        self.daily_limit = daily_limit
        self.withdrawn_today = 0
        self._add_transaction("Account created", initial_balance)

    def check_balance(self):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")
        return self.balance

    def deposit(self, amount):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += int(amount)
        self._add_transaction("Deposit", amount)
        return self.balance

    def withdraw(self, amount):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")

        amount = int(amount)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds to complete the withdrawal")

        # Verificar límite diario
        if hasattr(self, "daily_limit") and self.withdrawn_today + amount > self.daily_limit:
            raise ValueError("Daily withdrawal limit exceeded")

        self.balance -= amount
        self.withdrawn_today += amount
        self._add_transaction("Withdrawal", -amount)
        return self.balance

    def transfer(self, amount, destination_account):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")
        amount = int(amount)
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds to complete the transfer")
        
        self.balance -= amount
        destination_account.balance += amount
        
        self._add_transaction(f"Transfer to account", -amount)
        destination_account._add_transaction(f"Transfer from account", amount)
        
        return self.balance

    def get_transaction_history(self):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")
        return self.transaction_history.copy()

    def change_pin(self, old_pin, new_pin):
        if self.locked:
            raise AccountLockedError("Account locked due to multiple failed attempts")
        if old_pin != self.pin:
            self.failed_attempts += 1
            if self.failed_attempts >= 3:
                self.locked = True
                raise AccountLockedError("Account locked due to multiple failed attempts")
            raise InvalidPINError("Incorrect current PIN")

        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("New PIN must be exactly 4 digits")

        self.pin = new_pin
        self.failed_attempts = 0
        self._add_transaction("PIN changed", 0)
        return True

    def _add_transaction(self, transaction_type, amount):
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance
        })
