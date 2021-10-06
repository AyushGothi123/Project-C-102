import cv2
import dropbox
import random
import time

startTime = time.time()
def takePicture():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "sample"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        result = False

    return imageName
    print("Image is taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imageName):
    access_token = "u7wNh_rO3XAAAAAAAAAAAQns04l-78oh7RLRSiImKr2xSU6b-FJyucrlIIkVZZTw"
    file_from = imageName
    file_to = "/Project C-102/"+(imageName)
    dbx  = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True) :
        if ( (time.time()-startTime) > 10):
            name = takePicture()
            upload_file(name)

main()