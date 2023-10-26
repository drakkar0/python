#An application that counts apple boxes and total weight. 
#Those. the user enters the number of boxes and weight. and so on until 0 is entered. 
#After this, it will be possible to get the total number of boxes and total weight

from pathlib import Path
import csv

def inputvalue():
    #input qty 
    while True:
        try: 
             qty = int(input('Enter qty :'))
             break
        except ValueError as e:
            print(e)
    #input weight           
    while True:
        try: 
             kg = float(input('Enter weight: '))
             break
        except ValueError as e:
            print(e)

    return qty, kg    

#Create a dirrectory
path_to_folder = Path('groserycalc/data')
path_to_folder.mkdir(exist_ok=True) #Checking if dir is exist

#Create log file
path_to_file = Path(path_to_folder / 'log.csv')

#Ask user to put 1 or 2 from keyboard
what_to_do = input('What do you whant to do: (print 1 - to add new, print 2 - to summ all ')

#create variale for save value from file
qty = 0
total = 0

if  what_to_do == '1':
    #open file to append 
    with open(path_to_file, 'a',newline='') as csv_file:
        while True:
            x, y = inputvalue()
            
            if x == 0:
                break
            writer = csv.writer(csv_file, delimiter=';')
            writer.writerow([x,y])
 
            

else:
    with open(path_to_file) as csf_file:
       #open file to read 
    #    while True:
    #        line = f.readline()
    #        if not line:
    #            break
    #        #we read data from the file into a list, convert it into separate variables and count
    #        separate = line.split('|')
           

    #        conver_to_int = int(separate[0])
    #        qty = qty+ conver_to_int

    #        total_conver_to_float = float(separate[1])
    #        total = total + total_conver_to_float
        reader = csv.reader(csf_file, delimiter=';')
        for line in reader:
            print(line)
            conver_to_int = int(line[0])
            total_conver_to_float = float(line[1])

            qty = qty+ conver_to_int
            total = total + total_conver_to_float

    print(f"Thank you for yousing. Qty is {qty}. Total weight is {round(total,2)}")
           



           
        
