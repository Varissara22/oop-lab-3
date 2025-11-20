import csv, os
from pathlib import Path

class DataLoader:
    """Handles loading CSV data files."""
    
    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)
    
    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []
        
        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))
        
        return data

class DB:
    def __init__(self):
        self.data = {}
    
    def insert(self, table):
        self.data[table.name] = table

    def search(self, name):
        return self.data[name]
    
class Table:
    
    def __init__(self, name, table_data):
        self.name = str(name)
        self.table = table_data
        
        
    def filter(self, function=None):
        if function is None:
            return Table(self.name, self.table.copy())
        
        val = []
        for item in self.table:
            try:
                if function(item):
                    val.append(item)
            except Exception:
                continue
            
        return Table(self.name, val)
    
    def aggregate(self, aggregation_function, aggregation_key):
        data = []
        for item in self.table:
            x = item[aggregation_key]
            try:
                x = float(x)
            except ValueError:
                pass
            data.append(x)
        return aggregation_function(data)

    def join(self, other_table, key):
        joined_data = []
        table = {}
        for row in other_table.table:
            val_from_key = row.get(key)
            if val_from_key not in table:
                table[val_from_key] = []
            table[val_from_key].append(row)

        for row_self in self.table:
            val_key = row_self.get(key)
            if val_key in table:
                for row_self_two in table[val_key]:
                    merged = row_self.copy()
                    for key_t, val_t in row_self_two.items():
                        if key_t != key and key_t not in merged:
                            merged[key_t] = val_t
                    joined_data.append(merged)
        new_table_name = f"{self.name}_JOIN_{other_table.name}"
        return Table(new_table_name, joined_data)


    def __str__(self):
        return self.name + ':' + str(self.table)

loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:") 
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x)/len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:") 
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()