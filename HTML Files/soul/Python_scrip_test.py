#copilot test

#try and use keila docker file and see if it works well for what i want. 
#will probably delete this file later. 


import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = 'your_icloud_email@icloud.com'
    recipient_email = 'recipient@example.com'  # Change this to the recipient's email address
    app_specific_password = 'your_app_specific_password'

    subject = 'Hello from Python!'
    body = 'This is a test email sent via Python.'

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Set up the SMTP server
    smtp_server = 'smtp.mail.me.com'
    port = 587

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, app_specific_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print('Email sent successfully!')
    except Exception as e:
        print(f'Error sending email: {e}')

if __name__ == '__main__':
    send_email()


#Explanation:
#Replace 'your_icloud_email@icloud.com' with your actual iCloud email address.
#Modify recipient_email to the desired recipient’s email address.
#Replace 'your_app_specific_password' with the app-specific password you generated.
#The script creates a basic email with a subject and body.
#It establishes an encrypted connection to the SMTP server (smtp.mail.me.com) on port 587.
#The context ensures secure communication.
#The server.login() method authenticates using your iCloud credentials.
#Finally, the email is sent using server.sendmail().
#Server Setup:
#Place this Python script on your server where you want to run it.
#Ensure that Python is installed on your server.
#   You can schedule the script to run periodically (e.g., using cron jobs) or trigger it based on specific
#
    #i'll try integrate the below into the above to include a captcha check. 
"""import requests
import json

def send_email(to, subject, body, debug=False):
    # Set your actual values here
    sender_email = 'your_icloud_email@icloud.com'
    recipient_email = 'your_other_email@example.com'
    app_specific_password = 'your_app_specific_password'
    recaptcha_secret_key = 'your_recaptcha_secret_key'

    # Word filter (add more words if needed)
    spam_words = ['viagra', 'lottery', 'free money']

    # Verify reCAPTCHA response
    def verify_recaptcha(response):
        recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {'secret': recaptcha_secret_key, 'response': response}
        response = requests.post(recaptcha_url, data=payload)
        result = json.loads(response.text)
        return result.get('success', False)

    # Check for spam words
    for word in spam_words:
        if word.lower() in body.lower():
            print('Message contains spam words. Rejected.')
            return -1

    # Verify reCAPTCHA (replace 'g-recaptcha-response' with the actual form field name)
    recaptcha_response = 'your_recaptcha_response_from_form'
    if not verify_recaptcha(recaptcha_response):
        print('reCAPTCHA verification failed. Rejected.')
        return -1

    # Create the email message (similar to the original script)
    # ...

    # Send the email (similar to the original script)
    # ...

    if debug:
        print(request.text)
        print(request.status_code)

    if request.status_code != 200:
        return -1

    return 0

if __name__ == '__main__':
    # Example usage
    send_email(
        to='test-test@mailinator.com',
        subject='Test subject',
        body='Test line one. This is the email body.',
        debug=True
    )
"""

#Remember to replace the placeholders (your_...) with your actual values. 
#Also, adapt the script to your specific HTML form (including the reCAPTCHA widget) and handle form submissions accordingly.

