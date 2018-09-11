# Walt Disney Application (Flask)

Flask application 

Technologies used: Python, pip, Flask, Bootstrap, CSS, Jquery

***SCREENSHOTS***

HOME PAGE:
![flask1](https://user-images.githubusercontent.com/19771986/45358797-37529800-b5e8-11e8-851d-890893eb0621.PNG)



VIEW TRAILER:
![flask2](https://user-images.githubusercontent.com/19771986/45358902-96181180-b5e8-11e8-9e9a-e96b9ba2052f.PNG)



MOVIES PAGE with wikipedia redirection:
![flask3](https://user-images.githubusercontent.com/19771986/45358903-96181180-b5e8-11e8-90dc-6bffd378e222.jpg)

![flask4](https://user-images.githubusercontent.com/19771986/45358904-96181180-b5e8-11e8-9728-7d7bb0cf98c6.png)



UPCOMING MOVIES PAGE:
![flask5](https://user-images.githubusercontent.com/19771986/45358901-957f7b00-b5e8-11e8-8f2c-34839461cba8.png)




FUNCTIONALITIES:

1. Displays three different pages
      #HOME
      #MOVIES
      #UPCOMING_MOVIES
      
2. Page Routing done through python
   
3. #HOME_PAGE
   * Displays some walt-disney movies in carousel 
   * Displays corresponding trailer of the movies in modal
   
4. #MOVIES_PAGE
   * Displays n number of walt-disney movies in cards with details  
   * Cards datas from Object file "data.py"
   * Once click any card of the movie, it directs to the corresponding wikipedia page of the movie
   
4. #UPCOMING_MOVIES_PAGE
   * Displays n number of upcoming walt-disney movies in cards with details
   * Cards datas from Object file "upcomingData.py"
   * Once click any card of the movie, it directs to the corresponding wikipedia page of the movie
 


CONFIGURATION:

1. Download & Install python from official site (https://www.python.org/downloads/windows/)

2. Set environment variable Path -> (Python)

3. Install "pip" for Flask framework("sudo apt -get install python3-pip")

3. Type "pip install flask" -> It creates Flask application in the specified path
     
4. Inside the path create a root file "app.py" & import flask 


EXECUTION:

1. Type "python app.py" in root directory

2. Flask application opens in the localhost port "5000"


