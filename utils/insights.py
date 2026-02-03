def generate_insights(metrics, industry="General", business_size="Small"):
    insights = []

    profit_margin = metrics["profit_margin"]
    expense_ratio = metrics["total_expenses"] / metrics["total_revenue"]

    # 1. Profitability Insight
    if profit_margin >= 20:
        insights.append("🟢 Strong profitability indicates efficient operations and pricing strategy.")
    elif profit_margin >= 10:
        insights.append("🟡 Moderate profitability. There is room to improve margins through cost optimization.")
    else:
        insights.append("🔴 Low profitability detected. Immediate review of expenses and pricing is recommended.")

    # 2. Expense Control Insight
    if expense_ratio > 0.85:
        insights.append("🔴 Expenses are consuming most of the revenue. Focus on reducing fixed and operational costs.")
    elif expense_ratio > 0.7:
        insights.append("🟡 Expense levels are high. Consider renegotiating supplier contracts or improving efficiency.")
    else:
        insights.append("🟢 Expense levels are well controlled.")

    # 3. Business Size Insight
    if business_size == "Small":
        insights.append("📌 As a small business, maintaining cash reserves and short-term liquidity is crucial.")
    else:
        insights.append("📌 As a medium enterprise, scaling operations should be balanced with debt management.")

    # 4. Industry-Specific Insight
    if industry == "Manufacturing":
        insights.append("🏭 Manufacturing businesses benefit from inventory and procurement optimization.")
    elif industry == "Retail":
        insights.append("🛒 Retail businesses should focus on inventory turnover and demand forecasting.")
    elif industry == "E-commerce":
        insights.append("📦 E-commerce businesses should optimize logistics and customer acquisition costs.")
    elif industry == "Agriculture":
        insights.append("🌾 Agricultural businesses should plan for seasonal cash flow fluctuations.")
    else:
        insights.append("📊 Industry benchmarking can help identify performance gaps.")

    # 5. Funding Recommendation
    if profit_margin > 12:
        insights.append("💰 Business appears eligible for working capital loans or invoice financing.")
    else:
        insights.append("⚠️ Improve financial stability before applying for external credit.")

    return "\n\n".join(insights)
