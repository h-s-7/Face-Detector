import face_recognition as fc
import cv2
import sys
import pandas as pd
import numpy as np
import csv
    
def new_user():
    name = input("Enter your userID\n")
    cam = int(input("Enter 1 to start the camera\n"))
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
    
    

counter = 1

choice = int(input("***Press 1 for adding a new user \n***Press 2 for running the face detector\n***Press 3 to exit\n"))

while choice !=3:
    if counter >3:
        print("too many inncorrect attempts try after some time")
        sys.exit(0)
    else:
        if choice == 1:
            new_user()
            
        elif choice ==2:
            #loading the existing users
            user_id = input("Enter your userID\n")
            #checking if the user exists
            df = pd.read_csv('face_detect.csv')
            existing_users = df.iloc[:0]
            if user_id in existing_users:
                i = cv2.imread(r"E:\\image_data\\"+user_id+".jpg")
                f = fc.face_locations(i)
                e = fc.face_encodings(i,f)
            else:
                print("user not found")
                break
            
            #capturing the image
            cap = int(input("enter 1 to capture the image\n"))
            if cap == 1:
                v = cv2.VideoCapture(0)
                status,pic = v.read()
                fp = fc.face_locations(pic)
                [x1,y1,x2,y2] = fp[0]
                cv2.rectangle(pic,(y2,x1),(y1,x2),(0,0,255),5)
                ep = fc.face_encodings(pic,fp)[0]
                comparison = fc.compare_faces(e,ep)
                print(comparison)
                if True in comparison:
                    print("match found")
                    print("Hello ",user_id)
                else:
                    print("no match found")
                cv2.imshow("detector",pic)
                k = cv2.waitKey(100)
                if k == ord("q"):
                    cv2.destroyAllWindows()
                    v.release()

        elif choice == 3:
            print("Thank You")
            sys.exit(0)
        else:
            counter += 1
            print("sorry re enter your choice")
            choice = int(input("***Press 1 for adding a new user \n***Press 2 for running the face detector\n***Press 3 to exit\n"))
        choice = int(input("***Press 1 for adding a new user \n***Press 2 for running the face detector\n***Press 3 to exit\n"))


