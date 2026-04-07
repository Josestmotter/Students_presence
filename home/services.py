from home.models import Students, Classes
from django.db.models import F
import pandas as pd
from pathlib import Path
from io import TextIOWrapper

BASE_DIR = Path(__file__).resolve().parent.parent


def receive_spreadsheet(request):
    if request.method == "POST":
        path = request.FILES.get("file")
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def add_students():
    df = pd.read_csv("home/static/home/Stud_abs.csv")
    data = df.to_dict(orient="records")
    for person in data:
        Students.objects.get_or_create(
            number=person["Number"],
            defaults={
                "name": person["Name"],
                "absences": 0
            }
        )


def record_attendance(csv_file):
    for person in csv_file:
        if person["Attendance"] == "Absent":
            Students.objects.filter(number=person["Number"]).update(
                absences=F("absences") + 1
            )


def process_file(file):
    text_file = TextIOWrapper(file.file, encoding="utf-8")
    df = pd.read_csv(text_file)
    data = df.to_dict(orient="records")
    class_num = int(df["Class"].dropna().iloc[0])  # gets the first non-empty value
    return data, class_num


def update_class_number(request):
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add":
            Classes.objects.filter(id=1).update(class_number=F("class_number") + 1)
        elif action == "subtract":
            Classes.objects.filter(id=1).update(class_number=F("class_number") - 1)
        return Classes.objects.first()