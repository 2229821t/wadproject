import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'wadproject.settings')

import django

django.setup()

from LanguageExchange.models import MyUser


def populate():

    
    
    for i in range(0,10):
        User1 =  {  "email": str(i)+"23331c@student.gla.ac.uk",
                    "username": "Daivid"+str(i),
                    "password":"123456789",
                    "Nationalityty": "ALBANIA",
                    "Mother_language": "ALBANIAN",
                    "Wish_language": "ENGLISH",
                     "Profile_image":"profile_images/a"+str(i)+".jpg",
                     "status_message":"Hello I am David"+str(i)
                    }
        c=User(User1["email"],User1["username"],User1["password"],User1["Nationalityty"],User1["Mother_language"],User1["Wish_language"],User1["Profile_image"],User1["status_message"])          
         
    
    for i in range(0,10):
        User1 =  {    "email": str(i)+"201d@student.gla.ac.uk",
                    "username": "Daren"+str(i),
                    "password":"123456789",
                    "Nationalityty": "AFGHANISTAN",
                    "Mother_language": "AFRIKAANS",
                    "Wish_language": "ENGLISH",
                     "Profile_image":"profile_images/b"+str(i)+".jpg",
                     "status_message":"Hello I am Daren"+str(i)
                    }
                    
        c=User(User1["email"],User1["username"],User1["password"],User1["Nationalityty"],User1["Mother_language"],User1["Wish_language"],User1["Profile_image"],User1["status_message"])          
    
    for i in range(0,10):
        User1 =  {    "email": str(i)+"01c@student.gla.ac.uk",
                    "username": "Keil"+str(i),
                    "password":"123456789",
                    "Nationalityty": "AMHARIC",
                    "Mother_language": "AMHARIC",
                    "Wish_language": "ENGLISH",
                     "Profile_image":"profile_images/c"+str(i)+".jpg",
                     "status_message":"Hello I am Keil"+str(i)
                    }
                    
        c=User(User1["email"],User1["username"],User1["password"],User1["Nationalityty"],User1["Mother_language"],User1["Wish_language"],User1["Profile_image"],User1["status_message"])          


    
    i=0    
    for M in MyUser.objects.all():
            
           
            if i is 9:
                print("******************************************************KEEP POPULATING :)********************************************************************************")
                i=0;
                
            print("Email: "+"{0}".format(str(M)),"Nationality: "+M.Nationality,"Native_language: "+M.Mother_language,"Wish_language: "+M.Wish_language)
            i=i+1





    
                     

    
    
      
    
    
  
   
def User(email, username,password,Nationality,Mother_language,Wish_language,Profile_image,status_message):
   M = MyUser.objects.get_or_create(email=email)[0]
   M.username=username
   M.password=password
   M.Nationality=Nationality
   M.Mother_language=Mother_language
   M.Wish_language=Wish_language
   M.password=password
   M.status_message=status_message
   M.Profile_image=Profile_image
   M.save() 
   return M




# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    print("*******************************  NOW ONLY AVAILABLE SEARCH LANGUAGES ARE AFRIKAANS,ALBANIAN,AMHARIC  *******************************")
