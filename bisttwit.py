
# Twitter API'yi kullanmak için gerekli kütüphaneleri içe aktarın
import tweepy
import pandas as pd

# Gmail API'yi kullanmak için gerekli kütüphaneleri içe aktarın
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Twitter API anahtarlarınızı buraya girin
consumer_key = "..."
consumer_secret = "..."
access_token = "..."
access_token_secret = "..."

# Twitter API'ye bağlanın
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# BIST 100 ile ilgili son 50 tweeti alın
tweets = api.search(q="BIST 100", lang="tr", count=50)

# Tweetleri bir veri çerçevesine dönüştürün
df = pd.DataFrame([tweet.text for tweet in tweets], columns=["Tweet"])

# Veri çerçevesini bir csv dosyasına kaydedin
df.to_csv("tweets.csv", index=False)

# E-posta göndermek için Gmail hesabınızın bilgilerini buraya girin
gmail_user = "..."
gmail_password = "..."

# E-posta alıcılarının listesini buraya girin
recipients = ["...", "...", "..."]

# E-posta mesajını oluşturun
msg = MIMEMultipart()
msg["From"] = gmail_user
msg["To"] = ", ".join(recipients)
msg["Subject"] = "BIST 100 ile ilgili son 50 tweet"
body = "Merhaba,\n\nBu e-posta, BIST 100 ile ilgili son 50 tweeti içeren bir csv dosyası göndermek için otomatik olarak oluşturulmuştur.\n\nDosyayı e-postanın ekinde bulabilirsiniz.\n\nİyi günler."
msg.attach(MIMEText(body, "plain"))

# Csv dosyasını e-postaya ekleyin
filename = "tweets.csv"
attachment = open(filename, "rb")
part = MIMEBase("application", "octet-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", f"attachment; filename= {filename}")
msg.attach(part)

# Gmail sunucusuna bağlanın ve e-postayı gönderin
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, recipients, msg.as_string())
server.quit()
```