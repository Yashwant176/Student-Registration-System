from django.shortcuts import render, redirect, get_object_or_404
from .models import Details

def student_list(request):
    students = Details.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':    
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')
        standard = request.POST.get('standard')
        af = request.POST.get('af')
        pa = request.POST.get('pa')
        balance = int(af) - int(pa)

        Details.objects.create(
            name=name,
            age=age,
            city=city,
            mobile=mobile,
            standard=standard,
            af=af,
            pa=pa,
            balance=balance
        )
        return redirect('students:student_list')
    return render(request, 'student_form.html', {'student': {}})

def student_update(request, pk):
    student = get_object_or_404(Details, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.city = request.POST.get('city')
        student.mobile = request.POST.get('mobile')
        student.standard = request.POST.get('standard')
        student.af = request.POST.get('af')
        student.pa = request.POST.get('pa')
        student.balance = int(student.af) - int(student.pa)
        student.save()
        return redirect('students:student_list')
    return render(request, 'student_form.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Details, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students:student_list')
    return render(request, 'student_list_confirm.html', {'student': student})
