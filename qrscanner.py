import cv2 #use for camera 
from pyzbar .pyzbar import decode 
import time  #time input using pip file 
import mysql.connector

cam=cv2.VideoCapture(0)
cam.set(5, 640) # for hight 
cam.set(6, 480) #for length

connection  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "himanshu@2005"
)
print(connection )

cursor = connection .cursor()
connection.autocommit = True

cursor.execute("USE students_info")

camera=True
while camera == True:

    suceess,frame = cam.read()   # camera ko read krega 
    
    for i in decode(frame):
        print(i,type) 
        print(i.data.decode('utf-8'))  # is a character encoding that represents each character in the Unicode standard using variable-length sequences of 8-bit bytes
        input_string = i.data.decode('utf-8')
        lines = input_string.split('\n')
        print(lines) 
        name = lines[0]
        roll_no = lines[1]
        branch = lines[2]
        fathers_name = lines[3]
        phone_number = lines[4]
        address = lines[5] + lines[6]
        secondary_phone_number = lines[7]
        insert_query = (
        "INSERT INTO student_details "
        "(name, roll_no, fathers_name, branch, phone_number, address, secondary_phone_number) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (name, roll_no, fathers_name, branch, phone_number, address, secondary_phone_number))

    time.sleep()  #Time 

    cv2.imshow("QR_SCANNER",frame)
    cv2.waitKey(3)
 
# Show database
cursor.execute("SELECT * FROM student_details")

for x in cursor:
  print(x)


print("Total number of rows in table: ", cursor.rowcount)


connection.commit()
cursor.close()
connection.close()