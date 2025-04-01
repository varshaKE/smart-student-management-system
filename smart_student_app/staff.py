from flask import *
from database import *
from facedetection import *

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
    
    return render_template('staff_home.html')


@staff.route('/staff_view_notification')
def staff_view_notification():
    data={}
    u="select* from notification"
    data['view']=select(u)
    return render_template('staff_view_notification.html',data=data)


@staff.route('/staff_manage_student')
def staff_manage_student():
    data={}
    u="select* from student inner join course using(course_id)"
    data['view']=select(u)
    return render_template('staff_manage_student.html',data=data)

@staff.route('/staffmanagestudnetsface',methods=['get','post'])
def staffmanagestudnetsface():
    data={}
    sid=request.args['sid']
    if "Upload" in request.form:
        pid = str(sid)

        isFile = os.path.isdir(r"static/trainimages/" + pid)  
        print(isFile)

        if not isFile:
            os.mkdir(r'static/trainimages/' + pid)
        image1 = request.files['image1']
        path1 = "static/trainimages/" + pid + "/imag1.jpg"
        image1.save(path1)
        
        image2 = request.files['image2']
        path2 = "static/trainimages/" + pid + "/imag2.jpg"
        image2.save(path2)
        
        image3 = request.files['image3']
        path3 = "static/trainimages/" + pid + "/imag3.jpg"
        image3.save(path3)


        enf(r"static/trainimages/")
        flash('Successfully Added')
        return redirect(url_for('staff.staff_manage_student'))


    return render_template('staffmanagestudnetsface.html',data=data)




    
@staff.route('/staffmanageinternalmark', methods=['get', 'post'])
def staffmanageinternalmark():
    data = {}
    
    sid=request.args['sid']

    if 'submit' in request.form:

        subject_id=request.form['subject_id']
        mark=request.form['mark']

      
        q = "insert into internalmark values(NULL,'%s','%s','%s')" % (subject_id,sid,mark)
        insert(q)
        flash('Successfully Added')

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None

    if action == 'delete':
        q = "delete from internalmark where InternalMark_id='%s'" % (id)
        delete(q)
        flash('Successfully Deleted')
        return redirect(url_for('staff.staff_manage_student'))

    if action == 'update':
        q = "select * from internalmark where InternalMark_id='%s'" % (id)
        res = select(q)
        data['updater'] = res

    if 'update' in request.form:
        subject_id=request.form['subject_id']
        mark=request.form['mark']
        q = "update internalmark set subject_id='%s',mark='%s' where InternalMark_id='%s'" % (subject_id,mark,id)
        update(q)
        flash('Successfully Updated')
        return redirect(url_for('staff.staff_manage_student'))

    q = "select * from internalmark inner join subject using(Subject_id) inner join student using(student_id)"
    res = select(q)
    data['view'] = res

    ro="select * from subject"
    data['ty']=select(ro)

    return render_template('staffmanageinternalmark.html', data=data)





@staff.route('/staffmanageexternalmark', methods=['get', 'post'])
def staffmanageexternalmark():
    data = {}
    
    sid=request.args['sid']

    if 'submit' in request.form:

        subject_id=request.form['subject_id']
        mark=request.form['mark']

      
        q = "insert into externalmark values(NULL,'%s','%s','%s')" % (subject_id,sid,mark)
        insert(q)
        flash('Successfully Added')

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None

    if action == 'delete':
        q = "delete from externalmark where ExternalMark_id='%s'" % (id)
        delete(q)
        flash('Successfully Deleted')
        return redirect(url_for('staff.staff_manage_student'))

    if action == 'update':
        q = "select * from externalmark where ExternalMark_id='%s'" % (id)
        res = select(q)
        data['updater'] = res

    if 'update' in request.form:
        subject_id=request.form['subject_id']
        mark=request.form['mark']
        q = "update externalmark set subject_id='%s',mark='%s' where ExternalMark_id='%s'" % (subject_id,mark,id)
        update(q)
        flash('Successfully Updated')
        return redirect(url_for('staff.staff_manage_student'))

    q = "select * from externalmark inner join subject using(Subject_id) inner join student using(student_id)"
    res = select(q)
    data['view'] = res

    ro="select * from subject"
    data['ty']=select(ro)

    return render_template('staffmanageexternalmark.html', data=data)
