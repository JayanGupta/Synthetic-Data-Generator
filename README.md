<div align="center">

# Synthetic Data Generator — AI-Assisted Schema & Data Creation

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://aistudio.google.com)
[![Faker](https://img.shields.io/badge/Faker-Data%20Generation-2ea44f?style=for-the-badge)](https://faker.readthedocs.io)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)

*A generative AI system that converts natural language business requirements into normalized relational database schemas and automatically produces a Python-based synthetic data generator.*

</div>

---

A Streamlit application powered by Google Gemini 2.5 Flash that takes a plain-language description of a business domain and outputs a fully functional, Faker-based Python script for generating realistic synthetic datasets. The system handles entity inference, schema normalization, referential integrity, and dependency-ordered table generation end-to-end.

---

## Table of Contents

- [Background](#background)
- [System Workflow](#system-workflow)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

---

## Background

Synthetic data is a critical resource in machine learning, database prototyping, and application testing — yet generating it at scale, with realistic values and valid relational dependencies, typically requires significant manual effort. This project eliminates that friction by automating the full pipeline through a large language model.

Users describe a business scenario in natural language. The system infers the underlying data model, constructs a normalized relational schema with primary and foreign keys, and emits a ready-to-run Python script that populates every table with realistic, schema-aware synthetic records.

---

## System Workflow

The application follows a four-stage generation pipeline:

**1. Schema Inference**

The user provides a natural language description of a system — for example:

> *"E-commerce platform with users, products, orders, and payments."*

Gemini 2.5 Flash analyzes the prompt and infers entities, attributes, relationships, and key constraints.

**2. Relational Schema Construction**

The inferred structure is converted into normalized database tables:

| Component | Description |
|-----------|-------------|
| Tables | Entities extracted from the use case |
| Columns | Typed attributes for each entity |
| Primary Keys | Unique identifiers per table |
| Foreign Keys | Cross-table relationships with referential integrity |

**3. Synthetic Data Script Generation**

A Python script is generated using the `Faker` library, producing realistic values for names, addresses, timestamps, and domain-specific fields. Dataset size is configurable at runtime.

**4. Dependency Ordering**

Topological sorting is applied across all tables to determine a valid generation order that respects foreign key dependencies — for example, `Users → Orders → Order_Items` — preventing invalid references in the output.

---

## Features

| Feature | Description |
|---------|-------------|
| Natural language schema design | Convert business descriptions into relational schemas via LLM |
| Referential integrity | Automatic PK/FK relationship enforcement across all tables |
| Synthetic data generation | Faker-powered Python script with realistic, typed values |
| Dependency resolution | Topological ordering ensures valid foreign key population order |
| Interactive UI | Streamlit-based interface with sidebar API key configuration |
| One-click export | Download the generated script (`generate_data.py`) directly from the UI |

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Interface | Streamlit |
| Language Model | Google Gemini 2.5 Flash |
| Data Generation | Faker |
| Data Handling | Pandas |
| Environment Management | python-dotenv |
| Language | Python 3.8+ |

---

## Project Structure

```
synthetic-data-generator/
 └── code
 |   ├── app.py                  # Streamlit interface and user interaction
 |   ├── generator_logic.py      # LLM schema inference and script generation
 |   ├── requirements.txt        # Python dependencies
 └── README.md
```

---

## Installation

**Prerequisites:** Python 3.8+ and a Google Gemini API key.

Obtain an API key from [Google AI Studio](https://aistudio.google.com/).

Clone the repository and install dependencies:

```bash
cd synthetic-data-generator
pip install -r requirements.txt
```

Create a `.env` file in the project root and add your API key:

```
GEMINI_API_KEY=your_api_key_here
```

---

## Usage

Start the Streamlit application:

```bash
streamlit run app.py
```

Then follow these steps in the browser interface:

1. Enter your Gemini API key in the sidebar
2. Describe your business use case in plain language, for example:
   > *"Marketplace platform with buyers, sellers, products, and orders"*
3. The system generates a normalized relational schema
4. Download the generated `generate_data.py` script
5. Run the script locally to produce CSV datasets:

```bash
python generate_data.py
```

---

## Example Output

For an e-commerce use case, the pipeline produces CSV files such as:

| File | Contents |
|------|----------|
| `users.csv` | User records with names, emails, registration dates |
| `products.csv` | Product listings with categories, prices, stock levels |
| `orders.csv` | Order records referencing valid user IDs |
| `payments.csv` | Payment records referencing valid order IDs |

All tables maintain valid relational dependencies in the correct generation order.

---

## Future Work

- **Schema editing UI** — allow users to review and modify the inferred schema before script generation
- **Multi-format export** — support JSON, SQL `INSERT` statements, and Parquet in addition to CSV
- **Database seeding** — direct insertion into PostgreSQL or SQLite without intermediate files
- **Expanded LLM support** — pluggable provider interface for OpenAI, Anthropic, and local models
- **Validation layer** — post-generation checks to verify referential integrity across all output files

---

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request. Ensure any new code is accompanied by clear inline documentation.

---

## License

This project is released for academic and research purposes. See `LICENSE` for details.
