This document will describe how to run and what are the libraries are present in this project

import smtplib  as s                       (The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP                                              listener daemon.)

Starttls                                   (Now, before invoking login, you invoke starttls. This causes the connection to become encrypted, which, in turn, protects your password                                            against being snooped)
 
from email.mime.multipart import MIMEMultipart( When anyone send the email , then at the Top proper Sender eamil sender , Receiver email sender and Subject is mentioned )

from email.mime.text import MIMEText     (For Sending the text (Files ) )

from email.mime.image import MIMEImage   (For Sending the Images  ) 

import re                                (for expression(example : Verification of email address(regex))

import webbrowser                        (For opening webbrowser and what is the need of webbrowser because I have also given the documentation part in the program , there is a                                              button hyperlink or you can click on the speak button and speak "hyperlink" a window will get open atomatically in which all the                                                    libraries link are prsent , when you click at any link , documentation part of that libaray will get open in webbrowesr)

import pyttsx3                           ((Text-to-Speech in Python (TTS) Using Pyttsx3, [pip install pyttsx3 ]) What ever you will write it will read  all your content)

                                          engine = pyttsx3.init() (it  initializes the pyttsx3 package. The Instance of the initialized pyttsx3 package is stored in                                                       the engine variable. We are calling the variable engine as it works as the engine and converts Text-To-Speech whenever execute the                                               functions from the package.)
                                           
                                          (Say Function in pyttsx3)
                                          engine.say("This is Text-To-Speech Engine Pyttsx3")
                                          There is a built-in say() function in the pyttsx3 package that takes a string value and speaks it out.

                                           (runAndWait Function)
                                           engine.runAndWait() (This function keeps track when the engine starts converting text to speech and waits for that much time, and do                                              not allow the engine to close. If we don’t write this code, it may happen that the engine might not work properly as the processes                                                will not be synchronized.)

                                           After all the processes are over, we shut down the engine by calling stop() function.
                                           
                                           
                                           
                                           
                                           
   import speech_recognition             (There are many modules that can be used for speech recognition like google cloud speech, apiai, SpeechRecognition, watson-developer-                                            cloud, etc., but we are using Speech Recognition Module because it is easy to use since you don’t have to code scripts for accessing                                              audio devices also, it comes pre-packaged with many well-known API’s so you don’t have to signup for any kind of service which you                                                may have to while using any other module. And, it gets the job done pretty well.(https://www.codinground.com/speech-recognition/))
                                           
                                           
                                           
