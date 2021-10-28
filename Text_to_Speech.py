#Sample Text-To-Speech file
import boto3

polly = boto3.client(service_name='polly',region_name='us-east-1')

print('Starting the Polly Service')

response = polly.synthesize_speech(OutputFormat='mp3', VoiceId='Brian',
             Text='Hello, I am Polly Service! I am the sound of Brian')

file = open('speech.mp3', 'wb')
file.write(response['AudioStream'].read())
file.close()
print("Polly's output stored !")