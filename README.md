![pic](wireframes/mockup_book_review_club.PNG)
# [Book Review Club](https://book-review-club.herokuapp.com/) (Milestone project 3)

## Introduction

[Book review club](https://book-review-club.herokuapp.com/) is an python base application website that is going to be a 
reference for people looking for a book to read. Obviously, There are many 
books available to read, but find a good book could be frustrating sometimes. 
This web site present different books, give a short description of each book,
 and one can read other people reviews about books. Yet, this is not all.
This a book club. It means you can get familiar with other readers. 
You can see which book they have liked and their opinion about books. 
Then, you can like and share your opinion about the book too.

## Table of Contents

1. [Introduction](#1.introduction)<br/>
2. [UX](#ux)<br/>
3. [Features](#features)<br/>
    - 3.1. [Existing Features](#existing-features)<br/>
        -  3.1.1. [Home page](#home-page)<br/>
        -  3.1.2. [My page](#my-page)<br/>
        -  3.1.3. [My book collections](#my-book-collections)<br/>
    - 3.2. [Features Left to Implement](#features-left-to-implement)<br/>

4. [Technologies Used](#technologies-used)<br/>
5. [Testing](#testing)<br/>
    - 5.1. [Making a book library and share it with others](#making-a-book-library-and-share-it-with-others)<br/>
        - 5.1.1. [Create a user account](#create-a-user-account)<br/>
        - 5.1.2. [User personal book library](#user-personal-book-library)<br/>
        - 5.1.3. [Book section](#book-section)<br/>
        - 5.1.4. [Book review club home page](#book-review-club-home-page)<br/>
        - 5.1.5. [Search in the books](#search-in-the-books)<br/>
    - [5-2- The website validation](#the-website-validation)<br/>
        - 5.2.1. [Different validation services](#different-validation-services)<br/>
        - 5.2.2. [Website validation of different browsers](#website-validation-of-different-browsers)<br/>

6. [Deployment](#deployment)<br/>
    - [GitHub](#gitHub)<br/>
    - [Heroku](#heroku)<br/>

7. [Content](#content)<br/>
8. [Media](#media)<br/>
9. [Acknowledgements](#acknowledgements)<br/>
10. [Disclaimer](#disclaimer)<br/>

<br/>

## UX

This website makes it easier to find a book. 
Users will get to know various kinds of books through a user-friendly interface. 
Also, looking at other people's reviews could help to understand if the book is the 
right choice for them. On the other hand, this website could make a bookseller business-owner 
sell more books; this would be possible by creating a social media model website. 
People can share the books that they read and write a review about them.

This website consists of three main sections. 
In the main section, the home page, users can see different books, 
search for them, and create a user account for themselves. 
In the other section, the user page, users can make a user account and add a 
review about a book that likes to share with others. 
In each book section, people can read about the book and see other people's review. 

Here some user stories:

* As a book lover, this website helps me to find a book on the topic that I always 
wanted to read about it but did not have a proper reference to choose from.
* I am pleased that I can share my opinion about the book that I have read recently. 
Other people's feedback helps me to understand if I have the right conclusion.
* As a bookstore owner, I like the website because it can show people about different books and 
makes them interested in readings.

The desktop and mobile resolution wireframes of 
the Book Review Club can be found in the following [link](wireframes/Wireframes.pdf).

## Features

This project is going to be consist of three main sections:

* Home page
* My page
* My book collections

### Existing Features

#### Home page

On the home page, the user can get a warm feeling of being in a library or bookstore 
with the help of a warm brownish theme and bookstore background image through the website. 
There are some inspiring quotes from famous people on the hero image of the home page. 
Then a user can have an overview of the books available on the website 
with the title and name of the other. In addition, it is possible to see 
how many people liked or write a review of a book. If the user wants to see more 
details about a book, first need to be logged in to the website. 
This will be discussed in more detail in the following sections.

#### My page

In this section, user can sign up, login or loge out form the website. 
In the sign up section user needs to provide a username and 
password and agree to terms and conditions of the webpage. 
In the log in page user should provide and valid username and password. 
After log in, there is a profile page showing short info about the username. 
If the user is logged in then can see addition information about each book. 
Also, user can add its own collection of the books to the website 
in the my book collections section.

#### My book collections

In this section, the user can add his/her own favorite books. 
Also, the user can edit or delete the added books. 
These books will be added to the total collection of the books on the website and other 
users can add a review to them. Each user can delete its own reviews. 
However, there is an administrator user that can edit/delete other people's books or reviews.

### Features Left to Implement

There are several possible features to implement The most important ones:

* Add a link to each book to redirect the user to book store 
webpage which book can be purchased.
* More info for each users in their own webpage 
which can have users and they can be connect to each other.

## Technologies Used

The following technologies have been used in this project:

* Python 3.8.2 
    * Python is supposed to be the main hero of this project.
* Flask
    * web framework written in Python.
* MongoDB
    * It is a document-oriented database program.
* Heroku
    * It is a cloud platform to run this python project.
* HTML5
    * used to structure and presenting the content.
* CSS3
    * used for styling.
* JQuery
    * this project used JavaScript in the form of JQuery to simplify DOM manipulation.
* Materialize 1.0.0
    * CSS framework used for structuring and presenting the content.
* Fontawsome
    * used to create icons.
* Google font
    * used for formatting the fonts.

## Testing

### Making a book library and share it with others:

In this app user can create a library of their favorite books that 
might have read before and share it with others, other users can write reviews about the book. 
In this way, people get more interested in 
reading books and this could be valuable for a book retail owner.

This was achieved with following sections:

#### Create a user account:

User can create an account, as it can be seen in **Fig01**. 
The user needs to provide a valid/unique username and password and agree to 
the standard term and conditions provided with the webpage. After signing up is done, 
the user is directed to his/her profile page which user profile can be seen on the page. Besides, 
the user name is added to my page in 
the top-right corner and a new item (my books) is added to the navbar (**Fig02**).

![pic](testing/manual-testing/Fig01&Fig02.png)

#### User personal book library

In this section, the user can add the book to his/her collections. 
The user needs to provide a valid book title, author(s), book description, and book cover image 
link to submit the book to the database. An example is shown in **Fig03**. 
After submission, a flash is appearing in this test example “SUCCESSFULLY ADDED TO YOUR COLLECTION” and 
the book can be seen under the add form section (**Fig04**). In this part, the user can edit the added items 
or completely delete the book from the database. It is good to mention, if the book title length is more than 20 characters, 
the title is summarized as it is shown in the Fig04. 
By clicking on this section user is directed to the book section which can add reviews.

![pic](testing/manual-testing/Fig03&Fig04.png)

#### Book section

In this part, the user can see more details of the added book (book description). 
Also, users can be added to the user's lists which liked the booked (**Fig05**). 
It is worth to mention if the user likes the book, the heart turns red, and his/her 
username will be added to the list (**Fig06**). This will be saved in the database and a 
responsive message on the heart is shown if the user changes his/her mind. 
This means if the user clicks again on the heart, the heart goes back to the original 
white color and his/her name be removed from the list. Also, the user can add a review 
in this section. After submission of the review will be added at the bottom of the page
 with data and time. Reviews are ordered according to the time at which the 
 latest review will be at the top. Also, the user can remove his/her review (**Fig07**).

 ![pic](testing/manual-testing/Fig05&Fig06.png)

 ![pic](testing/manual-testing/Fig07.png)

#### Book review club home page

In this section, every visitor can browse through the books that are added to this 
webpage with different users (**Fig08**), also can search through them which will be discussed later. 
But, if a user would like to see more information by clicking on each book, 
then it will be redirected to the login page with a flash message 
saying “PLEASE LOGIN FIRST” (**Fig09**).

![pic](testing/manual-testing/Fig08&Fig09.png)

#### Search in the books

Every visitor can browse through the books by searching. 
The search function can search among Book title, author, and book description (**Fig10**). 
If there are no results can find in the database, 
a relevant message will be shown to the user as “No results found” (**Fig11**).

![pic](testing/manual-testing/Fig10&Fig11.png)

### The website validation

#### Different validation services

The HTML part is validated with Markup Validation Service W3C® without any major problem. 
There was one warning using html section element without using heading element. 
Problem resolved with changing html section element with div element. 
Results can be seen in the following [link](testing/validation/Markup_validation_HTML.pdf).

The W3C CSS validation service was used for CSS part. 
There was no problem regarding CSS validating. Results can be seen in the following [link](testing/validation/Markup_validation_CSS.pdf).

JS hint used for validation of JavaScript. There is no problem to report.

#### Website validation of different browsers

The website was tested on:

* Google chrome
    * There was no issue. The results can be seen in the following [link](testing/validation/Chrome_testing.pdf).
* Firefox
    * There was no issue. The results can be seen in the following [link](testing/validation/Firefox_testing.pdf).
* Opera
    * There was no issue. The results can be seen in the following [link](testing/validation/Opera_testing.pdf).
* Internet explorer
    * There was no issue. The results can be seen in the following [link](testing/validation/InternetExplorer_testing.pdf).
* Samsung S8
    * There was no issue. The results can be seen in the following [link](testing/validation/SamsungS8_testing.pdf).

## Deployment

### GitHub

It is possible to deploy this project in GitHub as your development environment, with following these steps:

* Save a copy of the github repository located at https://github.com/MajPaji/Book-Review-Club.git or with clone in git clicking

```
git clone https://github.com/MajPaji/Book-Review-Club.git
```
* Install all requirements modules with following CL:
```
pip3 install -r requirements.txt
```
* create `env.py` file with follwoing data:

```
MONGO_URI=mongodb+srv://...
SECRET_KEY=verysecretkey
```
* In the last line of `app.py` change `debug=False` to `debug=True`

* It is possible to run the application with following CL:

```
python app.py
```
### Heroku

It is possible to deploy this project to Heroku, with following steps:

* Make a requirements.txt file using follwing CL:

```
pip freeze > requirements.txt
```
* Make a Procfile in the CL:
```
echo web: python app.py > Procfile
```
* Push requirements and Procfile to the GitHub 

* Create a new app on the Heroku website (It is not possible to choose the simillar name as this project)

* In the Heroku dashbord click Deploy and in the Deployment method select GitHub

* Confirm the linking

* In the Heroku dashbord click Setting and Reveal Config Vars

* Set the following parameters

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
SECRET_KEY | `verysecretkey`
DEBUG | FALSE

* Click Deploy in the Heroku dashbord



## Content

* The book description and image links of this project is mainly from goodreads.com. https://www.goodreads.com/

* The quote section in the home page, they are imported from this page https://gist.github.com/nasrulhazim/54b659e43b1035215cd0ba1d4577ee80

* Term and condition section in sig up page used from free service of Terms And Conditions Generator https://www.termsandconditionsgenerator.com/

## Media

The photos used in this site were obtained from website with right for free to use, share or modify, even commercially:

* The hero image index (hero-image-index.jpg) https://unsplash.com/photos/HH4WBGNyltc

## Acknowledgements

I acknowledge Gerry (my mentor) guidance on this project.

## Disclaimer

Please contact if you have any issue regarding copyright content.
This project is only for educational purposes.
sababi@kth.se

















