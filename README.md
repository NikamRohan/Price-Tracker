# Price-Tracker
A Price Tracker to track the prices of your willing to buy products at E-Commerce websites once they fall below your mentioned Desired price.  


## Installation

1. **First clone the repository in your system.**

   `git clone https://github.com/NikamRohan/Price-Tracker.git`

2. **Then Change Directory to News-Aggregator.**

   `cd Price-Tracker`

3. **Then start Virtual Environment within current Directory.**

   `virtualenv virtual_environment_name`

   `virtual_environment_name\Scripts\activate`

4. **Then install the dependencies from requirements.txt.**

   `pip install -r requirements.txt`

5. **Then Apply Migrations.**

   `python manage.py makemigrations`

   `python manage.py migrate`

6. **Execute the manage.py file to runserver.**

   `python manage.py runserver`

7. **Then Goto your favourite Browser and Type in localhost:8000.**

8. **Now you should be able to navigate through the website and explore its features.**

9. **Now for tracking the prices in background you need to setup app password with your gmail account that would be used to send alert message to user if prices of product fall below desired price.**  
    1. **For seeting up app password   
      follow this url:https://suhailvs.github.io/blog02.html#:~:text=Click%20the%20tab%20for%20App,Generate%20application%2Dspecific%20password%20button. settings.py file could       be found in Price-Tracker/django_amazon/settings.py**
    2. **And then instead of directly setting EMAIL_HOST_USER = 'your-username@gmail.com' and EMAIL_HOST_PASSWORD = 'Application spectific password(for eg: smbumqjiurmqrywn)'         you can follow this url to set up environment variables for Email and password: https://stackoverflow.com/questions/13995932/how-to-secure-application-specific-passwords-       for-gmail.Give name to environment variables as mentioned in Price-Tracker/django_amazon/settings.py file**

10. **For Tracking the prices at background you need to open another Command Prompt  and goto the Project Directory Price-Tracker and run the command:**
   
   `python manage.py process_tasks`
   
   
   
## Screenshots of Website

**Home Page**

![Screenshot (201)](https://user-images.githubusercontent.com/63553348/81909329-137afd00-95e8-11ea-8fdb-302373080e49.png)


**About Page**

![Screenshot (202)](https://user-images.githubusercontent.com/63553348/81909341-170e8400-95e8-11ea-8ccb-86fce52c3877.png)


**Register Page**

![Screenshot (203)](https://user-images.githubusercontent.com/63553348/81909343-17a71a80-95e8-11ea-8e2e-42a38b4593f1.png)


**Login Page**

![Screenshot (204)](https://user-images.githubusercontent.com/63553348/81909344-183fb100-95e8-11ea-8667-25aedee110b3.png)


**User Dashboard**

![Screenshot (205)](https://user-images.githubusercontent.com/63553348/81909346-183fb100-95e8-11ea-862b-e959e097b56f.png)


![Screenshot (206)](https://user-images.githubusercontent.com/63553348/81909347-18d84780-95e8-11ea-9f96-560ed65af467.png)


**Profile Page**

![Screenshot (207)](https://user-images.githubusercontent.com/63553348/81909351-1aa20b00-95e8-11ea-968f-490382ea5d1e.png)


**Adding Product Page**

![Screenshot (208)](https://user-images.githubusercontent.com/63553348/81909352-1b3aa180-95e8-11ea-941f-c06c9622288b.png)


**User gets Email if Price of Product Drops**

![Screenshot_20200910-221655](https://user-images.githubusercontent.com/63553348/92766714-19c19000-f3b4-11ea-9963-0c21191bfc60.png)


**Password Reset**

![Screenshot (209)](https://user-images.githubusercontent.com/63553348/81909354-1b3aa180-95e8-11ea-9ed4-9da59000f021.png)
