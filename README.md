<!-- FIXME: Images in the readme on Github are not working -->
<!-- FIXME: Go through readme.md online, to make sure everything is displaying correctly -->


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
- Returning User Goals
    - As a Returning User, I want to find reviews and recommendations for books.
    - As a Returning User, I want to be able to quickly see all my reviews.
    - As a Returning User, I want to be able to create, update and delete reviews, and create, update and delete books.
    - As a Returning User, if I like a book, I want to be able to buy it, ideally via a link on the site.
- Site Owner Goals
    - As the site owner, I want to get recommendations for new books by crowdsourcing book reviews. The users of my site add reviews to books, which allows me to find new books I might like.
    - As the site owner, I want to earn money using affiliate links for the books on my site.

Screenshots that fulfill these user stories:

[Screenshot](readme-assets/screenshot_first_time_visitor.png)

[Screenshot](readme-assets/screenshot_review.png)

I see a couple of books with buttons to click for more information, I see upvotes, I see a link to login and a link to register, and a search function. This indicates that this site is about books and reviews of books. I can search for books, and if I register I can probably add books myself. If I get more info about a book, I see reviews as well. There is also a button that takes me to Amazon, where I can buy the book if I want to.

[Screenshot](readme-assets/screenshot_profile.png)

If I'm logged in, I have a link to my profile in the navbar, and if I go there I see a list of all the books and reviews I've added. I can edit and delete those as well. I can also add a book through a link in the navbar.

[Screenshot](readme-assets/screenshot_add_book.png)

[Screenshot](readme-assets/screenshot_add_review.png)

[Screenshot](readme-assets/screenshot_edit_book.png)

[Screenshot](readme-assets/screenshot_edit_review.png)

[Screenshot](readme-assets/screenshot_profile.png)

As the site owner, I know all books added get a button added as well, that allows visitors to buy books, which will earn me money. And I can look at the reviews and upvotes to find books I might like.


---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. I started off at the Strategy Plane:

#### Strategy Plane

The main goal for visitors is to find books that other users have upvoted and reviewed. This means that the home page has to list at least some of the books that are available in the site's database. It makes sense that this selection contains of the most upvoted books, if possible.

I also want visitors to come back. One way to encourage that is to have them register an account. Once they do that, they gain access to additional functionalities:
- the ability to upvote books.
- the ability to review books, and edit and delete their reviews.
- the ability to add, edit and delete books.
- access to their profile page, where they can find all their reviews, and edit or delete them. All the books they added are also listed, with options to edit and delete them. Also includes an option to delete their profile.


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
- a form for editing a book in the database, including a cancel button 

<ins>The Edit Review page</ins>
- a form for editing a review of a book in the database, including a cancel button

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

The active page is indicated with a different font color for the navigation item. When hovering over navigation items, the navigation item will be highlighted.

At the bottom of every page will be the same footer.


---

#### Surface Plane

Icons are sourced from Font Awesome, specifically version 5: https://fontawesome.com/v5/search. These icons add a bit of visual interest, but also add as indicators for the function of buttons.

The buttons are Bootstrap-style buttons: Bootstrap's design helps with a quicker understanding of functionality.

Bootstrap's cards functionality is used, as a quick way to add a certain style to the webapp.


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
- [Admin Portal](readme-assets/admin_portal.png)
- [Admin Portal - tablet](readme-assets/admin_portal_tablet_view.png)
- [Admin Portal - mobile](readme-assets/admin_portal_mobile_view.png)


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
    genre: "horror",
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
- make it possible to delete users, and add and delete categories on the admin page
- have the backend code check if the combination of both title and author are already in the database, to detect possible duplicates
- have a way to sort the books on the main page
- add a downvote functionality
- add a way for users to remove their upvotes
- redirect the admin directly to the admin portal, instead of to their profile
- allow the admin to edit all books from the book page itself, like owners of the book
- disable upvoting for the admin on the book page
- disable the Buy button for the admin on the book page
- disable the Review button for the admin on the book page
- use Flask for error handling. Have custom error pages - with inline CSS in case style.css can't be loaded - to handle 404 and 500 errors for instance.
- have Python error handle the input of genres: right now the genres are exposed to the user via HTML, which means that the user can edit the HTML and for instance input genres that are not in the database. When the user submits a form, Python should check the genre input, to see if it matches the genres in the database.
- using [Flask-login](https://flask-login.readthedocs.io/en/latest/?msclkid=377a241fa69a11ec912bffef67d76419) module to deal with login and session management


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
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): an automated tool in Chrome DevTools that audits for performance, accessibility, progressive web apps, SEO and more.
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): to keep track of todos, bugs, things that need to be fixed and such in my project.
- [autopep8](https://pypi.org/project/autopep8/): a Python package that helps with formatting Python code according to PEP8.


---

## Responsiveness of Pages

These screenshots indicate the responsiveness of the pages on various screens. Pages that require a login are not included.

**Home page**

![Responsive /get-books](readme-assets/responsive_home_page.png?raw=true "Get Books")

**Book page**

![Responsive /get_book](readme-assets/responsive_get_book.png?raw=true "Get Book")

**Login page**

![Responsive /login](readme-assets/responsive_login.png?raw=true "Login")

**Register page**

![Responsive /register](readme-assets/responsive_register.png?raw=true "Register")


---

## Testing

<ins>Tests for Readme.md:</ins>
- :heavy_check_mark: Realizing that I was doing a lot of manual work to check all the links, I googled for an automated solution. I found one using a Github Action Workflow. This Workflow checks all the links in markdown files.


<ins>Automated tests</ins>

I've tried doing some automated testing of the website. These automated tests are run against the actual webapp, as hosted on Heroku.

In order to run the tests yourself, do the following:
- pytest is already installed via requirements.txt
- Install selenium for Python: 
  
  ```pip install selenium```

  
- Tests were writting using the Chrome Driver for Selenium. This automates Google Chrome and interactions with Chrome. Download the correct one for your Chrome version: https://chromedriver.chromium.org/downloads

- After this you can run all tests using:

```python -m pytest``` 

- Use the following if you want more verbose logging:

```python -m pytest -v``` 


The tests can be found in selenium_test.py and test_app.py, in the test folder. All tests pass: 

[Output pytest](readme-assets/output_pytest.png)
  
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

Manually testing the webapp is quite involved: things change depending on whether a visitor is logged in, has added a book, reviewed a book or upvoted a book. Some functionality has already been tested by automatic tests: things like whether a visitor who is not logged in can only see certain nav items in the navbar, whether a logged in user sees other nav items and even what happens when you register or login and logout. Below are more elaborate tests:

**Search functionality**
| Tests for not logged in visitor | Expected |Passed |
| :------------- |:-------------| :-----:|
| Visitor uses the search functionality to search for a title | Books with the search term in the title field are displayed | &#9745; |
| Visitor uses the search functionality to search for an author | Books with the search term in the author field are displayed | &#9745; |
| Visitor uses the search functionality to search for a genre | Books with the search term in the genre field are displayed | &#9745; |



| Tests for logged in user | Expected |Passed |
| :------------- |:-------------| :-----:|
| User uses the search functionality to search for a title | Books with the search term in the title field are displayed | &#9745; |
| User uses the search functionality to search for an author | Books with the search term in the author field are displayed | &#9745; |
| User uses the search functionality to search for a genre | Books with the search term in the genre field are displayed | &#9745; |



**"More About This book" functionality**
| Tests for not logged in visitor | Expected |Passed |
| :------------- |:-------------| :-----:|
| Visitor clicks the "More About This Book" button for a book | More info about the correct book is displayed | &#9745; |
| Visitor clicks the "More About This Book" button for a book | Upvote button is disabled | &#9745; |
| Visitor clicks the "More About This Book" button for a book | Either reviews are displayed, or a text that there are no reviews | &#9745; |
| Visitor clicks the "More About This Book" button for a book | The Buy button is displayed  | &#9745; |
| Visitor clicks the "More About This Book" button for a book | There are no buttons to edit or delete the book, or add a review  | &#9745; |


| Tests for logged in user | Expected |Passed |
| :------------- |:-------------| :-----:|
| User clicks the "More About This Book" button for a book | More info about the correct book is displayed | &#9745; |
| User clicks the "More About This Book" button for a book | Upvote button is enabled | &#9745; |
| User clicks the upvote button | Upvote button is disabled and the upvote number is increased by 1. The page reloads with a flash message that the book has been upvoted | &#9745; |
| After upvoting a book, the user goes back to the main page | The number of upvotes for the book just upvoted has increased | &#9745; |
| User clicks the "More About This Book" button for a book | Either reviews are displayed, or a text that there are no reviews | &#9745; |
| User clicks the "More About This Book" button for a book | The Buy button is displayed  | &#9745; |
| User clicks the "More About This Book" button for a book | The "Review Book" button is displayed  | &#9745; |



**Review functionalities: Create, Read, Update, Delete**
| Tests for logged in user | Expected |Passed |
| :------------- |:-------------| :-----:|
| User clicks the "Review Book" button for a book | User is taken to a new page, with a form where they can add a review to the book. The book's title has been populated | &#9745; |
| User cancels submitting a review | User is taken back to the book they came from | &#9745; |
| User submits a review via the form | User is taken back to home page, with a flash message that the review has been added | &#9745; |
| User clicks the "More About This Book" button for the book they just reviewed | Their review is populated, and "Review Book" button has been disabled | &#9745; |
| User clicks the "Profile" button in the navbar | The review they added is visible on their profile page, with "Edit" and "Delete" buttons | &#9745; |
| User clicks the "Edit" button on the profile page for the review they added | The user is taken to a page with a form to edit their review, with fields prepopulated | &#9745; |
| User clicks the "Cancel" button on the edit review form | The user is taken back to the home page | &#9745; |
| User clicks the "Edit" button on the edit review form, after changing their review | The user is taken back to the home page, with a flash message that the review has been updated | &#9745; |
| User clicks the "More About This Book" button for the book they just changed their review for | More info about the book is displayed, including the changed review | &#9745; |
| User goes to their profile page and clicks the "Delete" button for a review they added | A modal popups asking the user to confirm they want to delete the review: the modal populates with the title of the book | &#9745; |
| User clicks on the "Cancel" button of the "Delete review" modal  | The modal disappears and the user is back on their profile page | &#9745; |
| User clicks on the "Delete" button of the "Delete review" modal  | The modal disappears and the user is taken back to the home page, with a flash message that the review has been deleted | &#9745; |
| User clicks the "More About This Book" button for the book they just deleted the review for | Their review is gone, and "Review Book" button is once more enabled | &#9745; |
| User goes to their profile page | The review they just deleted is no longer visible on the profile page | &#9745; |



**Book functionalities: Create, Read, Update, Delete**
| Tests for logged in user | Expected |Passed |
| :------------- |:-------------| :-----:|
| User clicks the "Add Book" button in the navbar | User is taken to a new page, where fields are populated to add a new book | &#9745; |
| User fills in a booktitle that is already in the database in the Add Book form | User is redirected to the Add book form, with a flash message that the book is already in the database* | &#9745; |
| User fills in a link for the cover image that is not a valid image | The form indicates to fill in a valid url | &#9745; |
| User fills in the form for adding a book and submits | User is taken back to the main page with a flash message that the book has been added | &#9745; |
| User clicks the "More About This Book" button for the book they just added | User is taken to page with the info for the book they just added, and the buttons "Delete Book" and "Edit Book" are visible | &#9745; |
| User goes to their profile page | The profile page is populated with the book they just added, including "Edit" and "Delete" buttons | &#9745; |
| User clicks the "Edit Book" button  | User is taken to a form with the info for the book prefilled, ready for editing | &#9745; |
| User cancels editing the book  | User is taken back to home page | &#9745; |
| User edits the book information and submits the form  | User is taken back to home page with flash message that the book has been updated | &#9745; |
| User clicks the "More About This Book" button for the book they just updated  | The edits are visible on the page | &#9745; |
| User edits a book using the "Edit" button on their profile page  | Works like editing from the book page | &#9745; |
| User clicks the "Delete book" button on the page for a book they added  | A modal pop ups, confirming that the user wants to delete the book | &#9745; |
| User clicks the "Cancel delete" button on the modal  | The modal disappears and they are back on the book page | &#9745; |
| User clicks the "Confirm delete" button on the modal  | The user is taken to the home page, with a flash message that the book has been deleted from the database. The book is no longer visible | &#9745; |
| User goes to their profile page  | The book they deleted is no longer listed on the page | &#9745; |
| User deletes a book using the "Delete" button on their profile page | Works like deleting from the book page  | &#9745; |
| Another logged in user clicks the "More About This Book" button for a book added by a user who deleted their profile  | The "Adopt Book?" button is now visible | &#9745; |
| The user clicks the "Adopt Book?" button  | The page is reloaded. A flash message stating that the book has been adopted appears, and the user now has Edit and Delete buttons for the book | &#9745; |
* This is intentional, but can be improved: it is possible for two different books to have the same title.



**Profile functionalities: Create, Read, Update, Delete** 
Several of these functionalities have already been tested: when reviews or books are added or deleted, this is updated on the profile page. Creating a profile has also been tested already, by the automatic tests. Below are the few tests remaining.

| Tests for logged in user | Expected |Passed |
| :------------- |:-------------| :-----:|
| User clicks on "Delete Profile" button at the bottom of their profile card  | A modal pop ups, confirming that the user wants to delete their profile | &#9745; |
| User clicks the "Cancel delete" button on the modal  | The modal disappears and they are back on their profile page | &#9745; |
| User clicks the "Confirm delete" button on the modal  | The modal disappears and the user is taken back to the home page, with a flash message that their profile has been deleted. The session has also been logged out. | &#9745; |
| User clicks the "More About This Book" button for a book they've upvoted and/or reviewed  | The upvote and/or review is gone | &#9745; |



**Admin functionalities: Create, Read, Update, Delete**
| Tests for admin | Expected |Passed | 
| :------------- |:-------------| :-----:|
| The admin logs in  | The "Admin Portal" navbar item is visible  | &#9745; |
| The admin clicks on the "Admin Portal" navbar item  | The admin is taken to the Admin Portal page, which is populated with all books, reviews, and users in the database  | &#9745; |
| The admin clicks on the "Edit" button for a book on the Admin Portal page | The admin is taken to the Edit Book page, which is prepopulated with the right data for the book to be edited, much like a normal user  | &#9745; |
| The admin clicks on the "Cancel" button on the Edit Book page  | The admin is taken to the home page  | &#9745; |
| The admin changes information on the Edit book page and clicks the "Edit Book" button  | The admin is taken to the home page, with a flash message that the book has been updated  | &#9745; |
| The admin clicks the "More About This Book" button for the book they just edited  | The admin is taken to the book page, and the data they changed is populated  | &#9745; |
| The admin clicks the "Delete" button for a book from the Admin Portal  | The admin is taken to the home page, with a flash message that the book has been deleted | &#9745; |
| The admin goes back to the Admin Portal  | The book that has just been deleted is no longer in the list of books | &#9745; |
| The admin clicks the "Delete" button for a review on the Admin Portal page | The admin is taken to the home page, with a flash message that the review has been deleted  | &#9745; |
| The admin goes back to the Admin Portal | The review that has just been deleted is no longer in the list of books | &#9745; |


<ins>Code validation:</ins> 

1. [HTML validation](https://validator.w3.org/nu/)
Only pages that can be accessed without logging in can be validated:

- http://code-institute-ms3-book-review.herokuapp.com/ and http://code-institute-ms3-book-review.herokuapp.com/get_books: 5 warnings and 9 errors. See Problems section for fixes.
- http://code-institute-ms3-book-review.herokuapp.com/get_book/62335798c7113074d825718d: this page is used as the page to be validated for all pages with book information, as these are based on a template: 1 warning found, pertaining to a section missing a heading. However, this section is only visible when there is a flash message, and as such needs no heading.
- http://code-institute-ms3-book-review.herokuapp.com/login: 1 warning found, pertaining to a section missing a heading. However, this section is only visible when there is a flash message, and as such needs no heading.
- http://code-institute-ms3-book-review.herokuapp.com/register: 1 warning found, pertaining to a section missing a heading. However, this section is only visible when there is a flash message, and as such needs no heading.


2. [CSS validation](https://jigsaw.w3.org/css-validator/)
- 728 warnings found in bootstrap.min.css and https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css, which I am not going to fix.


3. [Python Validation](http://pep8online.com/)
The results for the first validation run: 

[First validation](readme-assets/result_20220318_085319.txt) 

A lot of the problems found are about formatting problems: lines too long, trailing whitespaces, blank lines containing whitespaces. To try and fix this I used autopep8 - which I first installed using ```pip install -U autopep8```.

Running autopep8 fixed a lot of the problems: 

[Second validation](readme-assets/result_20220318_090139.txt) 

Manually fixed a lot of the problems with lines too long: 

[Third validation](readme-assets/result_20220318_092703.txt)

Fixed the last of the lines too long: 

[Fourth validation](readme-assets/result_20220318_093758.txt)

The remaining validation errors had to do with writing comparisons in a non-Python way, these have been fixed: 

[Fifth validation](readme-assets/result_20220318_094408.txt)

### Notable Bugs

While working on the project, there were no notable bugs that required a lot of troubleshooting found. Most bugs were a result of me forgetting that there are more places where certain data is registered in the database than just one field on a document.


### Problems

HTML validation http://code-institute-ms3-book-review.herokuapp.com/ and http://code-institute-ms3-book-review.herokuapp.com/get_books
1 warning for a section missing a heading. This section is used for displaying flash messages, and needs no heading: it is not always visible. 

4 warnings for the first appearance of an element ID: id="main-page-card-footer-div">. This id is used in the books.html template. After searching if this id was referenced elsewhere - in style.css or the tests - I found no references. The ID has been deleted.

4 of the 9 errors found also had to do with this id: these errors indicated that a duplicate ID had been found: this has been resolved by deleting the ID.

5 errors were found mentioning a stray end tag </a>. I must have missed deleting this in a previous edit, and it showed up 5 times, once for each book in the database. The stray end tag has been deleted.

---

## Deployment
The project has been deployed to Heroku. If you want to do the same:
1. You need a database for the webapp to store its data. This should be a MongoDB database. It will have four collections: books, reviews, users and genres. Only genres already needs data: without any documents for genres in this collection, the list to pick a genre when adding or editing a book will not populate.
1. Fork the repository to your own GitHub: https://github.com/RicardoAzuul/code-institute-ms3-backend.
1. Log in to Heroku (www.heroku.com) - or register if you don't have an account yet.
1. In the Heroku dashboard, click the New button in the top right corner and create a new app.
1. Give your new app a name and choose a region. The name has to be unique within Heroku.
1. On the page for your new Heroku app, go to Deployment method and choose "Connect to GitHub". If you haven't connected your GitHub account to Heroku yet, you will be able to do so now.
1. Choose the forked repository of this project from your own GitHub account.
1. If you want, you can enable Automatic Deploys here: whenever you perform a push to your GitHub repository, the Heroku app can redeploy. Otherwise you can deploy manually. Heroku will use the PROCFILE and requirements.txt to install dependencies and build the app.
1. You will also have to set some Config Vars in the Settings section of your Heroku app. There are 6 Config Vars:
   1. IP: set to 0.0.0.0
   2. MONGO_DBNAME: enter the name of your MongoDB here, which stores the books, reviews, genres and users.
   3. MONGO_URI: enter the uri to your MongoDB here.
   4. PORT: set to 5000.
   5. SECRET_KEY: enter the secret key needed for the flash package to display flash messages.
   6. DEBUG: set to False

### Run locally
If you want to run the project locally:
1. First, fork the repository to your own GitHub: https://github.com/RicardoAzuul/code-institute-ms3-backend.
1. Clone the forked repository to your own machine.
1. Install Python 3.9.10: https://www.python.org/downloads/release/python-3910/?msclkid=cffbdc88a5f911ecb325513f7d98b51f 
1. From the terminal, run the below to install required modules:
  ``` pip3 install -r requirements.txt ```
1. You will need to create an env.py file (or another form of environment file) for running the app locally. The content of this file:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "[secret key for use with flash package]")
os.environ.setdefault("MONGO_URI", "[uri to your MongoDB]")
os.environ.setdefault("MONGO_DBNAME", "[name of your MongoDB database")
os.environ.setdefault("DEBUG", "True")
```
1. To activate the Flask virtual environment, run one of the activate scripts from the venv/Scripts directory, depending on your environment.
1. To run the app:
   
   ``` python app.py ```

1. This will run the Flask app locally, you can then browse to http://192.168.1.68:5000/ to interact with the app.


---

## Credits

### Inspiration
The main inspiration for this webapp was one of the project suggestions from Code Institute: to make a webapp where users can add, review and upvote books, together with other CRUD functionality.

### Content
Book content was sourced from [Goodreads](https://www.goodreads.com/)

### Media
Book cover images were sourced from [Goodreads](https://www.goodreads.com/) as well.

### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). He pointed out for instance that it would be a good idea to add a decorator to functions that should have a logged in user.
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, and [Stackoverflow](https://stackoverflow.com/) for helping with finding solutions to coding problems, like animating the pictures in sequence instead of all at once. The documentation for MongoDB (https://docs.mongodb.com/) and Jinja (https://jinja.palletsprojects.com/) were also very helpful.
- My wife, Elizabeth Lane, for supporting me during this coding course.
