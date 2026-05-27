def calculate_tip(bill,tip_percent):
    tip_amount=(bill*tip_percent)/100
    total_amount=bill+tip_amount

    return{
    "tip":tip_amount,
    "Total":total_amount
    }
bill1=calculate_tip(100,10)
bill2=calculate_tip(1200,5)
bill3=calculate_tip(200,20)
print(bill1)
print(bill2)
print(bill3)

#return:- it retun values                                           
#         Mostly used with function,value is stored and can be reused
#print:-used to print statement,here value cant be reused,it only used for printing statement