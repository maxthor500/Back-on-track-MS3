## Testing

Main [README.md](README.md)

#### Validation

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)

- [W3C Markup Validation](https://validator.w3.org/)
  
  - The developer used the **W3C CSS Validation Service** and **W3C Markup Validation Service** to check the validity of the website code.
  
- [JShint](https://jshint.com/) check the validity of the javascript code.

- [PEP8](http://pep8online.com/) check the python code

- [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)

  <img src=".\assets\tests\mobile-friendly-test.jpg" alt="mobile-friendly-test" style="zoom:25%;" />

##### Error during the validation

**HTML**

the main issue I got from link tag, there are errors of the type as in the following PDF files

-  [html_validator.pdf](./assets/tests/html_validator.pdf) 
-  [login_validator.pdf](./assets/tests/login_validator.pdf) 
-  [profile_validator.pdf](./assets/tests/profile_validator.pdf) 

**CSS**

-  [CSS_validator.pdf](./assets/tests/CSS_validator.pdf) 

**JavaScript**

-   [JSHint_script.pdf](./assets/tests/JSHint_script.pdf) 
-  [JSHint_map.pdf](./assets/tests/JSHint_map.pdf) 
-  [JSHint_emailJS.pdf](./assets/tests/JSHint_emailJS.pdf) 

**P8P**

-  [app.py result in txt](./assets/tests/result_appP8P)
- [forms.py result in txt](./assets/tests/result_formsP8P)

**User Stories testing:**

- As a user I am looking for a responsive web design so that I can display content of website adequately     to the device.
  - The user can run the app from all devices.
  - I used Bootstrap to make a responsive design.

<img src=".\assets\wireframes\multi_device_BOT.png" alt="multi_device_BOT" style="zoom: 33%;" />

- As a new user, I would like to know what the website is about upon opening the site.

  - The user can visit the about us page to get information about the website.

    <img src=".\assets\readme_images\about.jpg" alt="about" style="zoom:30%;" />

- As a new user I am looking for some help from another people to organize my curriculum vitae 

  <img src=".\assets\readme_images\post_commented.jpg" alt="post_commented" style="zoom:30%;" />

- As a new user I can see examples of posts have been putted on site. 

  - The last 3 most recent posts are shown on the landing page to show the user what people are posting about.

  <img src=".\assets\readme_images\home_page_bottom.jpg" alt="about" style="zoom:30%;" />

- As a new user, I would like to easily register and login for the site.

  - the user can reach the registration page from the home page or by navbar.

  <img src=".\assets\readme_images\register_page.jpg" alt="about" style="zoom:30%;" />

- As a user I can save my username and password so I can easily enter to the site.

  - the user can reach the login page from the home page or by navbar.

  <img src=".\assets\readme_images\login_page.jpg" alt="about" style="zoom:30%;" />

- As a new user I can create save password following the requirements of the website. 

  - the user needs to insert a secure password as the following regex criteria:

  ```
  regex = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
  ```

- As a user, I would like to login and add a new post to the blog.

  - the user when is logged can share post easily.

  <img src=".\assets\readme_images\home_page_logged.jpg" alt="home_page_logged" style="zoom:30%;" />

- As a user I can contact by email or phone the website founder so that I can send him a message if I     want to know more about the website.

  - on the about page the user cans see the company phone, mail and address.
  - the user can reach by mail throughout the contact form

  <img src=".\assets\readme_images\contact.jpg" alt="contact" style="zoom:30%;" />

- As a user I can check when the post has been posted and by whom. 

  - The posts is immediately posted on the main page
  - the posts are shown from most recent

- As a user I can answer other users and give them advice. 

  - Each user cans comment the posts

- As a user I can delete my comments under a post. 

  - who make a comment is able to delete and re-add a new comment.

  <img src=".\assets\readme_images\post_commented.jpg" alt="post_commented" style="zoom:30%;" />

- As a user I can create, edit, delete or comment my post. 

  - the user can add a new post, edit his post and delete it.

  <img src=".\assets\readme_images\profile.jpg" alt="profile" style="zoom:30%;" />

- As a new user I can check on map where is located the website founder. 

  - on the about page the user can check where the company is located.



**General Testing**

* Tested all internal links within the pages.
* Tested all buttons work.
* Tested the responsive behavior of images and text on desktops, laptops, notebooks and various smartphones.
* Reduce and expand the width of the window to verify that each line of text behaves the way expected and that the text arrangement looks good on all device widths.
* CSS was put through a [CSS Autoprefixer](https://autoprefixer.github.io/) and the changes were added to the website.

**Navbar**

- Click on each navigation menu item and verify that it links to the correct page.
- Hover over call to action button and verify the hover colour change
- Change the screen size from desktop to tablet and mobile to verify that the navigation bar is responsive.
- Tested the logo linked back to the home page on all pages.

**Map**

- The marker icon loads a page with the map.
- The dojos are indicating with an icon on the map.
- The map is responsive.

**Forms**

- Try to submit the empty form and verify that an error message about the required fields appears
- Try to submit the form with an invalid email address and verify that a relevant error message appears
- Try to submit the form with all inputs valid and verify that a success message appears.
- Try to to submit the form with all inputs valid to verify the emailJS works and I receive the template.
- Reduce and expand the width of the window to verify that the form display behaves and centers the way expected and that it looks good on all device widths.

#### Bug

- Some flash messages are not flashed correctly 
- When the account is deleted, the comments from the other users are not deleted as well.

**Lighthouse**

 [Lighthouse_summary.pdf](./assets/tests/Lighthouse_summary.pdf) 

