from decimal import Decimal, InvalidOperation


class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float = 0):
        self.account_number: str = account_number
        self.account_holder: str = account_holder
        is_valid, balance_amount = self._validate_amount_decimal(balance)
        if not is_valid:
            raise ValueError(
                "Balance must be a decimal number with at most two decimal places."
            )
        self.balance: Decimal = balance_amount

    @staticmethod
    def _validate_amount_decimal(amount: float) -> (bool, Decimal):
        try:
            amount_str = str(amount)
            amount_decimal = Decimal(amount_str)
            if "." not in amount_str:
                return True, amount_decimal
            if len(amount_str.split(".")[1]) > 2:
                return False, amount_decimal
            return True, amount_decimal
        except InvalidOperation:
            return False, Decimal(0)

    def deposit(self, amount: float) -> None:
        is_valid, amount_decimal = self._validate_amount_decimal(amount)
        if not is_valid:
            print(
                "Deposit amount must be a decimal number with at most two decimal places."
            )
            return
        if amount_decimal <= Decimal(0):
            print("Deposit amount must be positive.")
            return

        self.balance += amount_decimal
        print(
            f"A/C No: {self.account_number} - Deposited ${amount_decimal}. New balance: ${self.balance}"
        )

    def withdraw(self, amount: float) -> None:
        is_valid, amount_decimal = self._validate_amount_decimal(amount)
        if not is_valid:
            print(
                "Withdrawal amount must be a decimal number with at most two decimal places."
            )
            return
        if amount_decimal <= Decimal(0):
            print("Withdrawal amount must be positive.")
            return
        if self.balance < amount_decimal:
            print(f"A/C No: {self.account_number} - Insufficient funds.")
            return
        
        self.balance -= amount_decimal
        print(
            f"A/C No: {self.account_number} - Withdrew ${amount_decimal}. New balance: ${self.balance}"
        )

    def check_balance(self) -> Decimal:
        print(f"A/C No: {self.account_number} - Current balance: ${self.balance}")
        return self.balance

    def display_details(self) -> None:
        print(f"Account Details of A/C No: {self.account_number}:")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")


if __name__ == "__main__":
    account = BankAccount("123456789", "Mainul Hoque", 1000)
    account.display_details()
    account.deposit(100.50)
    account.withdraw(200)
    account.withdraw(2000)
    account.display_details()
