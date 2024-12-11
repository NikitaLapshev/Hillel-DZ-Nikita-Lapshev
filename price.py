"""
    Classes...


Operation :=  OPERAND_A OPERATOR OPERAND_B -> RESULT
Opeartion :=   int(4)      *        int(2) ->  16
"""

from typing import Any


class Price:
    CURRENCY_RATES = {
        "USD": 1.0,
        "CHF": 0.9,
        "EUR": 1.1,
    }

    def __init__(self, value: int, currency: str):
        self.value: int = value
        self.currency: str = currency

    def __str__(self) -> str:
        return f"Price: {self.value} {self.currency}"

    def convert(self, to: str = "CHF") -> "Price":
        if to not in self.CURRENCY_RATES:
            raise ValueError(f"Unsupported currency: {to}")

        converted_value = (self.value * self.CURRENCY_RATES[self.currency]) / self.CURRENCY_RATES[to]
        return Price(value=converted_value, currency=to)

    def __add__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Pirces objects")
        else:
            if self.currency != other.currency:
                initial_currency = self.currency
                first_price_chf = self.convert()
                second_price_chf = other.convert()
                return Price(
                    value=first_price_chf.value + second_price_chf.value, currency="CHF"
                ).convert(initial_currency)


            return Price(value=self.value + other.value, currency=self.currency)


    def __sub__(self, other: Any) -> "Price":
        if not isinstance(other, Price):
            raise ValueError("Can perform operation only with Pirces objects")
        else:
            if self.currency != other.currency:
                initial_currency = self.currency
                first_price_chf = self.convert()
                second_price_chf = other.convert()
                return Price(
                    value=first_price_chf.value - second_price_chf.value, currency="CHF"
                ).convert(initial_currency)


            return Price(value=self.value - other.value, currency=self.currency)


phone = Price(value=200, currency="USD")
tablet = Price(value=400, currency="EUR")

total1: Price = phone + tablet
total2: Price = phone - tablet

print(total1)
print(total2)
