# 📰 News Personalization App (AI-Driven)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Deployment: AWS](https://img.shields.io/badge/Deployed%20on-AWS-orange.svg)](https://aws.amazon.com/)
[![Dockerized](https://img.shields.io/badge/Docker-Containerized-blue.svg)](https://www.docker.com/)

Welcome to the **News Personalization App** repository!  
This project delivers a smart, AI-powered news feed that personalizes content for users by combining OCR text extraction, Retrieval-Augmented Generation (RAG), Named Entity Recognition (NER), and LLM-based similarity checks.

---

## 📌 Project Overview

- Fetches real-time news articles using **Google News API**.
- Extracts text from uploaded images/documents via **Tesseract OCR**.
- Processes news content using a **RAG system** (Encoder → Retriever → Generator).
- Applies **Named Entity Recognition (NER)** to extract key information.
- Personalizes feeds dynamically based on user interactions and activity logs.
- Deployed on **AWS** using scalable and secure architecture.

---

## 🛠️ Tech Stack

| Layer         | Technologies Used |
|---------------|--------------------|
| Backend       | Flask, Python |
| AI/NLP        | Tesseract OCR, Gemini LLM, RAG System, NER APIs |
| Database      | MongoDB Atlas |
| External APIs | Google News API |
| Infrastructure| AWS (API Gateway, Load Balancer, EC2, S3), Docker |
| CI/CD         | GitHub Actions |
| Deployment    | Dockerized Flask app on AWS EC2 |

---

## 📐 Architecture Overview

User → AWS API Gateway → Load Balancer → EC2 (Flask App) → 
  [Google News API + Gemini LLM] → 
  RAG System (Encoder → Retriever → Generator) →
  MongoDB Atlas + S3 → 
User (Personalized Feed)




## 🛠️ Main Components

- **AWS Infrastructure:** API Gateway, VPC, Load Balancer, EC2, S3
- **Flask Application:** Handles user interactions and backend operations
- **RAG Client:** Processes news articles with Encoder, Retriever, Generator modules
- **Databases:** MongoDB Atlas for storing articles, user profiles, and OCR outputs



## 🚀 Features

- **OCR Integration:** Extracts readable text from uploaded images.
- **RAG System:** Enhances news search and summarization with AI retrieval.
- **Named Entity Recognition (NER):** Identifies and extracts key entities from articles.
- **Similarity Detection:** Prevents duplicate or highly similar article recommendations.
- **Personalized Feed:** Dynamic content recommendations based on user activity.
- **Activity Tracking:** Monitors user interactions to refine and improve personalization.


## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/news-personalization-app.git
   cd news-personalization-app
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Configure environment variables: Create a .env file and add:**
   ```bash
   MONGO_URI=your_mongodb_atlas_uri
   GOOGLE_NEWS_API_KEY=your_google_news_api_key
   GEMINI_LLM_API_KEY=your_gemini_llm_api_key
   AWS_ACCESS_KEY=your_aws_access_key
   AWS_SECRET_KEY=your_aws_secret_key
5. **Run the application locally:**
   ```bash
   python app.py




---

## ☁️ Deployment Architecture

- AWS EC2 instances running Dockerized Flask containers.
- API Gateway managing HTTP/HTTPS traffic routing.
- MongoDB Atlas hosting cloud databases.
- Amazon S3 for storing images and extracted OCR data.
- GitHub Actions for continuous integration and deployment (CI/CD).


## 📊 Future Scope

- Integrate **voice-based news summarization** using Speech-to-Text APIs.
- Expand **multilingual OCR** and **article translation** features.
- Build **predictive models** to recommend trending news topics.
- Incorporate additional **LLMs** for deeper contextual personalization.


   

