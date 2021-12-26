from backend import app

if __name__=="__main__":
    #app.run(debug=True,host="192.168.122.232",port='8000') 
    app.run(debug=True
    # ,MAIL_SERVER='smtp.gmail.com',
    # MAIL_PORT=465,
    # MAIL_USE_SSL=True,
    # MAIL_DEFAULT_SENDER=('admin', 'xxxxxx@gmail.com'),
    # MAIL_MAX_EMAILS=10,
    # MAIL_USERNAME='xxxxxxx@gmail.com',
    # MAIL_PASSWORD='xxxxxxxxx'
    )

    ##需到GMAIL啟用IMAP 、 Security Here 開啟權限
