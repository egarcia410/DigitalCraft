# Form Exercise

## Getting Started

1. Log into [AWS](https://aws.amazon.com/)

2. Search for SES (Simple Email Service) service
    * Once clicked, you will be brought to the SES console

3. Click on `Domains` tab

4. Click on `Verify a New Domain`

5. In the `Verify a New Domain` dialog box, enter your domain name, select the `Generate DKIM settings` check box, and then click `Verify This Domain`.
    * [Setting Up Easy DKIM for a New Domain](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html#easy-dkim-new-domain)
    * The domain name will be add to the list of Verified Identities with a Status of "pending verification"

6. Download Record Set as CSV

7. Go to website where you created your domain (ex. Google Domains)

8. Click on the DNS Configuration for your domain name

9. Under `Custom Recource Records`, add the TXT and CNAME records from step 5 to the domain's DNS setting.

10. In AWS SES, click on the `Email Addresses` tab

11. Click on `Verify a New Email Address`

12. Enter email addres and click `Verify This Email Address`

13. Go to your mail inbox and click on link provided to verify email address

14. Back in AWS, search from IAM (Identity and Access Management) service

15. Under `Groups` tab, click `Create New Group`

16. Set Group Name

17. Attach Policy, click on `AmazonSESFUllAccess`

18. Review Information and click `Create Group`

19. Under `Users` tab, click `Add User`

20. Set User name

21. Select AWS access type - `Programmatic access`

22. Add User to Group

23. Review information and click `Create user`

24. Download .csv file with `Access key ID` and `Secret access key`
    * These are your credentials

25. Insert Credentials into your project!

## Setting Up Project File
1. Install Dependencies inside Virtualenv:

        $ pip3 install boto3
        $ pip3 install python-dotenv

2. Configure project file with code below:

```python
import os
import boto3

from dotenv import load_dotenv

load_dotenv('.env')

SES_CLIENT = boto3.client(
  'ses',
  aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
  aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'),
  region_name="us-west-2"
)
```
* May have to update `region_name`

3. Inside Handler for sending email, insert post method below:
```python
    def post(self):
        name = self.get_body_argument('name')
        email = self.get_body_argument('email')
        text = self.get_body_argument('text')
        
        response = SES_CLIENT.send_email(
        Destination={
            'ToAddresses': ['EMAIL_ADDRESS'],
        },
        Message={
            'Body': {
            'Text': {
                'Charset': 'UTF-8',
                'Data': text,
            },
            },
            'Subject': {'Charset': 'UTF-8', 'Data': 'Portfolio Contact'},
        },
        Source='EMAIL_ADDRESS',
        )
        messages = 'Thank you, your email has been sent!'
        self.render_template('contact.html', message=messages )
```

## Setting Up Dokku
1. Insert AWS credentials into Dokku

        dokku config:set myproject AWS_ACCESS_KEY=INSERT_ACCESS_KEY
        dokku config:set myproject AWS_SECRET_KEY=INSERT_SECRET_KEY

## Contact Form

Create a "Contact Me" form on your site that accepts inputs like name, email, message, etc. On your backend when you recieve this data send it to yourself with [Amazon SES](https://aws.amazon.com/ses/).

Use the [Boto3](http://boto3.readthedocs.io/en/latest/) Library library to send email with Amazon SES.

1. [SES](http://boto3.readthedocs.io/en/latest/reference/services/ses.html)
2. [send_email](http://boto3.readthedocs.io/en/latest/reference/services/ses.html#SES.Client.send_email)


## CLI to Web

Convert one or more of your previous exercises from Python Part 1 to a web form. Examples to convert:

1. Work or Sleep In
2. [Celsius to Fahrenheit](https://github.com/egarcia410/temp-converter)
3. Tip Calculator
4. How many coins

## Bonus: Timezone Converter

Create a form that allows you input a datetime and select an input timezone and an output timezone. When the form is submitted, it should respond with the converted datetime.

Hint: use the libraries [pytz](http://pythonhosted.org/pytz/) and/or [arrow](http://arrow.readthedocs.io/en/latest/)