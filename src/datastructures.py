
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from ast import Delete
from operator import indexOf
from pickle import NONE
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {
                "id": 0,
                "first_name": "John",
                "age": 33,
                "lucky_numbers": "7, 13, 22"
            },

            {
                "id": 1,
                "first_name": "Jane",
                "age": 35,
                "lucky_numbers": "10, 14, 3"
            },

             {
                "id": 2,
                "first_name": "Jimmy",
                "age": 5,
                "lucky_numbers": "1"
            }
        ]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def _generateNumber(self):
        luckynumbers = []
        for i in range(0,3):
            luckynumbers.append(str(randint(0, 99)))
        return ",".join(luckynumbers)
            

    def add_member(self, member):
        self._members.append(member)
        pass

    def delete_member(self, id):
        
        # for index, individual in self._members:
        #     if individual.id == id:
        #         return self._members.pop(index)

        deleteTheMember = filter(lambda i: i.id != id, self._members)
        self._members = deleteTheMember
        return 
        pass

    def get_member(self, id):
        getTheMember = filter(lambda i: i.id == id, self._members)
        try:   
            return getTheMember[0],
        except IndexError: 
            return None
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
