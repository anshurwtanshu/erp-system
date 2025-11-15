

# **Employee Management System (Flask + MySQL)**

A simple web-based Employee Management System built using **Flask**, **MySQL**, and **HTML templates**.
This project provides admin login, employee registration, employee search, updating details, and deletion functionality.

---

## **📌 Features**

### ✅ **Admin Panel**

* Admin login (default: `admin` / `anshul`)
* Admin dashboard
* Secure session handling

### 👨‍💼 **Employee Management**

* Add new employee
* View all employees
* View employee profile
* Update employee details
* Delete employee
* Search employee by name

### 🗄️ **Database Integration**

* Uses **MySQL** database (`erpsystem`)
* CRUD operations on `employee` table
* Secure parameterized queries

---

## **📁 Project Structure**

```
project/
│── main.py
│── templates/
│     ├── home.html
│     ├── about.html
│     ├── admin.html
│     ├── admin_dashbord.html
│     ├── addemp.html
│     ├── searchemp.html
│     ├── admin_reg_suc.html
│     ├── showemployee.html
│     ├── adminprofile.html
│     ├── adminempupdate.html
│     ├── admin_emp_delete_success.html
│     ├── admin_emp_searchresult.html
└── static/
```

---

## **🛠️ Technologies Used**

* **Python Flask**
* **Flask-MySQLdb**
* **HTML / CSS**
* **MySQL Database**

---

## **🔧 Setup Instructions**

### **1️⃣ Install dependencies**

```bash
pip install flask flask-mysqldb
```

### **2️⃣ Create MySQL Database**

Run:

```sql
CREATE DATABASE erpsystem;

USE erpsystem;

CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(200),
    mobile VARCHAR(20),
    designation VARCHAR(100),
    salary VARCHAR(50)
);
```

### **3️⃣ Update database credentials (if needed)**

Inside `main.py`:

```python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "anshu@123"
app.config["MYSQL_DB"] = "erpsystem"
```

### **4️⃣ Run the project**

```bash
python main.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## **🔐 Admin Login**

| Username | Password |
| -------- | -------- |
| admin    | anshul   |

---

## **📸 Screenshots (Add your own)**

* Admin Login
* Dashboard
* Add Employee
* Employee List
* Update Employee
* Search Employee



