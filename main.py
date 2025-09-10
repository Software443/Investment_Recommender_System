# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class InvestorProfile(BaseModel):
#     Investor_ID: str   # changed from int → str
#     Country: str
#     Risk_Appetite: str
#     Preferred_Sector: str
#     Years_Active: int
#     Budget_NGN: float

# @app.post("/recommend")
# async def recommend_investments(profile: InvestorProfile):
#     recommendations = [
#         {"Sector": profile.Preferred_Sector, "Reason": "Matches preference"},
#         {"Sector": "Agriculture", "Reason": "High growth in Nigeria"},
#     ]
#     return {
#         "Investor_ID": profile.Investor_ID,
#         "Top_Recommendations": recommendations  # renamed key
#     }


from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

app = FastAPI()

class InvestorProfile(BaseModel):
    Investor_ID: str
    Country: str
    Risk_Appetite: str
    Preferred_Sector: str
    Years_Active: int
    Budget_NGN: float
    Investor_Type: str
    Amount_NGN: float
    Year: int
    Investment_Type: str

@app.post("/recommend")
async def recommend_investments(profile: InvestorProfile):
    # Example recommendation list
    sectors = ["Agriculture", "Energy", "Mining", "Real Estate", "Technology"]

    recommendations = []
    for sector in sectors:
        recommendations.append({
            "Sector": sector,
            "Reason": (
                "Matches preferred sector" if sector == profile.Preferred_Sector 
                else f"High growth potential in {profile.Country}"
            ),
            "Confidence_Score": round(random.uniform(0.6, 0.95), 2)  # simulate model confidence
        })

    # Sort by confidence
    recommendations = sorted(recommendations, key=lambda x: x["Confidence_Score"], reverse=True)[:3]

    return {
        "Investor_Profile": profile.dict(),   # Echo input
        "Top_Recommendations": recommendations
    }






# from fastapi import FastAPI
# import joblib
# import pandas as pd
# from schemas import InvestorProfile, InvestmentRecommendation, RecommendationResponse 

# # Load the pre-trained model
# model = joblib.load("models/investment_recommender.pkl")

# # Create app
# app = FastAPI(title="Investment Recommendation API")

# @app.get("/")
# def home():
#     return {"message": "Welcome to the Investment Recommendation API"}

# @app.post("/recommend", response_model=RecommendationResponse)
# def recommend(request: InvestorProfile):
#     # Define candidate opportunities
#     sectors = ["Agriculture", "Mining", "Technology", "Energy", "Healthcare", "Manufacturing"]
#     lgas = ["Lafia", "Keffi", "Karu", "Akwanga", "Wamba", "Doma", "Toto", "Obi", "Nasarawa", "Awe", "Keana" "Obi", "Nassarawa-Eggon"]

#     candidates = []
#     for sector in sectors:
#         for lga in lgas:
#             candidates.append({
#                 "Sector": sector,
#                 "LGA": lga,
#                 "Country": request.Country,
#                 "Risk_Appetite": request.Risk_Appetite,
#                 "Preferred_Sector": request.Preferred_Sector,
#                 "Budget_Range_NGN": request.Budget_NGN,
#                 "Years_Active": request.Years_Active
#             })
    
#     df_candidates = pd.DataFrame(candidates)
#     predictions = model.predict(df_candidates)

#     df_candidates["Estimated_ROI"] = predictions
#     top = df_candidates.sort_values(by="Estimated_ROI", ascending=False).head(5)

#     recommendations = [
#         InvestmentRecommendation(
#             Sector=row["Sector"],
#             LGA=row["LGA"],
#             Estimated_ROI=round(float(row["Estimated_ROI"]), 2),
#             Score=round(float(row["Estimated_ROI"]) / 100, 2)  # Example score calculation
#         ) for _, row in top.iterrows()
#     ]

#     return RecommendationResponse(recommendations=recommendations)




