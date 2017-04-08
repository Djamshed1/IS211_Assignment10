#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Connecting to the database pets.db and asks user for person's ID"""

import sqlite3 as lite

con = lite.connect('pets.db')

with con:
    cur = con.cursor()
    
    while True:
        person_id = raw_input("Please enter persons ID who is a pet owner, or enter -1 to exit: ")

        if person_id == '-1':
            print 'Successfully exited. Please run the program again for further search.'
            raise SystemExit

        cur.execute("SELECT first_name, last_name, person.age, name, breed,"
                    "pet.age, dead FROM person, pet, person_pet "
                    "WHERE person.id = person_pet.person_id AND "
                    "pet.id = person_pet.pet_id AND person.id=(?)", (person_id))

        person = cur.fetchall()

        if len(person) == 0:
            print 'Invalid ID number entered.'
            continue

        for row in person:
            first_name = row[0]
            last_name = row[1]
            age = row[2]
            pet_name = row[3]
            pet_type = row[4]
            pet_age = row[5]
            living = row[6]
            if living == 1:
                print ('{} {}, {} years old').format(first_name, last_name,
                                                     age)
                print ('{} {} owned {}, a {}, '
                       'that was {} years old.').format(first_name, last_name,
                                                       pet_name, pet_type,
                                                       pet_age)
            else:
                print ('{} {} owned {}, a {}, '
                       'that was {} years old.').format(first_name, last_name,
                                                       pet_name, pet_type,
                                                       pet_age)
