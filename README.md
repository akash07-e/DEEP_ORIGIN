🌊 DEEP ORIGIN
AI-powered eDNA biodiversity analysis platform for marine ecosystems.
DEEP ORIGIN helps identify taxonomy, assess biodiversity, and detect potential novel taxa from environmental DNA (eDNA) FASTA datasets using Machine Learning and sequence similarity pipelines.

🚀 Live Demo
https://deep-origin.vercel.app/

📌 Problem Statement
Pollution in deep-sea ecosystems, limited accessibility, and incomplete biological reference databases make biodiversity monitoring difficult.

Traditional pipelines are computationally expensive and often:

Misclassify species
Miss unknown organisms
Require heavy manual analysis
DEEP ORIGIN solves this with an intelligent AI-based workflow for faster biodiversity assessment.

🧠 Core Features
✅ Upload FASTA sequence files
✅ Automatic sequence preprocessing
✅ k-mer based DNA vectorization
✅ PCA embedding generation
✅ Taxonomic similarity classification
✅ Novel taxa detection
✅ Confidence scoring
✅ Cluster analytics
✅ Summary statistics dashboard
✅ Download-ready results

⚙️ Tech Stack
Frontend
React.js
TypeScript
Vite
Tailwind CSS
Backend
Flask
Python
Machine Learning
NumPy
Scikit-learn
PCA
Cosine Similarity
Deployment
Vercel (Frontend)
Railway (Backend)
🔬 How It Works
Step 1: Upload FASTA File
User uploads environmental DNA sequences.

Step 2: Preprocessing
DNA reads are cleaned and converted into k-mer patterns.

Step 3: Feature Encoding
Sequences are transformed into numerical vectors.

Step 4: Dimensionality Reduction
PCA creates embeddings for faster search.

Step 5: Classification
Compare with known reference embeddings.

Step 6: Novelty Detection
Unknown patterns are flagged as potential novel taxa.

Step 7: Results Dashboard
Outputs include:

Taxa labels
Confidence scores
Novel taxa alerts
Sequence lengths
Counts summary
📂 Project Structure
DEEP_ORIGIN/ ├── Deep Origin Model/ Flask backend + ML pipeline
├── ocean-dna-navigator/ React frontend
├── models/ Saved artifacts
└── uploads/ Uploaded FASTA files

💻 Run Locally
Clone Repo
git clone https://github.com/AnshSinghRathoree/DEEP_ORIGIN.git
cd DEEP_ORIGIN

Backend Setup
cd "Deep Origin Model"
pip install -r requirements.txt
python app.py

Runs on:
http://127.0.0.1:5000

Frontend Setup
cd ocean-dna-navigator
npm install
npm run dev

Runs on:
http://localhost:5173

🌍 Use Cases
Marine biodiversity monitoring
Pollution impact studies
Deep-sea ecosystem research
Novel species discovery
Conservation policy support
Scientific eDNA analysis
📈 Future Scope
Deep learning DNA transformer models
Real-time ocean sensor integration
Taxonomy tree visualization
GIS biodiversity mapping
PDF scientific reports
Multi-user research dashboard
👨‍💻 Team
DEEP ABYSS
Smart India Hackathon 2025

📜 License
MIT License

⭐ Support
If you like this project:

⭐ Star the repo
🍴 Fork it
🚀 Share it
