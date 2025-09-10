import streamlit as st
import requests

st.set_page_config(page_title="Investor Recommendation System", layout="centered")

st.title("💡Investor Recommendation System")

# Form for investor input
with st.form("investor_form"):
    investor_id = st.text_input("Investor ID (e.g., INV001)")
    country = st.text_input("Country", "Nigeria")
    risk = st.selectbox("Risk Appetite", ["Low", "Medium", "High"])
    sector = st.selectbox("Preferred Sector", ["Agriculture", "Mining", "Energy", "Technology", "Healthcare", "Manufacturing"])
    years = st.number_input("Years Active", min_value=0, value=5)
    budget = st.number_input("Budget (NGN)", min_value=0, value=50000000)
    
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    payload = {
        "Investor_ID": investor_id,
        "Country": country,
        "Risk_Appetite": risk,
        "Preferred_Sector": sector,
        "Years_Active": years,
        "Budget_NGN": budget,
    }

    try:
        response = requests.post("http://127.0.0.1:8000/recommend", json=payload)
        if response.status_code == 200:
            st.success("Recommendations received!")
            st.json(response.json())
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")


# import streamlit as st
# import requests
# import pandas as pd

# st.set_page_config(page_title="Investment Opportunity Recommender", layout="wide")

# st.title("💡 Investment Opportunity Recommendation System")
# st.markdown("Provide your profile and get **top 5 investment opportunities** in Nasarawa State.")

# # Sidebar for investor input
# st.sidebar.header("Investor Profile")

# investor_id = st.sidebar.text_input("Investor ID", "INV001")
# country = st.sidebar.text_input("Country", "Nigeria")
# risk_appetite = st.sidebar.selectbox("Risk Appetite", ["Low", "Medium", "High"])
# preferred_sector = st.sidebar.selectbox(
#     "Preferred Sector",
#     ["Agriculture", "Mining", "Energy", "Technology", "Healthcare", "Manufacturing"]
# )
# years_active = st.sidebar.slider("Years Active", 0, 30, 5)
# budget_ngn = st.sidebar.number_input("Budget (₦)", min_value=1000000, step=1000000, value=50000000)
# investor_type = st.sidebar.selectbox("Investor Type", ["Individual", "Corporate"])
# amount_ngn = st.sidebar.number_input("Investment Amount (₦)", min_value=1000000, step=1000000, value=20000000)
# year = st.sidebar.number_input("Year", min_value=2000, max_value=2050, value=2025)
# investment_type = st.sidebar.selectbox("Investment Type", ["Equity", "Debt", "Grant"])

# if st.sidebar.button("Get Recommendations"):
#     payload = {
#         "Investor_ID": investor_id,        # now allowed as string (e.g., "INV001")
#         "Country": country,
#         "Risk_Appetite": risk_appetite,
#         "Preferred_Sector": preferred_sector,
#         "Years_Active": years_active,
#         "Budget_NGN": budget_ngn, 
#         "Investor_Type": investor_type,
#         "Amount_NGN": amount_ngn,
#         "Year": year,
#         "Investment_Type": investment_type
#     }

#     try:
#         response = requests.post("http://127.0.0.1:8000/recommend", json=payload)

#         if response.status_code == 200:
#             data = response.json()["Top_Recommendations"]
#             st.success("✅ Recommendations fetched successfully!")
            
#             # Convert to DataFrame for display
#             df = pd.DataFrame(data)
#             st.dataframe(df)

#             # Bar chart for ROI
#             st.bar_chart(df.set_index("Sector")["Predicted_ROI"])
#         else:
#             st.error(f"Error: {response.status_code} - {response.text}")
#     except Exception as e:
#         st.error(f"Connection error: {e}")
