# PySpark

##### A end-to-end application developed in python using PySpark and Tkinter for predicting and visualizing university marks data

### Direction to run the above application
 
1. Install the requirements.txt with the command :
pip install -r requirements.txt

2. Navigate into DesktopApp folder 

3. python3 login.py
   or
   python login.py
   
 
 
-----------------------------------------------------------
## About
A Desktop application is created using Tkinter for GUI. Our application has a Login page to authorise the users. We provide six options or objectives for the users to choose from. These objectives are Visualisation of the performance of students in a particular subject based on total marks obtained. Prediction of the performance of a particular student based on the subject code (output- Grade) using machine learning. To check whether a Student with a backlog clears the exam in successive attempts. Visualisation of subcode versus number of students who pass or fail that subject. Visualization of student performance based on a particular year. Predicting the score of a student in the consecutive semester based on the score of the similar subject in present or previous semesters. On clicking any of these, another tab pops open for that particular objective. On providing the required information in the entry fields, the user obtains the desired output in the form of a graphical represention, Lists or values. These objectives are implemented using the PySpark library as the given dataset is large. For objectives with graphical repesentations, we use Matplotlib library. For formating the dataset according to our requirement we use PySpark and Pandas.

-----------------------------------------------------------

## Functional requirements
The function requirements of this project include:
1. The application allows the user to register and authenticates before providing access.
2. The Result data is analyzed and objectives have been identified. 
3. The application facilitates the user to choose among the given objectives.
4. Visualisation of the student performance in a particular subject based on the total marks obtained.
5. Prediction of the performance of a particular student based on the subject code (output- Grade) using machine learning.
6. To check whether a Student with a backlog clears the exam in successive attempts.
7. Visualisation of subcode versus number of students who pass or fail that subject.
8. Visualization of student performance based on a particular year.
9. Predicting the score of a student in the consecutive semester based on the score of the similar subject in present or previous semesters.

-----------------------------------------------------------

## Non Functional requirements 
The Non-function requirements of this project include: 
1. Reliability: The system shall be completely operational.
2. Usability: The application has a user-friendly interface and can be comprehended by any user.
3. Performance: The application runs seamlessly in both Windows and Linus operating system. This application does not need internet connection to run.
4. Security: Only authenticated users are allowed to operate the application.
5. Online User Documentation and Help: The application can be easily available in GitHub.

## Screenshots
Login
![[https://github.com/bitmos/PySpark/blob/ac03e7ec8947a5663de9d26507c196f0a81d26d0/assets/1_1.png]]

Home Page
![[Pasted image 20220421004031.png]]

Student perfomance in a subject
![[Pasted image 20220421004109.png]]

Performance Prediction
![[https://ibb.co/dLV6qQy]]

Backlog Analysis
![[Pasted image 20220421004432.png]]

Result Analysis
![[Pasted image 20220421004555.png]]

Semester-wise Performance Analysis
![[Pasted image 20220421004616.png]]

Consecutive Score Prediction
![[6_1.jpg]]
