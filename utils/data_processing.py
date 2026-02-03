import pandas as pd

def load_data(file):
    """
    Load CSV file into pandas DataFrame
    """
    df = pd.read_csv(file)
    return df


def calculate_metrics(df):
    """
    Calculate basic financial metrics
    """
    total_revenue = df["Revenue"].sum()
    total_expenses = df["Expenses"].sum()
    profit = total_revenue - total_expenses
    profit_margin = (profit / total_revenue) * 100

    # Simple health classification
    if profit_margin > 20:
        health_status = "Healthy"
    elif profit_margin > 5:
        health_status = "Moderate"
    else:
        health_status = "Risky"

    return {
        "total_revenue": total_revenue,
        "total_expenses": total_expenses,
        "profit": profit,
        "profit_margin": round(profit_margin, 2),
        "health_status": health_status
    }
