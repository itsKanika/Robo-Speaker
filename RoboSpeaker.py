import os
if __name__ =='__main__':
    print("welcome to ROBOSPEAKER -created by kanika")
    while True:
       x= input("enter what you want me to speak : ")
       if x=="q":
         break
       command=f"say {x}" 
       os.system(command)