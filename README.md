# The Barn Owl Inn

![]()



## Design Stage

### Wireframes

I sketched initial wireframes of the home page and of the tables selection screen that will be a key part of the reservation process.

![wireframes](readme_images/wireframe.jpg)

### User Stories

I planned my user stories and their acceptance criteria on paper, with some conversational assistance from a relative - who has experience of converting ideas in to formulaic written forms. I then transferred them to a GitHub Projects kanban board.

![drafting User Stories](readme_images/ustory_draft.jpg)
![GitHub Projects kanban board](readme_images/kanban_board.png)

## Development Stage

### Initial Workspace Setup

I pip-installed Django and other essential dependencies, and pip-froze them to a requirements file:

> `pip3 install Django~=4.2.1 gunicorn~=20.1 dj-database-url~=0.5 psycopg2~=2.9`
>
> `pip3 freeze --local > requirements.txt`

I started a project and then an app:

> `django-admin startproject barn_owl_inn .`
>
> `python3 manage.py startapp home`

In my project's settings file, I added my app to the list of installed apps.

I ran a server:

> `python3 manage.py runserver`

I opened it in browser, copied the relevant string from the error message, ended the server with Ctrl-C, and pasted the string in the empty allowed hosts list, again within the settings file. I preemptively added '.herokuapp.com' to the list.

I will also be changing debug to False before each git commit.

### Base template

On my user stories board, I moved 'Navigate the site' to the In Progress column.

![site navigation user story](readme_images/navigate_criteria.png)

I created **/templates/base.html** and **/home/templates/home/index.html**, putting HTML boilerplate in the former and `{% extends "base.html" %}` in the latter, which is DTL (Django Templating Language).

I also created **/static/css/style.css**, **/static/images**, and **static/js/script.js**. Then, I could add a link element to the head of the base template and give it a href of `{% static 'css/style.css' %}`, ready for applying CSS styles.

I like to have a live preview open while styling, to immediately see the changes. Since my project is not wired up yet, style changes were not being reflected, so an additional vanilla HTML link element has been added, which will be removed in due course.

I added an unordered list navigation menu to the base template and styled it in to a navbar.



## Deployment Stage



## .gitignore and .slugignore



I named the readme_images directory in a slugignore file, because the screenshots and photos in this readme will not be required by the deployed site. [Heroku's documentation](https://devcenter.heroku.com/articles/slug-compiler#ignoring-files-with-slugignore) suggests that this should cause that directory's "files to be removed after you push code to Heroku and before the buildpack runs", so that large, unnecessary files are not included.

## Credit

- As mentioned above, a relative helped with phrasing and structuring my user stories/acceptance criteria.
