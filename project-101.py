import dropbox

class TransferData:
    def __init__(self,Access_token):
        self.Access_token = Access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.Access_token)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)     
def main():
    Access_token = 'ot8Mqac6NpYAAAAAAAAAAcNcm0sdg1B7FKVSRScZmOg3Z4Z1XY9DkH-wfqM8_P18'  
    transferData = TransferData(Access_token)
    file_from = input("enter the file location: ")
    file_to = input("Enter full path to upload to dropbox: ")  

    transferData.upload_files(file_from,file_to)
    print("file has been moved") 

main()