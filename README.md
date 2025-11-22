# Data Processing (OOP Version)

This project demonstrates how to process CSV data using an object-oriented programming (OOP) approach in Python.  
It replaces procedural data-processing techniques with reusable classes — **DataLoader**, **Table**, and **DB** — that behave like a lightweight database engine.

The system can:

- Load CSV files safely  
- Store tables in an in-memory database  
- Filter rows based on any condition  
- Perform aggregation (min, max, count, average, etc.)  
- Join tables on a shared key (similar to SQL joins)  
- Chain operations together  

--- 

# Classes

## 1. `DataLoader`
Handles loading CSV files using Python’s built-in `csv.DictReader`.

### Features
- Automatically finds the script’s directory using `__file__`
- Loads CSV files into a list of dictionaries

## 2. `Table`

### Filtering
- Using Filter with keyword.

### Aggregation
- Using to find min, max, avg, etc.

### Join
- Join two tables together.

## 3. `DB`
- A tiny in-memory database holding multiple Table objects.

---

## Requirements

* Python 3.x

---

##  How to Use

To run the demonstration script, execute `data.processing.py` from your terminal:

```bash
