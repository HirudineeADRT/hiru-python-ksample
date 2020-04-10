import boto3
ses = boto3.client("ses")
import json

def handler(event, context):
    
    print(event)
 
    tabledetails = json.loads(json.dumps(event["Records"][0]["dynamodb"]))
    print(tabledetails)
 
    name = tabledetails["NewImage"]["Name"]["S"];
    email = tabledetails["NewImage"]["Email"]["S"];
    url = tabledetails["NewImage"]["URL"]["S"];
    messagebody = 'Hi'+ ' ' + name + '! your shopping cart is waiting for you. Follow this link to return to your cart' + ' ' + url
  
    try:
        data = ses.send_email(
            Source="hirudinee+123@adroitlogic.com",
            Destination={
                'ToAddresses': ["hirudinee@adroitlogic.com"]
            },
            Message={
                'Subject': {
                    'Data': "Kumudika test"
                },
                'Body': {
                    'Text': {
                        'Data': messagebody
                    }
                }
            }
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
