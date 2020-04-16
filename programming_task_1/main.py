import sys
from itertools import combinations

# This function turns the functional dependencies
# into a dicitonary
def dep_into_dict(dependencies):
    func_dep = dict()
    for i in range(len(dependencies)):
        tmp_list = dependencies[i].split(',')
        func_dep[tmp_list[0]] = tmp_list[1]
    return func_dep

def get_only_keys_of_dependencies(dependencies):
    tmp_list = []
    for k in dependencies.keys():
        tmp_list.append(k)
    return tmp_list

def handle_dependencies(keys_of_depencies, dependencies):
    new_dependency = dict()
    for i in range(len(keys_of_depencies)):
        tmp_list = keys_of_depencies[:i] + keys_of_depencies[i+1:]
        tmp_value = keys_of_depencies[i] + dependencies[keys_of_depencies[i]]
        for unused_var in range(3):
            for k in tmp_list:
                if all([i in tmp_value for i in k]) == True:
                    tmp_value += dependencies[k]
        # sort values and remove duplicates
        # a set is useful because it does not allow duplicates
        new_dependency[keys_of_depencies[i]] = ''.join(sorted(set(tmp_value)))
    return new_dependency

def turn_attributes_to_string(attributes):
    return ''.join(sorted(attributes))

def getCombo(rLen:int, relation:list):
    """Return different combination of relations"""
    res = set()
    for i in range(rLen+1):
        for subset in combinations(relation,i):
            if len(subset)==0:
                continue
            else:
                res.add(subset)
    return sorted([list(item) for item in res],key=len)

def get_final_list_of_candidate_keys(res):
    result = []
    mini = len(res[0])

    # check for the minimal length of key that is not 1
    for i in range(1,len(res)):
        if len(res[i]) != 1 and len(res[i]) < mini:
            mini = len(res[i])
    
    # get all the possible results
    for item in res:
        if len(item) <= mini:
            result+=[item]

    # final check to make sure that the keys whose length is not 1
    # does not contain a key another candidate key with a length of
    fRes =[]
    for item in result:
        check = True
        for char in item:
            if char in result:
                check = False
                break
        if len(item) == 1:
            check = True
        
        if check:
            fRes += ["".join(sorted(item))]

    return fRes

def find_possible_candidate_keys(attributes, new_dependencies):
    tmp = []
    # print(attributes)
    # print(new_dependencies)
    for k in new_dependencies:
        if new_dependencies[k] == attributes:
            tmp += [k]
            continue
        else:
            missing_vals = list(set(attributes) - set(new_dependencies[k]))
            combo = getCombo(len(missing_vals), missing_vals)

            # check all combo to see if it is a candidate key
            for c in combo:
                temp = "".join(sorted(k+"".join(c)))
                tempval = "".join(sorted(k+"".join(c)))
                for j in range(3):
                    for key in new_dependencies:
                        if all([i in tempval for i in key]):
                            tempval+=new_dependencies[key]

                if "".join(sorted(set(tempval))) == attributes:
                    tmp +=[temp]
    # turn list into a set and back into a list
    # to remove all duplicates 
    tmp = list(set(tmp))
    final_list = get_final_list_of_candidate_keys(tmp)
    return final_list

def print_candidate_keys(final_keys):

    for each_k in final_keys:
        print(f'Candidate Keys are: {each_k}')


    
if __name__ == '__main__':

    len_of_attributes = int(sys.argv[1])
    attributes = sys.argv[2:len_of_attributes+2]
    len_of_func_dep = int(sys.argv[2+len_of_attributes])
    dependencies = sys.argv[len_of_attributes+3:]

    dependencies = dep_into_dict(dependencies)
    # print(dependencies)

    keys_of_depencies = get_only_keys_of_dependencies(dependencies)

    new_dependencies = handle_dependencies(keys_of_depencies, dependencies)
    # print(new_dependencies)

    attributes = turn_attributes_to_string(attributes)
    # print(attributes)

    final_keys = find_possible_candidate_keys(attributes, new_dependencies)
    
    print_candidate_keys(final_keys)

    # dependencies = find_candidate_key(attributes, dependencies)





    