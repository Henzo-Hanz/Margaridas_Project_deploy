"""Endpoints para Treasury - Gerenciamento de despesas e receitas."""
from typing import Annotated, List
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.models.expense import Expense
from app.models.income import Income
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseResponse
from app.schemas.income import IncomeCreate, IncomeUpdate, IncomeResponse

router = APIRouter(prefix="/treasury", tags=["treasury"])


# ==================== EXPENSES ====================


@router.post("/expenses", response_model=ExpenseResponse)
def create_expense(
    expense_data: ExpenseCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Cria uma nova despesa."""
    expense = Expense(
        user_id=current_user.id,
        name=expense_data.name,
        value=expense_data.value,
        date=expense_data.date or datetime.now(),
        method=expense_data.method,
        notes=expense_data.notes,
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


@router.get("/expenses", response_model=List[ExpenseResponse])
def get_expenses(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Lista todas as despesas do usuário."""
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()
    return expenses


@router.get("/expenses/{expense_id}", response_model=ExpenseResponse)
def get_expense(
    expense_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Obtém uma despesa específica."""
    expense = db.query(Expense).filter(
        and_(Expense.id == expense_id, Expense.user_id == current_user.id)
    ).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Despesa não encontrada")
    return expense


@router.put("/expenses/{expense_id}", response_model=ExpenseResponse)
def update_expense(
    expense_id: int,
    expense_data: ExpenseUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Atualiza uma despesa."""
    expense = db.query(Expense).filter(
        and_(Expense.id == expense_id, Expense.user_id == current_user.id)
    ).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Despesa não encontrada")

    if expense_data.name is not None:
        expense.name = expense_data.name
    if expense_data.value is not None:
        expense.value = expense_data.value
    if expense_data.date is not None:
        expense.date = expense_data.date
    if expense_data.method is not None:
        expense.method = expense_data.method
    if expense_data.notes is not None:
        expense.notes = expense_data.notes

    db.commit()
    db.refresh(expense)
    return expense


@router.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Deleta uma despesa."""
    expense = db.query(Expense).filter(
        and_(Expense.id == expense_id, Expense.user_id == current_user.id)
    ).first()
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Despesa não encontrada")

    db.delete(expense)
    db.commit()
    return {"message": "Despesa deletada com sucesso"}


# ==================== INCOMES ====================


@router.post("/incomes", response_model=IncomeResponse)
def create_income(
    income_data: IncomeCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Cria uma nova receita."""
    income = Income(
        user_id=current_user.id,
        name=income_data.name,
        value=income_data.value,
        date=income_data.date or datetime.now(),
        notes=income_data.notes,
    )
    db.add(income)
    db.commit()
    db.refresh(income)
    return income


@router.get("/incomes", response_model=List[IncomeResponse])
def get_incomes(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Lista todas as receitas do usuário."""
    incomes = db.query(Income).filter(Income.user_id == current_user.id).all()
    return incomes


@router.get("/incomes/{income_id}", response_model=IncomeResponse)
def get_income(
    income_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Obtém uma receita específica."""
    income = db.query(Income).filter(
        and_(Income.id == income_id, Income.user_id == current_user.id)
    ).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    return income


@router.put("/incomes/{income_id}", response_model=IncomeResponse)
def update_income(
    income_id: int,
    income_data: IncomeUpdate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Atualiza uma receita."""
    income = db.query(Income).filter(
        and_(Income.id == income_id, Income.user_id == current_user.id)
    ).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")

    if income_data.name is not None:
        income.name = income_data.name
    if income_data.value is not None:
        income.value = income_data.value
    if income_data.date is not None:
        income.date = income_data.date
    if income_data.notes is not None:
        income.notes = income_data.notes

    db.commit()
    db.refresh(income)
    return income


@router.delete("/incomes/{income_id}")
def delete_income(
    income_id: int,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
):
    """Deleta uma receita."""
    income = db.query(Income).filter(
        and_(Income.id == income_id, Income.user_id == current_user.id)
    ).first()
    if not income:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")

    db.delete(income)
    db.commit()
    return {"message": "Receita deletada com sucesso"}


# ==================== ANALYTICS ====================


@router.get("/analytics/summary")
def get_summary(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    period: str = "6m",
):
    """Retorna um resumo das finanças para o período especificado."""
    now = datetime.now()
    
    # Define período em dias
    period_days = {
        "1m": 30,
        "3m": 90,
        "6m": 180,
        "12m": 365
    }.get(period, 180)  # Default 6m
    
    period_ago = now - timedelta(days=period_days)
    
    # Calcular totais de despesas
    total_expenses = db.query(Expense).filter(
        and_(Expense.user_id == current_user.id, Expense.date >= period_ago)
    ).all()
    
    expenses_total = sum(e.value for e in total_expenses)
    
    # Calcular totais de receitas
    total_incomes = db.query(Income).filter(
        and_(Income.user_id == current_user.id, Income.date >= period_ago)
    ).all()
    
    incomes_total = sum(i.value for i in total_incomes)
    
    return {
        "period": period,
        "expenses_total": expenses_total,
        "incomes_total": incomes_total,
        "balance": incomes_total - expenses_total,
    }


@router.get("/analytics/by-method")
def get_expenses_by_method(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    period: str = "6m",
):
    """Retorna despesas agrupadas por método de pagamento para o período especificado."""
    now = datetime.now()
    
    # Define período em dias
    period_days = {
        "1m": 30,
        "3m": 90,
        "6m": 180,
        "12m": 365
    }.get(period, 180)  # Default 6m
    
    period_ago = now - timedelta(days=period_days)
    
    expenses = db.query(Expense).filter(
        and_(Expense.user_id == current_user.id, Expense.date >= period_ago)
    ).all()
    
    by_method = {}
    for expense in expenses:
        method = expense.method.value
        if method not in by_method:
            by_method[method] = 0
        by_method[method] += expense.value
    
    return by_method


@router.get("/analytics/monthly")
def get_monthly_analytics(
    current_user: Annotated[User, Depends(get_current_user)],
    db: Annotated[Session, Depends(get_db)],
    period: str = "12m",
):
    """Retorna análise mensal para o período especificado."""
    now = datetime.now()
    
    # Define número de meses
    period_months = {
        "1m": 1,
        "3m": 3,
        "6m": 6,
        "12m": 12
    }.get(period, 12)  # Default 12m
    
    # Get expenses and incomes for the period
    period_ago = now - timedelta(days=30*period_months)
    expenses = db.query(Expense).filter(
        and_(Expense.user_id == current_user.id, Expense.date >= period_ago)
    ).all()
    incomes = db.query(Income).filter(
        and_(Income.user_id == current_user.id, Income.date >= period_ago)
    ).all()
    
    # Estrutura: {year-month: {expenses: [], incomes: []}}
    monthly = {}
    
    # Initialize last N months
    for i in range(period_months):
        date = now - timedelta(days=30*i)
        month_key = date.strftime("%Y-%m")
        if month_key not in monthly:
            monthly[month_key] = {"expenses": 0, "incomes": 0, "balance": 0}
    
    # Agregar despesas
    for expense in expenses:
        month_key = expense.date.strftime("%Y-%m")
        if month_key in monthly:
            monthly[month_key]["expenses"] += expense.value
    
    # Agregar receitas
    for income in incomes:
        month_key = income.date.strftime("%Y-%m")
        if month_key in monthly:
            monthly[month_key]["incomes"] += income.value
    
    # Calcular balance
    for month in monthly:
        monthly[month]["balance"] = monthly[month]["incomes"] - monthly[month]["expenses"]
    
    # Ordenar dados
    sorted_monthly = dict(sorted(monthly.items()))
    return sorted_monthly
