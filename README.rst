=================
Blog Demo Project
=================

This repository contains the code for my sample blog project

This README contains the following sections:

    1. `Project Description`_ 

    2. Instructions for `Running Locally`_ 
    
    3. `Extra Features`_ beyond the basic requirements
    
    4. Other `Notes`_ 


Project Description
===================

This project is intended to fulfill the requirements at https://github.com/votizen/careers/blob/master/RemoteCodingProblem.rst.

Running Locally
===============
1. Clone this project's code from github (http://github.com/eleather/blog).

Set up your machine
-------------------
2. Install python and django (https://docs.djangoproject.com/en/dev/intro/install/).
3. Install apache and mod_wsgi (http://code.google.com/p/modwsgi/).
4. Replace your httpd.conf with the one at the top level of this project.  This will enable WSGI in Apache. {TODO: where is this file likely to be?}
5. Install postgresql (http://www.postgresql.org/).

Set up the project
------------------
6. Create a postgresql user called 'emily' with the password 'emilytest'.
7. Create a postgresql database called 'emily'.
8. In your terminal, cd to the directory where you cloned this project, then into the 'emily' directory, and then run 'python manage.py syncdb' to load the schema into the database.

Run the project
---------------
9. Still in the top 'emily' directory in your terminal, run 'python manage.py runserver' to start a server.
10. Visit localhost:8000 in your browser to view the site.

Extra Features
==============
1. I deviated slightly from the instructions on the makeup of the Post object.  I added an 'author' field, because I think any good blog should have the ability to credit the author.
2. Three RSS 2.0 feeds are available:
  - mysite.com/posts/recent/rss - the 5 most recent posts
  - mysite.com/posts/rss - all posts
  - mysite.com/post/{id}/rss - all comments for a specified post
3. Slightly-better-than-plaintext styling.

Notes
=====
1. I used a number of django documentation and tutorial pages, blog posts, and stack overflow answers in writing this project, however the content is substantively mine.  
2. I've tried to follow as closely as I can to the PEP-8 style guidelines (http://www.python.org/dev/peps/pep-0008/), and the style in the Django example code.  Some of this style (especially the line breaks) disagrees with my usual style, and doesn't look as gorgeous to me as I usually want my code to be.  Hopefully it looks prettier to more experienced Python developers.
3. Project names, usernames, and passwords were intentionally kept simple for your convenience.  I used my name in many of the naming schemes to help avoid overlap with things already on your machine.  The password choices and repetition are insecure, and wouldn't be used in a real development setting.
4. I've used Python 2.7 and Django 1.4.  If you're using different versions, you may encounter issues (though I'm not experienced enough with Python and Django to be able to anticipate all of them).  For example, Python 2.7 uses a different testing library than previous versions, and if you're not using Python 2.7 you may need to change my 'import unittest' declarations to 'from django.utils import unittest'.
5. I started to develop this project using TDD with django.test.TestCase, then had trouble getting them to work as acceptance/integration tests and decided that you would probably rather see this project soon than see a well-tested project.  I strongly believe in good testing of models, controllers, and view content, and if this were a real project I wouldn't have cut that corner and would have figured out how to do acceptance tests correctly in Django.
6. I like to break my style definitions into multiple files and then use a tool that combines them all into a single one for the user to download (in Rails, this is SASS).  I didn't see something similar for Django, so apologies for the single, messy CSS file.
7. The template naming conventions are largely from Rails.  The 'post_details.html' convention felt inelegant, and I couldn't quickly find a description of a better one used by Django programmers.
8. There are a couple of form changes I didn't take the time to make:
  - The Post forms shouldn't display 'created_at' and 'user'.  Those should be added in on the server side when the creation form is saved, and not editable after that.
  - The Comment preview page is using the default one instead of a local template, which means that I couldn't have it inherit from base.html so it doesn't have the header, footer, or styling.
  - The 'staff_member_required' decorator takes the user to admin's login page, not mine.  I'm not sure of a simple way to change this.
9. It wasn't 100% clear from the 'all users can comment on posts' instruction whether that means all viewers, or all logged-in users.  My original implementation of comments required a user to login before posting a comment.  When I switched to using the built-in comments I couldn't find a way to replicate that restriction without a lot of extra work, so I willfully re-interpreted the instruction to allow all visitors to post comments, whether they're logged in or not.  Hopefully that's alright.
10. Overall this project was a great learning experience.  I'd really like to spend more time talking to developers who are more experienced with Django - I feel like there are more concise ways to do much of this, and lots of idioms I don't know.
