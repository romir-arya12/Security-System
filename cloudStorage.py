import cv2
import dropbox
import time
import random
start_time=time.time()
def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name
    print("SnapShot Taken")
    videoCaptureObject.relese
    cv2.destroyAllWindows()
def uploadFile(image_name):
    access_token="GkEoTwbbkdYAAAAAAAAAAVJADY4y6hblUZfgRs1yIurBvnsu5NYiSjOq_NQ5pbVC"
    file=image_name
    file_from=file
    file_to="/NewFolder123/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=1800):
            name=takeSnapshot()
            uploadFile(name)
main()