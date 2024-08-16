# The Barn Owl Inn

![]()



## Design Stage

### Wireframes

I sketched initial wireframes of the home page and of the tables selection screen that will be a key part of the reservation process.

![wireframes](readme_images/wireframe.jpg)

### User Stories/Acceptance Criteria

I planned my user stories and their acceptance criteria on paper, with some conversational assistance from a relative - who has experience of converting ideas in to formulaic written forms. I then transferred them to a GitHub Projects kanban board.

![drafting User Stories](readme_images/ustory_draft.jpg)
![GitHub Projects kanban board](readme_images/kanban_board.png)

### Entity Relationship Diagrams

![entity relationship diagrams](readme_images/erd.jpg)

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

In `barn_owl_inn/settings.py`, I added 'home' to the list of installed apps.

I ran a server:

> `python3 manage.py runserver`

I opened it in browser, copied the relevant string from the error message, ended the server with Ctrl-C, and pasted the string in the empty allowed hosts list, again within the settings file. I preemptively added '.herokuapp.com' to the list.

I will also be changing debug to False before each git commit.

### Base template

On my user stories board, I moved 'Navigate the site' to the In Progress column.

![site navigation user story](readme_images/navigate_criteria.png)

I created `/templates/base.html` and `/home/templates/home/index.html`, putting HTML boilerplate in the former and `{% extends "base.html" %}` in the latter, which is DTL (Django Templating Language).

I also created `/static/css/style.css`, `/static/images`, and `static/js/script.js`. Then, I could add a link element to the head of the base template and give it a href of `{% static 'css/style.css' %}`, ready for applying CSS styles.

I like to have a live preview open while styling, to immediately see the changes. Since my project was not wired up yet, style changes were not being reflected, so an additional vanilla HTML link element had been added - which was removed shortly after, once it became redundant.

I added an unordered list navigation menu to the base template and styled it in to a navbar.

### Home page

Through a fluid process combining experimenting, reviewing Django debugging messages, and consulting paper notes I had made or other files of code I had written, I managed to get to a point where a bare home page with a navbar is displayed upon running the server.

![home page with navbar](readme_images/bare_home.png)

This entailed additions to `barn_owl_inn/settings.py`, to `barn_owl_inn/urls.py`, the creation of `home/urls.py`, additions to `home/views.py`, to `home/templates/home/index.html`, and to `templates/base.html`, as well as changes to `static/css/styles.css`. All of these insertions and alterations will be captured in the 5th git commit (28 July '24), and are additionally reflected in these handwritten pages that I wrote also for my own future reference:

![code featured in fifth commit](readme_images/fifth_commit.jpg)

### Database Connection

I created a git-ignored `env.py` file, in which I set the URL of a PostgreSQL cloud database and a randomly-generated secret key. If env exists, it is imported in `settings.py`. Settings gets the database URL and secret key from the environment variables.

I activated database tables and registered admin:

> `python3 manage.py migrate`
>
> `python3 manage.py createsuperuser`

### Writing Database Model Classes

I started 2 more apps, 'menu' and 'reserve', and added them to the installed apps.

I moved 'View menu list' and 'Update menu' user stories to In Progress column.

![menu viewing user story](readme_images/menu_view_criteria.png)
![menu updating user story](readme_images/menu_update_criteria.png)

I wrote my Table, Reservation, and Dish models in the appropriate `models.py` files of the two new apps. I then migrated them to the database:

![migrating database models](readme_images/migrate_models_1.png)

### Adding Dishes to the Database

I registered the new models in the `admin.py` files of their apps and added a CSRF_TRUSTED_ORIGINS constant to the project's settings file. Then I ran the server and opened in browser, appended `/admin` to the URL, and logged in as the superuser. Now I, the developer, can add a number of example dishes (i.e., instances of the Dish class) to the database, and a future owner could add more just as easily - bringing the 'Update menu' user story close to fulfilment.

![admin panel new dish form](readme_images/add_dish.png)

An existing dish can be edited (to alter the price, for example) in a very similar manner, after selecting it from the dish list in the admin panel as shown here:

![dish list and edit dish form](readme_images/edit_dish.jpg)

#### Input Requirements/Restrictions

By purposefully inputting invalid data while adding new dishes, I manually tested:

- that `unique=True` had done as expected and prevented the name attributes of two different instances of the Dish class (now acting as a database schema) from being identical,

![testing dish name uniqueness](readme_images/unique_dish_name.png)

- that `blank=False` had indeed prevented the course field from being left empty,

![testing dish course requirement](readme_images/course_needed.png)

- that `max_digits=4` prevents an unrealistically high price from being entered, given that two decimal places were included,

![testing dish price requirement](readme_images/price_limited.png)

- and that `decimal_places=2` made a third decimal place invalid, since real-world currency is being represented.

![testing decimal place limit](readme_images/two_decimals.png)

### Dish List on Menu Page

I began by imitating my notes from `readme_images/fifth_commit.jpg`. This entailed adding URL patterns to `barn_owl_inn/urls.py` (existing) and `menu/urls.py` (new), adding a basic rendering method to `menu/views.py`, creating `menu/templates/menu/menu.html` and having it extend the base template, and adding a href to the Menu link of `templates/base.html`'s navbar.

I went through a period of confusion, trying to replace what I had just written as a placeholder with more suitable "class-based views". A prior 'Django blog walkthrough project' seemingly had left me with the impression that class-based views were required when more than one database entry had to be drawn upon (e.g., thumbnails of all blog posts rather than a specific post, or list of all dishes rather than just one dish). After experimentation, note-checking, and research, I concluded that I was mistaken and my original code before this detour was closer to the solution.

After this return to my initial pathway, I soon managed to get my database's dish objects crudely displaying on the menu page as seen below - principally (on the back end) by adding a curly braces argument to the render method, allowing my `menu.html` file to read the dishes data and show it. This of course was coupled with putting some provisional DTL (Django Templating Language) into the HTML file - a for loop in the `{% %}` logic marker and variables in their `{{ }}` marker.

![basic dish data display](readme_images/dishes_rendered.png)

In the process, I realised that neither of the `views.py` files required a `template_name=` before the file path string.

I still had to work out how to get the starters, main course dishes, and desserts displaying under the appropriate headings. I had the epiphany that my `views.py` file's `menu_page` method could contain multiple variables. In other words, rather than just `dishes = Dish.objects.all()` and then trying to apply logic with DTL, I could and should have three separate variables: `starters = Dish.objects.filter(course=1)`, and so on. All three could be conveyed to the HTML file via the dictionary object that is the third argument of the render method.

To refine the outcome, I added further HTML tags and attributes and styled them in `static/css/style.css`. Some of the HTML has no visual effect but will improve accesibility, particularly `aria-labelledby`.

![improved menu display](readme_images/viewable_menu.png)

I can now move my 'View menu list' and 'Update menu' user stories to Done, as all of their acceptance criteria have been met.

### Reservations Page

I repeated the pattern once again of putting appropriate basics in the URL files and views file as pertains this time to the `reserve` app.

#### User Authentication

Since much of the functionality of the reservations section will be dependent on a user being registered and authenticated, it was now time to move the 'Sign up/Log in' user story to 'In Progress'.

![Sign Up user story now in progress](readme_images/kanban_with_signup_moved.png)
![sign up and log in acceptance criteria](readme_images/signup_login_criteria.png)

I then installed the required user authentication package:

> `pip3 install django-allauth~=0.57.0`
>
> `pip3 freeze --local > requirements.txt`
>
> `pip3 show django-allauth`
>
> `cp -r <Location>/allauth/templates/* ./templates/`
>
> `pip3 manage.py showmigrations`
>
> `pip3 manage.py migrate`

On the first day of attempting the migrate command, there was an external database problem. Not definitively knowing that, I tried extensively to get it to work, but ultimately had to resume work the following day when the issue elsewhere had been addressed. It was at least reassuring that the command failing was no fault of my own.

I had also made appropriate additions to the settings file:

![additions to settings file](readme_images/allauth_settings.png)

At this time, I could give a real href to the remaining navbar links in `base.html`. DTL if-else logic will mean that an unauthenticated user will see 'Sign up' and 'Log in' but a logged-in user will just see 'Log out' instead.

I also removed some of the automatic code in some of the relevant Django allauth template files, so that allauth could integrate better with my existing project. For example, I removed the rest of a path in front of 'base' so that my own custom base template is referenced instead where relevant.

#### Reservations Page Itself

I moved the remaining user stories to 'In Progress', as all pertain to the reservation functionalities.

![kanban board In Progress column updated](readme_images/all_ustories_in_progress.png)

From the admin panel, I created my instances of Table. In the process, I manually tested that two instances indeed cannot have the same table number, as shown here:

![unique table number required](readme_images/unique_table_number.png)

From the admin panel, I created a dummy reservation.

![creating mock reservation](readme_images/dummy_reservation.png)

In `my_reservations.html`, I utilised DTL logic and variables to simply display the details of this reservation, but only to a logged-in user who was responsible for the reservation's creation.

- The Django Templating Language code:

![initial templating to show or hide reservations](readme_images/reservation_details_dtl.png)

- What was seen when still logged in with the superuser account:

![own reservation visible while logged in](readme_images/own_booking_seen.png)

- What was seen after logging out and again navigating to the reservations page:

![reservation invisible when logged out](readme_images/no_bookings_seen.png)

#### Login Prompt

I added a piece of logic such that, when navigating to the My Reservations page, an unauthenticated user will see a message that they should sign up/log in, whereas a logged-in user will see their existing reservations and - once I have coded it - the form with which they can make a new reservation.

### The Reservation Form

This will be some of the core functionality of my project. I added a ReservationForm class to `reserve/forms.py`, a form element to `reserve/templates/reserve/my_reservations.html`, and an if statement into the reservations_page method in `reserve/views.py`, for handling submission of the completed form - looking to my recent 'Django blog walkthrough project' for a rough guide of how to handle this updating of the database with user-inputted details.

As seen below, I now had a basic but functional reservations form which I could then refine. I had already created a dummy reservation via the admin panel; the second group of reservation details visible here was added to the database with this new reservation form, confirming that the form was indeed functioning.

![simple reservation form](readme_images/basic_form.png)

The first improvement I wanted was to make the date selection easier for the user. I did so via `forms.py`, using Django Forms widgets. The effect was that a calendar-like date selector was now available, like it had been automatically when reserving from the admin panel.

![calendar style date selection](readme_images/date_selector.png)

#### Table Map

I have been intending for the tables to be selected by clicking buttons styled to loosely resemble the corresponding restaurant tables. This is not strictly essential in terms of core functionality, but I believe it would significantly enhance the user experience, introducing a visual aspect to the otherwise abstract thing that is "the reservation" - and also make the project more satisfying to create, fulfilling my initial vision of it. The visual representation of the tables might help customers more confidently choose what tables they want, since their relative size will be visible and - if I am able in the available time to position the buttons as I originally imagined - their location within the restaurant could be perceptible too.

As a first step towards this, in `my_reservations.html`, I added a div with an ID of 'tables-map' that contains multiple buttons. With DTL logic and variables, my instances of Table are iterated through and the relevant table number and seating capacity is shown on each button. I then resized these appropriately in `static/css/style.css`.

![styled but inactive table select buttons](readme_images/sized_table_buttons.png)

Again using widgets, I made the form's current table selector into a checkbox format. It will be a more user-friendly fallback if the tables map system cannot come to fruition within the next 5 remaining days before the project deadline. Additionally, it might be easier for me to code that clicking the tables indirectly clicks discrete checkboxes and vice versa.

I also reordered the form fields so that date and time will be above tables, since my user stories ask that tables can be shown as unavailable within the selected timeslot and this is a prerequisite for that.

### Table Map-Reservation Form Connection

I addded a `{% block script %}` to `base.html`, which in `my_reservations.html` will be filled with a script element with an src of `{% static 'js/table_select.js' %}`.

In `style.css`, I repositioned my tables map diagram to be alongside the table selector checkboxes. I will have to consider responsiveness but this suffices for now.

In `table_select.js`, I experimented extensively with trying to create my desired buttons-to-checkboxes connectivity. A git commit on the 14th of August includes some commented-out code that related to these attempts, which will of course later be either uncommented or removed.

Since my initial all-at-once attempt was not yet working out, I commented everything out and went back to basics. One at a time, I introduced the following three lines of code and checked that they worked. They are not required by my project but demonstrated to me that the JavaScript file was correctly linked up to the Python-served HTML file and could enact simple effects.

> `document.getElementsByTagName("h2")[0].addEventListener("click", function() {this.style.color = "red"});`
>
> `document.getElementsByTagName("button")[0].addEventListener("click", function() {this.style.backgroundColor = "blue"});`
>
> `document.getElementsByClassName("table")[1].addEventListener("click", function() {this.style.backgroundColor = "green"});`

![checking JavaScript file connected](readme_images/js_experiment_1.png)

Encouraged by this, I built on it by replacing these with code that iterated all of the table selection buttons, attached an event listener to each, checked the clicked button's current background color, and changed it as appropriate, the successful result seen below. It has been relatively long since I have significantly used JavaScript, since the course has recently had a Python focus, but I am quite quickly getting refreshed on JavaScript's differences.

![checking JavaScript color change](readme_images/js_experiment_2.png)

I decided that enabling the user to edit their reservations was more crucial than a fancy table selection method, so I put the latter on hold to focus on the former for now.

### Reservation Editing

I created `edit_reservation.js` in `static/js/` (alongside `table_select.js`) and similarly linked to it inside the `{% block script %}`. In the new script file, event listeners are attached to the Edit buttons that will be beneath each existing reservation displayed on the My Reservations page. (I preemptively added Delete buttons at the same time.) When the button is clicked, the details of that reservation will be copied into the form fields. The Submit button will also change to read 'Update'. I added IDs to several elements in `my_reservations.html` to facilitate this, and checked devtools to see what IDs Django had automatically given to the form fields.

![debugging with devtools](readme_images/formatting_alert.png)

A devtools error message alerted me that the formatting of the dates and times was preventing them being transferred to the form fields, which I then addressed in the HTML file by adding pipes to their DTL variables:

`{{ reservation.date|date:"Y-m-d" }}` and `{{ reservation.start_time|time:"H:i" }}`.

Trying to transfer the table numbers to checks in the appropriate checkboxes in the form was presenting challenges. Taking a step back from that, I tried to simply have the length of the list of tables logged to the console. I was surprised to see that the output was 0.

To confirm that an issue with logging to the console was not at fault, I added a temporary Hello World message at the top of the script. (My preferred Hello World is "Can you hear me?" - which is a reference to a TV show called _Person of Interest_.)

I ultimately realised that only my first reservation via the admin panel had a table number appearing on the My Reservations page, while the reservations added with the user-facing form were missing it. This seemed strange, as the form would have been invalid if a value for the table field was not initially acknowledged. I looked into it and determined that it could be remedied just by adding `reservation_form.save_m2m()` in `views.py`. Because the submission to the database was being briefly halted to add the 'reserver' to their reservation data, the code needed this extra step to properly save the ManyToManyField.

This done, I added another new reservation with the form. When I subsequently clicked Edit, all of the other fields were auto-filled into the form and the table field's console log correcly gave an output of 2, reflecting that the reservation had two tables associated with it.


Ultimately, I introduced a for loop into the code that, for each table of the reservation, checks the checkbox of the matching table number.

I had mistakenly been under the impression that the automatic ID/primary key of the tables would start from 0. When the checkbox getting checked was out by 1, I realised that this was why. It meant that I did not need to use my otherwise clever solution that I had come up with of giving an element a custom attribute whose value matched the automatic ID of the theoretically corresponding checkbox: `data-table_id="id_tables_{{ table.id }}`.

In `reserve/views.py`, I added a `reservation_edit` method that would handle the update better than reusing the existing form-saving code, by allowing a specific ID to be attached instructing which database entry to alter and finishing with a HTTP redirect back to the standard `/my-reservations` page of the site. I then added the appropriate URL pattern to `reserve/urls.py`.

### Reservation Deleting

I created `delete_reservation.js`, which adds event listeners to the Delete buttons, to show a modal seeking confirmation of intentional deletion. I again added an appropriate path in `urls.py`. The code required in `views.py` was simpler than for editing, since there was not the need to handle each individual form field.

I wanted to use a standard, non-Bootstrap modal because I have not been relying on Bootstrap up to now in this project. I therefore consulted [this W3S page](https://www.w3schools.com/howto/howto_css_modals.asp) and used some of its example CSS.

## Deployment Stage



## .gitignore and .slugignore



I named the readme_images directory in a slugignore file, because the screenshots and photos in this readme will not be required by the deployed site. [Heroku's documentation](https://devcenter.heroku.com/articles/slug-compiler#ignoring-files-with-slugignore) suggests that this should cause that directory's "files to be removed after you push code to Heroku and before the buildpack runs", so that large, unnecessary files are not included.

## Credit

- As mentioned above, a relative helped with phrasing and structuring my user stories/acceptance criteria.

- The CSS styling targeting the deletion confirmation modal was sourced from [W3Schools](https://www.w3schools.com/howto/howto_css_modals.asp), as mentioned above.