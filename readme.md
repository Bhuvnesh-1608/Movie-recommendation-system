# 🎬 CineMatch: Full-Stack Movie Recommendation Hub

An AI-powered full-stack web application that delivers real-time movie recommendations using content-based filtering. The system features an engineered vector-space machine learning engine coupled with a high-performance web API and a modern, responsive user interface.

### 🌐 Live Production Links
* **Frontend Web App:** [CineMatch on Vercel](https://movie-recommendation-system-nurq.vercel.app)
* **Backend API Server:** [CineMatch Engine on Render](https://movie-recommendation-system-bflc.onrender.com)

---

## 🚀 Key Features
* **AI-Driven Vector Recommendations:** Utilizes text vectorization and cosine similarity matrices to map user favorites to the closest multi-dimensional neighbors.
* **Granular Multi-Column Search:** Includes case-insensitive dynamic filtering across deep metadata layers like structural Genres, Directors, and Top-5 Cast entries.
* **Robust Input Sanitization:** JavaScript-driven automatic whitespace removal and uniform lowercase parsing to prevent data mismatch errors.
* **Decoupled Cloud Architecture:** Frontend UI hosted on Vercel seamlessly communicating with a centralized Python REST API hosted on Render.

---

## 🛠️ System Architecture & Tech Stack

* **Machine Learning & Core Engineering:** Python, Pandas, NumPy, Scikit-Learn (Cosine Similarity, Data Aggregation)
* **Backend Application Server:** FastAPI, Uvicorn ASGI server (Deployed on Render)
* **Frontend Web Interface:** Native HTML5, CSS3, Asynchronous JavaScript Fetch API (Deployed on Vercel)
* **Version Control & CI/CD:** Git, GitHub, Git LFS (Large File Storage for ML models)

---

## 📂 Project Structure

```text
movie_recmd/
│
├── datasets/               # Raw TMDB metadata CSV files
├── main.py                 # FastAPI backend routing logic 
├── index.html              # Responsive dark-theme frontend web interface
├── sol.ipynb               # Jupyter Notebook tracking vector training & ETL pipeline
├── .gitignore              # Tells git to exclude non-essential files
├── .gitattributes          # Git LFS configuration for heavy .pkl files
└── README.md               # Interactive repository documentation