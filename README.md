# GmailAPI - Send Email sample

Send email sample using the Gmail API. Google provides various samples that had to be stitched together in order to get this to work end to end. I wrote a small sample, stitching together the Gmail API's samples with a little bit of extra glue. I also inject an HTML file as an inline html body (as local file 'report.html').

I heavily copied, relied upon the following documentation, code:

* [Gmail API - Creating Messages](https://developers.google.com/gmail/api/guides/sending#creating_messages)
* [Gmail API - Sending Email](https://developers.google.com/gmail/api/guides/sending)
* [Stack Overflow - Gmail API Error from Code Sample - a bytes-like object is required, not 'str'](https://stackoverflow.com/questions/43352496/gmail-api-error-from-code-sample-a-bytes-like-object-is-required-not-str)
