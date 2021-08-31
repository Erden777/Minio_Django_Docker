from django.shortcuts import render

# Create your views here.
from . import minio_connection

def index(request):
    minio_connection.init_minio()
    image_url = minio_connection.init_minio()
    print(image_url)
    image_url = 'http://172.17.0.2:9000/images/ssh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=5ZNQLGPH0ELEM55Q7YVV%2F20210831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210831T044914Z&X-Amz-Expires=604800&X-Amz-Security-Token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3NLZXkiOiI1Wk5RTEdQSDBFTEVNNTVRN1lWViIsImV4cCI6MzYwMDAwMDAwMDAwMCwicG9saWN5IjoiY29uc29sZUFkbWluIn0.R7ZU7ANln7wqhW7NeJXd2G5RK0djv_n7ykoXawVrfXWcBz454nfR__Pq-uIT3zILe3um3CsBWJKcsNtrKZpYQQ&X-Amz-SignedHeaders=host&versionId=null&X-Amz-Signature=18c96a209e6284608db5def3f69f980f5a44c056e3bbe851cecf9253ae60c069'
    return render(request, "home.html", {'image_url': image_url})