# 🚗 Smart Traffic Intelligence & Risk-Aware Routing System

> A production-style data science project that simulates how modern cities can **predict traffic, detect accident hotspots, and optimize routes intelligently** using machine learning, geo-spatial analysis, and graph algorithms.

---

## 🔥 Project Overview

Urban traffic is chaotic, unpredictable, and often dangerous. This project tackles that problem by building an **end-to-end intelligent system** that:

- 📊 Analyzes real-world accident data  
- 🚦 Predicts traffic congestion patterns  
- 🧠 Calculates accident risk levels  
- 🗺️ Optimizes routes based on **traffic + safety**  

This is not just a notebook — it's a **full-stack data science system** similar to what senior data scientists build in industry.

---

## 🎯 Key Features

### 🚦 Traffic Prediction
- Predicts daily travel time using machine learning  
- Uses historical congestion patterns (AM, PM, Midday, etc.)

### ⚠️ Accident Risk Modeling
- Computes **risk score** based on:
  - accident frequency  
  - severity ratio  
  - injury ratio  
- Classifies regions into **Low / Medium / High risk**

### 🗺️ Geo-Spatial Hotspot Detection
- Uses clustering (DBSCAN) to detect accident-prone zones  
- Visualized via interactive heatmaps  

### 🧭 Smart Route Optimization
- Uses graph algorithms (Dijkstra via NetworkX)  
- Considers:
  - distance  
  - traffic congestion  
  - accident risk  

👉 Outputs the **fastest AND safest route**

### 🌐 API + Dashboard
- Backend built with FastAPI  
- Interactive UI with Streamlit  
- Real-time predictions and route suggestions  

---

## 🧱 Project Architecture
Data Sources → Ingestion → Processing → Feature Engineering → Models → API → Dashboard


---


---

## 📊 Data Sources

- Government road accident datasets (India)  
- Uber Movement / Traffic datasets  (Kaggle)
- OpenStreetMap (road network)  
- Weather data (optional)  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ayush-Debnath/smart-traffic.git
cd smart-traffic
```
---
### Running the Project
## Run FastAPI Backend
```bash
uvicorn src.api.app:app --reload

Open:
http://127.0.0.1:8000/docs
```

### Run Streamlit Dashboard
```bash
streamlit run dashboards/app.py
```