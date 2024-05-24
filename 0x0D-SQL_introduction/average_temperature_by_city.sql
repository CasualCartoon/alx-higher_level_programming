-- This script calculates and displays the average temperature (Fahrenheit) by city
-- ordered by temperature in descending order.

-- Selecting city and calculating average temperature
SELECT city, AVG(temperature_fahrenheit) AS average_temperature
FROM weather_data  -- Replace with the actual table name
GROUP BY city
ORDER BY average_temperature DESC;
