# 🌊 DEEP ORIGIN

AI-powered eDNA biodiversity analysis platform for marine ecosystems.

DEEP ORIGIN helps identify taxonomy, assess biodiversity, and detect potential novel taxa from environmental DNA (eDNA) FASTA datasets using Machine Learning and sequence similarity pipelines.

---

# 🚀 Live Demo

https://deep-origin.vercel.app/

---

# 📌 Problem Statement

Pollution in deep-sea ecosystems, limited accessibility, and incomplete biological reference databases make biodiversity monitoring difficult.

Traditional biodiversity analysis pipelines are computationally expensive and often:

* Misclassify species
* Miss unknown organisms
* Require heavy manual analysis

DEEP ORIGIN solves this with an intelligent AI-based workflow for faster, scalable, and automated biodiversity assessment.

---

# 🧠 Core Features

✅ Upload FASTA sequence files
✅ Automatic DNA sequence preprocessing
✅ k-mer based DNA vectorization
✅ PCA embedding generation
✅ Taxonomic similarity classification
✅ Novel taxa detection
✅ Confidence scoring
✅ Cluster analytics
✅ Summary statistics dashboard
✅ Download-ready analysis results

---

# ⚙️ Tech Stack

## Frontend

* React.js
* TypeScript
* Vite
* Tailwind CSS

## Backend

* Flask
* Python

## Machine Learning

* NumPy
* Scikit-learn
* PCA
* Cosine Similarity

## Deployment

* Vercel (Frontend)
* Railway (Backend)

---

# 🔬 How It Works

## Step 1: Upload FASTA File

Users upload environmental DNA (eDNA) FASTA datasets.

## Step 2: Preprocessing

DNA reads are cleaned and converted into k-mer sequence patterns.

## Step 3: Feature Encoding

Sequences are transformed into numerical vector embeddings.

## Step 4: Dimensionality Reduction

PCA generates compressed embeddings for faster similarity analysis.

## Step 5: Taxonomic Classification

Sequences are compared against known reference embeddings.

## Step 6: Novel Taxa Detection

Unknown sequence patterns are flagged as potential novel organisms.

## Step 7: Results Dashboard

Generated outputs include:

* Taxa labels
* Confidence scores
* Novel taxa alerts
* Sequence lengths
* Cluster summaries
* Biodiversity statistics

---

# 📂 Project Structure

```bash
DEEP_ORIGIN/
├── Deep Origin Model/        # Flask backend + ML pipeline
├── ocean-dna-navigator/      # React frontend
├── models/                   # Saved ML artifacts
└── uploads/                  # Uploaded FASTA files
```

---

# 💻 Run Locally

## Clone Repository

```bash
git clone https://github.com/your-username/DEEP_ORIGIN.git
cd DEEP_ORIGIN
```

---

## Backend Setup

```bash
cd "Deep Origin Model"
pip install -r requirements.txt
python app.py
```

Runs on:

```bash
http://127.0.0.1:5000
```

---

## Frontend Setup

```bash
cd ocean-dna-navigator
npm install
npm run dev
```

Runs on:

```bash
http://localhost:5173
```

---

# 🌍 Use Cases

* Marine biodiversity monitoring
* Pollution impact assessment
* Deep-sea ecosystem research
* Novel species discovery
* Conservation policy support
* Scientific eDNA analysis

---

# 📈 Future Scope

* Deep learning DNA transformer models
* Real-time ocean sensor integration
* Taxonomy tree visualization
* GIS biodiversity mapping
* Automated PDF scientific reports
* Multi-user research dashboard

---

# 👨‍💻 Developer

**Individual Project**
Developed for AI-powered marine biodiversity analysis and eDNA research applications.

---

# 📜 License

MIT License

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🚀 Share it with others
