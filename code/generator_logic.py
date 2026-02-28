import google.generativeai as genai
import os
import json
import re
from typing import Dict, List, Any

class DataGeneratorLogic:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def _get_json_from_response(self, text: str) -> Any:
        try:
            # Look for JSON block in the response
            match = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL)
            if match:
                return json.loads(match.group(1))
            return json.loads(text)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return None

    def infer_schema(self, use_case: str) -> Dict:
        prompt = f"""
        You are a Database Architect. Analyze the following business use case and design a normalized relational schema.
        
        Business Use Case:
        "{use_case}"
        
        Return the schema in the following JSON format:
        {{
            "tables": [
                {{
                    "name": "table_name",
                    "description": "purpose of the table",
                    "columns": [
                        {{
                            "name": "column_name",
                            "type": "data_type",
                            "is_pk": true/false,
                            "is_fk": true/false,
                            "references": "other_table.column_name" (or null),
                            "faker_type": "appropriate_faker_method" (e.g., name, email, date_this_decade, random_int)
                        }}
                    ]
                }}
            ]
        }}
        
        Ensure:
        1. Correct Primary Keys (PK) and Foreign Keys (FK).
        2. Referential integrity.
        3. normalized structure.
        4. Appropriate faker types for each column.
        """
        
        response = self.model.generate_content(prompt)
        schema = self._get_json_from_response(response.text)
        return schema

    def generate_faker_script(self, schema: Dict, record_counts: Dict[str, int] = None) -> str:
        if not record_counts:
            record_counts = {table['name']: 10 for table in schema['tables']}
        
        # We need to sort tables by dependency to avoid FK errors
        # Simple topological sort (for now, assuming no circular deps)
        sorted_tables = self._topological_sort(schema['tables'])
        
        script = f"""import pandas as pd
from faker import Faker
import random

fake = Faker()

# Data Storage
data = {{}}
"""
        
        for table in sorted_tables:
            table_name = table['name']
            count = record_counts.get(table_name, 10)
            
            script += f"\n# Generating data for {table_name}\n"
            script += f"records = []\n"
            script += f"for _ in range({count}):\n"
            script += f"    record = {{\n"
            
            for col in table['columns']:
                col_name = col['name']
                if col.get('is_pk'):
                    # Simple incremental ID for now, or use faker if specified
                    script += f"        '{col_name}': _ + 1,\n"
                elif col.get('is_fk'):
                    ref = col['references'].split('.')
                    ref_table = ref[0]
                    ref_col = ref[1]
                    script += f"        '{col_name}': random.choice(data['{ref_table}'])['{ref_col}'],\n"
                else:
                    faker_method = col.get('faker_type', 'word')
                    script += f"        '{col_name}': fake.{faker_method}(),\n"
            
            script += f"    }}\n"
            script += f"    records.append(record)\n"
            script += f"data['{table_name}'] = records\n"
        
        script += """
# Export to CSV
for table_name, records in data.items():
    pd.DataFrame(records).to_csv(f"{table_name}.csv", index=False)
    print(f"Generated {len(records)} records for {table_name}.csv")
"""
        return script

    def _topological_sort(self, tables: List[Dict]) -> List[Dict]:
        # Basic dependency sorting
        visited = set()
        result = []
        
        def visit(table_name):
            if table_name in visited:
                return
            
            # Find the table object
            table = next((t for t in tables if t['name'] == table_name), None)
            if not table:
                return
                
            # Check dependencies
            for col in table['columns']:
                if col.get('is_fk') and col.get('references'):
                    ref_table = col['references'].split('.')[0]
                    if ref_table != table_name:
                        visit(ref_table)
            
            visited.add(table_name)
            result.append(table)

        for table in tables:
            visit(table['name'])
            
        return result
