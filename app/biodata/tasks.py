# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task
def upload_detail(request):
    if request.method == 'GET':
        return render(request, 'biodata/upload_detail.html')
    
    csv_file = request.FILES['file']
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file, please upload a csv file.')
    
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set) # Putting it in a stream
    next(io_string)

    for column in csv.reader(io_string, delimiter = ',', quotechar = '|'):
        # _, allows us to skip the .save() call
        _, created = Biodata.objects.update_or_create(
            firstname = column[0],
            lastname = column[1],
            age = column[2],
            gender = column[3],
            address = column[4],
            date_of_birth = column[5],
            email = column[6]
        )
        context = {}
        return render(request, 'biodata/preview.html', context, prompt)