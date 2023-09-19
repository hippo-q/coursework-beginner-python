import contact

TEST_CONTACT_DICT_1 = {}
TEST_CONTACT_DICT_2 = {"foo": []}
TEST_CONTACT_DICT_3 = {"foo": [], "bar": []}
TEST_CONTACT_DICT_4 = {"foo": ["bar"], "bar": []}
TEST_CONTACT_DICT_5 = {"foo": ["bar", "baz", "qux"], "bar": []}
TEST_CONTACT_DICT_6 = {"foo": [], "bar": ["baz", "qux"], "qux": ["foo"], "quux": ["qux"], "quuux": ["foo", "bar", "baz", "quux"], "quuuux": ["quuux"]}

def test_file_exist_returns_true_on_file_found():
    assert contact.file_exists("DataSet0.txt") == True

def test_file_exist_returns_true_on_file_not_found():
    assert contact.file_exists("foo") == False

def test_contact_dict_1_patient_zero():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_1)) == set()

def test_contact_dict_2_patient_zero():
    assert set(contact.find_patients_zero(TEST_CONTACT_DICT_2)) == {"foo"}

def test_contact_dict_3_patient_zero():
    assert set(contact.find_patients_zero(TEST_CONTACT_DICT_3)) == set(("foo", "bar"))

def test_contact_dict_4_patient_zero():
    assert set(contact.find_patients_zero(TEST_CONTACT_DICT_4)) == {"foo"}

def test_contact_dict_5_patient_zero():
    assert set(contact.find_patients_zero(TEST_CONTACT_DICT_5)) == {"foo"}

def test_contact_dict_6_patient_zero():
    assert set(contact.find_patients_zero(TEST_CONTACT_DICT_6)) == {"quuuux"}

def test_contact_dict_1_potential_zombie():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_1)) == set()

def test_contact_dict_2_potential_zombie():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_2)) == set()

def test_contact_dict_3_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_3)) == set()

def test_contact_dict_4_potential_zombie():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_4)) == set()

def test_contact_dict_5_potential_zombie():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_5)) == {"baz", "qux"}

def test_contact_dict_6_potential_zombie():
    assert set(contact.find_potential_zombies(TEST_CONTACT_DICT_6)) == {"baz"}

def test_contact_dict_1_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_1)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_1)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_1, patient_zero_list, potential_zombies)) == set()

def test_contact_dict_2_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_2)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_2)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_2, patient_zero_list, potential_zombies)) == set()

def test_contact_dict_3_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_3)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_3)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_3, patient_zero_list, potential_zombies)) == set()

def test_contact_dict_4_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_4)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_4)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_4, patient_zero_list, potential_zombies)) == {"bar"}

def test_contact_dict_5_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_5)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_5)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_5, patient_zero_list, potential_zombies)) == {"bar"}

def test_contact_dict_6_neither_potential_zombie_or_patient_0():
    patient_zero_list = contact.find_patients_zero(TEST_CONTACT_DICT_6)
    potential_zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_6)
    assert set(contact.find_not_zombie_nor_zero(TEST_CONTACT_DICT_6, patient_zero_list, potential_zombies)) == {"foo", "bar", "qux", "quux", "quuux"}

def test_contact_dict_1_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_1)) == set()

def test_contact_dict_2_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_2)) == set()

def test_contact_dict_3_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_3)) == set()

def test_contact_dict_4_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_4)) == {"foo"}

def test_contact_dict_5_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_5)) == {"foo"}

def test_contact_dict_6_most_viral():
    assert set(contact.find_most_viral(TEST_CONTACT_DICT_6)) == {"quuux"}

def test_contact_dict_1_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_1)) == set()

def test_contact_dict_2_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_2)) == set()

def test_contact_dict_3_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_3)) == set()

def test_contact_dict_4_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_4)) == {"bar"}

def test_contact_dict_5_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_5)) == {"bar", "baz", "qux"}

def test_contact_dict_6_most_contacted():
    assert set(contact.find_most_contacted(TEST_CONTACT_DICT_6)) == {"foo", "baz", "qux"}

def test_contact_dict_1_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_1)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_1, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == set()

def test_contact_dict_2_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_2)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_2, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == {("foo", 0)}

def test_contact_dict_3_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_3)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_3, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == {("foo", 0), ("bar", 0)}

def test_contact_dict_4_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_4)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_4, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == {("foo", 0), ("bar", 0)}

def test_contact_dict_5_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_5)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_5, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == {("foo", 1), ("bar", 0), ("baz", 0), ("qux", 0)}

def test_contact_dict_6_find_maximum_dist():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_6)
    dist_dict = contact.find_maximum_distance_from_zombie(TEST_CONTACT_DICT_6, zombie_list)
    distance_tuples = set(((person, dist) for person, dist in dist_dict.items()))
    assert distance_tuples == {("foo", 0), ("bar", 1), ("baz", 0), ("qux", 0), ("quux", 0), ("quuux", 2), ("quuuux", 3)}

def test_contact_dict_1_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_1)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_1, zombie_list)) == set()

def test_contact_dict_2_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_2)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_2, zombie_list)) == set()

def test_contact_dict_3_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_3)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_3, zombie_list)) == set()

def test_contact_dict_4_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_4)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_4, zombie_list)) == set()

def test_contact_dict_5_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_5)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_5, zombie_list)) == set()

def test_contact_dict_6_spreader_zombie():
    zombie_list = contact.find_potential_zombies(TEST_CONTACT_DICT_6)
    assert set(contact.find_spreader_zombies(TEST_CONTACT_DICT_6, zombie_list)) == set()

def test_contact_dict_1_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_1)) == set()

def test_contact_dict_2_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_2)) == set()

def test_contact_dict_3_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_3)) == set()

def test_contact_dict_4_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_4)) == {"foo"}

def test_contact_dict_5_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_5)) == set()

def test_contact_dict_6_zombie_predator():
    assert set(contact.find_zombie_predator(TEST_CONTACT_DICT_6)) == {"qux", "quux", "quuuux"}

def test_contact_dict_1_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_1)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_1)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_1, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_1, spreaders, predators)) == set()

def test_contact_dict_2_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_2)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_2)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_2, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_2, spreaders, predators)) == set()

def test_contact_dict_3_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_3)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_3)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_3, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_3, spreaders, predators)) == set()

def test_contact_dict_4_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_4)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_4)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_4, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_4, spreaders, predators)) == set()

def test_contact_dict_5_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_5)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_5)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_5, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_5, spreaders, predators)) == {"foo"}

def test_contact_dict_6_regular_zombie():
    zombies = contact.find_potential_zombies(TEST_CONTACT_DICT_6)
    predators = contact.find_zombie_predator(TEST_CONTACT_DICT_6)
    spreaders = contact.find_spreader_zombies(TEST_CONTACT_DICT_6, zombies)
    assert set(contact.find_regular_zombies(TEST_CONTACT_DICT_6, spreaders, predators)) == {"bar", "quuux"}

def test_everyone_function_with_contact_dict_1():
    assert set(contact._everyone(TEST_CONTACT_DICT_1)) == set()

def test_everyone_function_with_contact_dict_2():
    assert set(contact._everyone(TEST_CONTACT_DICT_2)) == {"foo"}

def test_everyone_function_with_contact_dict_3():
    assert set(contact._everyone(TEST_CONTACT_DICT_3)) == {"foo", "bar"}

def test_everyone_function_with_contact_dict_4():
    assert set(contact._everyone(TEST_CONTACT_DICT_4)) == {"foo", "bar"}

def test_everyone_function_with_contact_dict_5():
    assert set(contact._everyone(TEST_CONTACT_DICT_5)) == {"foo", "bar", "baz", "qux"}

def test_everyone_function_with_contact_dict_6():
    assert set(contact._everyone(TEST_CONTACT_DICT_6)) == {"foo", "bar", "baz", "qux", "quux", "quuux", "quuuux"}

def test_all_contacts_function_with_contact_dict_1():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_1)) == set()

def test_all_contacts_function_with_contact_dict_2():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_2)) == set()

def test_all_contacts_function_with_contact_dict_3():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_3)) == set()

def test_all_contacts_function_with_contact_dict_4():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_4)) == {"bar"}

def test_all_contacts_function_with_contact_dict_5():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_5)) == {"bar", "baz", "qux"}

def test_all_contacts_function_with_contact_dict_6():
    assert set(contact._all_contacts(TEST_CONTACT_DICT_6)) == {"foo", "bar", "baz", "qux", "quux", "quuux"}