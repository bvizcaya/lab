class Account:
    def __init__(self, name: str) -> None:
        """Initializes an Account object with a given name and a balance of 0."""
        self.__name = name
        self.__balance = 0

    def deposit(self, amount: float) -> bool:
        """Deposits the specified amount into the account balance.

        Args:
            amount: A positive float value representing the amount to be deposited.

        Returns:
            A boolean value indicating whether the deposit transaction was successful.
            True if the deposit was successful, False otherwise.
        """
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """Withdraws the specified amount from the account balance.

        Args:
            amount: A positive float value representing the amount to be withdrawn.

        Returns:
            A boolean value indicating whether the withdrawal transaction was successful.
            True if the withdrawal was successful, False otherwise.
        """
        if amount <= 0 or amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True

    def get_balance(self) -> float:
        """Returns the current account balance as a float."""
        return self.__balance

    def get_name(self) -> str:
        """Returns the account name as a string."""
        return self.__name
