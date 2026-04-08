# BookSocialMedia

It is a social media platform made to post book and posts about the books

---

## *What it can do*

* You can create, update and delete posts
* You can login, register, sing in and logout your user
* There are also some navigation tools trough navbar books filtering and also by genre 
* There are clubs that you can create and join

---
## How to install it

1. clone the repo, with the code below
2. create an environment or use mine which I uploaded
3. download the needed libraries found in the requirements.txt
4. in your terminal do ' cd BookSocialMedia ' 
5. Apply the migrations by doing 'python manage.py makemigrations'
6. Then 'python manage.py migrate'
7. Now you can host on your local server by using ' python manage.py runserver '
* _NB_ it will be on your browser at (https:// 127.0.0.1:8000)
8. Now you can use it as a socialmedia website

#### Admin
- Only an admin can validate a bokk that a normal user gives
- To create an admin write ( python manage.py createsuperuser ) fill the infos then go to...
- https:// 127.0.0.1:8000/admin and start managing like an admin

#  an example of the website can be found at "https://booksocialmedia.pythonanywhere.com/"

- For the modifications of the project it is a normaldjango project no big difference just to know the basics

##### thanks for reading

