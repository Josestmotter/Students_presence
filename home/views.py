from django.http import HttpResponse
from django.shortcuts import render
from .models import Students, Classes
from .services import process_file, record_attendance
import pandas as pd


def home(request):
    students = Students.objects.all()
    data = None
    selected_student = None
    last_class = Classes.objects.last()
    class_num = int(last_class.class_number) if last_class else 0
    number = request.GET.get("number") or request.POST.get("number")

    if number:
        selected_student = Students.objects.filter(number=int(number)).first()

    if request.method == "POST":
        file = request.FILES.get("file")

        if file:
            data, class_name = process_file(file)

            if Classes.objects.filter(class_number=class_name).exists():
                return render(request, "home/home.html", {
                    "error": f"Class {class_name} has already been submitted.",
                    "students": students,
                    "class_num": class_num,
                    "last_class": last_class,
                })

            Classes.objects.create(class_number=class_name)
            record_attendance(data)

            students = Students.objects.all()
            last_class = Classes.objects.last()

            if number:
                selected_student = Students.objects.filter(number=int(number)).first()

    if selected_student and last_class and last_class.class_number:
        absences = int(selected_student.absences)
        class_num = int(last_class.class_number)
        attendance = (class_num - absences) / class_num * 100
    else:
        attendance = 0

    total_absences = [s.absences for s in students]
    overall_attendance = (
        (class_num * students.count() - sum(total_absences)) / (class_num * students.count()) * 100
    ) if class_num > 0 and students.count() > 0 else 0

    return render(request, "home/home.html", {
        "students": students,
        "student": selected_student,
        "class_num": class_num,
        "data": data,
        "last_class": last_class,
        "attendance": f"{attendance:.1f}",
        "overall_attendance": f"{overall_attendance:.1f}",
        "total_absences": sum(total_absences),
    })


def export_csv(request):
    total_classes = Classes.objects.count()

    data = []
    for student in Students.objects.all():
        attendance = round((total_classes - student.absences) / total_classes * 100, 1) if total_classes > 0 else 0
        data.append({
            "Name": student.name,
            "Number": student.number,
            "Absences": student.absences,
            "Attendance %": attendance,
        })

    df = pd.DataFrame(data)

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="report.csv"'
    df.to_csv(response, index=False)

    return response