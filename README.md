## ASK system using Django

### Installation

  1. Make sure you have installed Python 2.7 and `pip`

  2. Run: `pip install -r requirements.txt`

  3. Go inside the directory folder, and create the tables:

      `python manage migrate`

  4. Test that everything works: `python manage runserver` and
      go to `localhost:8000`

### REST API / Django

In order for the student to learn how to create a REST API and write migrations to the database, there are some TODO's written in code for the student to complete and familiarize with the framework.

Here we provide a list of short TODO's:

  - Create a migration that allows you to not enter immediately the `assigned` User in the `Service` model.

  - Create REST end points to:

    - create a service
	- CRUD (create / read / update / delete) service and skills
	- create new users

  - Add authentication and permission to the REST API