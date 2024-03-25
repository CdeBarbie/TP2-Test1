"""2.2 Now a new party called MK party which has 5300 members wants to apply to register the
party for the next election. Write python statements that will show how will the function that
you created in question 2.1 be executed such that it registers the MK party if it meets the
criteria as per IEC regulations. Assume that the last party that was registered had a registration
number 10003318, and every new party that is being registered will be generated a registration
number that increments the last registered party by 1"""
import pandas as pd

party_name =  ""
member_count = 0
reg_number = 0

Parties = {'party_name': [party_name], "reg_number":[reg_number], "member_count":[member_count]}

countParty = input("Enter number of parties to be registered: ")
countParty = int(countParty)

def register_party(countParty):

    party_name =  set("MK PArty")
    member_count = set(5300)
    reg_number = set(1211112)

    lastRegnum = 10003318
    generate = 0

    for n in Parties:
        party_name = input("Enter party name: ")
        reg_number = input("Enter registration number: ")
        reg_number = int(reg_number)
        generate = lastRegnum + 1

        member_count = input("Enter number of mebers: ")
        member_count = int(member_count)

        for n in Parties:
            if member_count >= 1000:
                    print("This party ", party_name, "is registered with a number of ", member_count)
            
            else:
                print("This party ", party_name, "is not registered with a number of ", member_count, "due to a minimum of members")
            return generate
    
    df = pd.DataFrame(Parties)

register_party(countParty)

