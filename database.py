from google.cloud import bigquery

from google.oauth2 import service_account

# TODO(developer): Set key_path to the path to the service account key
#                  file.
key_path = ".keys/CovidDataKey.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)



def query(queryString):
    return client.query(queryString)





# TESTS: Print the results.
# query_job = query(query_string)
# for row in query_job.result():  # Wait for the job to complete.
#    print("{}: {}, {}, {}, {}, {}, {}".format(row["date"], row["new_confirmed"], row["new_deceased"], row["cumulative_confirmed"], row["cumulative_deceased"], row["latitude"], row["longitude"]))