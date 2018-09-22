# Send email sample using the Gmail API. Google provides various samples that had to be stitched together
# in order to get the 'send email' use case working end to end. I wrote a small collective sample, stitching together 
# the Gmail API's samples with a little bit of extra glue. I also inject an HTML file as an inline html body.
#
# Make sure you enable your account for Gmail API access: 
# * https://developers.google.com/gmail/api/auth/about-auth
#
# I heavily copied the samples, relied upon the following documentation, code provided by Google and Stack Overflow:
# * Gmail API - Creating Messages : https://developers.google.com/gmail/api/guides/sending#creating_messages
# * Gmail API - Sending Email : https://developers.google.com/gmail/api/guides/sending
# * Gmail Auth Scopes : https://developers.google.com/gmail/api/auth/scopes
# * Stack Overflow - Gmail API Error from Code Sample : https://stackoverflow.com/questions/43352496/gmail-api-error-from-code-sample-a-bytes-like-object-is-required-not-str
#
# You will need to replace all of the '<...>' strings as appropriate to your own environment, setup.

from __future__ import print_function

# Import google api client, GMail API's 
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Import http libraries
from httplib2 import Http
from oauth2client import file, client, tools

# Import email libraries
import smtplib, base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# If modifying these scopes, delete the file token.json.
# Gmail API auth scopes can be found here: https://developers.google.com/gmail/api/auth/scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEMultipart('alternative')
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  
  message.attach(MIMEText(message_text, 'plain'))
  message.attach(MIMEText(open('<a_file.html>', 'r', encoding = "utf-8").read(), 'html'))

  # Google sample code fix, via Stack Overflow:
  # https://stackoverflow.com/questions/43352496/gmail-api-error-from-code-sample-a-bytes-like-object-is-required-not-str
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    print('Message Id: %s' % message['id'])
    return message

  # fixed this from the Google provided sample, was:
  # >> except errors.HttpError, error:
  except HttpError as error:
    print('An error occurred: %s' % error)

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    store = file.Storage('token.json')
    creds = store.get()
    
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # create and send test message
    test_message = create_message('<from@your.domain>', '<to1@your.domain>, <to2@your.domain>', '<the subject>', '<the text body>')
    send_message(service, 'me', test_message)

if __name__ == '__main__':
    main()