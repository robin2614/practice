import boto3

def get_csv_to_s3(bucket_name, s3_key, file_name):
	s3 = boto3.client('s3')
	try:
		s3.download_file(bucket_name, s3_key, file_name) # kuchh bhi change nahi karna hain
		print("File download successfully to s3")
	except Exception as e:
		print(f"An error occurred: {str(e)}")

bucket_name = 'datasem5a-2614' # bucket name jisme file hain
file_name = 'jitu.xlsx' # save as file name dena
s3_key = 'JITUBHAI.xlsx' # jo file download karna hain uska name

get_csv_to_s3(bucket_name, s3_key, file_name)