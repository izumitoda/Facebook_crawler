# Facebook_crawler
using python and selenium to get users' timeline text information


you can run this .py and input the url of the user's personal homepage you want to crawl and save the information into the database

but before you use it, you have to make some changes:  
(1) login facebook once so that you chrome can remember you  
(2) download chromedriver.exe and change **C:\chromedriver.exe** in
line 10 `chrome_driver = os.path.abspath("C:\chromedriver.exe")` into you chromedriver.exe's path  
(3) find you user-date of chrome usually in the file **C:\Users\your_username\AppData\Local\Google\Chrome\User Data** and copy them to a new place and change **D:/User Data** in line 13 `options.add_argument("user-data-dir=D:/User Data")` into you new path  
(4) from line 49-53 you can change the information into you own database
 
