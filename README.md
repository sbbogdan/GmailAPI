# GmailAPI - send email end to end sample

Send email sample using the Gmail API.

Google provides various samples that had to be stitched together in order to get the 'send email' use case working end to end. I wrote a small sample, stitching together the Gmail API's samples with a little bit of extra glue. I also inject an HTML file as an inline html body.

Make sure you enable your account for Gmail API access: 
 * https://developers.google.com/gmail/api/auth/about-auth

I heavily copied the samples, relied upon the following documentation, code provided by Google and Stack Overflow:
* [Gmail API - Creating Messages](https://developers.google.com/gmail/api/guides/sending#creating_messages)
* [Gmail API - Sending Email](https://developers.google.com/gmail/api/guides/sending)
* [Gmail API Auth Scopes](https://developers.google.com/gmail/api/auth/scopes)
* [Stack Overflow - Gmail API Error from Code Sample - a bytes-like object is required, not 'str'](https://stackoverflow.com/questions/43352496/gmail-api-error-from-code-sample-a-bytes-like-object-is-required-not-str)

You will need to replace all of the '<...>' strings as appropriate to your own environment, setup.
