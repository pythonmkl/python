from ftplib import FTP


ftp = FTP('ftp.mydomain.com')
ftp.login('myusername', 'secretpassword')

# Get the listing of files and directories
file_list = []
ftp.retrlines('LIST', file_list.append)
for line in file_list:
    print(line)

ftp.quit()
