import smtplib
from email.mime.text import MIMEText




SMTP_SERVER = "smtp.gmail.com"  
SMTP_PORT = 587
EMAIL_ADDRESS = "eldiiarbekzhan@gmail.com"  
EMAIL_PASSWORD = "adfa"  
TO_EMAIL = "eldiiarbekzhan@gmail.com"  


subject = "Server Alert: Scheduled Email"
body = "This is an automated email from your server."

msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = EMAIL_ADDRESS
msg["To"] = TO_EMAIL



try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, TO_EMAIL, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
