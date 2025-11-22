# Data Processing (OOP Version)

This project demonstrates how to transform CSV-based data handling into a clean, object-oriented Python design.  
It includes three main classes:

- **DataLoader** – loads CSV files into Python dictionaries  
- **Table** – supports filtering, aggregation, and table joining  
- **DB** – a simple in-memory table storage and lookup system  

The script processes data from `Cities.csv` and `Countries.csv`, performs filtering, aggregation, and joins, and prints the results.

---

## Features

### 1. DataLoader
Handles importing CSV files.

- Automatically sets base path to the script’s directory if none is provided.
- `load_csv(filename)` returns a list of dictionaries representing rows.

### 2. DB (Simple In-Memory Database)
A lightweight storage class.

- `insert(table)` stores a Table object by name.
- `search(name)` retrieves a stored table.

### 3. Table Class
Represents a data table and offers:

#### Filtering
```python
table.filter(lambda row: condition)

---

## Requirements

* Python 3.x

---

##  How to Use

To run the demonstration script, execute `data.processing.py` from your terminal:

```bash
