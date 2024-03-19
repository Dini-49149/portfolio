from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def project_detail(request, project_id):
    # Logic to select the correct project template based on project_id
    template_name = f'projects/{project_id}.html'
    return render(request, template_name)