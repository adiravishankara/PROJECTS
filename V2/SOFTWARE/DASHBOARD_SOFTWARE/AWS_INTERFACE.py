import boto3

# Set the AWS IoT endpoint
endpoint = 'aligx8s99yr21-ats.iot.ap-northeast-1.amazonaws.com'

# Set the certificate and key paths
certificate_path = "CERTS/certificate.pem.crt"
private_key_path = "CERTS/private.pem.key"

# Create an AWS IoT client
client = boto3.client("iot", endpoint_url=endpoint, )

# Connect to AWS IoT
response = client.connect(
    caCertificate=certificate_path,
    clientCertificate=certificate_path,
    clientKey=private_key_path
)

# Print the response
print(response)