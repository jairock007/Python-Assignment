# Weather Data Aggregation and Prime Factorization Application

This application consists of two main functionalities:
1. Aggregating weather data by city to calculate average temperatures and humidity.
2. Performing prime factorization of an integer.

## Features
- **Aggregate Weather Data**: Calculates average temperature and humidity from weather records for different cities.
- **Prime Factorization**: Finds and returns the prime factors of a given integer.

## Requirements
- Python 3.x
- No additional libraries required (standard libraries only).

## Setup

1. **Clone the Repository**:
   ```bash
   git clone [repository-url]
   cd [repository-directory]
   ```

2. **Run Weather Data Aggregation**:
   - Open a Python environment (interpreter, script, or IDE) and run the following code to aggregate weather data.
   ```python
   def aggregate_weather_data(records):
       # Function implementation here...

   weather_records = [
       {"city": "CityA", "temperature": 30, "humidity": 70},
       {"city": "CityB", "temperature": 20},
       {"city": "CityA", "temperature": 25, "humidity": 60},
       {"city": "CityB", "humidity": 65}
   ]

   aggregate_weather_data(weather_records)
   ```

3. **Run Prime Factorization**:
   - Use the following function to obtain the prime factors of an integer.
   ```python
   def prime_factors(n):
       # Function implementation here...

   print(prime_factors(60))  # Output: [(2, 2), (3, 1), (5, 1)]
   ```

4. **Optional SQL Operation**: 
   - If you want to increase prices in a database (assuming you have a `products` table), you can execute the following SQL query:
   ```sql
   UPDATE products
   SET price = price * 1.10;
   ```

   - To view the updated prices:
   ```sql
   SELECT name, price AS new_price
   FROM products;
   ```

## Usage

### Aggregating Weather Data
Input your weather records as dictionaries, with keys being `"city"`, `"temperature"`, and `"humidity"`. Call the `aggregate_weather_data` function with the list of records to print the averaged results for each city.

### Prime Factorization
Call the `prime_factors` function with an integer `n` to receive a list of tuples, where each tuple represents a prime factor and its count.

## Notes
- Ensure that your Python environment is properly set up to run these scripts.
- The SQL part assumes you have a SQL server environment set up, such as MySQL or PostgreSQL, and already populated with the appropriate table structure.
- Modify the SQL queries according to your database schema.

## Contributions
Feel free to contribute to the code by forking the repository and submitting a pull request.

## License
This project is licensed under the MIT License.
```

You can copy this text into a file named `README.md` in your project directory. Adjust the `[repository-url]` and `[repository-directory]` placeholders as needed for your specific project setup.
