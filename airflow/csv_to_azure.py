from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from airflow.hooks.base_hook import BaseHook
import os

# Get the current working directory
current_directory = os.getcwd()

# Define the filename
filename = "premier_league_results.csv"

# Construct the full file path
file_path = os.path.join(current_directory, filename)

# Load the data and process it as per your requirements
# Assuming your existing script generates a DataFrame 'df' 
# Replace this with your actual data processing steps

# Save the dataframe to a CSV file locally
csv_file = file_path

 # Get Azure Blob Storage connection details from Airflow connection
conn = BaseHook.get_connection('azure_blob_id')
account_name = conn.login
account_key = conn.password
container_name = "storage"  # Your container name

# Blob client setup
blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net",
    credential=account_key
)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=filename)



# Upload the CSV file to Azure Blob Storage
with open(csv_file, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

# print(f"File uploaded to https://sshresthadatalake.blob.core.windows.net/storage/premier_league_results.csv")
# print("Data has been written to 'premier_league_results.csv'.")

print(f"File uploaded to https://{account_name}.blob.core.windows.net/{container_name}/{filename}")
print(f"Data has been written to '{filename}'.")

def delete_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)
            print(f"File '{file_path}' has been successfully deleted.")
        else:
            print(f"The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")

# Example usage
file_to_delete = file_path
delete_file(file_to_delete)

