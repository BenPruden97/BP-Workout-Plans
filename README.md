# BP Workout Plans

### Backend Development Milestone Project

#### BP Workout Plans is a community based website where members can search, create and share their own workout plans with each other.

[View BP Workout Plans Here](https://bp-workout-plans.herokuapp.com/)

# Table of Contents

* [UX](#ux)
  * [Project Goals](#project-goals)
  * [User Goals](#user-goals)
  * [User Stories](#user-stories)
* [Five Development Planes](#five-development-planes)
  * [Strategy Development Plane](#strategy-development-plane)
  * [Scope Development Plane](#scope-development-plane)
  * [Structure Development Plane](#structure-development-plane)
  * [Skeleton Development Plane](#skeleton-development-plane)
  * [Surface Development Plane](#surface-development-plane)
* [Data Schema](#data-schema)
  * [Member Collection](#members-collection)
  * [Workout Plans Collection](#workout-plans-collection)
  * [Workout Plans Category Collection](#workout-plans-category-collection)
  * [Workout Plans Difficulty Collection](#workout-plans-difficulty-collection)
* [Project Features](#project-features)
  * [Design Features](#design-features)
  * [Navigation Bar Features](#navigation-bar-features)
  * [Home Page Features](#navigation-bar-features)
  * [Sign Up Page Features](#navigation-bar-features)
  * [Log In Page Features](#navigation-bar-features)
  * [Contact Page Features](#navigation-bar-features)
  * [Find Workout Plans Page Features](#find-workout-plans-page-features)
  * [Create A Workout Plan Page Features](#create-a-workout-plan-page-features)
  * [Edit Workout Plan Page Features](#edit-workout-plan-page-features)
  * [Workout Plan Page Features](#workout-plan-page-features)
  * [My Workout Plans Page Features](#my-workout-plans-page-features)
  * [Profile Page Features](#profile-page-features)
  * [Edit Account Page Features](#edit-account-page-features)
* [Features To Implement In The Future](#features-to-implement-in-the-future)
* [Issues And Bugs](#issues-and-bugs)
* [Technologies Used](#technologies-used)
* [Testing.md File](TESTING.md)
* [Project Deployment](#project-deployment)
  * [MongoDB Database Deployment](#mongodb-database-deployment)
  * [GitHub Deployment](#github-deployment)
  * [Heroku App Deployment](#heroku-app-deployment)
* [Credits](#credits)

# Project Goals

The primary goal of BP Workout Plans is to provide a web-based fitness community, that allows users to create, search, save, delete and share their favourite workout plans with fellow members. This website was inspired by my first project BP Fitness where members could find workout plans on the member benefits page.

# User Goals

### The user is looking for:

* A database where the user can search for different workouts for several muscle groups.
* Be able to create their own account by signing up or loggin in.
* Update their account (edit details if needed).
* Delete their account (if needed).
* Create their own workout plans.
* Read/ View workout plans from other members.
* Update/ Edit workout plans created by the member.
* Delete workout plans created by the member.

# Developer/ Site Owner Goals

### The Developer is looking to:

*	Create a fitness-based community where all members can share workout plans with each other.
*	Allow users to sign up and log into their account.
*	Allow users to create workout plans to share with other members.
* Allow users to search for different workouts using the search bar.
*	Allow users to contact the developer if there are any issues, would like to give feedback or need any help.

# User Stories

### As A User, I want to:

* Find Workout Plans from the database.
* Search for Workout Plans from the database.
* View Workout Plans created by members of BP Workout Plans.
* Sign up for an account to become a member.
*	Log into their account once signed up.
*	Contact the Developer/ Site Owner for any feedback or issues they may have.

# As a Member, I want to:

* Find Workout Plans from the database.
* Search for Workout Plans from the database.
* View all Workout Plans created by the member.
*	Log into their account once signed up.
*	Create A Workout Plan to share with the community.
*	Edit my Workout Plans.
*	Edit Account details.
*	Delete my Workout Plans.
*	Delete Account Option.
*	Contact the Developer/ Site Owner for any feedback or issues they may have.

# As an administrative Account Holder, I want to:

* Find Workout Plans from the database
* Seach for Workout Plans from the database
* View all workout plans that have been uploaded to BP Workout Plans database.
* Log into their account
* Create A Workout Plan to share with the community
* Edit Any Workout Plan from the database
* Delete Any Workout Plan from the data

[Back to Table of Contents](#table-of-contents)

# Five Development Planes

## 1. Strategy Development Plane

Here is how I broke down the Strategy Development Plane:

1. Users/ Members
   * Users (not registered/ not signed up)
   * Members (signed up/ logged in)

2. Demographic/ Target Audience
   * Loves going to the gym/ working out
   * Gym goers looking for workout plans
   * Gym goers of all ages
   * Gym goers of all levels

3. The website will need to enable a user to:
   * Sign Up for an account
   * Log into their account once signed up
   * Contact the site owner/ Developer using the contact form
   * Find workout plans created by members
   * View members workout plans
   * Search using the search bar input for specific workout plans

4. The website will need to enable a member to:
   * Log into their account
   * Contact the site owner/ Developer using the contact form
   * Find workout plans created by other members
   * View other members workout plans
   * Search using the seach bar input for specific workout plans
   * Create their own workout plans to share with the community
   * Edit their own workout plans to make changes
   * Delete their own workout plans (if needed)
   * View their profile
   * Edit their account to change either their username or password
   * Delete their account if they would like to
   * View their own workout plans created by themselves

With the above strategy options in mind, I have created a User & Member strategy table (below) to show the importance and viability for all of the following options:

### User Strategy Table

![User Strategy Table](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/user-strategy-table.png)

### Member Strategy Table

![Member Strategy Table](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-strategy-table.png)

## 2. Scope Development Plane

Here is how I broke down the Scope Development Plane in order to align with the Strategy Development Plane listed above. The Scope Development Plane is broken down into two categories:

### 1. Content Requirements

* Easily readable primary and secondary font
* Buttons and links are easily visible and clickable
* Headings and text can are easily visible
* Aesthetic colors that work well together
* Easy Naviagtion
* Responsive design for all devices
* * Sign Up Page
* Log In Page
* Contact Page
* View Workout Plans
* Search for Workout Plans

### 2. Functionality Requirements

* Sign Up for an account
* Log In to account
* Contact Developer/ Site Owner
* Customise and update username & password
* Edit Profile
* Delete Profile
* View Workout Plans
* Search for Workout Plans
* Edit Workout Plans
* Delete Workout Plans
* My Workout Plans Page
* Create Workout Plan
  * Workout Plan Muscle Group
  * Workout Plan Difficulty
  * Workout Plan Name
  * Workout Plan Description
  * Exercise Names
  * Exercise Sets
  * Exercise Reps
  * Exercise Rest Time
  * Exercise Weight Used
  * Total Exercise Amount
  * Total Workout Time
  * Created By

## 3. Structure Development Plane

Within the Structure Development Plane I have created a hierarchial structure chart to show how the users & members of BP Workout Plans can navigate around the site with ease and efficiency, the hierarchial structure chart is displayed below:

### User Structure Chart

![User Structure Chart](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/user-hierarchial-structure-chart.png)

### Member Structure Chart

![Member Structure Chart](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-hierarchial-structure-chart.png)

## 4. Skeleton Development Plane

The wireframe mockups for BP Workout Plans were created using Adobe XD with the User Experience and User Interface in mind:

### Home Page Wireframe

![Home Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/home-page-wireframe.png)

### Sign Up Page Wireframe

![Sign Up Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/sign-up-page-wireframe.png)

### Log In Page Wireframe

![Log In Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/log-in-page-wireframe.png)

### Contact Page Wireframe

![Contact Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/contact-page-wireframe.png)

### Find Workout Plans Page Wireframe

![Find Workout Plans Page](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/find-workout-page-wireframe.png)

### Create A Workout Plan Page Wireframe

![Create A Workout Plan Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/create-workout-plan-page-wireframe.png)

### Edit Workout Plan Page Wireframe

![Edit Workout Plan Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/edit-workout-plan-page-wireframe.png)

### Workout Plan Page

![Workout Plan Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/workout-plan-page-wireframe.png)

### Member Workout Plans Page Wireframe

![Member Workout Plans Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-workout-plans-page-wireframe.png)

### Member Profile Page Wireframe

![Member Profile Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-profile-page-wireframe.png)

### Edit Account Page Wireframe

![Edit Account Page Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/edit-account-page-wireframe.png)

### Member Navigation Bar Wireframe

![Member Navbar Wireframe](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-navbar-wireframe.png)

# 5. Surface Development Plane

### Colors

![Project Colors](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/project-colors.png)

### Typography

The primary font used with BP Workout Plans was "Poppins". I wanted the font to match well with the UI of the website with its simplicity but was also very easy to read and understand.

The secondary font used was "San Serif" which would display if the primary font was not able to load onto the user/ members device.

### Images/ Screenshots

The images/ screenshots used within BP Workout Plans or the README.md file were created using Adobe XD. Using Adobe XD for the entirety of my project allowed me to keep a good consistency throughout.

[Back to Table of Contents](#table-of-contents)

# Data Schema

I used MongoDB  to store my data for my BP Workout Plans project. Within MongoDB I created four collections to store different types of data for different members and workout plans. The four data collections are displayed below:

![Data Schema Tables](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/data-schema.png)

## Members Collection

The Members collection stored the following data for the Sign Up Page to allow the user to create an account and be able to Log In once created:

* Username (Unique username used to log in using the log in page)
* Email Address
* Password (Unique password used to log in using the log in page)

## Workout Plans Collection

The Workout Plans collection stored the following data to allow members to Create, Read, Update & Delete Workout Plans to share with the community

* Workout Plan Muscle Group (Workout Plan Category Collection)
* Workout Plan Difficulty (Workout Plan Difficulty Collection)
* Workout Plan Name
* Workout Plan Description
* Exercise Name: 1, 2, 3, 4, 5 & 6
* Number Of Sets: 1, 2, 3, 4, 5 & 6
* Number Of Sets: 1, 2, 3, 4, 5 & 6
* Rest Time: 1, 2, 3, 4, 5 & 6
* Weight Used: 1, 2, 3, 4, 5 & 6
* Total Workout Time
* Created By

## Workout Plans Category Collection

The Workout Plan Category Collection stores five muscle groups that the member can choose from to base their workout plan around. Those five options are:

* Chest
* Back
* Arms
* Legs
* Shoulders

Each category has its own image selected for users/ members to tell which muscle group each workout plan is based around.

## Workout Plans Difficulty Collection

The Workout Plan Difficulty Collection stores three difficulty options for the member to choose from. Those three options are:

* Beginner
* Intermediate
* Advanced

Having this option allows for users/ members of all fitness levels to feel included.

# Project Features

## Design Features

Jinja templating was used to extend the base.html template across every page for BP Workout Plans. This is to keep consistency and functionality for each page that extends the base.html template. The sections within the base.html template that are implemented for each page are:

* The Navigation Bar (Both User & Member Navigation Bars)
* The Footer Section - Includes social links
* The Flash Messages - Used to flash messages to let a user/ member know an action they have completed (e.g: Succession of signing up for an acccount)
* The Burger Menu - Used to display the Navigation Links on Tablet and Mobile Devices

#### Base Template Example

Here is an example of the base.html template for the Log In Page. At the top of the page {% extends "base.html" %} is used to display the content from the base.html page which is the Navigation Bar & Footer Section. The {% block content %} is then used to display the content from each page between the Navigation Bar & Footer Section.

![Base Template Example Screenshot](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/base-template.png)

## Navigation Bar Features

The Navigation Bar is split into three sections. Theses sections are listed below:

* The User Navigation Bar:
  * Home Page
  * Find Workout Plans Page (Allows the user to find workout plans created by BP Workout Plan's Members)
  * Sign Up Page (Allows the user to sign up for an account)
  * Log In Page (Allows the user to log into their account)
  * Contact Page (Allows the user to contact the developer/ site owner for any questions, queries or assistance)

![User Navigation Bar Screenshot](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/user-navigation-bar.png)

* The Member Navigation Bar:
  * Home Page
  * Find Workout Plans Page (Allows the member to find workout plans created by other BP Workout Plan's Members)
  * Create A Workout Plan Page (Allows the member to create a workout plan to share with the community
  * Contact Page (Allows the member to contact the developer/ site owner for any questions, queries or assistance)
  * My Workout Plans Page (Allows the member to view all of the workout plans created by that member)
  * View Profile (Allows the member to view their member profile to edit or delete their profile)
  * Log Out Functionality (Allows the member to log out of their account)

![Member Navigation Bar Screenshot](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-navigation-bar.png)

* Burger Menu Navigation Bar:
  * Displays the user navigation links if a user of BP Workout Plans for Tablet & Mobile Devices
  * Displays the member navigation links if a member of BP Workout Plans for Tablet & Mobile Devices

![User Burger Menu Screenshot](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/user-burger-menu.png)
![Member Burger Menu Screenshot](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/member-burger-menu.png)

## Home Page Features

The Home Page features are as follows:

* User & Member Navigation Bar
* Display a limit of 6 Workout Plans from the database that has been created by Members.
  * The workout plans are clickable which will take the user/ member to that workout plans id page to view all of that workout plan's information/ details.
* A Sign Up & Log In Section to allow the user to Sign Up for an account or Log Into their account if they are already a member (User Only).
* Create A Workout Plan Section to encourage the member to create their own workout plan to share with the community (Member Only).
* Footer Section

## Sign Up Page Features

* User & Member Navigation Bar
* Sign Up Section to allow the user to sign up for an account to become a member of BP Workout Plans.
  * Input Fields to allow the user to enter their information.
    * The required attribute is used to allow the user/ member to fill in the required fields before submitting.
  * Icons to identify each input field.
  * Password Authentication - Werkzeug was used to hash the password on entry.
  * Password Validation was used to make sure the user was entering the same password twice for security purposes. The sign up button was disabled until passwords were a match.
* Footer Section

## Log In Page Features

* User & Member Navigation Bar
* Log In Section to allow the user to log into their account if they are already a member of BP Workout Plans.
  * Input Fields to allow the user to enter their information.
    * The required attribute is used to allow the user/ member to fill in the required fields before submitting.
  * Icons to identify each input field.
  * Password Authentication - Werkzeug was used to un-hash the password on entry for login verification.
* Footer Section

## Contact Page Features

* User & Member Navigation Bar
* Contact Form Section to allow the user/ member to send a message to the developer/ site owner.
  * Input Fields to allow the user to enter their information.
    * The required attribute is used to allow the user/ member to fill in the required fields before submitting.
  * Icons to identify each input field.
  * Text Area section to allow the user to type in their message.
* Footer Section

## Find Workout Plans Page Features

* User & Member Navigation Bar
* Search Input Section
  * Query Search input to allow the user/ member to search either the Workout Plan Category or Difficulty and will display the workout plans with those queries.
  * 0 Search Results section which lets the user/ member know that there are 0 results and to research with recommended keywords given.
  * A Reset Link to reset the search query.
  * A Search Button with icon to search for the query by the user/ member
* Workout Plans Display Section to display all of the current workout plans from the MongoDB database within the Workout Plans Collection
* Page Pagination Links: This displays only 6 workout Plans per page and has pagination links at the bottom of that section for the user/ member to move onto the next or           previous pages.
* Footer Section

## Create A Workout Plan Page Features

* Member Navigation Bar
* Create A Workout Plan Form Section.
  * Input Fields to allow the member to enter information.
    * The required attribute is used to allow the user/ member to fill in the required fields before submitting.
  * Select Options to allow the member to choose from the options available for their workout plan.
    * The required attribute is used to allow the user/ member to fill in the required fields before submitting.
  * Text Area for the Workout Plan Description.
  * Each Field has its own label to let the member know which information is needed.
  * A Cancel Button so the member can cancel creating the workout plan.
  * A Create Workout Plan Button which will create the workout plan and add onto the MongoDB Database.
* Footer Section

## Edit Workout Plan Page Features

The member will only be able to edit workout plans that they have created themselves. They are not able to edit other member's workout plans.

* Member Navigation Bar
* Create A Workout Plan Form Section.
  * Input Fields to allow the member to edit the information they had entered when creating the workout plan.
  * Select Options to allow the member to edit the option chosen when creating the workout plan.
  * Text Area to edit the Workout Plan Description entered when creating the workout plan.
  * Each Field has its own label to let the member know which information they are editing.
  * A Cancel Button so the member can cancel editing the workout plan.
  * An Edit Workout Plan Button which will update all of the fields changed and update the workout on the MongoDB Database.
  * A Delete Workout Plan button which will remove the workout plan from the MongoDB database if the member wishes to do so.
* Footer Section

## Workout Plan Page Features

* Member Navigation Bar
* Image Section with the image for the muscle group category chosen by the member
  * The Workout Name that the member inputted is displayed
  * The name of the member is also displayed to let users and other members know who created that workout plan
* The Workout Plan Category, Difficulty, Total Exercise Amount & Total Workout Time is displayed
* The Workout Plan Description is displayed
* Each Exercise is then displayed using the accordion element from Bootstrap. The exercise sections include:
  * The Exercise Name inputted by the member
  * The Number Of Sets inputted by the member
  * The Number Of Reps inputted by the member
  * The Rest Time inputted by the member
  * The Weight Used inputted by the member
* There are then some options to choose from:
  * Go Back Button (For Both A User & Member)
  * Log In To Create A Workout Plan Button (For Users or non logged in Members)
  * Create A Workout Plan Button (For Members Only)
  * Edit Workout Plan Button (For Member who Created that Workout Plan Only)
  * Delete Workout Plan Button which will display a delete workout plan modal with a confirmation message (For Member who Created that Workout Plan Only)
* Footer Section

## My Workout Plans Page Features

* Member Navigation Bar
* Create A Workout Plan Section to allow the member to create a workout plan
* Displays all of the Member's Workout Plans that they have created
* Page Pagination Links: This displays only 6 workout Plans per page and has pagination links at the bottom of that section for the member to move onto the next or previous       pages.
* Footer Section

## Profile Page Features

* Member Navigation Bar
* Welcome Back Message for the member
* Find A Workout Plan Section for the member to find other member's workout plans
* Create A Workout Plan Section to encourage a Workout Plan to share with the community
* My Workout Plans section which will take the member to their workout plans page
* Edit Account section which will take the member to the Edit Account Page
* Delete Account Modal Which will allow the member to delete their account with a confirmation message.
* Footer Section

## Edit Account Page Features

* Member Navigation Bar.
* Update Username Section which allows the member to update their current username.
  * Username input field to update their current username.
    * The required attribute is used to allow the member to fill in the required fields before submitting.
  * Username icon to identify the input field.
  * A Cancel button to cancel updating the member's username.
  * An Update Username Button which will update the member's current username to the updated username. This will also log the member out and ask the member to log back in using     their updated/ new username.
* Update Password Section which allows the member to update their current password.
  * Password input field to update their current password.
    * The required attribute is used to allow the member to fill in the required fields before submitting.
  * Password Icon to identify the input field.
  * Password Authentication - Werkzeug was used to hash the password on entry.
  * Password Validation was used to make sure the member was entering the same password twice for security purposes. The Update Password button was disabled until passwords were     a match.
  * A Cancel Button to cancel updating the member's current password.
  * An Update Password Button which will update the member's current password to the updated password. This will also log the member out and ask the member to log back in using     their updated/ new password.
* Footer Section

[Back to Table of Contents](#table-of-contents)

# Features To Implement In The Future

### 1. Email Verification/ Forgotten Password

* Email Verification:

Once the user signs up to an account with BP Workout Plans, a verification email will be sent to the user using the email address they have provided. The user will then have to verify their email address before being able to log in as a member.

* Forgotten Password

If the member has forgotten their password then they can select the forgotten password option on the log in page. The member will then receive an email to provide their username and email address they used when signing up. If the information provided is validated, the member will then have the option to change their password and log back in using their username and updated password.

### 2. Be Able To Like Other Members Workout Plans

On the workout plan id page there will be an option for the member to like that workout plan which will then display within the member's liked workout plans. This allows members to save other member's workout plans that they may find helpful or useful.

### 3. Have Workout Category And Workout Difficulty Fitler Options

This option will give the user/ member options on what they can search for instead of having to type in the correct keywords into the search bar to display the workout plans they are trying to search for.

For example: I want to find all workout plans that were created for Beginners for the Chest Muscle Group. I can then select the Chest and Beginner options and only workout plans that have a workout difficulty of Beginner and workout category of Chestwill display. This will save the user/ member time on finding the workout plans they are looking for and makes sure they are getting the correct results.

### 4. Give The Member The Option To Remove And Add Exercises To Their Workout Plan

When a member is currently creating a workout plan they have by default 6 exercises to fill in before completing the workout plan. This option will give the member more flexibility on how many exercises they would like to have for their workout plan. The minimum amount of exercises per workout plan would now be 3 and the max amount of exercises would be 8. 

With this new feature, as soon as the member creates a workout plan the default amount of exercises will now be 3. The member can then add more exercises as they go on by clicking on the plus button until they reach the max amount of 8 exercise which the plus button will then not be available. The member can also remove exercises if they have created too many by using the minus button. 

This will allow more customisation and flexibility when creating and viewing workout plans.

### 5. A Comment Section Under Each Workout Plan For Suggestions And Help

The comment section would be displayed underneath the options for each workout plan. This will allow other members to give their opinion on member's workout plans and maybe offer some advice or point out errors or mistakes the member who created the workout plan has made. The member who created the workout plan will have authority over which comments they can keep or remove for the workout plan.

[Back to Table of Contents](#table-of-contents)

# Issues And Bugs

The developer encounted some issues while developing BP Workout Plans which have been listed below:

### 1. Create A Workout Plan Input Validation

When a member is creating a workout plan using the form within the create a workout plan page, if there are any input fields that the member has left empty, the browser default message of "Please fill in this fields" does not display within Google Chrome & Microsoft Edge browsers. To try and fix this issue I tried to:
* Use the bootstrap form validation code with the class of "form-control" however that did not fix the issue.
* I sent a message to my mentor to see if they could find any issues or problems that was causing the field message to not display.
* I then contacted tutor support to try and find a solution as to why the field message was not displaying. I spoke to 2 tutors over live chat who was also unable to find the       problem or a solution to fix this issue

I then tested the create a workout plan form on the Internet Explorer browser and the form validation and "Please fill in this form" message was displaying.
Here is a screenshot of the create a workout plan form within the Internet Explorer browser:

![Create Form Validation Error](https://github.com/BenPruden97/BP-Workout-Plans/blob/main/static/screenshots/form-validation-error.png)

### 2. Edit Account Page

Error:
When a member was to change their username within the edit account page to a new one. When the username was changed and the member was to then navigate to their member profile, an error would occur as the member's username had changed.

Solution:
To Fix this error, I used 'session.pop("member")' to log the member out after changing their username. A flash message would display to let the member know that their username had been updated successfully. The member would then have to log back into their account using the updated username which fixed the profile error.

### 3. Flash Message JS File

I had created a seperate js file for flash messages to only display on the pages where flash messages were going to display. The issue here was that the log out functionality had a flash message to let the member know that they had logged out successfully. I decided to leave the flash message js script tag within the base.html file. Because of this, there are error messages for the flash message js file within the console when displaying a page where there are no flash messages to display.

### 4. Search Query Pagination Issue

When a user/ member was to use the search query and if the query result had more then one page, every page after the first link would throw an error.

To Fix this issue I change the following code:

1. The Create A Workout Plan Form method from method="POST" to method="GET".
2. Removed the methods of "GET" & "POST" within the search query route.
3. Changed the query variable from request.form.get('query') to request.args.get('query').

By changing the code above, this fixed the pagination links for when users/ members were to query workout plans with more then one page of results.

[Back to Table of Contents](#table-of-contents)

# Technologies Used

### Languages

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

### Programs Used

* [Git](https://git-scm.com/)
  * Git was used as version control for my project. This was so I could add, commit & push my code to my GitHub Repository.

* [GitHub](https://github.com/)
  * GitHub was used as a software hosting platform to host my project. GitHub is where all of my project files, images, screenshots, code and folders are stored.

* [GitPod](https://gitpod.io/workspaces)
  * GitPod was used as a development hosting platform for me to create my project code.

* [Heroku App](https://www.heroku.com/)
  * The Heroku App was used to be able to deploy my project website.

* [Adobe XD](https://www.adobe.com/uk/products/xd.html)
  * Adobe XD was used to be able to create my wireframes, screenshots & images for my project.

* [Google Fonts](https://fonts.google.com/)
  * Google Fonts was used to display my primary font (Poppins) & secondary font (Sans-Serif)

* [Font Awesome](https://fontawesome.com/)
  * Font Awesome was used to display icons used throughout my project

### Libraries

* [Bootstrap](https://getbootstrap.com/)
  * Bootstrap was used to implement responsiveness to my project pages and bootstrap classes for design features.

* [EmailJS](https://www.emailjs.com/)
  * EmailJS was used to allow users/ members to send messages using the contact form directly to the Developer's email address using JavaScript.

* [SweetAlert](https://sweetalert.js.org/docs/)
  * SweetAlert was used alongside EmailJS to provide an email validation pop up once the email had been sent. 

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  * Flask was used as a web framework for my project application.

* [Flask Pagination Links](https://pythonhosted.org/Flask-paginate/)
  * Pagination Links were used for pages where workout plans were going to be displayed. The flask_paginate extension was used to display only 6 workout plans per page and           provided links to more pages if required.

* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
  * Jinja templating was used within the base.html file to display html code throughout the project application.

* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
  * Werkzeug security was used for password hashing, authentication and validation.

### Database Management

* [MongoDB](https://www.mongodb.com/)
  * MongoDB was used to store the data collections used for this project

[Back to Table of Contents](#table-of-contents)

# Testing 

* The testing for BP Workout Plans was created in a separate file. The TESTING.md file can be found here - [TESTING.md File](TESTING.md)

# Project Deployment

### 1. MongoDB Database Deployment

The Developer used MongoDB to store the data for the project BP Workout Plans

Here is how you can create your own database by following these steps:

1. Log into your MongoDB account or create an account if you don't have one
2. Once you have logged into your account
3. Locate your MongoDB projects and select create a new project and give your project a name and then select, Create Project.
4. Once the project has been created:
  * Select Build Database
  * Choose the Free Cluster Option
  * Make sure you have selected 'Shared' from the 3 options at the top
  * Move onto the Cloud Provider & Region Option and select the correct options for you (The developer used AWS and Ireland)
  * Move onto Cluster Tier and select the Free forever option listed under the base price (The developer used M0 Sandbox)
  * Lastly move onto the Cluster Name and give your cluster a name.
  * Lastly Select Create Cluster Button (The Cluster may take some time to be created)
5. Once the cluster has been created, select 'Database Access' on the left hand side. Once selected, select the 'Add New Database User'
  * Choose the 'Password' Authentication Method
  * Enter a username and password
  * Move onto 'Database User Privileges' and select the 'Read and write to any database' option
  * Lastly click on the 'Add User' Button
6. Select the 'Network Access' on the left hand side under the 'Database Access' option. Once selected, select the 'Add IP Address'
  * Select 'allow access from anywhere'
  * Lastly click on the 'Confirm' Button
7.  Select 'Database' on the left hand side of the page. Once selected, select 'Browse Collections' and click on the 'Create' Button.
  * Click on the 'Add My Own Data' Button
  * Enter A Database name and collection name to get started. Once entered click on the 'Create Button'
  * Once created, select the 'Insert Document' option and start building your collections.

### GitHub Deployment

1. Forking A Repository
  * Log into your GitHub Account
  * Select your project repository
  * On the top right of your repository page, click on the 'Fork' Button
  * You should now have a copy of your GitHub project repository in your GitHub account.

2. Cloning A Repository
  * Log into your GitHub Account
  * Select your project repository
  * Click on the green 'GitPod' button on the right hand side of the respository page. This will open up a new GitPod workspace for you to work on.

There are also 3 other options that you can use to clone your repository. Select the 'Code' dropdown button to left of the green 'GitPod' Button.
  1. To clone your repository using HTTPS, click on the "HTTPS" option and copy the link using the copy button to the right of the https link.
  2. To clone your repository using a SSH key, click on the "SSH" option and copy the link using the copy button to the right of the SSH link.
  3. To clone your repository using a GitHub CLI, click on the "GitHub CLI" option and copy the link using the copy button to the right of the GitHub CLI link.

### Heroku App Deployment

Herku is a cloud application platform that supports many programming languages. As this project is using a server, application and database, the developer thought Heroku was the best app to deploy his project.

Before you can deploy your project to Heroku, you must complete the following steps to allow the Heroku app to work.

* You will need to create a requirements.txt file to install project requirements. The following code is used to create the requirements.txt within the terminal.

pip3 install -r requirements.txt

Once created push to your repository:

git add requirements.txt
git commit -m "Add requirements.txt"
git push

* You will also need to create a Procfile so Heroku will know which file runs the app. The following code is used to create the Procfile within the terminal.

echo web: python app.py > Procfile

Once created push to your repository:

git add Procfile
git commit -m "Add Procfile"
git push

Once you have completed these steps:

1. Log Into Heroku or create an account if you don't already have one
2. Once logged in, Click on the 'New' Button on the right hand side of the page
3. Select the 'Create New App' option
4. Give your app a name and select your region (The developer chose Europe)
5. Lastly click on the 'Create App' Button
6. Select the 'Deploy' option from the navigation links
7. Within the Deployment Method section, select the 'Connect to GitHub' option
8. Search for your project repository name and select your respository
9. Click on the 'Connect' Button to connect Heroku to your GitHub repository
10. Once connected select the 'Settings' option from the navigation links
11. Within the Config Vars section, select 'Reveal Config Vars'
12. Once open you will want to Keys & Values:

|Key|Values|
|:-----:|:-----:|
|IP|0.0.0.0|
|PORT|5000|
|SECRET_KEY|<your_secret_key>|
|MONGO_URI|<your_connection_string>|
|MONGO_DBNAME|<your_mongdb_name>|
 
13. Navigate back to the 'Deploy' navaigation link
14. Within the 'Automatic Deploys' section make sure that your main branch is selected and click on 'Enable Automatic Deploys'
 
Your Project is now deployed onto Heroku and any code pushed to GitHub will also be pushed to the Heroku App.
 
You can preview your app at anytime by clicking on the 'Open App' button at the top right hand side of the page.

[Back to Table of Contents](#table-of-contents)

# Credits

### Websites Used For Help

Here is a list of the websites that the developer has used for any help or solutions

1. [YouTube](https://www.youtube.com/)
2. [Bootstrap](https://getbootstrap.com/)
3. [W3Schools](https://www.w3schools.com/)
4. [Stack Overflow](https://stackoverflow.com/)
5. [CSS Tricks](https://css-tricks.com/)

### Mentors

Seun & Brian (Last Session Call) had given me support and guidance for this project and answered any questions that I had.

### Code Institute

* Tutor support was a massive help when I couldn't get certain parts of code to work.
* The Backend Development Mini Project was used as a reference for me during the development process.

[Back to Table of Contents](#table-of-contents)
