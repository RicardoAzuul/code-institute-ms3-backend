# Bookable
A book review and recommendation site, using MongoDB, Python, Flask, HTML, CSS and JavaScript.

Must haves for this project:
- a way for users to view books, including a cover image, number of upvotes and reviews.
- a way for users to add, edit or delete books.
- a way for users to add, edit or delete reviews.
- a profile page for a logged in user, with all their reviews and books.
- a login and a register page.
- search functionality.

Nice to have: 
- a sort functionality, so the books shown can be sorted based on title, author name, genre, et cetera.
- an admin portal, where an admin user can edit and delete all books, reviews and users.

To see the site in action, visit [https://code-institute-ms3-book-review.herokuapp.com/](https://code-institute-ms3-book-review.herokuapp.com/)

---

## Table of Contents
- [Bookable](#bookable)
  - [Table of Contents](#table-of-contents)
  - [UI and UX](#ui-and-ux)
    - [User stories](#user-stories)
    - [The 5 Planes of Design](#the-5-planes-of-design)
      - [Strategy Plane](#strategy-plane)
      - [Scope Plane](#scope-plane)
      - [Structure Plane](#structure-plane)
      - [Skeleton Plane](#skeleton-plane)
      - [Surface Plane](#surface-plane)
  - [Database Design](#database-design)
  - [Features](#features)
    - [Existing Features](#existing-features)
  - [- an admin portal, where the admin can delete and edit books, and delete reviews](#--an-admin-portal-where-the-admin-can-delete-and-edit-books-and-delete-reviews)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technologies Used](#technologies-used)
  - [Responsiveness of Pages](#responsiveness-of-pages)
  - [Testing](#testing)
    - [Notable Bugs](#notable-bugs)
    - [Problems](#problems)
  - [Deployment](#deployment)
    - [Run locally](#run-locally)
  - [Credits](#credits)
    - [Inspiration](#inspiration)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgements](#acknowledgements)

---

## UI and UX
 
### User stories
- First Time Visitor Goals
    - As a First Time Visitor, I want to easily understand the main purpose of the site. If I see a couple of books, together with upvotes and reviews, I'll quickly realize what the site is about.
    - As a First Time Visitor, I want to be able to easily navigate the site to find content.
    - As a First Time Visitor, I want to get information that indicates how actively the site is used, to determine how valuable the reviews and recommendations are.
- Returning User Goals
    - As a Returning User, I want to find reviews and recommendations for books.
    - As a Returning User, I want to be able to quickly see all my reviews.
    - As a Returning User, I want to be able to create, update and delete reviews, and create, update and delete books.
- Frequent User Goals
    - As a Frequent User, I want to find all reviews from a particular user, to determine how valuable their opinion is, which helps in finding new books.
- Site Owner Goals
    - As the site owner, I want to get recommendations for new books by crowdsourcing book reviews. The users of my site add reviews to books, which allows me to find new books I might like.
    - As the site owner, I want to earn money using affiliate links for the books on my site.

---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. I started off at the Strategy Plane:

#### Strategy Plane

The main goal for visitors is to find books that other users have upvoted and reviewed. This means that the home page has to list at least some of the books that are available in the site's database. It makes sense that this selection contains of the most upvoted books, if possible.

I also want visitors to come back. One way to encourage that is to have them register an account. Once they do that, they gain access to additional functionalities:
- the ability to upvote books.
- the ability to review books, and edit and delete their reviews.
- the ability to add, edit and delete books.
- access to their profile page, where they can find all their reviews, and edit or delete them. All the books they added are also listed, with options to edit and delete them. Als includes an option to delete their profile.

---

#### Scope Plane

The functional specifications of the site:
- A responsive website, mobile first design - with *at least* the following content:
    - a main page with a selection of the books available in the site's database. This needs:
        - a collection of books, with details like titles, authors, a blurb, a cover image, upvotes and reviews
        - a search bar
        - a way to change the sorting order: by title, by author, number of upvotes and number of reviews
    - a navbar, which changes if a user is logged in or not
    - a basic footer
    - a page to add new books: only visible when logged in
    - a way to edit or delete books: to prevent abuse this is only accessible to people who added the book, or admins. Only visible when logged in
    - a way to add reviews: only visible when logged in
    - a way to edit or delete reviews: to prevent abuse this is only accessible to people who added the review, or admins. Only visible when logged in
    - a page to view the logged in user's profile: only visible when logged in
    - a page to register: only visible when not logged in
    - a page to log in: only visible when not logged in
    - a link to log out: only visible when logged in

Content requirements:
- information about books, and reviews of said books
- users


---

#### Structure Plane
All pages should have the same navigation bar and footer:
- the navigation bar contains links to all the pages, as well as the home page. The content does change depending on login status.
- the footer contains copyright info.

<ins>The Home Page</ins>
- the site's logo
- cards containing books from the site's database, with buttons to get more info
- if the visitor is not logged in, at the bottom there will be a call to action to register for an account
- initially, buttons to edit or delete books, and to upvote and review them, were to be added to this page as well, but that would have led to a very cluttered interface

<ins>The New Book page</ins>
- a form for adding a new book to the database, including a cancel button

<ins>The New Review page</ins>
- a form for adding a new review of a book to the database, including a cancel button

<ins>The Edit Book page</ins>
- a form for editing a book in the database, including a delete button 

<ins>The Edit Review page</ins>
- a form for editing a review of a book in the database, including a delete button

<ins>The Profile page</ins>
- shows a user's profile, including their reviews and books
- provides functionality to delete or edit a review, delete or edit a book, and delete the profile. Deleting the profile will delete reviews and upvotes, but leave the books: these can then be adopted by other users

<ins>The Log In page</ins>
- a form for logging in, including a cancel button

<ins>The Register page</ins>
- a form for registering, including a cancel button 

---

#### Skeleton Plane

The navigation bar will be added to the top of every page and will always remain visible. There are links to all pages on this navbar, though some links are only visible if the user has logged in. 
On the left will be the logo, which when clicked upon will take the visitor back to the home page.

The active page is indicated with a line under the navigation item. When hovering over navigation items, the navigation item will be highlighted.

At the bottom of every page will be the same footer.

---

#### Surface Plane

Icons are sourced from Font Awesome, specifically version 5: https://fontawesome.com/v5/search. These icons add a bit of visual interest, but also add as indicators for the function of buttons.

The buttons are Bootstrap-style buttons: Bootstrap's design helps with a quicker understanding of functionality.

Bootstrap's cards functionality is used, as a quick way to add a certain style to the webapp.

<!-- TODO: Update wireframes: wait with making wireframes for admin portal -->
<ins>Wireframes</ins>
- [Home](readme-assets/home.png)
- [Home - tablet](readme-assets/home_tablet_view.png)
- [Home - mobile](readme-assets/home_mobile_view.png)
- [New Book](readme-assets/new_book.png)
- [New Book - tablet](readme-assets/new_book_tablet_view.png)
- [New Book - mobile](readme-assets/new_book_mobile_view.png)
- [New Review](readme-assets/new_review.png)
- [New Review - tablet](readme-assets/new_review_tablet_view.png)
- [New Review - mobile](readme-assets/new_review_mobile_view.png)
- [Edit Book](readme-assets/edit_book.png)
- [Edit Book - tablet](readme-assets/edit_book_tablet_view.png)
- [Edit Book - mobile](readme-assets/edit_book_mobile_view.png)
- [Edit Review](readme-assets/edit_review.png)
- [Edit Review - tablet](readme-assets/edit_review_tablet_view.png)
- [Edit Review - mobile](readme-assets/edit_review_mobile_view.png)
- [Profile](readme-assets/profile.png)
- [Profile - tablet](readme-assets/profile_tablet_view.png)
- [Profile - mobile](readme-assets/profile_mobile_view.png)
- [Login](readme-assets/login.png)
- [Login - tablet](readme-assets/login_tablet_view.png)
- [Login - mobile](readme-assets/login_mobile_view.png)
- [Register](readme-assets/register.png)
- [Register - tablet](readme-assets/register_tablet_view.png)
- [Register - mobile](readme-assets/register_mobile_view.png)

---

## Database Design

Bookable makes use of a MongoDB database. This means a non-relational or NoSQL database, where data is represented as documents. Whereas in a relational database you can have many tables, all with a little bit of data about an entity, this is less desired in MongoDB and other databases like it: join operations is something you want to avoid.
As such,I needed to decide on collections, which represent documents that I want to be able to retrieve from the database.

Looking at [Learn MongoDB The Hard Way](http://learnmongodbthehardway.com/schema/schemabasics/), I decided the following:
1. I'll have documents for users, in their own collection. These reference reviews using a foreign id, because reviews ~~are in buckets~~ are in their own collection.
1. I'll have documents for books, in their own collection.
1. The site mentions the example of a blog post with many comments, which is very similar to a book with many reviews. A book can have many reviews, but one review only belongs to one book. If I take growth into account, then I need to think about documents not reaching their max size of 16 MB. Each review added to a book document would grow that document, so I want to separate reviews from books. However, I also don't want a document for each and every review: very popular books might get thousands of reviews, which means that I need to tell MongoDB to retrieve every review from the database separately. So I'll use the bucketing mentioned on Learn MongoDB The Hard Way.
1. Documents for Authors, in their own collection. These are then linked to books using foreign ids, much like in a relational database. The same goes for books: I'll add foreign ids for the authors to the book documents.
1. I'll also have a collection for genres. This is because, as the site mentions, it's possible that many books belong to a particular genre. Embedding those books within the genre document would then mean that the maximum size of the document could be reached.

**Update 1** 
While talking to my mentor about my database design, he made some poignant observations:
- the genre of a book or the author of a book will not change. As such it makes more sense to have genre and author as properties of the book document. This information is static: a book will always have been written by the same author, and will always have the same genre: it will not suddenly change from horror to romance.

**Update 2**
Realizing that I was adding extra complexity to the database design, I decided to simplify it. A real-life webapp would make use of something along the lines of the above database design, in order to deal with potential hundreds or thousands of reviews, but right now, it's better to keep it simple. This meant not using the bucket concept for reviews, but having a collection for reviews, with each review being their own document.


So, in a JSON-ish structure, my current database design:

**books, collection of book documents:**
```
{
    _id: ObjectId("1"),
    title: "The Shining",
    authors: "Stephen King",
    genres: "horror, psychological horror",
    coverImageURL: "https://images-na.ssl-images-amazon.com/images/I/81w6JNKs5BS.jpg",
    blurb: "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister. And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.", 
    upvotes: 13,    
    affiliateLink: "https://fake.affiliate.link",    
    addedby: "richard",
    reviews: [
        0: ObjectId("review_1")
        1: ObjectId("review_2")
    ],
    upvotedBy: [
        0: "richard"
        1: "hank.schrader"
    ]
}
```

**reviews, collection ~~of buckets~~ of reviews:**
```
{
    _id: ObjectId("1"),
    booktitle: "The Shining",
    reviewtext: "Great!"
    addedByUser: "richard" 
}
```

**users, collection of user documents:**
```
{
    _id: ObjectId("1"),
    username: "richard",
    password: {passwordhash},
    booksAdded: [
        0: "book_id"
        1: "book_id"
    ],
    reviewsAdded: [
        0: ObjectId("review_1")
        1: ObjectId("review_2")
    ],
    booksUpvoted: [
        0: "book_id"
        1: "book_id"
    ]    
}
```

**genres, collection of genre documents:**
```
{
    _id: ObjectId("1"),
    genreName: "fantasy" 
}
```



---

## Features

### Existing Features
- a home page with cards representing books on it. The cards contain title, author and genre of each book, as well as cover image. The number of upvotes is also indicated, and there is a button the user can click on to get more info about the book.
- a page template for each book, that fills the page with the book's details, and adds buttons to add, edit or delete reviews, and edit or delete the book, depending on the user who is logged in. Upvoting is also possible for logged in users.
- a page to add a new book, that asks for all the necessary info to add a book to the database.
- a profile page, from where the logged in user can edit or delete the books and reviews they added, or even delete their entire profile.
- register and login/logout functionality.
- when a new book is added, a proof of concept affiliate link is created and added to the book document. This is used to generate a button which takes the user to an Amazon search page.
- an admin portal, where the admin can delete and edit books, and delete reviews
---

### Features Left to Implement
IMPROVE: expand admin portal
- make it possible to delete users, and add and delete categories on the admin page

---

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): provides the content and structure of the site.
- [CSS3](https://en.wikipedia.org/wiki/CSS3): provides the formatting, layout and styling of the site.
- [Bootstrap](https://getbootstrap.com/): provides a popular CSS framework with many custom elements to quickly bootstrap a site. I've used Bootstrap 4.6.
- [Python3](https://www.python.org/): the backend of the webapp.
- [Flask](https://flask.palletsprojects.com/): a popular micro web framework for Python.
- [MongoDB](https://www.mongodb.com/): a document-oriented database program.
- [Selenium](https://selenium.dev/): software for automating and testing browser interactions. Used in this project to test functions of the webapp.
- [FontAwesome](https://fontawesome.com/): provides several icons I've used on the site.
- [Visual Studio Code](https://code.visualstudio.com/): a free IDE with enough features to be useful but not so many features as to confuse you.
- [GitHub](https://github.com): for hosting the git repository.
- [git](https://git-scm.com/): as one of the most popular source code management tools.
- [Heroku](https://heroku.com/): a Platform as a Service, for hosting the webapp.
- [Balsamiq](https://balsamiq.com): for creating wireframes of all the pages.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): for quick debugging and testing of HTML and CSS. 
- [Am I Responsive?](http://ami.responsivedesign.is/): to generate screenshots of the site at various viewpoints, indicating responsiveness.
- [EyeDropper](https://eyedropper.org/): to pick colours from an image.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): an automated tool in Chrome DevTools that audits for performance, accessibility, progressive web apps, SEO and more.
- [JSHint](https://jshint.com/): a linter for JavaScript, to help identify coding problems
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [ScreenToGif](https://www.screentogif.com/): to make screen recordings and turn them into gifs.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.
- TODO: Add Python tools

---

## Responsiveness of Pages

These screenshots indicate the responsiveness of the pages on various screens. Pages that require a login are not included.

![Responsive /get-books](readme-assets\responsive_home_page.png?raw=true "Get Books")

![Responsive /get_book](readme-assets\responsive_get_book.png?raw=true "Get Book")

![Responsive /login](readme-assets\responsive_login.png?raw=true "Login")

![Responsive /register](readme-assets\responsive_register.png?raw=true "Register")


---

## Testing

<ins>Tests for Readme.md:</ins>
- :heavy_check_mark: Realizing that I was doing a lot of manual work to check all the links, I googled for an automated solution. I found one using a Github Action Workflow. This Workflow checks all the links in markdown files. The action does generate an error: a 403 status for the Pexels website. This error is probably due to a blacklist, because I ran the workflow too often.
<br/>

<ins>Automated tests</ins>
Selenium
pip install selenium
install chromedriver for selenium --> download correct one for your chrome version: https://chromedriver.chromium.org/downloads
TODO: Write out how to do automated tests
I've written some automatic tests. These can be found in selenium_test.py and test_app.py. All tests pass:
- [Output pytest](readme-assets/output_pytest.png)
  
Functionality tested:
test_app.py tests browsing to different pages: /, /get_books, /register and /login:
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /  THEN check for status code 200
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /    THEN check for <div class="card  in the returned data: this indicates that the template has been filled with data from the db
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /  get_books THEN check for status code 200
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /get_books THEN check for '<div class="card' in the returned data: this indicates that the template has been filled with data from the db
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /register THEN check for status code 200
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /register THEN check the h1 element with class "card-title" and text "Register Your Account"
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /login THEN check for status code 200
- :heavy_check_mark: GIVEN a running Flask app WHEN the client browses to /login THEN check the h1 element with class "card-title" and text "Log In To Your Account"

selenium_test.py tests several user interactions:
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client browses to /
THEN check the title is "Bookable"
- :heavy_check_mark: GIVEN an existing username WHEN the client tries to register the existing username THEN check for the "Sorry, your username has already been taken!" flash message
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the brand nav THEN check the url ends with get_books
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the All Books button THEN check the url ends with get_books
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the Log In nav THEN check the url ends with login
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the Register nav THEN check the url ends with register
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the Log In link at the bottom of the Register page THEN check the url ends with login
- :heavy_check_mark: GIVEN a running Heroku app WHEN the client clicks the Register link at the bottom of the Log In page THEN check the url ends with register
- :heavy_check_mark: GIVEN a running Heroku app WHEN the user registers THEN check that the user is sent to its profile page
- :heavy_check_mark: GIVEN a running Heroku app WHEN the logged in user logs out THEN check that the user is sent back to the login page with the message that the user has been logged out
- :heavy_check_mark: GIVEN a running Heroku app WHEN the user is logged out THEN check that the user only sees navs for All Books, Log In and Register
- :heavy_check_mark: GIVEN a running Heroku app WHEN the user logs in THEN check that the user is sent to the profile page with a flash message
- :heavy_check_mark: GIVEN a running Heroku app WHEN the user is logged in THEN check that the user only sees navs for All Books, Add Book, Profile and Log Out
- :heavy_check_mark: GIVEN a running Heroku app WHEN the user deletes their profile THEN check that the user is sent to the home page with a flash message



<ins>Manual tests</ins>
TODO: Add manual tests, for the things that I am not testing automatically.

[ ] Test getting more info about a book: do I get info about the right book?
[ ] Test search: I should be able to search titles, authors and genres
[ ] Test getting more info about a book when logged in:
    - I should be able to review a book --> this should be disabled if I already reviewed the book
    - I should be able to upvote a book --> this should be disabled if I already upvoted the book
    - if I added the book, I should be able to edit or delete it
    - if the book has no current "owner", I should be able to adopt it
[ ] Test adding a book
[ ] Test adding a review
[ ] Test editing and deleting from profile page
[ ] Test deleting profile and seeing what happens to reviews, books and upvotes




<ins>Code validation:</ins>
1. [HTML validation](https://validator.w3.org/nu/)
2. [CSS validation](https://jigsaw.w3.org/css-validator/)
3. [VS Code JSHint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint)
4. [Python Validation](http://pep8online.com/)
TODO: Add validation results

### Notable Bugs

### Problems

---

## Deployment
TODO: Write how to deploy to Heroku

### Run locally

1. If you want to run the project locally 

pip install -r requirements.txt to install required modules

To activate Flash virtual environment:
& "g:/My Drive/A-B-C/Coding/Github 
Repos/code-institute-ms3-backend/venv/Scripts/Activate.ps1"

run the app: python app.py


pip3 install -r requirements.txt


---

## Credits

### Inspiration
The main inspiration for this webapp was one of the project suggestions from Code Institute: to make a webapp where users can add, review and upvote books, together with other CRUD functionality.

### Content
Book content was sourced from [Goodreads](https://www.goodreads.com/)

### Media
Book cover images were sourced from [Goodreads](https://www.goodreads.com/) as well.

### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). 
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, and [Stackoverflow](https://stackoverflow.com/) and [MDN](https://developer.mozilla.org/en-US/) for helping with finding solutions to coding problems, like animating the pictures in sequence instead of all at once.
- My wife, Elizabeth Lane, for supporting me during this coding course.