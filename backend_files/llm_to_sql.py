import requests
import re

OLLAMA_URL="http://localhost:11434/api/generate"

def nl_to_sql(user_question):
    prompt=f"""

    Convert the question into SAFE SQL query.
    Rules:
    - Only SELECT queries
    - No DELETE, UPDATE, DROP

    Schema:
    departments (id,name) 
    employees (id,name, department_id, email, salary)
    products (id,name, price)
    orders (id,customer_name, employee_id, order_total, order_date) 

    Question:
    {user_question}

    SQL:

    """
        

    response=requests.post(
    OLLAMA_URL,
    json={
    "model":"mistral",
    "prompt":prompt,
    "stream":False
    }
    )



       
    text=response.json()["response"].strip()

        # Extract only the SQL from the text
    # This regex finds the first SELECT ... ; block
    match = re.search(r"(SELECT[\s\S]+?;)", text, re.IGNORECASE)
    if match:
        sql_query = match.group(1)
    else:
        raise Exception("No SQL query found in LLM response")

   
    sql_query = sql_query.strip()

    return sql_query
