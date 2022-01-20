# <a name="top"></a>DJANGO Tutorials - Table of Contents:
   [1. Install PYTHON & DJANGO v4.0](#install_django)<br>
   <br>

## <a name="install_django"></a>Install PYTHON & DJANGO 4 Framework [&#8593; top](#top)

Download and install [PYTHON](https://www.python.org/downloads/ "PYTHON - Python"). To install
[DJANGO](https://docs.djangoproject.com/en/4.0/intro/tutorial01/ "DJANGO v4 - Python Web Framework") you just need to open Windows PowerShell and type in one of the following commands:

<span style="color:red; font-weight:bold;">
    <pre>
<span style="color:white; font-weight:normal;">         (install django):</span> python -m pip install Django
<span style="color:white; font-weight:normal;">(create a django project):</span> django-admin startproject project_name
<span style="color:white; font-weight:normal;">    (create a django app):</span> python manage.py startapp app_name
<span style="color:white; font-weight:normal;">(run database migrations):</span> python manage.py migrate
<span style="color:white; font-weight:normal;">    (create a super user):</span> python manage.py createsuperuser
<span style="color:white; font-weight:normal;">             (run server):</span> python manage.py runserver</pre>
</span>

## <a name="common_commands"></a>Common DJANGO commands [&#8593; top](#top)

Common [DJANGO](https://docs.djangoproject.com/en/4.0/intro/tutorial01/ "DJANGO v4 - Common Commands"):

<span style="color:red; font-weight:bold;">
    <pre>
<span style="color:white; font-weight:normal;">         (django version):</span> python -m django --version
<span style="color:white; font-weight:normal;">             (run server):</span> python manage.py runserver specify_different_port</pre>
</span>

each time you modify a model, run the following to update the database:
python manage.py makemigrations app_name
python manage.py migrate