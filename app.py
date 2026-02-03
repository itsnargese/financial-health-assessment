import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import io


st.set_page_config(
    page_title="Financial Health Assessment Tool",
    layout="wide"
)


st.markdown("""
<style>
.block-container { padding-top: 1.2rem; }

.section-title {
    background: linear-gradient(90deg,#020617,#0f172a);
    padding: 12px 16px;
    border-radius: 10px;
    margin-top: 26px;
    margin-bottom: 14px;
    border-left: 5px solid #22c55e;
}

.section-title h2 {
    margin: 0;
    font-size: 22px;
    font-weight: 700;
}

.metric-box {
    background: #020617;
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #1e293b;
}

.highlight {
    background: #064e3b;
    padding: 12px;
    border-radius: 10px;
    font-weight: 600;
    border: 1px solid #047857;
}

.risk {
    background: #7c2d12;
    padding: 12px;
    border-radius: 10px;
    border: 1px solid #b45309;
}

.profile-panel {
    background: #020617;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #1e293b;
    margin-bottom: 20px;
}
.profile-panel h3 {
    margin: 0;
    font-size: 18px;
    font-weight: 700;
}
.profile-panel span {
    font-size: 12px;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.markdown("""
<div class="profile-panel">
    <h3>Business Profile</h3>
    <span>Company configuration & preferences</span>
</div>
""", unsafe_allow_html=True)

business_name = st.sidebar.text_input("Business Name")
industry = st.sidebar.selectbox(
    "Industry",
    ["Manufacturing", "Retail", "Agriculture", "Services", "Logistics", "E-commerce"]
)
business_size = st.sidebar.radio("Business Size", ["Small", "Medium"])
language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi (Coming Soon)", "Tamil (Coming Soon)"]
)
st.sidebar.info("All data processed locally & securely")


st.title("Financial Health Assessment Tool")
st.caption(
    "Professional dashboard for SMEs to assess financial health, credit readiness, "
    "risk exposure, and short-term growth outlook."
)


st.markdown("<div class='section-title'><h2>Upload Financial Data</h2></div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])


if uploaded_file:
    df = pd.read_csv(uploaded_file)

    total_revenue = int(df["Revenue"].sum())
    total_expenses = int(df["Expenses"].sum())
    profit = total_revenue - total_expenses
    profit_margin = round((profit / total_revenue) * 100, 2)
    expense_ratio = round(total_expenses / total_revenue, 2)

    health = "Strong & Stable" if profit_margin > 15 else "Moderate" if profit_margin > 8 else "At Risk"

    st.markdown("<div class='section-title'><h2>Data Preview</h2></div>", unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True)

   
    st.markdown("<div class='section-title'><h2>Financial Summary</h2></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div class='metric-box'>Total Revenue<br><h2>₹ {total_revenue:,}</h2></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-box'>Total Expenses<br><h2>₹ {total_expenses:,}</h2></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-box'>Net Profit<br><h2>₹ {profit:,}</h2></div>", unsafe_allow_html=True)

    st.progress(min(profit_margin / 100, 1.0))
    st.markdown(f"<div class='highlight'>Financial Health Status: {health}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'><h2>Industry Benchmark Comparison</h2></div>", unsafe_allow_html=True)
    industry_benchmarks = {
        "Manufacturing": 12, "Retail": 10, "Agriculture": 8,
        "Services": 15, "Logistics": 9, "E-commerce": 14
    }
    benchmark = industry_benchmarks[industry]

    if profit_margin >= benchmark:
        st.markdown(
            f"<div class='highlight'>Profit margin ({profit_margin}%) is ABOVE the {industry} benchmark ({benchmark}%).</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='risk'>Profit margin ({profit_margin}%) is BELOW the {industry} benchmark ({benchmark}%).</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='section-title'><h2>Creditworthiness & Risk</h2></div>", unsafe_allow_html=True)
    credit_score = min(
        100,
        50
        + (25 if profit_margin > 15 else 15 if profit_margin > 8 else 0)
        + (20 if expense_ratio < 0.75 else 10 if expense_ratio < 0.85 else 0)
    )
    st.metric("SME Credit Score", f"{credit_score} / 100")

    
    st.markdown("<div class='section-title'><h2>AI-Driven Insights & Recommendations</h2></div>", unsafe_allow_html=True)

    insights = []
    insights.append(
        "Strong profitability indicates efficient operations."
        if profit_margin > 15 else
        "Moderate profitability with scope for cost optimisation."
        if profit_margin > 8 else
        "Low profitability signals financial stress."
    )
    insights.append(
        "Expenses are well controlled."
        if expense_ratio < 0.75 else
        "Expense monitoring is advised."
        if expense_ratio < 0.85 else
        "High expense ratio increases financial risk."
    )
    insights.append(
        "High lender confidence due to strong credit profile."
        if credit_score >= 80 else
        "Moderate lender confidence."
        if credit_score >= 65 else
        "Low lender confidence."
    )
    insights.append(
        "AI Recommendation: Maintain margins and leverage forecasted growth for expansion."
    )

    for i in insights:
        st.markdown(f"<div class='highlight'>• {i}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'><h2>Bank Loan Eligibility Recommendation</h2></div>", unsafe_allow_html=True)

    if credit_score >= 80 and profit_margin >= 15:
        eligibility, loan_amount, reason = "Eligible", int(total_revenue * 0.4), "Strong credit profile and high profitability"
    elif credit_score >= 65:
        eligibility, loan_amount, reason = "Partially Eligible", int(total_revenue * 0.25), "Moderate financial strength"
    else:
        eligibility, loan_amount, reason = "Not Eligible", 0, "High financial risk"

    st.markdown(
        f"<div class='highlight'><b>Status:</b> {eligibility}<br>"
        f"<b>Recommended Loan Amount:</b> ₹ {loan_amount:,}<br>"
        f"<b>Reason:</b> {reason}</div>",
        unsafe_allow_html=True
    )

    
    st.markdown("<div class='section-title'><h2>Download Report</h2></div>", unsafe_allow_html=True)

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setFont("Helvetica", 11)

    y = 800
    for line in [
        "Financial Health Assessment Report",
        f"Total Revenue: ₹ {total_revenue:,}",
        f"Total Expenses: ₹ {total_expenses:,}",
        f"Net Profit: ₹ {profit:,}",
        f"Profit Margin: {profit_margin}%",
        f"Credit Score: {credit_score}/100",
        f"Loan Eligibility: {eligibility}"
    ]:
        pdf.drawString(50, y, line)
        y -= 22

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    st.download_button(
        "Download PDF Report",
        buffer,
        file_name="financial_health_report.pdf",
        mime="application/pdf"
    )

else:
    st.info("Upload a CSV file to start analysis.")
