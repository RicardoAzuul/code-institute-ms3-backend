# Bookable
A book review and recommendation site, using MongoDB, Python, Flask, HTML, CSS and JavaScript

Must haves for this project:
- a way for users to view books, including a cover image, number of upvotes and reviews
- a way for users to edit or delete books
- a way for users to add, edit or delete reviews
- a profile page for a logged in user, with all their reviews
- a login and a register page

Nice to have: 
- the editing and adding functionality is done using modals, so not so many separate pages are needed.


To see the site in action, visit [https://code-institute-ms3-book-review.herokuapp.com/](https://code-institute-ms3-book-review.herokuapp.com/)

---

## Table of Contents
1. [UI and UX](#ui-and-ux)
    1. [User Stories](#user-stories)
    1. [The 5 Planes of Design](#the-5-planes-of-design)
        1. [Strategy Plane](#strategy-plane)
        2. [Scope Plane](#scope-plane)
        3. [Structure Plane](#structure-plane)
        4. [Skeleton Plane](#skeleton-plane)
        5. [Surface Plane](#surface-plane)
1. [Database Design](#Database-design)
1. [Features](#Features)
    1. [Existing Features](#existing-features)
    1. [Features Left To Implement](#features-left-to-implement)
1. [Technologies Used](#technologies-used)
1. [Responsiveness of Pages](#responsiveness-of-pages)
1. [Testing](#Testing)
    1. [Notable Bugs](#notable-bugs)
1. [Deployment](#Deployment)
1. [Credits](#Credits)
    1. [Content](#Content)
    2. [Media](#Media)
    3. [Acknowledgements](#Acknowledgements)

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

The main goal for visitors is to find books that other users have upvoted and reviewed. This means that the home page has to list at least some of the books that are available in the site's database. It makes sense that this selection contains of the most upvoted books.

I also want visitors to come back. One way to encourage that is to have them register an account. Once they do that, they gain access to additional functionalities:
- the ability to upvote books.
- the ability to review books, and edit and delete their reviews.
- the ability to add, edit and delete books.
- access to their profile page, where they can find all their reviews, and edit or delete them. Als includes an option to delete all their reviews or even their profile.

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
    - a page to edit or delete books: to prevent abuse this is only accessible to people who added the book, or admins. Only visible when logged in
    - a page to add reviews: only visible when logged in
    - a page to edit or delete reviews: to prevent abuse this is only accessible to people who added the review, or admins. Only visible when logged in
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
- tiles containing various books from the site's database
    - if the visitor is logged in, there should be buttons visible on the book tiles in order to edit or delete books, and to upvote and review them

<ins>The New Book page</ins>
- a form for adding a new book to the database, including a cancel button

<ins>The New Review page</ins>
- a form for adding a new review of a book to the database, including a cancel button

<ins>The Edit Book page</ins>
- a form for editing a book in the database, including a delete button 

<ins>The Edit Review page</ins>
- a form for editing a review of a book in the database, including a delete button

<ins>The Profile page</ins>
- shows a user's profile, including their reviews.
- provides functionality to delete or edit a review, delete all reviews and delete the profile

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

The icons are sourced from Font Awesome.

The buttons are Bootstrap-style buttons: Bootstrap's design helps with a quicker understanding of functionality.

Fonts are sourced from Google Fonts. 

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
1. I'll have documents for users, in their own collection. These reference reviews using a foreign id, because reviews are in buckets.
1. I'll have documents for books, in their own collection.
1. The site mentions the example of a blog post with many comments, which is very similar to a book with many reviews. A book can have many reviews, but one review only belongs to one book. If I take growth into account, then I need to think about documents not reaching their max size of 16 MB. Each review added to a book document would grow that document, so I want to separate reviews from books. However, I also don't want a document for each and every review: very popular books might get thousands of reviews, which means that I need to tell MongoDB to retrieve every review from the database separately. So I'll use the bucketing mentioned on Learn MongoDB The Hard Way.
1. Documents for Authors, in their own collection. These are then linked to books using foreign id's, much like in a relational database. The same goes for books: I'll add foreign ids for the authors to the book documents.
1. I'll also have a collection for genres. This is because, as the site mentions, it's possible that many books belong to a particular genre. Embedding those books within the genre document would then mean that the maximum size of the document could be reached.

**Update** 
After talking to my mentor about my database design, he made some poignant observations:
- the genre of a book or the author of a book will not change. As such it makes more sense to have genre and author as properties of the book document. This information is static: a book will always have been written by the same author, and will always have the same genre: it will not suddenly change from horror to romance.

So, in a JSON-ish structure:

~~authors, collection of author documents:~~
```
{
    _id: 1,
    name: "Stephen King"
    books: [1]
}
```

books, collection of book documents:
```
{
    _id: 1,
    title: "The Shining",
    coverImageURL: "https://images-na.ssl-images-amazon.com/images/I/81w6JNKs5BS.jpg",
    blurb: "Jack Torrance's new job at the Overlook Hotel is the perfect chance for a fresh start. As the off-season caretaker at the atmospheric old hotel, he'll have plenty of time to spend reconnecting with his family and working on his writing. But as the harsh winter weather sets in, the idyllic location feels ever more remote...and more sinister. And the only one to notice the strange and terrible forces gathering around the Overlook is Danny Torrance, a uniquely gifted five-year-old.", 
    upvotes: 13,
    genres: ["horror", "psychological horror"]
    affiliatieLink: "https://fake.affiliate.link",
    authors: Stephen King
}
```

~~genres, collection of genre documents:~~
```
{
    _id: 1,
    name: "horror"
}
```

reviews, collection of buckets of reviews:
```
{
    bookId: 1,
    page: 1,
    count: 10,
    reviews: [{
        _id: 1,
        name: "Hank Schrader",
        review: "The Shining is a classic."
    },
    {
        _id: 2,
        name: "Bob Schwartz",
        review: "Easily King's best."  
    }]
}
```

users, collection of user documents:
```
{
    _id: 1.
    name: "Hank Schrader",
    reviews: [1]
}
```


---

## Features

### Existing Features

---

### Features Left to Implement
Create a web application that allows users to upload details of books, including book name, author name, link to cover image and any other relevant fields. Allow users to write comments about any book and upvote it.
Create the backend code and frontend form(s) to allow users to add new books and reviews to the site, edit them and delete them.
Add a link such as the following to each book page, such that you could conceivably earn money from people looking to buy the book: https://www.amazon.com/s?tag=faketag&k=alice+in+wonderland Note that we do not actually encourage you to create an affiliate link, but rather want to demonstrate how this could work. Instead, for this project, we encourage you to just keep the tag value as something fake. Also, note that in general it's better to link directly to the book's page in the store, but that's a bit more difficult.

---

## Technologies Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5): provides the content and structure of the site.
- [CSS3](https://en.wikipedia.org/wiki/CSS3): provides the formatting, layout and styling of the site.
- [Bootstrap](https://getbootstrap.com/): provides a popular CSS framework with many custom elements to quickly bootstrap a site. I've used Bootstrap 4.6.
- Python
- Flask
- MongoDB
- [FontAwesome](https://fontawesome.com/): provides several icons I've used on the site.
- [Visual Studio Code](https://code.visualstudio.com/): a free IDE with enough features to be useful but not so many features as to confuse you.
- [Live Server](https://ritwickdey.github.io/vscode-live-server/): a Visual Studio Code extension that allows you to run your site on your local machine, for quick debugging, testing and developing.
- [GitHub](https://github.com): for hosting the git repository.
- [git](https://git-scm.com/): as one of the most popular source code management tools.
- Heroku: for hosting the webapp.
- [Balsamiq](https://balsamiq.com): for creating wireframes of all the pages.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): for quick debugging and testing of HTML and CSS. 
- [Am I Responsive?](http://ami.responsivedesign.is/): to generate screenshots of the site at various viewpoints, indicating responsiveness.
- [EyeDropper](https://eyedropper.org/): to pick colours from an image.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): an automated tool in Chrome DevTools that audits for performance, accessibility, progressive web apps, SEO and more.
- [JSHint](https://jshint.com/): a linter for JavaScript, to help identify coding problems
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [ScreenToGif](https://www.screentogif.com/): to make screen recordings and turn them into gifs.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.

---

## Responsiveness of Pages

These screenshots indicate the responsiveness of the pages on various screens.

---

## Testing

<ins>Tests for Readme.md:</ins>
- :heavy_check_mark: Realizing that I was doing a lot of manual work to check all the links, I googled for an automated solution. I found one using a Github Action Workflow. This Workflow checks all the links in markdown files. The action does generate an error: a 403 status for the Pexels website. This error is probably due to a blacklist, because I ran the workflow too often.
<br/>

<ins>Code validation:</ins>
1. [HTML validation](https://validator.w3.org/nu/)
1. [CSS validation](https://jigsaw.w3.org/css-validator/)
1. [VS Code JSHint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.jshint)
1. [Python Validation](http://pep8online.com/)

### Notable Bugs

### Problems

---

## Deployment

### Run locally

1. If you want to run the project locally 

---

## Credits

### Inspiration

### Content

### Media

### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). 
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, and [Stackoverflow](https://stackoverflow.com/) and [MDN](https://developer.mozilla.org/en-US/) for helping with finding solutions to coding problems, like animating the pictures in sequence instead of all at once.
- My wife, Elizabeth Lane, for supporting me during this coding course.