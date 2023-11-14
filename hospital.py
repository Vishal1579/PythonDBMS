import mysql.connector as ms
con=ms.connect(host='127.0.0.1',user='root',password='Nithya@123',charset='utf8')
cur=con.cursor()
cur.execute("create database Hospital system")
cur.execute("use Hospital system")
cur.execute("create table if not exists patient(patient id int primary key, name varchar(20),age int, blood group varchar(10), contact_number int, gender varchar(10),address varchar(75), doctor id int)")
cur.execute("create table if not exists doctor(doctor id int primary key, name varchar(20),age int, dept varchar(25),experience int, contact_number int, gender varchar(10), address varchar(75))")
def add_p():
    pid=int(input("Enter patient id:"))
    name=input("Enter patient name:")
    age=int(input("Enter patient age:"))
    bg=input("Enter blood group")
    mn=int(input("Enter contact number:"))
    g=input("Enter gender:")
    ad=input("Enter address:")
    did=int(input("Enter doctor id:"))
    cur.execute(insert ignore into patient values({0},{1},{2},{3},{4},{5},{6},{7}).format(pid,name,age,bg,mn,g,ad,did))
    con.commit()
    print("Patient info added!")
def add_d():
    did=int(input("Enter doctor id:"))
    name=input("Enter doctor name:")
    age=int(input("Enter doctor age:"))
    dept=int(input("Enter department:"))
    ex=input("Enter experience:")
    mn=int(input("Enter contact number:"))
    g=input("Enter gender:")
    ad=input("Enter address:")
    cur.execute(insert ignore into patient values({0},{1},{2},{3},{4},{5},{6},{7}).format(did,name,age,dept,ex,mn,g,ad))
    con.commit()
    print("Doctor info added!")
def del_p():
    pid=int(input("Enter patient id to delete:"))
    cur.execute("delete from patient where patient id={}".format(pid))
    con.commit()
    print("Patient record deleted")
def del_d():
    did=int(input("Enter doctor id to delete:"))
    cur.execute("delete from doctor where doctor id={}".format(did))
    con.commit()
    print("Doctor record deleted")
def search_p():
    pid=int(input("Enter patient id to search"))
    cur.execute("select * from patient where patient id={}".format(pid))
    data=cur.fetchone()
    print(data)
def search_d():
    did=int(input("Enter doctor id to search"))
    cur.execute("select * from patient where doctor id={}".format(did))
    data=cur.fetchone()
    print(data)
def patient():
    print("1.Add new patient\n2.Delete patient record\n3.Search patient information\n4.Show all records") 
    c=int(input("Enter choice:"))
    if c==1:
        add_p()
    elif c==2:
        del_p()
    elif c==3:
        search_p()
    elif c==4:
        cur.execute("select * from patient")
        data=cur.fetchall()
        for x in data:
            print(x)
    else:
        print("Invalid choice")
def doctor():
    print("1.Add new doctor\n2.Delete doctor record\n3.Search doctor information\n4.Show all records") 
    c=int(input("Enter choice:"))
    if c==1:
        add_d()
    elif c==2:
        del_d()
    elif c==3:
        search_d()
    elif c==4:
        cur.execute("select * from doctor")
        data=cur.fetchall()
        for x in data:
            print(x)
    else:
        print("Invalid choice")    
print("\tLogin")
username='admin'
pwd='admin'
u=input("Username:")
pw=input("Password:")
while True:
    if u==username and pw==pwd:
        while True:
            print("1.Patient records\n2.Doctor records\n3.Exit")
            ch=int(input("Enter choice:"))
            if ch==1:
                patient()
            elif ch==2:
                doctor()
            elif ch==3:
                break
            else:
                print("Invalid choice")
        break
    else:
        print("Incorrect username or paaaassword")