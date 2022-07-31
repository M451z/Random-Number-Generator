import time
import sys

def load():
  print("""
    _____        _             _                                     
   | ____|_ __  (_) ___  _   _| |                                    
   |  _| | '_ \ | |/ _ \| | | | |                                    
   | |___| | | || | (_) | |_| |_|                                    
   |_____|_| |__/ |\___/ \__, (_)           __  __ _  _  ____  _     
   |  \/  | __|__/__| | _|___/ |__  _   _  |  \/  | || || ___|/ |____
   | |\/| |/ _` |/ _` |/ _ \ | '_ \| | | | | |\/| | || ||___ \| |_  /
   | |  | | (_| | (_| |  __/ | |_) | |_| | | |  | |__   ____) | |/ / 
   |_|  |_|\__,_|\__,_|\___| |_.__/ \__, | |_|  |_|  |_||____/|_/___|
                                    |___/                            
   """)
  
  animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
  
  for i in range(len(animation)):
      time.sleep(0.4)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()
  
  print("\n")