## Testing

Main [README.md](README.md)

#### Validation

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
- [W3C Markup Validation](https://validator.w3.org/)
  - The developer used the **W3C CSS Validation Service** and **W3C Markup Validation Service** to check the validity of the website code.
- [JShint](https://jshint.com/) check the validity of the javascript code.
- [PEP8](http://pep8online.com/) check the python code
- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

##### Error during the validation

- I checked every HTML file an error occurs in calendar.html from line 69 because <tr> tag has no cells beginning on it.
- The CSS files have no error.
- In every Javascript files there are warnings due to ES6 syntax.



**User Stories testing:**

​	User Stories

- As a user I am looking for a responsive web design so that I can display content of website adequately     to the device.
- As a new user, I would like to know what the website is about upon opening the site.
- As a new user I am looking for some help from another people to organize my curriculum vitae 
- As a new user I can see examples of posts have been putted on site. 
- As a new user, I would like to easily register and login for the site.
- As a user I can save my username and password so I can easily enter to the site. 
- As a new user I can create save password following the requirements of the website. 
- As a user, I would like to login and add a new post to the blog.
- As a user I can contact by email or phone the website founder so that I can send him a message if I     want to know more about the website.
- As a user I can check when the post has been posted and by whom. 
- As a user I can answer other users and give them advice. 
- As a user I can delete my comments under a post. 
- As a user I can create, edit, delete or comment my post. 
- As a new user I can check on map where is located the website founder. 



**General Testing**

* Tested all internal links within the pages.
* Tested all buttons work.
* Tested the responsive behaviour of images and text on desktops, laptops, notebooks and various smartphones.
* Reduce and expand the width of the window to verify that each line of text behaves the way expected and that the text arrangement looks good on all device widths.
* CSS was put through a [CSS Autoprefixer](https://autoprefixer.github.io/) and the changes were added to the website.

**Navbar**

- Click on each navigation menu item and verify that it links to the correct page.
- Hover over call to action button and verify the hover colour change
- Change the screen size from desktop to tablet and mobile to verify that the navigation bar is responsive.
- Tested the logo linked back to the home page on all pages.

**Memory Game**

- Tests were done to ensure the Card Matching game functions as intended. This was done on desktop PC and mobile.
- The first screen to be seen on the Card Matching page will be a window describing to the player with instructions on how to play the game. Once the “Play” button is clicked, this window will disappear and the cards will appear, along with the Time, Attempts.
- The player has 60 seconds to find and match the cards. The timer decreases by 1 for each second correctly.
- Each click on a card will increase the Attempts counter by 1. This is also working correctly.
- When the player has found all matching pairs, the “victory” overlay will appear.
- When the timer reaches zero, the player has lost the game and the “Loss” overlay will appear along.
- When the user clicks either of the two overlays to restart the game, the “Time” and “Attempts” are reverted to their original state. 60 for the Time and 0 for the Attempts.

**Modals**

- The user icon opens a modal with description of Master Del Plato.
- The content of the modal is responsive.
- The modal is closed when clicking on [x] or outside of it.

**Map**

- The marker icon loads a page with the map.
- The dojos are indicating with an icon on the map.
- The map is responsive.

**Calendar**

- The calendar shows every days of the month.
- The user can check the event of the day.
- The current day is in evidence.
- The calendar is responsive.

**Form contact**

- Try to submit the empty form and verify that an error message about the required fields appears
- Try to submit the form with an invalid email address and verify that a relevant error message appears
- Try to submit the form with all inputs valid and verify that a success message appears.
- Try to to submit the form with all inputs valid to verify the emailJS works and I receive the template.
- Reduce and expand the width of the window to verify that the form display behaves and centres the way expected and that it looks good on all device widths.

**Dark Mode**

- If the users press the adjust icon every elements change look.
- When the adjust icon is pressed the dark mode is active in every pages.
- The users are able to disable the dark mode from every pages.

#### Bug

- the map and the calendar don't open modals but load different pages.
- On the mobile the techniques of the cards is turned of the 90 degree.
- The calendar shows the events of today. The users don't have feedback when pressing another day.
- When on the mobile, the users open the navbar menu of the map page the map is covered.