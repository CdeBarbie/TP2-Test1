"""2.3Implement a function called “update_voter_info” where each key is a voter_id and the
value is another dictionary containing name, voting_district and has_voted. The function
should update the voter’s information or add a vote if not already voted."""

import pandas as pd

"""party_name =  ""
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
register_party(countParty)"""

Voters = {'name': ["Luzuko"], 'voting_district': ["Halima Court"], "has_voted": ["has_voted"]}

def update_voter_info(Voters):
    print("Update voter's information: ")
    Voters.append({
        'name': input("update voter's name: "),
        'voting_district': input("update voter's voting district: "),
        'has_voted' != True: input("add vote"),
    })

    df = pd.DataFrame(Voters)

update_voter_info(Voters)

