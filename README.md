# helloidol2
---
1. startproject helloidol2
   1. python -m pip install django~=4.2
   2. django-admin startproject helloidol2 .
   3. File > settings... > Language & Frameworks > Django [v] Enable Django Support
   4. RUN > Edit Configurations... > + > Django Server > Name : runserver
   5. VCS > Enable Version Control Intergration... > git > ok
2. startapp 세븐틴
   1. python manage.py startapp 세븐틴
   2. '세븐틴', in INSTALLED_APPS in settings.py
3. 세븐틴/
   1. models
      1. Character
         1. name, feature, created_at, updated_at
      2. python manage.py makemigrations 콩순이
      3. python manage.py migrate 세븐틴
      4. 