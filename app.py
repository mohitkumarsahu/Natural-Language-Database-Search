from flask import Flask, render_template, request
from llm_to_sql import nl_to_sql
from db_execute import execute_sql

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sql = None
    results = None
    error = None

    if request.method == 'POST':
        question = request.form.get('query', '').strip()
        
        if not question:
            error = "Please enter a question"
            return render_template("index.html", sql=sql, results=results, error=error)

        try:
            print(f"\n=== DEBUG INFO ===")
            print(f"Question: {question}")
            
            # Generate SQL from natural language
            sql = nl_to_sql(question)
            print(f"Generated SQL: {sql}")
            
            # Execute SQL query
            cols, rows = execute_sql(sql)
            print(f"Columns: {cols}")
            print(f"Rows count: {len(rows)}")
            print(f"Rows data: {rows}")
            
            # Convert to list of dictionaries
            results = [dict(zip(cols, row)) for row in rows]
            print(f"Results: {results}")
            print(f"Results length: {len(results)}")
            print(f"=== END DEBUG ===\n")
            
        except Exception as e:
            error = str(e)
            print(f"ERROR: {error}")
            import traceback
            traceback.print_exc()

    return render_template(
        "index.html",
        sql=sql,
        results=results,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)