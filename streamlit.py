import streamlit as st
import requests
import pandas as pd
from io import BytesIO
import streamlit.components.v1 as components

st.set_page_config(page_title="Investment Recommendation System", layout="wide")

# ======================================
# 🎨 PREMIUM DARK STYLING
# ======================================
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
}

/* Cleaner KPI Card */
.kpi-card {
    background-color: #141922;
    padding: 22px;
    border-radius: 12px;
    text-align: center;
    color: white;
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0px 2px 8px rgba(0,0,0,0.25);  /* soft shadow */
    transition: all 0.2s ease-in-out;
}

.kpi-card:hover {
    transform: translateY(-3px);
}

/* Recommendation Card */
.recommend-card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 14px;
    color: #f5f5f5;
    margin-bottom: 18px;
    border-left: 6px solid #1E90FF;
}

/* AI Insight */
.insight-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 12px;
    color: #e5e7eb;
    line-height: 1.6;
    font-size: 15px;
    margin-top: 10px;
}

/* Confidence Badges */
.badge-green {
    background-color: #16a34a;
    padding: 6px 14px;
    border-radius: 20px;
    color: white;
    font-size: 13px;
}

.badge-yellow {
    background-color: #ca8a04;
    padding: 6px 14px;
    border-radius: 20px;
    color: white;
    font-size: 13px;
}

.badge-red {
    background-color: #dc2626;
    padding: 6px 14px;
    border-radius: 20px;
    color: white;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# ======================================
# 🎉 MARQUEE HEADER
# ======================================
st.markdown("""
<marquee behavior="scroll" direction="left" scrollamount="5">
👏 Welcome Investor! AI Investment Opportunity System 🚀
</marquee>
""", unsafe_allow_html=True)

# ======================================
# 📌 SIDEBAR
# ======================================
st.sidebar.header("Investor Profile")

investor_data = {
    "Investor_ID": st.sidebar.text_input("Investor ID", "INV001"),
    "Country": st.sidebar.text_input("Country", "Nigeria"),
    "Risk_Appetite": st.sidebar.selectbox("Risk Appetite", ["Low", "Medium", "High"]),
    "Preferred_Sector": st.sidebar.selectbox("Preferred Sector",
                                             ["Agriculture", "Energy", "Mining",
                                              "Real Estate", "Technology"]),
    "Years_Active": st.sidebar.number_input("Years Active", min_value=0, value=5),
    "Budget_NGN": st.sidebar.number_input("Budget (NGN)", min_value=0.0, value=59000000.0),
    "Investor_Type": st.sidebar.selectbox("Investor Type",
                                          ["Individual", "Corporate", "Government"]),
}

RECOMMEND_API = "http://127.0.0.1:8000/recommend"
GENERATE_API = "http://127.0.0.1:8000/generate_sector_content"

# ======================================
# 🔍 GET RECOMMENDATIONS
# ======================================
if st.sidebar.button("Get Recommendations"):

    response = requests.post(RECOMMEND_API, json=investor_data)

    if response.status_code != 200:
        st.error("API Error")
    else:
        data = response.json()
        recommendations = data["Top_Recommendations"][:3]

        # ======================================
        # 🔢 CLEAN KPI CARDS WITH ANIMATION
        # ======================================
        st.subheader("📈 Investment Snapshot")

        budget = int(investor_data["Budget_NGN"])
        avg_conf = int(sum([r["Confidence_Score"] for r in recommendations]) / 3 * 100)
        top_sector = recommendations[0]["Sector"]

        counter_html = f"""
        <div style="display:flex; gap:20px;">

            <div class="kpi-card" style="flex:1;">
                <div style="font-size:14px; opacity:0.7;">💰 Budget</div>
                <div style="font-size:26px; font-weight:600; margin-top:8px;" id="budgetCounter">0</div>
            </div>

            <div class="kpi-card" style="flex:1;">
                <div style="font-size:14px; opacity:0.7;">📊 Avg Confidence</div>
                <div style="font-size:26px; font-weight:600; margin-top:8px;" id="confidenceCounter">0%</div>
            </div>

            <div class="kpi-card" style="flex:1;">
                <div style="font-size:14px; opacity:0.7;">🏆 Top Sector</div>
                <div style="font-size:26px; font-weight:600; margin-top:8px;">{top_sector}</div>
            </div>

        </div>

        <script>
        function animateValue(id, start, end, duration, suffix="") {{
            let obj = document.getElementById(id);
            let range = end - start;
            let current = start;
            let increment = end > start ? 1 : -1;
            let stepTime = Math.abs(Math.floor(duration / range));
            let timer = setInterval(function() {{
                current += increment;
                obj.innerHTML = current.toLocaleString() + suffix;
                if (current == end) {{
                    clearInterval(timer);
                }}
            }}, stepTime);
        }}

        animateValue("budgetCounter", 0, {budget}, 800);
        animateValue("confidenceCounter", 0, {avg_conf}, 800, "%");
        </script>
        """

        components.html(counter_html, height=160)

        # ======================================
        # 🏷️ SECTOR ICON MAP
        # ======================================
        sector_icons = {
            "Agriculture": "🌾",
            "Energy": "⚡",
            "Mining": "⛏️",
            "Real Estate": "🏢",
            "Technology": "💻"
        }

        # ======================================
        # 📊 RECOMMENDATIONS
        # ---------------------------------------
        st.subheader("📊 Top Sector Recommendations")

        for rec in recommendations:
            sector = rec["Sector"]
            confidence = int(rec["Confidence_Score"] * 100)
            reason = rec.get("Reason", "AI-driven recommendation.")

            icon = sector_icons.get(sector, "📌")

            if confidence >= 85:
                badge_class = "badge-green"
            elif confidence >= 70:
                badge_class = "badge-yellow"
            else:
                badge_class = "badge-red"

            st.markdown(f"""
            <div class="recommend-card">
                <h4>{icon} {sector}</h4>
                <p>{reason}</p>
                <span class="{badge_class}">
                    Model Confidence: {confidence}%
                </span>
            </div>
            """, unsafe_allow_html=True)

            st.progress(confidence / 100)

        # ======================================
        # ✨ AI INSIGHTS
        # ======================================
        st.subheader("✨ AI-Powered Sector Insights")

        for rec in recommendations:
            sector = rec["Sector"]

            with st.expander(f"{sector} Insight"):

                payload = {
                    "Sector": sector,
                    "Budget": investor_data["Budget_NGN"],
                    "Risk_Appetite": investor_data["Risk_Appetite"],
                    "Investor_ID": investor_data["Investor_ID"]
                }

                content_resp = requests.post(GENERATE_API, json=payload)

                if content_resp.status_code == 200:
                    content = content_resp.json()

                    if "error" not in content:
                        st.image(content["Image_URL"], use_column_width=True)

                        st.markdown(f"""
                        <div class="insight-box">
                        {content["AI_Writeup"]}
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.warning(content["error"])
                else:
                    st.warning("Could not generate AI content")

        # ======================================
        # ⬇️ EXPORT
        # ======================================
        st.subheader("⬇️ Export")

        df = pd.DataFrame(recommendations)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv,
                           file_name="recommendations.csv",
                           mime="text/csv")