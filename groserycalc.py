from pathlib import Path

#Create a dirrectory
path_to_folder = Path('data')
path_to_folder.mkdir(exist_ok=True) #Checking if dir is exist

#Create log file
path_to_file = Path(path_to_folder / 'log.txt')

#Ask user to put 1 or 2 from keyboard
what_to_do = input('What do you whant to do: (print 1 - to add new, print 2 - to summ all ')

#create variale for save value from file
qty = 0
total = 0

if  what_to_do == '1':
    #open file to append 
    with open(path_to_file, 'a') as f:
        while True:
            x = int(input('Enter qty :'))
            y = float(input('Enter weight: '))
            if x == 0:
                break
            f.write(str(x))
            f.write('|')
            f.write(str(y))
            f.write('\n')

else:
    with open(path_to_file) as f:
       #open file to read 
       while True:
           line = f.readline()
           if not line:
               break
           #we read data from the file into a list, convert it into separate variables and count
           separate = line.split('|')
           

           conver_to_int = int(separate[0])
           qty = qty+ conver_to_int

           total_conver_to_float = float(separate[1])
           total = total + total_conver_to_float
    print(f"Thank you for yousing. Qty is {qty}. Total weight is {total}")
           



           
        
