import database

query_string = """SELECT date, place_id, new_confirmed, new_deceased, cumulative_confirmed, cumulative_deceased, latitude, longitude FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code LIKE '%CA%' AND latitude IS NOT null AND new_confirmed IS NOT null
ORDER BY date DESC
LIMIT 100000
"""

table = database.query(query_string)
