# 1.Python Function for Aggregating Weather Data


def aggregate_weather_data(records):
    # Dictionary to store aggregated data for each city
    city_data = {}

    # Loop through each record
    for record in records:
        city = record.get("city")
        if city not in city_data:
            # Initialize a dictionary to store data for the city
            city_data[city] = {"temp_sum": 0, "temp_count": 0, "humidity_sum": 0, "humidity_count": 0}

        # Check and add temperature data
        if "temperature" in record:
            city_data[city]["temp_sum"] += record["temperature"]
            city_data[city]["temp_count"] += 1

        # Check and add humidity data
        if "humidity" in record:
            city_data[city]["humidity_sum"] += record["humidity"]
            city_data[city]["humidity_count"] += 1

    # Calculate averages and handle missing data
    for city, data in city_data.items():
        avg_temp = data["temp_sum"] / data["temp_count"] if data["temp_count"] > 0 else None
        avg_humidity = data["humidity_sum"] / data["humidity_count"] if data["humidity_count"] > 0 else None
        print(f"City: {city}, Avg Temperature: {avg_temp}, Avg Humidity: {avg_humidity}")

# Example Usage
weather_records = [
    {"city": "CityA", "temperature": 30, "humidity": 70},
    {"city": "CityB", "temperature": 20},
    {"city": "CityA", "temperature": 25, "humidity": 60},
    {"city": "CityB", "humidity": 65}
]

aggregate_weather_data(weather_records)


# 2. Python Function for Prime Factorization

def prime_factors(n):
    factors = []
    divisor = 2

    # Factor out the smallest primes
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1

    return factors

# call the function
print(prime_factors(60))  

# 3. SQL Query to Increase Prices by 10%

# 
# UPDATE products
# SET price = price * 1.10;

# SELECT name, price AS new_price
# FROM products;
