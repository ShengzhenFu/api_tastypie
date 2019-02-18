API tastypie
---------------------------------
This program is used to create APIs to provide json data to other apps

Overview
---------------------------------
It now support below API calls via the link below 

    /api/v1/Server/?format=json
    /api/v1/TechnicalService/?format=json
    /api/v1/Team/?format=json

The source data of above are maintained in django admin site
    
    /admin
    
   ![admin](https://user-images.githubusercontent.com/30173222/52926467-d2f2ec00-3370-11e9-9494-caa22ce1c558.JPG)

Installation instructions
---------------------------------
1. download the source code

2. Install python packages listed in Requirements.txt

3. run command at the source code directory:

   3.1 python manage.py runserver 127.0.0.0:8000
   
   3.2 access localhost:8000/admin to manage the meta data
   
   3.3 call APIs in Postman via the links below to verify result
   
       http://localhost:8000/api/v1/Server/?format=json
       http://localhost:8000/api/v1/Team/?format=json
       http://localhost:8000/api/v1/TechnicalService/?format=json
       http://localhost:8000/api/v1/Server/?format=json&ts_id__exact=ts00165
    
    ![callapi](https://user-images.githubusercontent.com/30173222/52926655-a8edf980-3371-11e9-8da6-73f509f8269b.JPG)
    
Technical support
---------------------------------   
   For technique issues, please contact fushengzhen@163.com 