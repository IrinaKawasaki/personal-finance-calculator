import pytest
from finance import (
    add_income, add_expense, total_income,
    total_expense, savings, savings_rate
)

def test_add_income():
    original = []
    result = add_income(original, "salary", 5000)
    assert len(original) == 0  # Проверяем, что исходный список не изменился
    assert len(result) == 1
    assert result[0]["amount"] == 5000.0

def test_total_income():
    incomes = [
        {"label": "salary", "amount": 5000}, 
        {"label": "bonus", "amount": 1000}
    ]
    assert total_income(incomes) == 6000.0

def test_total_expense():
    expenses = [
        {"label": "rent", "amount": 2000}, 
        {"label": "food", "amount": 500}
    ]
    assert total_expense(expenses) == 2500.0

def test_savings():
    assert savings(6000, 2500) == 3500.0

def test_savings_rate_normal():
    # 3500 / 6000 * 100 = 58.333...%
    assert savings_rate(6000, 2500) == pytest.approx(58.333, rel=1e-3)

def test_savings_rate_zero_income():
    # Защита от деления на ноль
    assert savings_rate(0, 100) == 0.0

def test_negative_savings():
    # Если расходы больше доходов, накопления отрицательные
    assert savings(1000, 1500) == -500.0
