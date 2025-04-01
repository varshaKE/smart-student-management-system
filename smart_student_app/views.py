from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .facedetection import *
import os
from django.core.files.storage import FileSystemStorage
from PIL import Image
# from django.core.files import File

# Create your views here.

def home(request):
    # enf(r"D:/smart_student/media/trainimages/")/
    

    return render(request,'index.html')
def detected(request):
    # enf(r"D:/smart_student/media/trainimages/")/

    
    vallogin()

    # """When a student marks attendance, update weekday count."""
    # today = datetime.today()

    # if today.weekday() < 5:  # Monday to Friday
    #     month = today.strftime("%B")
    #     year = today.year

    #     obj, created = Attendance.objects.get_or_create(
    #         month=month, year=year,
    #         defaults={'weekday_count': 0}
    #     )

    #     # Ensure count updates only once per day
    #     if obj.weekday_count < today.day:
    #         obj.weekday_count += 1
    #         obj.save()

    return render(request,'index.html')

def student_home(request):

    return render(request,'student_home.html')

def parent_home(request):

    return render(request,'parent_home.html')


def teacher_home(request):

    return render(request,'teacher_home.html')

def login(request):
    
    if 'submit' in request.POST:
        uname=request.POST['username']
        pwd=request.POST['password']
        res=Login.objects.filter(username=uname,password=pwd).first()
        if res:
            request.session['lid'] = res.pk
            if res.usertype=='admin':
                return HttpResponse("<script>alert('login success');window.location='admin_home'</script>")
            elif res.usertype=='student':
                resss = Student.objects.get(login_id=request.session['lid'])
                request.session['sid'] = resss.pk
                return HttpResponse("<script>alert('login success');window.location='student_home'</script>")
            elif res.usertype=='teacher':
                ress = Teacher.objects.get(login_id=request.session['lid'])
                request.session['tid'] = ress.pk
                return HttpResponse("<script>alert('login success');window.location='teacher_home'</script>")
            elif res.usertype=='parent':
                ress = Parent.objects.get(login_id=request.session['lid'])
                request.session['pid'] = ress.pk
                return HttpResponse("<script>alert('login success');window.location='parent_home'</script>")
        else:
            return HttpResponse("<script>alert('incorrect!!');window.location='login'</script>")
    return render(request,'login.html')

def adminhome(request):

    return render(request,'adminhome.html')


def adminteacher(request):
    aa=Teacher.objects.all()
    departments=Department.objects.all()
    if 'submit' in request.POST:
        name=request.POST['name']
        address=request.POST['address']
        gender=request.POST['gender']
        dob=request.POST['dob']
        phno=request.POST['phonenumber']
        email=request.POST['email']
        qly=request.POST['qualification']
        dept=request.POST['department']
        username=request.POST['username']
        password=request.POST['password']
        log=Login(username=username,password=password,usertype='teacher')
        log.save()
        ff=Teacher(name=name,address=address,gender=gender,dob=dob,phone_no=phno,email=email,qualification=qly,dept_id=dept,login_id=log.pk)
        ff.save()
        return HttpResponse("<script>alert('Added!!');window.location='/adminteacher'</script>")

    return render(request,'adminteacher.html',{'ffg':aa,'departments':departments})



def adminteacher_update(request,id1):
    departments=Department.objects.all()

    oo=Teacher.objects.get(id=id1)
    if 'update' in request.POST:
        name=request.POST['name']
        address=request.POST['address']
        gender=request.POST['gender']
        dob=request.POST['dob']
        phno=request.POST['phonenumber']
        email=request.POST['email']
        qly=request.POST['qualification']
        dept=request.POST['department']
        oo.name=name
        oo.address=address
        oo.gender=gender
        oo.dob=dob
        oo.phone_no=phno
        oo.email=email
        oo.qualification=qly
        oo.dept_id=dept
        oo.save()
        return HttpResponse("<script>alert('Updated!!');window.location='/adminteacher'</script>")

    return render(request,'adminteacher.html',{'qw':oo,'departments':departments})



def admin_manage_parent(request):
    dd=Parent.objects.all()
    if 'submit' in request.POST:
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phno=request.POST['phone_no']
        username=request.POST['usrname']
        password=request.POST['passwd']
        log=Login(username=username,password=password,usertype='parent')
        log.save()
        yu=Parent(name=name,address=address,phone_no=phno,email=email,login_id=log.pk)
        yu.save()
        return HttpResponse("<script>alert('Added!!');window.location='/admin_manage_parent'</script>")
    return render(request, 'admin_manage_parent.html', context={"dd": dd})  # ✅ Correct format



def admin_manage_parent_update(request,id1):
    dd=Parent.objects.get(id=id1)
    if 'update' in request.POST:
        name=request.POST['name']
        relation=request.POST['relation']
        address=request.POST['address']
        email=request.POST['email']
        phno=request.POST['phone_no']
        dd.name=name
        dd.relation=relation
        dd.address=address
        dd.email=email
        dd.phone_no=phno
        return HttpResponse("<script>alert('Updated!!');window.location='/admin_manage_parent'</script>")
    return render(request,'admin_manage_parent.html',{'ff':dd})    


def adminteacher_delete(request,id2):
    hh=Teacher.objects.get(id=id2)
    log=Login.objects.get(id=hh.login_id)
    hh.delete()
    log.delete()
    
    return HttpResponse("<script>alert('Deleted!!');window.location='/adminteacher'</script>")

def admin_manage_parent_delete(request,id2):
    hh=Parent.objects.get(id=id2)
    log=Login.objects.get(id=hh.login_id)
    hh.delete()
    log.delete()
    
    return HttpResponse("<script>alert('Deleted!!');window.location='/admin_manage_parent'</script>")

def admin_student(request, id1):
    enf(r"D:/smart_student/media/trainimages/")
    gg = Student.objects.filter(parent_id=id1)
    departments = Department.objects.all()

    

    if 'submit' in request.POST:
        name = request.POST['name']
        address = request.POST['address']
        gender = request.POST['gender']
        dob = request.POST['dob']
        phno = request.POST['phonenumber']
        religion = request.POST['religion']
        email = request.POST['email']
        course = request.POST['course']
        qly = request.POST['qualification']
        dept = request.POST['department']
        aadhar = request.POST['aadhar']
        username = request.POST['username']
        password = request.POST['password']

        login_entry = Login.objects.create(username=username, password=password, usertype="student")

        student_entry = Student.objects.create(
            parent_id=id1,
            name=name,
            address=address,
            gender=gender,
            dob=dob,
            phone_no=phno,
            religion=religion,
            email=email,
            course_id=course,
            qualification=qly,
            dept_id=dept,
            aadhaar_no=aadhar,
            login=login_entry
        )

        pid = str(student_entry.pk)
        folder_path = os.path.join('media', 'trainimages', str(pid))

        # Create the directory if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)

        # Save image1
        image1 = request.FILES['image1']
        k=FileSystemStorage()
        fn=datetime.now().strftime("%Y%m%d%H%M%S")+".png"
        pht1=k.save(r"trainimages//"+ str(pid)+"//"+image1.name,image1)
        print(pht1)
        # Save image2
        image2 = request.FILES['image2']
        l=FileSystemStorage()
        pht2=l.save(r"trainimages//"+ str(pid)+"//"+image1.name,image2)

        # Save image3
        image3 = request.FILES['image3']
        j=FileSystemStorage()
        pht3=j.save(r"trainimages//"+ str(pid)+"//"+image1.name,image3)

        # Call your face encoding or processing function if needed
        enf(r"D:/smart_student/media/trainimages/")

        return HttpResponse(f"<script>alert('Inserted!!');window.location='/admin_student/{id1}'</script>")

    return render(request, 'admin_student.html', {'gg': gg, 'departments': departments})


from django.http import JsonResponse

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(dept_id=department_id).values('id', 'course_name')
    return JsonResponse(list(courses), safe=False)

def admin_student_update(request,id1):
    de=Student.objects.get(id=id1)
    dhe=Parent.objects.all()
    fg=de.parent_id
    if 'update' in request.POST:
        name=request.POST['name']
        address=request.POST['address']
        gender=request.POST['gender']
        dob=request.POST['dob']
        phno=request.POST['phonenumber']
        religion=request.POST['religion']
        email=request.POST['email']
        qly=request.POST['qualification']
        aadhar=request.POST['aadhar'] 
        de.name = name
        de.address = address
        de.gender = gender
        de.dob = dob
        de.phone_no = phno
        de.religion = religion
        de.email = email
        de.qualification = qly
        de.aadhaar_no = aadhar
        de.save()
        return HttpResponse(f"<script>alert('Updated!!');window.location='/admin_student/{fg}'</script>")
    return render(request,'admin_student.html',{'ff':de,'dhe':dhe})


def admin_student_delete(request,id2):
    hh=Student.objects.get(id=id2)
    hh.delete()
    
    return HttpResponse("<script>alert('Deleted!!');window.location='/admin_student'</script>")


def admin_manage_dept(request):
    dept=Department.objects.all()
    if 'submit' in request.POST:
        dept=request.POST['dept']
        dept_entry = Department.objects.create(dept_name=dept)
        
        return HttpResponse("<script>alert('Added!!');window.location='/admin_manage_dept'</script>")
    return render(request,'admin_manage_dept.html',{'depts':dept})

# def admindept_edit(request,id1):
#     dept=Department.objects.get(id=id1)
#     if 'update' in request.POST:
#         dept=request.POST['dept']
#         dept.dept_name=dept
#         dept.save()
#         return HttpResponse("<script>alert('Updated!!');window.location='/admin_manage_dept'</script>")
#     return render(request,'admin_manage_dept.html',{'dept':dept})


def admindept_edit(request, id1):
    dept = Department.objects.get(id=id1)
    
    if request.method == 'POST' and 'update' in request.POST:
        dept_name = request.POST['dept']  # Get new department name from form
        dept.dept_name = dept_name  # Assign it to the object
        dept.save()  # Save the changes
        return HttpResponse("<script>alert('Updated!!');window.location='/admin_manage_dept'</script>")
    
    return render(request, 'admin_manage_dept.html', {'dept': dept})


def admindept_delete(request,id2):
    hh=Department.objects.get(id=id2)
    hh.delete()
    
    return HttpResponse("<script>alert('Deleted!!');window.location='/admin_manage_dept'</script>")


def admin_manage_course(request,id1):
    que=Course.objects.filter(dept_id=id1)
    if 'submit' in request.POST:
        cname=request.POST['cname']
        course = Course.objects.create(course_name=cname,dept_id=id1)
        return HttpResponse(f"<script>alert('Added!!');window.location='/admin_manage_course/{id1}'</script>")
    return render(request,'admin_manage_course.html',{'cname':que})

 
def admin_courseedit(request, id4):
    course = Course.objects.get(id=id4)
    
    if request.method == 'POST' and 'update' in request.POST:
        cname=request.POST['cname']
        course.course_name = cname  # Assign it to the object
        course.save()  # Save the changes
        return HttpResponse(f"<script>alert('Updated!!');window.location='/admin_manage_course/{course.dept_id}'</script>")
    
    return render(request, 'admin_manage_course.html', {'course': course})   


def admin_coursedelete(request,id2):
    hh=Course.objects.get(id=id2)
    
    hh.delete()
    
    return HttpResponse(f"<script>alert('Deleted!!');window.location='/admin_manage_course/{hh.dept_id}'</script>")

def admin_manage_sem(request,id1):
    que=Semester.objects.filter(course_id=id1)
    if 'submit' in request.POST:
        sem=request.POST['sem']
        sem = Semester.objects.create(sem=sem,course_id=id1)
        return HttpResponse(f"<script>alert('Added!!');window.location='/admin_manage_sem/{id1}'</script>")
    return render(request,'admin_manage_sem.html',{'sems':que})

def admin_sem_edit(request, id1):
    sem = Semester.objects.get(id=id1)
    if request.method == 'POST' and 'update' in request.POST:
        sem_value = request.POST['sem']
        sem.sem = sem_value 
        sem.save() 
        return HttpResponse(f"<script>alert('Updated!!');window.location='/admin_manage_sem/{sem.course_id}'</script>")
    
    return render(request, 'admin_manage_sem.html', {'sem': sem})

def admin_sem_delete(request,id2):
    hh=Semester.objects.get(id=id2)
    hh.delete()
    hk=hh.course_id
    
    return HttpResponse(f"<script>alert('Deleted!!');window.location='/admin_manage_sem/{hk}'</script>")

def admin_manage_subject(request,id1):
    sname=Subject.objects.filter(sem_id=id1)
    if 'submit' in request.POST:
        sem=request.POST['sname']
        sub = Subject.objects.create(subject_name=sem,sem_id=id1)
        return HttpResponse(f"<script>alert('Added!!');window.location='/admin_manage_subject/{id1}'</script>")
    return render(request, 'admin_manage_subject.html', {'sname': sname})

def admin_subedit(request, id1):
    sub = Subject.objects.get(id=id1)
    
    if request.method == 'POST' and 'update' in request.POST:
        sname = request.POST['sname']  # Get new subject name        
        sub.subject_name = sname  # Assign new subject name
        
        sub.save()  # Save changes
        
        return HttpResponse(f"<script>alert('Updated!!');window.location='/admin_manage_subject/{sub.sem_id}'</script>")
    
    return render(request, 'admin_manage_subject.html', {'sub': sub})

def admin_subdelete(request,id2):
    hh=Subject.objects.get(id=id2)
    hh.delete()
    ho=hh.sem_id
    return HttpResponse(f"<script>alert('Updated!!');window.location='/admin_manage_subject/{ho}'</script>")

from django.utils import timezone
def admin_announcement(request):
    if 'submit' in request.POST:
        ann = request.POST['ano']
        Announcement.objects.create(announcement=ann, date=timezone.now().date())
        return HttpResponse("<script>alert('Added!!');window.location='/admin_announcement'</script>")
    
    announcements = Announcement.objects.all()
    return render(request, 'admin_announcement.html', {'ann': announcements})


def admin_anueedit(request, id1):
    ann = Announcement.objects.get(id=id1)

    if request.method == 'POST' and 'update' in request.POST:
        ann_value = request.POST['ano']  # Get new announcement value
        ann.announcement = ann_value  # Assign new announcement value
        ann.save()  # Save changes
        return HttpResponse("<script>alert('Updated!!');window.location='/admin_announcement'</script>")
    
    return render(request, 'admin_announcement.html', {'announ': ann, 'ann': Announcement.objects.all()})

def admin_anudelete(request, id2):
    hh = Announcement.objects.get(id=id2)
    hh.delete()
    return HttpResponse("<script>alert('Deleted!!');window.location='/admin_announcement'</script>")


# def admin_viewteacher(request):
#     teachers = Teacher.objects.select_related('dept').all()
#     departments = Department.objects.all()
#     courses = Course.objects.all()
#     semesters = Semester.objects.all()
#     subjects = Subject.objects.all()
#     if 'submit' in request.POST:
#         teacher=request.POST['selected_teacher']
        
#         sub=request.POST['selected_subject']
#         assign=AssignTeacher.objects.create(teacher_id=teacher,subject_id=sub,date=timezone.now().date())
#         return HttpResponse("<script>alert('Assigned!!');window.location='/admin_viewteacher'</script>")
    
#     return render(request, 'admin_viewteacher.html', {'teachers': teachers,'departments': departments,'courses': courses,'semesters': semesters,'subjects': subjects,})
    
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
from .models import Teacher, Department, Course, Semester, Subject, AssignTeacher

def admin_viewteacher(request):
    teachers = Teacher.objects.select_related('dept').all()
    departments = Department.objects.all()
    courses = Course.objects.all()
    semesters = Semester.objects.all()
    subjects = Subject.objects.all()

    if 'submit' in request.POST:
        teacher_id = request.POST.get('selected_teacher')
        subject_id = request.POST.get('selected_subject')

        # Check if the teacher is already assigned to the subject
        existing_assignment = AssignTeacher.objects.filter(teacher_id=teacher_id, subject_id=subject_id).exists()

        if existing_assignment:
            return HttpResponse("<script>alert('Already Assigned! Please assign a different subject.');window.location='/admin_viewteacher'</script>")

        # Assign the teacher if not already assigned
        AssignTeacher.objects.create(teacher_id=teacher_id, subject_id=subject_id, date=timezone.now().date())
        return HttpResponse("<script>alert('Assigned Successfully!');window.location='/admin_viewteacher'</script>")

    return render(request, 'admin_viewteacher.html', {
        'teachers': teachers,
        'departments': departments,
        'courses': courses,
        'semesters': semesters,
        'subjects': subjects,
    })


def teacher_view_assignedsub(request):
    assign=AssignTeacher.objects.filter(teacher_id=request.session['tid'])
    return render(request,'teacher_view_assignedsub.html',{'assign':assign})

def teacher_send_assignment(request,id1):
    if 'submit' in request.POST:
        assignment=request.POST['assignment'] 
        date=request.POST['date']
        desc=request.POST['desc']
        assign=Assignments.objects.create(subject_id=id1,teacher_id=request.session['tid'],assignment=assignment,due_date=date,description=desc,date=timezone.now().date()) 
        return HttpResponse(f"<script>alert('Added!!');window.location='/teacher_send_assignment/{id1}'</script>")
    return render(request,'teacher_send_assignment.html')

# def student_viewdept_course(request):
#     std=Student.objects.get(id=request.session['sid'])
#     return render(request,'student_viewdept_course.html',{'std':std})


# def student_viewdept_course(request):
#     std = Student.objects.get(id=request.session['sid'])
    
#     # Fetch semesters related to the student's course
#     semesters = Semester.objects.filter(course=std.course)
    
#     # Fetch subjects related to the course's semesters
#     subjects = Subject.objects.filter(sem__course=std.course)

#     return render(request, 'student_viewdept_course.html', {
#         'std': std,
#         'semesters': semesters,
#         'subjects': subjects
#     })


def student_viewdept_course(request):
    std = Student.objects.get(id=request.session['sid'])
    
    # Fetch semesters related to the student's course
    semesters = Semester.objects.filter(course=std.course)
    
    # Fetch subjects related to the course's semesters
    subjects = Subject.objects.filter(sem__course=std.course)
    
    # Fetch assignments related to the subjects
    assignments = Assignments.objects.filter(subject__in=subjects)

    if 'submit' in request.POST:
        assignment_id = request.POST['selected_assignment']
        student_id = request.session['sid']
        
        # Check if student has already submitted this assignment
        existing_submission = UploadAssignments.objects.filter(student_id=student_id,assignment_id=assignment_id).exists()
    
        if existing_submission:
            return HttpResponse("<script>alert('You have already submitted this assignment!');window.location='/student_viewdept_course'</script>")
        assignment = request.POST['selected_assignment']
        FILES = request.FILES['assignment_file']
        file_storage = FileSystemStorage()
        pht = file_storage.save(FILES.name, FILES)
        UploadAssignments.objects.create(
            student_id=request.session['sid'],
            assignment_id=assignment,
            file=pht,
            grade='pending',
            date=timezone.now().date(),
            status='Pending',
            marks='Not Graded'
        )
        return HttpResponse("<script>alert('Uploaded!!');window.location='/student_viewdept_course'</script>")
    
    return render(request, 'student_viewdept_course.html', {
        'std': std,
        'semesters': semesters,
        'subjects': subjects,
        'assignments': assignments  # Added assignments
    })


def student_view_marks(request):
    # Get the logged-in student
    student = Student.objects.get(id=request.session['sid'])
    
    # Get all semesters related to the student's course
    semesters = Semester.objects.filter(course=student.course)
    
    # Initialize variables
    selected_semester = None
    uploaded_assignments = []
    
    # Handle semester selection from dropdown
    if request.method == 'GET' and 'semester' in request.GET:
        semester_id = request.GET.get('semester')
        if semester_id:
            selected_semester = Semester.objects.get(id=semester_id)
            
            # Get subjects for the selected semester
            semester_subjects = Subject.objects.filter(sem=selected_semester)
            
            # Get assignments for these subjects
            semester_assignments = Assignments.objects.filter(subject__in=semester_subjects)
            
            # Get the student's uploaded assignments for these assignments
            uploaded_assignments = UploadAssignments.objects.filter(
                student=student,
                assignment__in=semester_assignments
            ).select_related('assignment', 'assignment__subject')
    
    context = {
        'student': student,
        'semesters': semesters,
        'selected_semester': selected_semester,
        'uploaded_assignments': uploaded_assignments,
    }
    
    return render(request, 'student_view_marks.html', context)

# View for detailed mark information
def view_assignment_mark_detail(request, assignment_id):
    student = Student.objects.get(id=request.session['sid'])
    
    try:
        # Get the specific assignment submission
        submission = UploadAssignments.objects.get(
            id=assignment_id,
            student=student
        )
        
        context = {
            'student': student,
            'submission': submission,
            'assignment': submission.assignment,
            'subject': submission.assignment.subject
        }
        
        return render(request, 'student_uploaded_viewassignment.html', context)
        
    except UploadAssignments.DoesNotExist:
        return HttpResponse("<script>alert('Assignment submission not found.');window.location='/student_view_marks'</script>")
    
    
    
def student_send_complaint(request):
    complaint=Complaint.objects.filter(login_id=request.session['lid'])
    if 'submit' in request.POST:
        complaint=request.POST['issues']
        
        Complaint.objects.create(login_id=request.session['lid'],complaint=complaint,reply='pending',date=timezone.now().date())
        return HttpResponse("<script>alert('Sent!!');window.location='/student_send_complaint'</script>")
    return render(request,'student_send_complaint.html',{'complaint':complaint})

def student_view_announcements(request):
    announcements = Announcement.objects.all()
    return render(request, 'student_view_announcements.html', {'announcements': announcements})

def parent_view_announcement(request):
    announcements = Announcement.objects.all()
    return render(request, 'parent_view_announcement.html', {'announcements': announcements})

def teacher_view_student(request):
    # Get the logged-in teacher's department
    teacher = Teacher.objects.get(id=request.session['tid'])
    students = Student.objects.filter(dept=teacher.dept)

    return render(request, 'teacher_view_student.html', {'students': students})

def teacher_view_attendance(request,student_id):
    assignments = newAttandacess.objects.filter(student_id=student_id).order_by('-at_date')

    # """Fetch weekday count for each month and send to the template."""
    # attendance_data = Attendance.objects.all().values("month", "year", "weekday_count")
    
    # Convert queryset into a dictionary for easy access in template
    # month_data = {item["month"]: item["weekday_count"] for item in attendance_data}

    return render(request, 'teacher_view_attendance.html', {'assignments': assignments})




def teacher_view_all_attend(request):
    assignments = newAttandacess.objects.order_by('-at_date') 

    return render(request, 'teacher_view_all_attend.html', {'assignments': assignments})




def view_assignments(request, student_id):
    student = Student.objects.get(id=student_id)
    assignments = UploadAssignments.objects.filter(student=student)

    return render(request, 'teacher_view_assignments.html', {'student': student,'assignments': assignments})






    
from django.shortcuts import redirect
from django.contrib import messages

def add_marks(request, id1):
    try:
        up = UploadAssignments.objects.get(id=id1)
        
        if request.method == 'POST':
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'marks' in request.POST:
                marks = request.POST.get('marks')
                try:
                    marks = int(marks)
                    if not (0 <= marks <= 100):
                        return JsonResponse({
                            "success": False, 
                            "error": "Marks must be between 0 and 100"
                        })
                        
                    # Update marks and calculate grade
                    up.marks = marks
                    up.status = 'Graded'
                    up.grade = up.calculate_grade()  # Use the model method
                    up.save()
                    
                    return JsonResponse({
                        "success": True, 
                        "grade": up.grade,
                        "marks": marks
                    })
                except ValueError:
                    return JsonResponse({
                        "success": False, 
                        "error": "Invalid marks value"
                    })
            
            # Handle regular form submission
            marks = request.POST.get('marks')
            try:
                marks = int(marks)
                if 0 <= marks <= 100:
                    up.marks = str(marks)
                    up.status = 'Graded'
                    up.grade = up.calculate_grade()
                    up.save()
                    return HttpResponseRedirect(f'/view_assignments/{up.student.id}/')
            except (ValueError, TypeError):
                pass
        
        student = up.student
        assignments = UploadAssignments.objects.filter(student=student)
        context = {
            'student': student,
            'assignments': assignments
        }
        return render(request, 'teacher_view_assignments.html', context)
        
    except UploadAssignments.DoesNotExist:
        return JsonResponse({"success": False, "error": "Assignment not found"}, status=404)

    
from django.db.models import Subquery, OuterRef
from .models import Complaint, Student

def admin_view_complaint(request):
    student_subquery = Student.objects.filter(login=OuterRef('login')).values('name')[:1]

    complaints = Complaint.objects.annotate(student_name=Subquery(student_subquery)).all()
    if 'submit' in request.POST:
        complaint_id = request.POST.get('complaint_id')
        reply = request.POST['reply']
        
        complaint = Complaint.objects.get(id=complaint_id)
        complaint.reply = reply
        complaint.save()
        
        return HttpResponse("<script>alert('Sent Reply!!');window.location='/admin_view_complaint'</script>")
    return render(request, "admin_view_complaint.html", {"look": complaints})


def parent_view_semester(request, student_id):
    student = Student.objects.get(id=student_id)
    semesters = Semester.objects.filter(course=student.course)
    marks = []
    selected_semester = None

    if 'semester' in request.GET:
        semester_id = request.GET.get('semester')
        selected_semester = semester_id
        
        # Get subjects for the selected semester
        subjects = Subject.objects.filter(sem_id=semester_id)
        
        # Get marks for each subject
        for subject in subjects:
            internal_marks = InternalMarks.objects.filter(
                student=student,
                subject=subject
            ).first()
            
            assignment_marks = UploadAssignments.objects.filter(
                student=student,
                assignment__subject=subject
            ).values('marks', 'status')
            
            marks.append({
                'subject': subject,
                'internal_marks': internal_marks.marks if internal_marks else 'Not Added',
                'assignment_marks': ', '.join([m['marks'] for m in assignment_marks]) if assignment_marks else 'Not Added',
                'status': 'Completed' if internal_marks and assignment_marks else 'Pending'
            })

    context = {
        'student': student,
        'semesters': semesters,
        'marks': marks,
        'selected_semester': selected_semester
    }
    
    return render(request, 'parent_view_semester.html', context)

def parent_view_student(request):
   
        # Get students associated with the logged-in parent
    attendance_data = newAttandacess.objects.select_related('student').order_by('-at_date') 
    return render(request, 'parent_view_student.html', {'student': attendance_data})
   

def parent_view_studdets(request):
    lid = request.session.get('lid')
    par = Parent.objects.get(login=lid)
    Stud = Student.objects.filter(parent=par)
    
    return render(request, 'parent_view_studdets.html', {'students' : Stud})

def parent_view_marks(request,sid):
    # Get the logged-in student
    student = Student.objects.get(id=sid)
    
    # Get all semesters related to the student's course
    semesters = Semester.objects.filter(course=student.course)
    
    
    # Initialize variables
    selected_semester = None
    uploaded_assignments = []
    
    # Handle semester selection from dropdown
    if request.method == 'GET' and 'semester' in request.GET:
        semester_id = request.GET.get('semester')
        if semester_id:
            selected_semester = Semester.objects.get(id=semester_id)
            
            # Get subjects for the selected semester
            semester_subjects = Subject.objects.filter(sem=selected_semester)
            
            # Get assignments for these subjects
            semester_assignments = Assignments.objects.filter(subject__in=semester_subjects)
            
            # Get the student's uploaded assignments for these assignments
            uploaded_assignments = UploadAssignments.objects.filter(
                student=student,
                assignment__in=semester_assignments
            ).select_related('assignment', 'assignment__subject')
    
    context = {
        'student': student,
        'semesters': semesters,
        'selected_semester': selected_semester,
        'uploaded_assignments': uploaded_assignments,
    }
    
    return render(request, 'parent_view_marks.html', context)

def parent_view_assignment_mark_detail(request, assignment_id, sid):
    student = Student.objects.get(id=sid)
    
    try:
        # Get the specific assignment submission
        submission = UploadAssignments.objects.get(
            id=assignment_id,
            student=student
        )
        
        context = {
            'student': student,
            'submission': submission,
            'assignment': submission.assignment,
            'subject': submission.assignment.subject,
            'sid' : sid
        }
        
        return render(request, 'parent_view_assignment_mark_detail.html', context)
        
    except UploadAssignments.DoesNotExist:
        return HttpResponse("<script>alert('Assignment submission not found.');window.location='/parent_view_marks'</script>")
    

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                                #/////////////////Chat-Bot///////////////////////////#
# from django.shortcuts import render
# from django.http import JsonResponse
# import textwrap
# import google.generativeai as genai
# import json


# # Google Gemini API Key
# GOOGLE_API_KEY = 'AIzaSyAdbPNd0d037Wad2-DZ8PKPzidNJ4H6anE'

# genai.configure(api_key=GOOGLE_API_KEY)

# model = None
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         break

# def to_markdown(text):
#     text = text.replace('*', ' ')
#     return textwrap.indent(text, '> ', predicate=lambda _: True)

# def generate_gemini_response(prompt):
#     # Add a specific context for mental health
#     context_prompt = (
#     f"This conversation includes both financial discussions and casual chats. "
#     f"If the user asks about finance, provide expert financial advice on topics like budgeting, investment strategies, "
#     f"savings, loans, and financial planning with practical and easy-to-understand insights. "
#     f"For general conversations, engage in a friendly and natural manner, responding appropriately to greetings, small talk, "
#     f"or personal inquiries. "
#     f"User Query: {prompt}")
#     response = model.generate_content(context_prompt)
#     return response.text
# def handle_small_talk(message):
#     casual_responses = {
#         "hello": "Hi there! How can I assist you today?",
#         "how are you": "I'm just a chatbot, but I'm always here to help!",
#         "what's up": "Not much, just helping people with their finances!",
#         "thank you": "You're welcome! Let me know if you need more help.",
#         "bye": "Goodbye! Take care and manage your finances well!",
#         "goodbye": "Goodbye! Take care and manage your finances well!"
#     }
#     return casual_responses.get(message.lower(), "That's interesting! Tell me more.")

# def get_financial_advice(message):
#     return f"Great question! When it comes to {message}, it's important to plan wisely. Consider diversifying your investments."

# def chatbot(request):
#     return render(request, 'chatbot.html')

# def chat(request):
#     if request.method == 'POST':
#         try:
#             body = json.loads(request.body.decode('utf-8'))
#             user_message = body.get('message', '').strip()  # Safely extract and clean the message
#         except json.JSONDecodeError:
#             return JsonResponse({'response': 'Invalid JSON input.'})

#         if not user_message:
#             return JsonResponse({'response': 'Please provide a valid message.'})

#         # Filter user input for specific topics (e.g., mental health-related)
#         if 'mental health' not in user_message.lower():
#             return JsonResponse({'response': 'Please ask questions related to mental health details and related content.'})
#         else:
#         # Handle casual conversation
#             response_message = handle_small_talk(user_message)
#         # Generate a response
#         gemini_response = generate_gemini_response(user_message)
#         return JsonResponse({'response': gemini_response})

#     return JsonResponse({'response': 'Invalid request method.'})


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def teacher_add_internal_marks(request, student_id):
    student = Student.objects.get(id=student_id)
    teacher = Teacher.objects.get(id=request.session['tid'])
    
    # Verify teacher belongs to student's department
    if student.dept_id != teacher.dept_id:
        return HttpResponse("<script>alert('Unauthorized access');window.location='/teacher_home'</script>")
    
    semesters = Semester.objects.filter(course=student.course)
    existing_marks = InternalMarks.objects.filter(
        student=student
    ).select_related('subject', 'subject__sem')
    
    context = {
        'student': student,
        'semesters': semesters,
        'existing_marks': existing_marks
    }
    return render(request, 'teacher_add_internal_mark.html', context)

def get_subjects(request, semester_id):
    teacher = Teacher.objects.get(id=request.session['tid'])
    subjects = Subject.objects.filter(
        sem_id=semester_id,
        assignteacher__teacher=teacher
    ).values('id', 'subject_name')
    return JsonResponse(list(subjects), safe=False)



def student_view_attendance(request):
   
        # Get students associated with the logged-in parent
    attendance_data = newAttandacess.objects.select_related('student').filter(student_id=request.session['sid']).order_by('-at_date')
    return render(request, 'student_view_attendance.html', {'student': attendance_data})
   



def add_internal_marks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            student = Student.objects.get(id=data['student_id'])
            subject = Subject.objects.get(id=data['subject_id'])
            marks = data['marks']
            
            # Check if marks already exist
            existing_mark = InternalMarks.objects.filter(
                student=student,
                subject=subject
            ).first()
            
            if existing_mark:
                return JsonResponse({
                    'success': False,
                    'error': 'Marks already exist for this subject'
                })
            
            # Create new internal marks entry
            InternalMarks.objects.create(
                student=student,
                subject=subject,
                marks=marks,
                date=timezone.now().date(),
                status='Published'
            )
            
            return JsonResponse({'success': True})
            
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
# Code to count weekdays till today
def count_weekdays_till_today(year, month):
    """Counts the number of weekdays from the 1st of the month to today."""
    today = datetime.today().day  # Get today's date
    weekday_count = 0

    for day in range(1, today + 1):
        if datetime(year, month, day).weekday() < 5:  # Monday-Friday (0-4)
            weekday_count += 1

    return weekday_count






# code to calcultae % chatgpt

# import calendar
# from datetime import datetime

# def get_total_working_days(year, month):
#     # Get the total number of days in the given month
#     total_days_in_month = calendar.monthrange(year, month)[1]
    
#     # Initialize a counter for working days (Monday to Friday)
#     working_days_count = 0
    
#     # Iterate through all the days in the month
#     for day in range(1, total_days_in_month + 1):
#         # Check the day of the week (0: Monday, 1: Tuesday, ..., 6: Sunday)
#         day_of_week = datetime(year, month, day).weekday()
        
#         # Increment the working days count if it's Monday to Friday (not Saturday/Sunday)
#         if day_of_week < 5:  # 0 to 4 corresponds to Monday to Friday
#             working_days_count += 1

#     return working_days_count

# def calculate_attendance_percentage(total_working_days, attended_days):
#     # Calculate attendance percentage
#     if total_working_days == 0:
#         return 0
#     attendance_percentage = (attended_days / total_working_days) * 100
#     return attendance_percentage

# # Example usage:
# year = 2025
# month = 3

# # Get total working days (excluding weekends)
# total_working_days = get_total_working_days(year, month)
# print(f"Total working days in {calendar.month_name[month]} {year}: {total_working_days}")

# # Assume the student attended all 6 periods on 3 working days
# attended_days = 3  # For example, the student attended 3 working days

# # Calculate the attendance percentage
# attendance_percentage = calculate_attendance_percentage(total_working_days, attended_days)
# print(f"Attendance percentage: {attendance_percentage:.2f}%")
