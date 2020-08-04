import requests
import boto3
s3 = boto3.client("s3")

def handler(event, context):
    try:
        data = s3.list_objects(
            Bucket="cloud9-ktest",
            MaxKeys=10
        )
        print(data)
    except BaseException as e:
        print(e)
        raise(e)
    
        try:
            res = requests.get(
                "http://demo.fintechsandpit.com/contact-for-access",
                params={},
                headers={"Accept":""}
            )
            print(res)
            # your code goes here
        except BaseException as e:
            # error handling goes here
            print(e)
            raise(e)
    
    return {"message": "Successfully executed"}
