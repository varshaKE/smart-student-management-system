import os
import cv2
import face_recognition
import pickle
# from flask import *
from .database import *
import uuid
from datetime import datetime

def enf(path):
        imagePaths = path

	# initialize the list of known encodings and known names
        knownEncodings = []
        knownNames = []
        for  fname in os.listdir(imagePaths):
            facedir=os.path.join(imagePaths,fname)
            for  imagePt in os.listdir(facedir):
                img=os.path.join(facedir,imagePt)
		
               
                name = fname
                 
                # load the input image and convert it from RGB (OpenCV ordering)
                # to dlib ordering (RGB)

                image = cv2.imread(img)
                rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                print(rgb)

                # detect the (x, y)-coordnates of the bounding boxes
                # corresponding to each face in the input image
                boxes = face_recognition.face_locations(rgb,model='hog')

		# compute the facial embedding for the face
                encodings = face_recognition.face_encodings(rgb, boxes)

                # loop over the encodings
                for encoding in encodings:
                        # add each encoding + name to our set of known names and
                        # encodings
                        knownEncodings.append(encoding)
                        knownNames.append(name)

        # dump the facial encodings + names to disk
        print("[INFO] serializing encodings...")
        data = {"encodings": knownEncodings, "names": knownNames}
        f = open('faces.pickles', "wb")
        f.write(pickle.dumps(data))
        f.close()


# camera for image testing
def val():
	size = 4


	# We load the xml file
	classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

	webcam = cv2.VideoCapture(0) #Using default WebCam connected to the PC.
	(rval, im) = webcam.read()
	flag=0
	while True:
		(rval, im) = webcam.read()
		im=cv2.flip(im,1,0) #Flip to act as a mirror

		# Resize the image to speed up detection
		mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

		# detect MultiScale / faces 
		faces = classifier.detectMultiScale(mini)



		# Draw rectangles around each face
		flag=0
		for f in faces:
			(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
			cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

			#Save just the rectangle faces in SubRecFaces
			sub_face = im[y:y+h, x:x+w]

			FaceFileName = "static/test.jpg" #Saving the current image from the webcam for testing.
			

			cv2.imwrite(FaceFileName, sub_face)
	
			# break
			val=rec_face_image(FaceFileName)
			print(val)
			# print("user",vals)
			str1=""
			for ele in val:  
				str1 = ele
			print(str1)
			val=str1.replace("'","")
			print("val : ",val)
			q="select * from face where face_id='%s'" %(val)
			res=select(q)
			if res:
				newfile="static/faces/"+str(uuid.uuid4())+".jpg"
				cv2.imwrite(newfile, sub_face)
				valnew="Welcome "+res[0]['name']
				print(valnew)
				# flash("Face Detected !")
				now = datetime.now()
				current_time = now.strftime("%H:%M:%S")
				if current_time>"09:00:00" and current_time<"12:59:00":
					pass
					# flash("Face Detected !")
					# q="select * from attandance where student_id='%s' and date=curdate()" %(val)
					# res2=select(q)
					# print(res)
					# if res2:
					# 	flash("Your attandance is Already Marked")
					# else:
					# 	q="insert into attandance values(null,'%s',curdate(),curtime(),'Present','%s')" %(val,newfile)
					# 	insert(q)
					# 	flash("Attanadance Marked")
				# else:
				# 	q="select * from attandance where student_id='%s' and date=curdate()" %(val)
				# 	res2=select(q)
				# 	print(res)
				# 	if res2:
				# 		flash("Your attandance is Already Marked")
				# 	else:
				# 		q="insert into attandance values(null,'%s',curdate(),curtime(),'Present,'%s')" %(val,newfile)
				# 		insert(q)
						# flash("Attanadance Marked")
						# flash("You are late")
				flag=1
			# else:
				# print("No Staff")
				# flash("Sorry!....your Face is Not Recognized!!")
				# flag=1

					
		cv2.imshow('Capture(Press Esc to exit)',   im)
		key = cv2.waitKey(10)
		print("key : ",key)
		# # if Esc key is press then break out of the loop 
		if key == 27: #The Esc key
			break
			return "failed"

		if flag==1:
			break


def vallogin():
    size = 4

    # Load the face detection XML file
    classifier = cv2.CascadeClassifier('smart_student_app/haarcascade_frontalface_alt.xml')

    # Initialize webcam
    webcam = cv2.VideoCapture(0)
    (rval, im) = webcam.read()
    flag = 0
    while True:
        (rval, im) = webcam.read()
        im = cv2.flip(im, 1, 0)  # Flip to act as a mirror

        # Resize the image to speed up detection
        mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

        # Detect faces
        faces = classifier.detectMultiScale(mini)

        

        flag = 0
        for f in faces:
            (x, y, w, h) = [v * size for v in f]  # Scale the face size back up
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 4)

            # Save the detected face
            sub_face = im[y:y + h, x:x + w]
            FaceFileName = "static/test.jpg"
            cv2.imwrite(FaceFileName, sub_face)

            # Call face recognition function
            val = rec_face_image(FaceFileName)
            print("Face Recognition Result:", val)

            if not val or val[0] == "Unknown":
                print("Unknown face detected or recognition failed")
                continue

            # Get the recognized student ID
            student_id = val[0].replace("'", "")
            print("Recognized Student ID:", student_id)

            # Get current time
            current_time = datetime.now()

            # Detailed query to check previous attendances
            today_attendance_query = """
            SELECT id, at_date 
            FROM smart_student_app_newattandacess 
            WHERE student_id='%s' 
            AND DATE(at_date) = CURDATE()
            ORDER BY at_date DESC
            """ % (student_id)
            today_attendance = select(today_attendance_query)

            # Debug print previous attendances
            print("Today's Previous Attendances:", today_attendance)

            # Attendance marking logic with comprehensive checks
            try:
                if not today_attendance:
                    # First attendance of the day
                    r = "INSERT INTO smart_student_app_newattandacess VALUES (NULL, '%s', 'pending', '%s')" % (current_time, student_id)
                    insert(r)
                    print(f"First attendance marked for student {student_id} at {current_time}")
                else:
                    # Check the last attendance time
                    # Modify this line to handle datetime object directly
                    last_attendance = today_attendance[0]['at_date']
                    
                    # Calculate time difference
                    time_difference = current_time - last_attendance

                    # Debug print time difference
                    print(f"Time since last attendance: {time_difference}")
                    print(f"Hours since last attendance: {time_difference.total_seconds() / 3600}")

                    # Check if 1 hours have passed
                    if time_difference.total_seconds() >= 1 * 3600:
                        r = "INSERT INTO smart_student_app_newattandacess VALUES (NULL, '%s', 'pending', '%s')" % (current_time, student_id)
                        insert(r)
                        print(f"Attendance marked for student {student_id} at {current_time}")
                    else:
                        print(f"Cannot mark attendance. Less than 4 hours since last attendance.")

            except Exception as e:
                print(f"Error marking attendance: {e}")

            # Query student details for display
            query = "SELECT * FROM smart_student_app_student WHERE id='%s'" % (student_id)
            student_res = select(query)
            
            if student_res:
                # Display student name on the frame
                cv2.putText(im, f"{student_res[0]['name']}", (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Show the video frame
        cv2.imshow('Capture (Press Esc to exit)', im)
        key = cv2.waitKey(10)

        # If Esc key is pressed, break out of the loop
        if key == 27:
            break

        if flag == 1:
            break

    cv2.destroyAllWindows()



def vallogins(path):
	size = 4
	


	# We load the xml file
	classifier = cv2.CascadeClassifier('smart_student_app/haarcascade_frontalface_alt.xml')

	
	im = cv2.imread(path)
	im=cv2.flip(im,1,0) #Flip to act as a mirror

	# Resize the image to speed up detection
	mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))

	# detect MultiScale / faces 
	faces = classifier.detectMultiScale(mini)

	# if faces:

	# Draw rectangles around each face
	flag=0
	for f in faces:
		(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
		cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

		#Save just the rectangle faces in SubRecFaces
		sub_face = im[y:y+h, x:x+w]

		FaceFileName = "static/test.jpg" #Saving the current image from the webcam for testing.
		

		cv2.imwrite(FaceFileName, sub_face)

		# break
		val=rec_face_image(FaceFileName)
		print(val)
		# print("user",vals)
		str1=""
		for ele in val:  
			str1 = ele
		print(str1)
		val=str1.replace("'","")
		print("val : ",val)
		q="select * from login  where login_id='%s'" %(val)
		print(q)
		res=select(q)
		r="insert into smart_student_app_internalmarks values(null,'%s',curdate())"%(val)
		insert(r)
		if res:
			# if 0==0:
			# utype = res[0]['usertype']
			# if utype == "employee":
			# 	valnew="Welcome "+res[0]['name']
			# 	print(valnew)
			return "ok"

		
		else:
			print("Failed")
			# flash("Sorry! Login failed...")
			# newfile="static/faces/"+str(uuid.uuid4())+".jpg"
			# cv2.imwrite(newfile, sub_face)
			valnewerr="No face detected, Try register again..."
			return valnewerr
			flag=1
	# else:
	# 	# Draw rectangles around each face
	# 	flag=0
	# 	for f in faces:
	# 		(x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
	# 		cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)

	# 		#Save just the rectangle faces in SubRecFaces
	# 		sub_face = im[y:y+h, x:x+w]

	# 		noface="noface"
	# 		return noface
	# 		# flag=1

				
	# cv2.imshow('Capture(Press Esc to exit)',   im)
	# key = cv2.waitKey(10)
	# print("key : ",key)
	# # if Esc key is press then break out of the loop 
	



def rec_face_image(imagepath):
    print(imagepath)

    data = pickle.loads(open('faces.pickles', "rb").read())

    # load the input image and convert it from BGR to RGB
    image = cv2.imread(imagepath)
    #print(image)
    h,w,ch=image.shape
    print(ch)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # detect the (x, y)-coordinates of the bounding boxes corresponding
    # to each face in the input image, then compute the facial embeddings
    # for each face
    print("[INFO] recognizing faces...")
    boxes = face_recognition.face_locations(rgb,
        model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)

    # initialize the list of names for each face detected
    names = []

    # loop over the facial embeddings
    for encoding in encodings:
        # attempt to match each face in the input image to our known
        # encodings
        matches = face_recognition.compare_faces(data["encodings"],
            encoding,tolerance=0.4)
        name = "Unknown"

        # check to see if we have found a match
        if True in matches:
            # find the indexes of all matched faces then initialize a
            # dictionary to count the total number of times each face
            # was matched
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            # loop over the matched indexes and maintain a count for
            # each recognized face face
            for i in matchedIdxs:

                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            print(counts, " rount ")
            # determine the recognized face with the largest number of
            # votes (note: in the event of an unlikely tie Python will
            # select first entry in the dictionary)
            if len(counts) >= 1:
                name = max(counts, key=counts.get)
            # else:
            #     name = "-1"
        # update the list of names
        # if name not in names:
        if name != "Unknown":
            names.append(name)
    return names

	

# vallogin()
# enf("media/trainimages")