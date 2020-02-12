import msvcrt
while True:
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        print(key_stroke)   # will print which key is pressed
        if key_stroke == "0":
          num0 = True
        else:
          if key_stroke == "3":
            if num0 == True:
            num3 = True
          else:
            
        
          
