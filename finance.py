def add_income(incomes, label, amount):
    """Добавляет доход в список"""
    new_list = incomes.copy()
    new_list.append({"label": label, "amount": float(amount)})
    return new_list

def add_expense(expenses, label, amount):
    """Добавляет расход в список"""
    new_list = expenses.copy()
    new_list.append({"label": label, "amount": float(amount)})
    return new_list

def total_income(incomes):
    """Считает общий доход"""
    return sum(item["amount"] for item in incomes)

def total_expense(expenses):
    """Считает общие расходы"""
    return sum(item["amount"] for item in expenses)

def savings(income_total, expense_total):
    """Считает накопления (доход минус расход)"""
    return income_total - expense_total

def savings_rate(income_total, expense_total):
    """Считает процент накоплений"""
    if income_total == 0:
        return 0.0
    return (savings(income_total, expense_total) / income_total) * 100
