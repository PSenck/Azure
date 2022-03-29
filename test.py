from biomoni.file_manager import pull_azure_file
import os


connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
connection_string = "DefaultEndpointsProtocol=https;AccountName=biomonistorage;AccountKey=hwA0oCscA7HbTxYvkyainLR/5WrVk3lBkfsiCTJEbQCTAur5BHddOVnRxJlgt0iSxqxufqBmQUZvGCk3epXXBQ==;EndpointSuffix=core.windows.nett"
share_name = "biomoni-storage"
azure_exp_file_path = "Measurement-data/current_ferm/data.csv" 
azure_metadata_file_path = "Measurement-data/metadata_OPCUA.ods"
[pull_azure_file(connection_string= connection_string, share_name= share_name, azure_file_path= i) for i in [azure_exp_file_path, azure_metadata_file_path]]