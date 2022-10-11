# Imports:
import threading # Imports module containing the Thread class.

def person_print(name, age, delay_time_ms = 1000):
   """
   person_print: Prints person data continuously with a specified interval.
         
                 - name         : The name of the person.
                 - age          : The age of the person.
                 - delay_time_ms: Time interval between prints.
   """
   import time
   while True:
      print("Name: " + str(name) + "")
      print("Age: " + str(age) + "\n")
      time.sleep(delay_time_ms / 1000.0)
   return 

def main():
   """
   main: Creating two threads and connecting to the function person_print with arguments.
         The threads are implemented by the Thread class of the threading module. To setup
         a thread, we set a target function with the use of the target argument and we set
         the functions parameters as a tuple with the use of the args argument. The arguments
         are enclosed with a parenthesis and ends with a decimal character. To start a thread
         we call the start method. To synchronize threads so that they all have to finish
         before continuing the program, we call the join method.
   """
   # Creating new threads, connecting to function person_print, sending person data:
   t1 = threading.Thread(target = person_print, args = ("Kalle Anka", 88, 2000, ))
   t2 = threading.Thread(target = person_print, args = ("Musse Pigg", 94, 500,))

   # Starting threads by calling the start method:
   t1.start()
   t2.start()

   # Synchronizing threads by calling the join method:
   t1.join()
   t2.join()

   return

# If this is the start script, the main function is called to start the program:
if __name__ == "__main__":
   main()