##AWS IOT BUTTON
If you have an AWS IOT Button you can use this project to send an SMS to anyone who is subscribed.

###Summary
Initially, I received a AWS IOT Button at a AWS Conference in San Francisco. I decided to utilize the IOT Button in order to notify
either my partner or myself when the other had arrived home. 

###Tech

| Technology | Description |
| --- | --- |
| Python 2.7 | python runtime |
| virtualenv | virtual environment for python |
| pip | python package manager |
| boto3 | AWS SDK |
| pytz | timezone library |

###Build & Deploy
In order to build and deploy the lambda function you will need to have the AWS cli enabled.

1. enable [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html)
2. git clone this repository
3. create your virtualenv environment
    - ```virtualenv env```
    - ```env source/bin/activate```
4. pip install requirements.txt file
    - ```pip install -r requirements.txt```
5. use AWS IOT Core to manage your IOT Button and create your rules, refer to my blog article[]()
6. next zip your files to be uploaded to your lambda function
    - ```zip -r ./upload.zip main.py env/lib/python2.7/site-packages```
7. upload your zip file to aws lambda
    - ```aws lambda  update-function-code --zip-file fileb://./upload.zip  --function home-alerts-iot```
8. congrats your are ready to test

###Source Code Structure

###License
MIT © [Jason Durant]()
