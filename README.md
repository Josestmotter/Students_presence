# Student Administrator

Web app to track student attendance. Upload a CSV with your class list,
check each student's presence history, and download the final report.

## Tech Stack
- Python
- Django
- Pandas

## Getting Started

```bash
git clone https://github.com/yourprofile/student-administrator.git
cd student-administrator

pip install django pandas

python manage.py migrate
python manage.py runserver
```

Then open `http://localhost:8000`

## How to use

Upload a `.csv` file formatted like this:
```
Name,Number,Attendance,Contact,Class
John Smith,101,Present,11999999999,1
Mary Johnson,102,Absent,11988888888,1
```
Pick a student from the sidebar to see their stats.
Hit **Download CSV Report** whenever you need the full report.

> Each class number can only be uploaded once — duplicates are rejected.

## Author
José Motter Tenfen
