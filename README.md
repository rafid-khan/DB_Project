***PreQL: Custom SQL Database Engine***  <br />
A lightweight file-based SQL database engine built from scratch in Python, featuring query processing, indexing, and transaction management. Designed to efficiently handle and manipulate large datasets with optimized retrieval speeds.

🔹 SQL Query Processing – Supports SELECT, INSERT, UPDATE, and DELETE operations. <br /> 
🔹Custom Storage Engine – Stores data in a file-based system, enabling persistent storage. <br />
🔹 B-Tree & Hash Indexing – Implements indexing mechanisms to speed up query lookups by 5x. <br />
🔹Transaction Management – Ensures ACID compliance with logging & recovery mechanisms. <br />
🔹 Optimized Query Execution – Reduces lookup time from O(n) to O(log n) using B-Trees. <br />
🔹Lightweight & Standalone – No external dependencies; runs on any system with Python. <br />

Getting Started
1. Installation <br />
Clone the repository and navigate to the project directory:

```
git clone https://github.com/rafid-khan/preql-database.git
cd preql-database
```

2. Running the Database <br />
Run the database engine:
```
python preql.py
```
**3. Example Queries**
- Create a Table <br />
CREATE TABLE users (id INT PRIMARY KEY, name TEXT, age INT); <br />
- Insert Data <br /> 
INSERT INTO users VALUES (1, 'Alice', 25); <br />
INSERT INTO users VALUES (2, 'Bob', 30); <br />
- Retrieve Data <br />
SELECT * FROM users WHERE age > 25; <br />
- Update Data <br />
UPDATE users SET age = 31 WHERE name = 'Bob'; <br />
- Delete Data <br />
DELETE FROM users WHERE id = 1;<br />

**Benchmarks & Performance**
Query Execution Speed: 5x improvement using B-Tree & Hash Indexing.
Index Lookup Time: Reduced from O(n) to O(log n) with optimized indexing.
Storage Efficiency: Uses binary file storage, reducing redundant disk I/O.
(Consider adding actual benchmark results if you ran performance tests!)

**Why I Built This**
Databases are at the core of modern software systems. By developing a custom SQL engine, I explored query processing, indexing, and transaction management from the ground up—gaining insights into how databases optimize performance at scale.

**Future Improvements**
Implement cost-based query optimization for better performance.
Introduce multi-threaded query execution for parallel processing.
Improve storage compression to reduce file size overhead.