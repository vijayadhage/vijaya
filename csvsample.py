import csv

def set_values():
    ans1 = float(input('Please enter the first number: '))

    ans2 = float(input('Please enter the second number: '))

    ans3 = float(input('Please enter the third number: '))

    levels = int(input('Please set the amount of levels between 5 and 10: '))


    return (ans1, ans2, ans3, levels) 


def display_model_values(ans1, ans2, ans3, levels):
    print('The outcome for model 1 is ',ans1)
    print('The outcome for model 2 is ',ans2)
    print('The outcome for model 3 is ',ans3)
    print('The number of levels are ',levels)


def run_model(ans1, ans2, ans3, levels):
    total = ans1+ans2+ans3
    print ("\t","Level","\t","Answer 1","\t","Answer 2","\t","Answer 3","\t","Total")
    for i in range (0,levels+1):
        print("\t",i,"\t\t",ans1,"\t\t",ans2,"\t\t",ans3,"\t\t",total)
        result1 =ans2*ans3
        result2 = ans2/ans1
        total = ans1+result1+result2
    return (i,result1, result2, total)


def export_data(ans1,ans2,ans3,total):
    table = [ans1, ans2, ans3,total]

    nameoffile = input('what would you like to call the filename')
    nameoffile = open(nameoffile+".csv","w")
    csv_file_ref = csv.writer(nameoffile)
    csv_file_ref.writerow(table)
    nameoffile.close()

##    with open(nameoffile+'.csv', 'w') as csvfile:
##        writer = csv.writer(csvfile)
##        writer.writerow(r) for r in table]




choice = ''
count = 0
while choice != 'q':
    print('Main Menu')
    print ('1)Set Model Values')
    print ('2)Display Model Values')
    print ('3)Run Model')
    print ('4)Export Data')
    print ('Q)Quit')
    choice = input('Please Enter Choice')


    if choice =='1':
        ans1, ans2, ans3, levels = set_values()
        count = count +1

    elif choice == '2':
        if count < 1:
           print ('you need to choose option 1 first')
        else:
            display_model_values(ans1,ans2,ans3,levels)


    elif choice =='3':
        if count < 1:
            print('you need to choose option 1 first')
        else:
            run_model(ans1,ans2,ans3,levels)

    elif choice =='4':
        if count < 1:
           print ('you need to choose option 1 first')
        else:
            export_data(ans1,ans2,ans3,total)

    elif choice == 'Q':
            break
    else:
        print('not an option')


