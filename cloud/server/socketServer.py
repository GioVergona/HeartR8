import socket
import json
import boto3


PORT_USER = 3389

# User's socket creation
sockListenUser = socket.socket()
print("USER Socket successfully created")
sockListenUser.bind(('', PORT_USER))
print("socket binded to %s" % (PORT_USER))

sockListenUser.listen(5)
print("socket USER is listening")
socketConnListenUser, addr = sockListenUser.accept()
print('Got connection from', addr)

# Especifica la región AWS
region_name = 'eu-west-3'

# Nombre de la función Lambda
function_name = 'insertDataBase'


while True:
        data = socketConnListenUser.recv(1024)
        if not data:
                print("Connection closed")
                break

        print(data.decode())

        # Receive JSON from the socket
        dataDictionary = data.decode()

        # Convert JSON string to a Python dictionary
        json_data = json.loads(dataDictionary)

        # Convert the dictionary to a JSON string
        payload_json = json.dumps(json_data)

        # Crea un cliente de AWS Lambda
        lambda_client = boto3.client('lambda', region_name=region_name)

        # Payload de la función Lambda (si es necesario)
        payload = data.decode

        # Invoca la función Lambda
        response = lambda_client.invoke(
            FunctionName=function_name,
            Payload=payload_json.encode('utf-8')  # Encode the string to bytes
        )

        # Procesa la respuesta según sea necesario
        result = response['Payload'].read()
        print(result.decode('utf-8'))