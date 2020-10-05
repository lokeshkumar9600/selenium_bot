from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import gtts
from playsound import playsound
# make request to google to get synthesis

tts = gtts.gTTS("helloo this is megalodonn." , lang="en-ca")
insta_voice = gtts.gTTS("Opening instagram" , lang="en-ca")
you_call = gtts.gTTS("you can call me MEG" , lang="en-ca")
command = gtts.gTTS("please enter your command" , lang="en-ca")
youtube_voice = gtts.gTTS("opening youtube" ,lang="en-ca")
greet = gtts.gTTS("whats your name" , lang="en-ca")
# save the audio file
tts.save("hello.mp3")
you_call.save("me.mp3")
insta_voice.save("insta.mp3")
command.save("command.mp3")
youtube_voice.save("youtube.mp3")
greet.save("greet.mp3")
# play the audio file



playsound("hello.mp3")
playsound("me.mp3")
playsound("greet.mp3")
name  = input("whats your name : : ")
ns = gtts.gTTS("hello " + name )
ns.save("ns.mp3")
playsound("ns.mp3")



PATH = "C:\chromedriver.exe" #please specify the path of the chrome driver here 
while True :
     print("waiting for your command...")
     print("Megaladon loaded up........")
     
     playsound("command.mp3")
     x  = input("enter your command : : :: ")
     x.lower()
     z = ["instagram" , "insta"]
     y = ["tweet" , "twitter"]
     mil = ["email" , "mail" , "mails" ,"emails"]
     #code to access insta
     for ins in z:
             if ins in  x :
                 #authentication of insta with meg pass
                 passw = input("enter your Megalodon  password :  ")
                 if passw == "SET-YOUR-PASSWORD":
                      playsound("insta.mp3")
                      driver = webdriver.Chrome(PATH)
                      driver.get("https://www.instagram.com/?hl=en")
                      sleep(3)
                      username_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
                      password_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
                      username_input.send_keys("ENTER-YOUR-USERNAME")#specify your username before running the script
                      password_input.send_keys("ENTER-YOUR-PASSWORD")#specify your password before running the script
                      btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
                      btn.click()
                      sleep(5)
                      nt_now1 = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
                      nt_now1.click()
                      sleep(2)
                      nt_now2 = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
                      nt_now2.click()
                      break
                 else:
                     break
      #code to access youtube              
     if "youtube" in x :

         auth = input("would you like to search for something in youtube(y/n) : ")
         auth.lower()
         if auth == "n":
            playsound("youtube.mp3")
            driver = webdriver.Chrome(PATH)
            driver.get("https://www.youtube.com/")
            
         elif auth == "y":
            inp_yt = input("what would you like to search for : ")
            search_voice = gtts.gTTS("opening youtube and searching for " + inp_yt , lang="en-ca")
            search_voice.save("search.mp3")
            playsound("search.mp3")
            driver = webdriver.Chrome(PATH)
            driver.get("https://www.youtube.com/")
            sleep(1)
            input_yt = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
            input_yt.send_keys(inp_yt)
            input_yt_btn = driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button")
            input_yt_btn.send_keys(Keys.RETURN)
            
    #code to access google
     if "search" in x :
         y = input("what would you like to seach for : ")
         srch = gtts.gTTS("opening google and searching for " + y ,  lang="en-ca")
         srch.save("srch.mp3")
         playsound("srch.mp3")
         driver = webdriver.Chrome(PATH)
         driver.get("https://www.google.co.in/")
         sleep(3)
         inp = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")
         inp.send_keys(y)
         inp.send_keys(Keys.RETURN)
         continue
         
    #code to access twitter
     for stuff in y:
         if stuff in x :
            opt = input("would you like to tweet or just open : ")
            if "tweet" in opt :
                twt = input("what would you like to tweet :")
                twtr = gtts.gTTS("opening twitter and tweeting" + twt , lang="en-ca")
                twtr.save("twtr.mp3")
                playsound("twtr.mp3")
                driver = webdriver.Chrome(PATH)
                driver.get("https://twitter.com/")
                sleep(2)
                log_in_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]")
                log_in_tweet.click()
                sleep(1)
                username_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
                username_tweet.send_keys("ENTER-TWITTER-USERNAME")
                password_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
                password_tweet.send_keys("ENTER-TWITTER-PASSWORD")
                tweet_btn  = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
                tweet_btn.click()
                sleep(2)
                tweet_entry = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
                tweet_entry.send_keys(twt)
                tweet_entry_btn = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]")
                tweet_entry_btn.click()
                break

                  
            else:
                sss = gtts.gTTS("opening twitter" , lang="en-ca")
                sss.save("sss.mp3")
                playsound("sss.mp3")
                driver = webdriver.Chrome(PATH)
                driver.get("https://twitter.com/")
                sleep(2)
                log_in_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div[1]/div/a[2]")
                log_in_tweet.click()
                sleep(1)
                username_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input")
                username_tweet.send_keys("ENTER-TWITTER-USERNAME")
                password_tweet = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input")
                password_tweet.send_keys("ENTER-TWITTER-PASSWORD")
                tweet_btn  = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div")
                tweet_btn.click()
                break
     
     
     for stuff_2 in mil:
         if stuff_2 in x :
             fd = gtts.gTTS("hang on a second " + name +  "i will open your mails as quick as possible")
             fd.save("fd.mp3")
             playsound("fd.mp3")
             driver = webdriver.Chrome(PATH)
             driver.get("https://login.yahoo.com/")
             sleep(3)
             det = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]")
             det.click()
             username_inp = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input")
             username_inp.send_keys("ENTER-MAILID")
             username_mail_btn = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input")
             username_mail_btn.click()
             sleep(2)
             password_mail = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[2]/input")
             password_mail.send_keys("ENTER-MAIL-PASSWORD")
             password_mail_btn = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/form/div[3]/button")
             password_mail_btn.click()
             sleep(5)
             mm = driver.find_element_by_xpath("/html/body/header/div/div/div/div[1]/div[1]/div[2]/ul/li[3]/a")
             mm.click()
             break



     


         






