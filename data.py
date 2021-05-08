import database

query_string = """SELECT date, location_key , place_id, new_confirmed, new_deceased, cumulative_confirmed, cumulative_deceased, latitude, longitude FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code LIKE '%CA%' AND latitude IS NOT null AND new_confirmed IS NOT null
ORDER BY date DESC
LIMIT 100000
"""

table = database.query(query_string)

#  for row in table.result():  # Wait for the job to complete.
#     print("{}: {}, {}, {}, {}, {}, {}".format(row["date"], row["new_confirmed"], row["new_deceased"], row["cumulative_confirmed"], row["cumulative_deceased"], row["latitude"], row["longitude"]))

byProvince = {}

for row in table.result():
    Provinces = byProvince.keys()
    if row["location_key"] not in Provinces:
        byProvince[row["location_key"]] = [row]
    else:
        byProvince[row["location_key"]].append(row)

