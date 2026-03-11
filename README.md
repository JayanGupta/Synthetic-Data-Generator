# 🧬 Synthetic Data Generator — AI-Assisted Schema & Data Creation

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Gemini](https://img.shields.io/badge/LLM-Gemini%202.5%20Flash-purple)
![Faker](https://img.shields.io/badge/Data-Faker-green)
![CSV](https://img.shields.io/badge/Output-CSV-orange)

> A generative AI system that converts natural language business requirements into **normalized relational database schemas** and automatically produces a **Python-based synthetic data generator**.

The application uses **Google Gemini 2.5 Flash** to infer entities, relationships, and constraints, and generates a ready-to-run **Faker-powered Python script** to populate the schema with realistic synthetic datasets.

---

# 📂 Project Overview

This project implements a **natural language → database schema → synthetic data pipeline**.

Users can describe a business scenario in plain language, and the system will automatically:

1. Infer database entities and relationships  
2. Construct a normalized relational schema  
3. Enforce primary and foreign key constraints  
4. Generate a Python script that produces synthetic CSV datasets  

The result is a **fully functional dataset generator** suitable for:

- Machine learning experimentation
- database prototyping
- analytics testing
- application development

---

# ⚙️ System Workflow

The system follows a structured generation pipeline.

### 1. 🧠 Schema Inference
The user provides a **natural language description** of a system.

Example:

> “E-commerce platform with users, products, orders, and payments.”

The LLM analyzes the prompt and infers:

- entities
- attributes
- relationships
- keys and constraints

---

### 2. 🗄️ Relational Schema Construction

The application converts the inferred structure into **normalized database tables** including:

| Component | Description |
|---|---|
| Tables | Entities extracted from the use case |
| Columns | Attributes of each entity |
| Primary Keys | Unique identifiers |
| Foreign Keys | Relationships across tables |

Referential integrity is preserved across all generated tables.

---

### 3. 🧪 Synthetic Data Script Generation

After the schema is created, the system generates a **Python script** that uses the `Faker` library to produce realistic synthetic data.

Key features include:

- realistic names, addresses, timestamps
- customizable dataset sizes
- schema-aware column generation

---

### 4. 🔗 Dependency Ordering (Topological Sorting)

To ensure foreign key constraints are respected, the system applies **topological sorting** to determine the correct order of table generation.

For example:
Users → Orders → Order_Items

This prevents invalid references during dataset creation.

---

# 🌟 Core Features

| Feature | Description |
|---|---|
| Natural Language Schema Design | Convert business descriptions into relational schemas |
| Referential Integrity | Automatic PK/FK relationship enforcement |
| Synthetic Data Generation | Python script generation using Faker |
| Dependency Resolution | Topological ordering of table generation |
| Interactive UI | Streamlit-based interface |
| One-Click Export | Download ready-to-run data generation script |

---

# 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Interface | Streamlit |
| Language Model | Gemini 2.5 Flash |
| Data Generation | Faker |
| Data Handling | Pandas |
| Environment Management | python-dotenv |
| Language | Python |

---

# 🗂️ Project Structure
synthetic-data-generator/

├── app.py # Streamlit interface
├── generator_logic.py # LLM schema inference + script generation
├── requirements.txt # Python dependencies


---

# 🚀 Getting Started

### Prerequisites

Ensure the following are installed:

- Python **3.8+**
- Google **Gemini API Key**

Get one from:

https://aistudio.google.com/

---

### Installation

Clone the repository and install dependencies:

```bash
cd code
pip install -r requirements.txt
```
▶️ Running the Application

Start the Streamlit interface:

streamlit run app.py
📌 Usage

Enter your Gemini API Key in the sidebar

Describe your business use case

# Example:
- Marketplace platform with buyers, sellers, products, and orders
- The system generates a relational schema
- Download the generated script:
- generate_data.py
- Run the script to generate CSV datasets:

python generate_data.py
# 📊 Example Output

Generated datasets may include tables such as:

1. users.csv
2. orders.csv
3. products.csv
4. payments.csv

All tables maintain valid relational dependencies.

# 👨‍💻 Author

Jayan Gupta
Data Scientist | Machine Learning | AI Systems
