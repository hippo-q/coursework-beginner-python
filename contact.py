#!/usr/bin/env python3
"""Analyse a given dataset of sick people and their contacts. Identify
characteristics related to disease spreading as set out in the coursework
brief.
Student number:
"""

from calendar import c
import sys
import os.path
from format_list import format_list

def file_exists(file_name: str):
    """Verify that the file exists.

    Args:
        file_name (str): name of the file

    Returns:
        boolean: returns True if the file exists and False otherwise.
    """

    return os.path.isfile(file_name)


def parse_file(file_name: str):
    """Read the input file, parse the contents and return a dictionary
    containing sick people and their contacts.

    Args:
        file_name (str): Contains the name of the file.

    Returns:
        dict: Contains contact tracing information. The keys are the sick
        people. The corresponding values are stored in a list that contains
        the names of all the people that the sick person has had contact with.
    """

    dataset = {}
    with open(file_name, 'r') as file:
        for line in file.readlines():
            split = line.strip().split(',')
            dataset[split[0]] = split[1:]

    return dataset



def find_patients_zero(contacts_dic: dict):
    """Return list of people who do not appear in any sick person's contact
    list.

    Args:
        contacts_dic (dic): each entry is a sick person's name (key) and their
        list of contacts.

    Returns:
        list: names of people who do not appear in any sick person's contact
        list.
    """
    # Make this two lines so it is < 80 chars per line ;)

    all_contacts = _all_contacts(contacts_dic)
    return [sick for sick in contacts_dic.keys() if sick not in all_contacts]


def find_potential_zombies(contacts_dic: dict):
    """Return list of people who do not appear to be sick yet. They appear in
    the contact lists but do not have their own contacts entry.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: names of people who are not listed as sick.
    """

    all_sick = contacts_dic.keys()
    zombies = []

    for contact in _all_contacts(contacts_dic):
        if contact not in zombies and contact not in all_sick:
            zombies.append(contact)

    return zombies


def find_not_zombie_nor_zero(contacts_dic: dict, patients_zero_list: list, zombie_list: list):
    """Return names of those people who are neither a zombie nor a patient
    zero.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.
        patients_zero_list (list): sick people identified as patient zero(es).
        zombie_list (list): contacts who are not a sick person (don't have
        their own contact list).

    Returns:
        list: people who are neither a zombie nor a patient zero.
    """

    # This simply just means everyone that is sick
    # And is not patient 0..
    all_sick = contacts_dic.keys()

    return [sick for sick in all_sick if sick not in patients_zero_list]


def find_most_viral(contacts_dic: dict):
    """Return the most viral contacts: those sick people with the largest
    contact list

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: contains the names of sick people who have the largest contact
        lists
    """
    if len(contacts_dic.values()) == 0:
        return []

    most_contacts = len(max(contacts_dic.values(), key = len))
    if most_contacts == 0:
        return []

    most_virals = []
    for sick, contacts in contacts_dic.items():
        if len(contacts) == most_contacts:
            most_virals.append(sick)
    return most_virals


def find_most_contacted(contacts_dic: dict):
    """Return the contact or contacts who appear in the most sick persons'
    contact list.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their list
        of contacts.

    Returns:
        list: contains the names of contacts who appear in the most sick
        persons' contact list.
    """
    traces = {}
    for contact in _all_contacts(contacts_dic):
        traces[contact] = 1 if contact not in traces else traces[contact] +  1

    if not traces:
        return []

    most_traces = []
    for contact, num_traces in traces.items():
        if num_traces == max(traces.values()):
            most_traces.append(contact)
    return most_traces

def find_maximum_distance_from_zombie(contacts_dic: dict, zombie_list: list):
    """Return the maximum distance from a zombie for everyone in the dataset.
    The maximum distance from a potential zombie is the longest contact
    tracing path downwards in the dataset from a sick person to a potential
    zombie.

    Args:
        contacts_dic (dic): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): all zombies

    Returns:
        dic: contains heights (maximum distance) of person from a zombie
    """
    
    max_dists = {}
    for p in _everyone(contacts_dic):
        max_dists[p] = _find_max_dist(p, 0, contacts_dic, max_dists)

    return max_dists

def find_spreader_zombies(contacts_dic: dict, zombie_list: list):
    """Returns all sick people who has had only contacts
    with potential zombies

    Args:
        contacts_dic (dict): each entry is a sick person's name and their
        list of contacts.
        zombie_list (list): list of zombies

    Returns:
        (list): all spreader zombies
    """
    spreader_zombies = []
    for sick_person, contacts in contacts_dic.items():
        if contacts and all([contact in zombie_list for contact in contacts]):
            spreader_zombies.append(sick_person)

    return spreader_zombies

def find_regular_zombies(contacts_dic: dict, spreader: list, zombie_predator: list):
    """Return all regular zombies who has had contacts with regular zombies
    and sick people

    Args:
        contacts_dic (dict): each entry is a sick person's name and their
        list of contacts.
        spreader (list): list of spreader zombies
        zombie_predator (list): list of zombie_predators

    Returns:
        list: list of regular zombies
    """

    regular_zombies = []
    for sick, contacts in contacts_dic.items():
        if sick not in spreader and sick not in zombie_predator and contacts:
            regular_zombies.append(sick)

    return regular_zombies

def find_zombie_predator(contacts_dic: dict):
    """Returns all zombie predators who has had contacts with only sick people

    Args:
        contacts_dic (dict): each entry is a sick person's name and their
        list of contacts.

    Returns:
        list: all zombie predators
    """
    zombie_predator = []
    sick_people = contacts_dic.keys()
    for sick_person, contacts in contacts_dic.items():
        if contacts and all([contact in sick_people for contact in contacts]):
            zombie_predator.append(sick_person)

    return zombie_predator

def _find_max_dist(person, dist, contacts, dists):
    """Recursively fill the max_dists dictionary with every person's
    max distance from a zombie. The dictionary is used to remove any 
    redundant calculations. 

    Args:
        person (str): the name of the person we are calculating for
        dist (int): the current distance (depth of the search)
        contacts (dic): each entry is a sick person's name and their
        list of contacts.
        dists (dic): contains heights (max distances) of a person from a 
        zombie
        check (list): contains everyone who passed through the recursion
        calls

    Returns:
        (int): the maximum distance for person from a zombie
    """
    if person in dists:
        return dists[person] + dist

    if person not in contacts:
        return dist

    dists = []
    for p in contacts[person]:
        dists.append(_find_max_dist(p, dist + 1, contacts, dists))

    return max(dists) if dists else 0
    

def _everyone(contacts_dic: dict):
    """Returns a list of everyone there are in the data set.

    Args:
        contacts_dic (dict): each entry is a sick person's name and their
        list of contacts.

    Returns:
        set: contains names of everyone
    """
    everyone = _all_contacts(contacts_dic)
    everyone.extend(contacts_dic.keys())

    return set(everyone)


def _all_contacts(contacts_dic: dict):
    """Returns a list of every contacts there are in the data set.

    Args:
        contacts_dic (dict): each entry is a sick person's name and their
        list of contacts.

    Returns:
        list: contains names of all contacts
    """
    return [c for contacts in contacts_dic.values() for c in contacts]

def main():
    """Main logic for the program.
    """
    filename = ""
    # Get the file name from the command line or ask the user for a file name
    args = sys.argv[1:]
    if len(args) == 0:
        filename = input("Please enter the name of the file: ")
    elif len(args) == 1:
        filename = args[0]
    else:
        print("""\n\nUsage\n\tTo run the program type:
        \tpython contact.py infile
        where infile is the name of the file containing the data.\n""")
        sys.exit()

    # Section 2. Check that the file exists
    if not file_exists(filename):
        print("File does not exist, ending program.")
        sys.exit()

    # Section 3. Create contacts dictionary from the file
    # Complete function parse_file().
    contacts_dic = parse_file(filename)
    # print(contacts_dic)
    # Section 4. Print contact records
    # Add your code here.

    # Section 5. Identify the possible patients zero. Patient(s) zero are those
    #    people who do not appear in another's contact list.
    # Complete function find_patients_zero() and add code here to print the
    # output as specified in the brief.
    patients_zero_list = find_patients_zero(contacts_dic)

    # Section 6. Find potential zombies. Potential zombies are those people who
    # have been in contact with a sick person but have not yet been identified
    # as sick.
    # Complete function find_potential_zombies() and add code here to print the
    # output as specified in the brief.
    zombie_list = find_potential_zombies(contacts_dic)

    # Section 7. Find people who are neither patient zero(s) nor potential
    # zombies.
    # Complete function find_not_zombie_nor_zero() and add code here to print
    # the output as specified in the brief.
    not_zombie_nor_zero = find_not_zombie_nor_zero(contacts_dic,
                                    patients_zero_list, zombie_list)

    # Section 8. Find the most viral people.
    # Complete function find_most_viral() and add code here to print the
    # output as specified in the brief.
    most_viral_list = find_most_viral(contacts_dic)


    # Section 9. Find most contacted. The people who appear in the most sick
    # persons' lists.
    # Complete function find_most_contacted() and add code here to print the
    # output as specified in the brief.
    most_contacted = find_most_contacted(contacts_dic)

    # Section 10. Maximum Distance from Zombie
    # Complete function find_maximum_distance_from_zombie() and add code here
    # to print the output as specified in the brief.
    heights_dic = find_maximum_distance_from_zombie(contacts_dic, zombie_list)

    ######
    # Extra functionality - no function headers provided.
    ######

        # Additional:
    # Find all spreader zombies
    spreader_zombies = find_spreader_zombies(contacts_dic, zombie_list)

    # Find all zombie predators
    zombie_predators = find_zombie_predator(contacts_dic)

    # Find all regular zombies
    regular_zombies = find_regular_zombies(contacts_dic, spreader_zombies, zombie_predators)

    ######
    # Print output as format
    ######
    
    print("\nContact Records: ")
    
    for sick, contacts in contacts_dic.items():
        print(f" {sick} had contact with {format_list(contacts)}")

    print("\n")
    print(f"Patient Zero(s): {format_list(patients_zero_list)}")
    print(f"Potential Zombies: {format_list(zombie_list)}")
    print(f"Neither Patient Zero or Potential Zombie: {format_list(not_zombie_nor_zero)}")
    print(f"Most Viral People: {format_list(most_viral_list)}")
    print(f"Most Contacted: {format_list(most_contacted)}")

    print("\nHeights:")
    height_dic_items = list(heights_dic.items())
    sorted_tup = sorted(height_dic_items, key = lambda x: x[1], reverse=True)
    for person, dist in sorted_tup:
        print(f" {person}: {dist}")

    print("\nFor additional marks:")
    print(f" Spreader Zombies: {format_list(spreader_zombies)}")
    print(f" Regular Zombies: {format_list(regular_zombies)}")
    print(f" Zombie Predators: {format_list(zombie_predators)}")



if __name__ == "__main__":
    main()
