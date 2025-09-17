# Investment Recommender System  

## 📌 Project Overview  
The **Investment Recommender System** is a machine learning–driven application designed to help investors identify the most promising sectors and locations for investment opportunities. It leverages state-level economic, demographic, and business data to provide personalized recommendations based on factors such as **Return on Investment (ROI), risk levels, sector performance, and local government penetration**.  

This project is particularly tailored for **Nasarawa State Investment and Development Agency (NASIDA)** and other government/investment promotion agencies, enabling **data-driven decision-making** and **smart investment promotion**.  

---

## 🚀 Features  
- 📊 **Data Analysis Dashboard**: Explore investment trends across sectors and LGAs.  
- 🤖 **Machine Learning Model**: Recommends investment opportunities based on investor profile.  
- 🌍 **Geospatial Insights**: Maps investments to specific LGAs for location-based decisions.  
- 🖥️ **API Service (FastAPI)**: Provides endpoints for integrating recommendations into external platforms.  
- 📈 **Investor Profiles**: Tailored recommendations by risk appetite, sector preference, and capital.  

---

## 🛠️ Tech Stack  
- **Languages**: Python (3.9+)  
- **Frameworks**: FastAPI, Scikit-learn, Pandas, NumPy  
- **Visualization**: Plotly, Matplotlib, Folium  
- **Data**: State-level sector investment datasets (synthetic + real data integration)  
- **Deployment**: Streamlit (for UI), Docker (optional), Hugging Face Spaces  

---

## 📂 Project Structure  
```
investment-recommender-system/
│── data/                # Datasets (sectors, LGAs, investor profiles)
│── notebooks/           # Jupyter notebooks for EDA and model training
│── app/                 
│   ├── main.py          # FastAPI backend
│   ├── recommender.py   # Core recommendation logic
│   └── models/          # Trained ML models (pickle/joblib files)
│── dashboard/           # Streamlit frontend
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup  

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/investment-recommender-system.git
cd investment-recommender-system
```

2. **Create virtual environment & install dependencies**  
```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt
```

3. **Run the FastAPI backend**  
```bash
uvicorn app.main:app --reload
```
API available at: `http://127.0.0.1:8000/docs`  

4. **Run the Streamlit dashboard**  
```bash
streamlit run dashboard/app.py
```

---

## 🧠 How It Works  
1. Load **sector & LGA investment data**.  
2. Preprocess investor input (capital, risk profile, preferred sector).  
3. Apply **machine learning models** (e.g., Random Forest, XGBoost, Logistic Regression).  
4. Generate **ranked recommendations** of investment opportunities.  
5. Visualize recommendations via **dashboard and API**.  

---

## 📊 Example Use Case  
- **Investor A**: ₦10M capital, low risk appetite, prefers Agriculture.  
- **System Output**:  
  - Agriculture in Lafia (ROI: 18%, Risk: Low)  
  - Agro-processing in Keffi (ROI: 15%, Risk: Medium)  
  - Livestock in Akwanga (ROI: 14%, Risk: Low)  

---

## 📌 Future Improvements  
- ✅ Integration with **real-time economic indicators**.  
- ✅ Multi-sector recommendation scoring.  
- ✅ Advanced **NLP for investor profiling**.  
- ✅ Deploy full system on **Hugging Face Spaces / AWS**.  

---

## 🙌 Acknowledgments  
Special thanks to **NASIDA Strategy & Innovation Team** for supporting the vision of a **data-driven investment promotion system**.  
