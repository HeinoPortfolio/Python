# IS211_FinalProject
Dear Professor Ledon,

The command to run the program is:          python app.py.

There are two user: 1) test1@gmail.net password: fill   2) test2@gmail.net password: what

This application lets you view contact information, view a simple schedule of classes, and allow to student to drop andadd a few  classes to their schedule.  This application makes use of the following items:   

1) SQLAlchemey 
2) Flask-ALchemey 
3) Flask-wtf (forms) 
4) CSS 
5) HTML 
6) SQLAlchemey_ultils.  

These technologies were used to solve the problem of creating the application.  HTML and CSS were used to render and style the webpages of the application.  They added styling to make the application look more user friendly.  SQLAlchemey and Flask-Alchemey were used to provide the backend - the database.  These libraries were applied to create the tables, insert data and issue queries against the data base. Tables used were the following:  

1) User - held login information such and email ( used as login) and password
2) Contact_Info - held the contact information of the user
3) Registered_Courses -  holds the classes that the students have registered for.
4) Course_Info - holds a description of the course
5) Available courses - holds a list of the courses that availabe to register for.

These tables gave the application some reasonable funtionality.  There is room for some improvement for the tables.  But the tables as they are could show the potential of the application of the program.  If had more time on the program.  The reason for storint certain things like course infrormation in a separate table is that this information does not need to be stored more than once.  The most dynamic tables will be the Registered_courses and contact information.  These tables will under go the most edits so it seemed best to store only the bare minimum of information and use a join to get the rest of it from the Course_Info table.

While there are a few shortcoming with this program.  It does make use of a lot of the concepts that were covered in class during the semester. 
