# AI-Powered Synthetic Data Generator

An intelligent, Streamlit-based web application that leverages Google's Gemini 2.5 Flash model to instantly translate business use cases into normalized relational database schemas. It automatically infers the correct tables, columns, primary keys, and foreign keys while enforcing referential integrity. In addition, it generates a complete, ready-to-use Python script (utilizing the `Faker` library) that you can run to populate your new schema with realistic synthetic data in CSV format.

## Features

- **Natural Language to Schema:** Describe your business requirement (e.g., "E-commerce system with users, products, and orders") and the AI will design a complete database schema for you.
- **Referential Integrity:** Ensures correct relationships, Primary Keys (PK), and Foreign Keys (FK) across inferred tables.
- **Synthetic Data Script Generation:** Automatically creates a Python script that uses `Faker` to generate synthetic data based on the inferred schema.
- **Topological Sorting:** Orders data generation intelligently to prevent foreign key constraint violations.
- **One-Click Download:** Provides a downloadable, ready-to-run Python (`generate_data.py`) script right from the app interface.
- **Sleek, Premium UI:** Enjoy an intuitive, dark-themed user interface designed for a seamless user experience.

## Requirements

The application requires Python 3.8+ and relies on the following packages:
- `streamlit`
- `pandas`
- `google-generativeai`
- `faker`
- `python-dotenv`

## Installation

1. Clone or download this repository.
2. Navigate to the `code` directory.
3. Install the required dependencies using pip:

```bash
cd code
pip install -r requirements.txt
```

## Usage

1. **Get an API Key:** Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).
2. **Run the Application:** Start the Streamlit app by running the following command from the `code` directory:

```bash
streamlit run app.py
```

3. **Provide Your Key:** Enter your Gemini API key in the app's sidebar. *(Note: Your API key is used only for the current session and is never stored.)*
4. **Generate Your Schema:** Describe your business usecase in the prompt area. The AI will output an ER schema as a set of logical tables.
5. **Download Script:** Review the schema, then download the generated `generate_data.py` script.
6. **Generate Data:** Run the generated script locally to produce realistic CSVs for each table.

```bash
python generate_data.py
```

## Structure

- `app.py`: The main Streamlit web application frontend and chat interface.
- `generator_logic.py`: Contains `DataGeneratorLogic` class responsible for communicating with the Gemini API to infer schemas and write the Python Faker script.
- `requirements.txt`: Defines Python dependencies for this project.

## Author

Built By Jayan Gupta
