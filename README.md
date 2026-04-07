# 📚 Student Administrator

A web system for managing student attendance. Import class lists via CSV,
view attendance statistics per student, and export the final report.

## 🛠️ Tech Stack
- Python
- Django
- Pandas

## ⚙️ How to run

### Prerequisites
- Python 3.x installed
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourprofile/student-administrator.git
cd student-administrator

# Install dependencies
pip install django pandas

# Run database migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Access it in your browser: `http://localhost:8000`

## 📋 How to use

1. Prepare a `.csv` file in the following format:
Name,Number,Attendance,Contact,Class
John Smith,101,Present,11999999999,1
Mary Johnson,102,Absent,11988888888,1
2. Upload the file through the interface
3. Select a student from the list to view their attendance details
4. Click **Download CSV Report** to export the final report

> Each class number can only be submitted once. The system automatically rejects duplicates.

## Status
Completed.

## Author
Made by [Your Name](https://github.com/yourprofile)
