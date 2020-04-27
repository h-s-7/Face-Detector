import face_recognition as fc
import cv2
import sys
import csv
import pandas as pd
def new_user(name,cam):
    v = cv2.VideoCapture(0)
    status,user = v.read()
##store this image(user)
    cv2.imwrite(r"E:\\image_data\\"+name+".jpg",user)
    with open('face_detect.csv','a',newline='') as f:
        thewriter=csv.writer(f)
        thewriter.writerow([name])
    
    k = cv2.waitKey(0)
    if k == ord("q"):
        cv2.destroyAllWindows()
        v.release()
    
    
def detector(user_id,cap):
    #checking if the user exists
    df = pd.read_csv('face_detect.csv')
    existing_users = list(df.user_id)
    if user_id in existing_users:
        i = cv2.imread(r"E:\\image_data\\"+user_id+".jpg")
        f = fc.face_locations(i)
        e = fc.face_encodings(i,f)
    else:
        return "user id not found"
    
    if cap == 1:
        v = cv2.VideoCapture(0)
        status,pic = v.read()
        fp = fc.face_locations(pic)
        [x1,y1,x2,y2] = fp[0]
        cv2.rectangle(pic,(y2,x1),(y1,x2),(0,0,255),5)
        ep = fc.face_encodings(pic,fp)[0]
        comparison = fc.compare_faces(e,ep)
        cv2.imshow("detector",pic)
        k = cv2.waitKey()
        if k == ord("q"):
            cv2.destroyAllWindows()
            v.release()
                
        if True in comparison:
            #print("match found")
            return_statement = "Hello "+user_id
            return return_statement
        else:
            return "no match found"

    
            
            

