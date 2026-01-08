from db import get_connection
from sentence_transformers import SentenceTransformer

model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

conn=get_connection()
cur=conn.cursor()


def create_embeddings():   # we are creating embeddings only for product name because mostly user query by product name and these are closly related.
    cur.execute("SELECT id, name from products")
    rows=cur.fetchall()

    for prod_id, name in rows:
        vector=model.encode(name).tolist()
        cur.execute(
            "UPDATE products SET embedding = %s WHERE id= %s", (vector,prod_id)
        )


    conn.commit()
    conn.close()

create_embeddings()



    
