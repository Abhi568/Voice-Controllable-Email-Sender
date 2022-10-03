This document will describe how to run and what are the libraries are present in this project

First refer to this vedio to get an idea how this project works (you can send audio,vedio, documents , images)

 It supports the extensions of images, example:'jpg','png','gif','jpeg'}
 It supports the extensions of files,example :'pdf','csv','xps','txt','ppt','docx','py','rar','mp4','mp3'}
 
 This project supports these many extensions which you can send( it supports other extensions also , which you can explore) but i have used this because these are the common ones.
 
https://drive.google.com/file/d/1TphM5RiIcWQbjkBwsax_K-SSq68_pEf-/view?usp=sharing
 

import smtplib  as s                       (The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP                                              listener daemon.)

Starttls                                   (Now, before invoking login, you invoke starttls. This causes the connection to become encrypted, which, in turn, protects your password                                            against being snooped)
 
from email.mime.multipart import MIMEMultipart( When anyone send the email , then at the Top proper Sender email sender , Receiver email sender and Subject is mentioned to receiver side)

from email.mime.text import MIMEText     (For Sending the text (Files ) )

from email.mime.image import MIMEImage   (For Sending the Images  ) 

import re                                (for expression(example : Verification of email address(regex))

import webbrowser                        (For opening webbrowser but what is the need of webbrowser because I have also given the documentation part in the program , there is a                                              button hyperlink or you can click on the speak button and speak , "hyperlink" that opens a window  automatically in which all the                                                    libraries link are present , when you click at any link , documentation part of that libaray will get open in webbrowesr)

import pyttsx3                           ((Text-to-Speech in Python (TTS) Using Pyttsx3, [pip install pyttsx3 ]) What ever you will write it will read  all your content)

engine = pyttsx3.init() (it  initializes the pyttsx3 package. The Instance of the initialized pyttsx3 package is stored in the engine variable. We are calling the variable engine as it works as the engine and converts Text-To-Speech whenever execute the functions from the package.)
                                           
(Say Function in pyttsx3)
engine.say("This is Text-To-Speech Engine Pyttsx3")
There is a built-in say() function in the pyttsx3 package that takes a string value and speaks it out.

(runAndWait Function)
 engine.runAndWait() (This function keeps track when the engine starts converting text to speech and waits for that much time, and do                                              not allow the engine to close. If we don’t write this code, it may happen that the engine might not work properly as the processes                                                will not be synchronized.)

After all the processes are over, we shut down the engine by calling stop() function.
                                           
                                           
                                           
 import speech_recognition             (There are many modules that can be used for speech recognition like google cloud speech, apiai, SpeechRecognition, watson-developer-                                            cloud, etc., but we are using Speech Recognition Module because it is easy to use since you don’t have to code scripts for accessing                                              audio devices also, it comes pre-packaged with many well-known API’s so you don’t have to signup for any kind of service which you                                                may have to while using any other module. And, it gets the job done pretty well.(https://www.codinground.com/speech-recognition/))
 
 from email import encoders
from email.mime.base import MIMEBase   (When creating Message objects from scratch, you often need to encode the payloads for transport through compliant mail servers. This is                                          especially true for image/* and text/* type messages containing binary data.
                                       The email package provides some convenient encoders in its encoders module. These encoders are actually used by the MIMEAudio and                                                MIMEImage class constructors to provide default encodings. All encoder functions take exactly one argument, the message object to encode.                                        They usually extract the payload, encode it, and reset the payload to this newly encoded value. They should also set the Content-Transfer-                                        Encoding header as appropriate.
                                       Note that these functions are not meaningful for a multipart message. They must be applied to individual subparts instead, and will raise                                        a TypeError if passed a message whose type is multipart.
                                       PAYLOAD: In general, the payload is the part of transmitted data that is the actual intended message. The payload excludes any headers or                                        metadata sent solely to facilitate payload delivery.
                                       Base64 Decode and Encode, a simple online tool that does exactly what it says; decodes Base64 encoding and encodes into it quickly and                                            easily. Base64 encode your data in a hassle-free way, or decode it into human-readable format.
                                       Base64 encoding schemes are commonly used when there is a need to encode binary data that needs be stored and transferred over media that                                        are designed to deal with textual data. This is to ensure that the data remains intact without modification during transport. Base64 is                                          used commonly in a number of applications including email via MIME, and storing complex data in XML or JSON.
                                       
                                           
                                           
                                           
