from pydantic import BaseModel
from typing import List, Optional

# Define input schema
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
    Investment_Type: str # accept this instead of Budget_Range_NGN

# Define output schema
class InvestmentRecommendation(BaseModel):
    Sector: str
    LGA: str  # Local Government Area
    Estimated_ROI: float  # in percentage
    Score: float  # confidence score

class RecommendationResponse(BaseModel):
    recommendations: List[InvestmentRecommendation]