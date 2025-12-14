from django.shortcuts import render
from datetime import datetime

def index(request):
    context = {
        'first_name': 'zyad',
        'last_name': 'astal',
        'student_id': 120210866,
        'address': 'gaza palestine',
        'email': 'zastal@students.iugaza.edu.ps',
        'birth_date': datetime(2003, 7, 11),
    }
    return render(request, 'pages/index.html', context)
