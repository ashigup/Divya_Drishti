import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACa0e1648cd8a36f6790e41fb4a6067774' 
auth_token = '1269dbcafe4084905c5e1ccfc4e5fdc6'
client = Client(account_sid, auth_token)

message = client.messages.create(  
                              messaging_service_sid='MG4e8b8464fc8ef507366a16825e611d1e', 
                              body='Alertfffff11111111',      
                              to='+917488160265' 
                                        ) 

print(message.sid)