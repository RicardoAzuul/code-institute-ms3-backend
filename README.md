# code-institute-ms3-backend
A book review and recommendation site, using MongoDB, Python, Flask, HTML, CSS and JavaScript

Must haves for this project:


Nice to have: 


To visit the site, go to []()

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

External user’s goal: Find books they would like to read.

Site owner's goal: Earn money on each book purchased via a link from the site.

---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. We start off at the Strategy Plane:

#### Strategy Plane

The main goal for visitors to the site is to play a game. This means that upon visiting the page, a game must be ready to start. For this, we need a board of pictures. Because the game is about memorizing sequences, we need a start button, otherwise players might miss the first sequence and lose straight away. The start button gives them a chance to get their bearings, and then start the game. 

We want players to come back as well. For this, we implement a scoreboard, so players can keep track of their progress between sessions and work on getting better at the game.  

---

#### Scope Plane

The functional specifications of the site:


Content requirements:


---

#### Structure Plane
All pages should have the same navigation bar and footer:
- the navigation bar contains links to all the pages, as well as the home page.
- the footer contains copyright info.

<ins>The Home Page</ins>

 

---

#### Skeleton Plane


---

#### Surface Plane

The color palette is based on the theme: the colors were taken from a picture of a typical pug: 

The icons are sourced from Font Awesome.

The game buttons and game settings buttons are Bootstrap-style buttons: I used the Bootstrap button classes as easy ways to complement the function of buttons.

Fonts are sourced from Google Fonts. 

<ins>Wireframes</ins>


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
- 2 errors in Bootstrap. These I will ignore, as they are errors in a third-party extension.


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

- I also received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). He gave me the tip to use docstrings for instance.
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, and [Stackoverflow](https://stackoverflow.com/) and [MDN](https://developer.mozilla.org/en-US/) for helping with finding solutions to coding problems, like animating the pictures in sequence instead of all at once.
- My wife, Elizabeth Lane, for supporting me during this coding course.