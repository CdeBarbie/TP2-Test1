party_name =  ""
member_count = 0
reg_number = 0
Parties = {'party_name': [party_name], "reg_number":[reg_number], "member_count":[member_count]}

def register_party():
    party_name = input("Enter party name: ")
    reg_number = input("Enter registration number: ")
    reg_number = int(reg_number)
    member_count = input("Enter number of mebers: ")
    member_count = int(member_count)
    
    for n in Parties:
        if member_count >= 1000:
             print("This party ", party_name, "is registered with a number of ", member_count)
        
        else:
            print("This party ", party_name, "is not registered with a number of ", member_count, "due to a minimum of members")

register_party()
