# 🎬 CineMatch: Full-Stack Movie Recommendation Hub

An AI-powered full-stack web application that delivers real-time movie recommendations using content-based filtering. The system features an engineered vector-space machine learning engine coupled with a high-performance web API and a modern, responsive user interface.

---

## 🚀 Key Features
* **AI-Driven Vector Recommendations:** Utilizes text vectorization and cosine similarity matrices to map user favorites to the closest multi-dimensional neighbors.
* **Granular Multi-Column Search:** Includes case-insensitive dynamic filtering across deep metadata layers like structural Genres, Directors, and Top-5 Cast entries.
* **Robust Input Sanitization:** JavaScript-driven automatic whitespace removal and uniform lowercase parsing to prevent data mismatch errors.
* **Sleek UX Layout:** An immersive, modern dark-themed interface built natively without heavy third-party framework dependencies.

---

## 🛠️ System Architecture & Tech Stack

* **Machine Learning & Core Engineering:** Python, Pandas, NumPy, Scikit-Learn (Cosine Similarity, Data Aggregation)
* **Backend Application Server:** FastAPI, Uvicorn ASGI server
* **Frontend Web Interface:** Native HTML5, CSS3 (Flexbox/Grid layout layouts), Asynchronous JavaScript Fetch API

---

## 📂 Project Structure

```text
movie_recmd/
│
├── datasets/               # Raw TMDB metadata CSV files
├── main.py                 # FastAPI backend routing logic 
├── index.html              # Responsive dark-theme frontend web interface
├── sol.ipynb               # Jupyter Notebook tracking vector training & ETL pipeline
├── .gitignore              # Tells git to exclude heavy serialized models (.pkl)
└── README.md               # Interactive repository documentation