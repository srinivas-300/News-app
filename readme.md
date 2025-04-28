📰 News Personalization App (AI-Driven)
Welcome to the News Personalization App repository!
This project delivers a smart, AI-powered news feed that personalizes content for users by combining OCR text extraction, Retrieval-Augmented Generation (RAG), Named Entity Recognition (NER), and LLM-based similarity checks.

📌 Project Overview
Fetches real-time news articles using Google News API.

Extracts text from uploaded images/documents via Tesseract OCR.

Processes news content using a RAG system (Encoder → Retriever → Generator).

Applies Named Entity Recognition (NER) to extract key information.

Personalizes feeds dynamically based on user interactions and activity logs.

Deployed on AWS using scalable and secure architecture.

🛠️ Tech Stack

Layer	Technologies Used
Backend	Flask, Python
AI/NLP	Tesseract OCR, Gemini LLM, RAG System, NER APIs
Database	MongoDB Atlas
External APIs	Google News API
Infrastructure	AWS (API Gateway, Load Balancer, EC2, S3), Docker
CI/CD	GitHub Actions
Deployment	Dockerized Flask app on AWS EC2
📐 Architecture Overview
plaintext
Copy
Edit
User → AWS API Gateway → Load Balancer → EC2 (Flask App) → 
  [Google News API + Gemini LLM] → 
  RAG System (Encoder → Retriever → Generator) →
  MongoDB Atlas + S3 → 
User (Personalized Feed)
Main Components:

AWS Infrastructure: API Gateway, VPC, Load Balancer, EC2, S3

Flask Application: Handles user interactions and backend operations

RAG Client: Processes news articles with Encoder, Retriever, Generator modules

Databases: MongoDB Atlas for storing articles, user profiles, OCR outputs

🚀 Features
OCR Integration: Extracts readable text from uploaded images.

RAG System: Enhances news search and summarization with AI retrieval.

Named Entity Recognition: Identifies and extracts key entities from articles.

Similarity Detection: Prevents duplicate or highly similar article recommendations.

Personalized Feed: Dynamic content recommendations based on user activity.

Activity Tracking: Monitors interactions to refine and improve personalization.

📦 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/news-personalization-app.git
cd news-personalization-app
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure environment variables:

Create a .env file:

ini
Copy
Edit
MONGO_URI=your_mongodb_atlas_uri
GOOGLE_NEWS_API_KEY=your_google_news_api_key
GEMINI_LLM_API_KEY=your_gemini_llm_api_key
AWS_ACCESS_KEY=your_aws_access_key
AWS_SECRET_KEY=your_aws_secret_key
Run the application locally:

bash
Copy
Edit
python app.py
🗄️ Project Structure
plaintext
Copy
Edit
/app
  ├── routes/
  ├── services/
  │     ├── ocr_service.py
  │     ├── rag_service.py
  │     ├── ner_service.py
  │     ├── news_fetch_service.py
  │     ├── similarity_service.py
  ├── models/
  │     ├── article_model.py
  │     ├── user_model.py
  ├── utils/
  ├── config.py
  ├── app.py
/docker
/scripts
/tests
README.md
requirements.txt
Dockerfile
☁️ Deployment Architecture
AWS EC2 instances running Dockerized Flask containers.

API Gateway managing HTTP/HTTPS traffic routing.

MongoDB Atlas hosting cloud databases.

Amazon S3 for storing images and extracted OCR data.

GitHub Actions for continuous integration and deployment (CI/CD).

📊 Future Scope
Integrate voice-based news summarization using Speech-to-Text APIs.

Expand multilingual OCR and article translation features.

Build predictive models to recommend trending news topics.

Incorporate additional LLMs for deeper contextual personalization.

🤝 Contributing
Contributions are welcome!
Please open an issue first to discuss major changes.
Feel free to fork the repository, make your changes, and submit a pull request.

🛡️ License
This project is licensed under the MIT License.
