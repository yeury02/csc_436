import sys
import itertools

# This function turns the functional dependencies
# into a dicitonary
def dep_into_dict(dependencies):
    func_dep = dict()
    for i in range(len(dependencies)):
        tmp_list = dependencies[i].split(',')
        # this line puts each character either as key of value
        # e.g A,B which is A->B would be turn into A:B
        func_dep[tmp_list[0]] = tmp_list[1]
    return func_dep

# This function returns a list of keys in functional dependency dict
def get_only_keys_of_dependencies(dependencies):
    tmp_list = []
    for k in dependencies.keys():
        # puts every key in dictionary into a list
        tmp_list.append(k)
    return tmp_list

# returns the new functional dependencies expanded
def handle_dependencies(keys_of_depencies, dependencies):
    new_dependency = dict()
    flag = True
    for i in range(len(keys_of_depencies)):
        tmp1 = keys_of_depencies[:i]
        tmp2 = keys_of_depencies[i+1:]
        tmp3 = keys_of_depencies[i]
        tmp4 = dependencies[keys_of_depencies[i]]
        tmp_list = tmp1 + tmp2
        tmp_value = tmp3 + tmp4
        # iterate multiple times for assurance
        for unused_var in range(0, 3, 1):
            for k in tmp_list:
                if all([i in tmp_value for i in k]) == flag:
                    tmp_value += dependencies[k]
        # sort values and remove duplicates
        # a set is useful because it does not allow duplicates
        tmp_value = sorted(set(tmp_value))
        new_dependency[keys_of_depencies[i]] = ''.join(tmp_value)
    return new_dependency

# this function simply turns the list of attributes into a sorted string
def turn_attributes_to_string(attributes):
    return ''.join(sorted(attributes))

# this functions returns combinations of attributes (different ones)
def combinations(len_of_missing_vals, missing_vals):
    comb = set()
    for i in range(0, 1+len_of_missing_vals, 1):
        for j in itertools.combinations(missing_vals,i):
            if len(j)==0:
                continue
            else:
                # adds valye randomly to the set
                # does not add repeated values
                comb.add(j)
    ans = sorted([list(k) for k in comb],key=len)
    return ans 

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
    for k in new_dependencies:
        if new_dependencies[k] == attributes:
            tmp += [k]
            continue
        else:
            x = set(attributes)
            y = set(new_dependencies[k])
            missing_vals = list(x-y)
            len_of_missing_vals = len(missing_vals)

            all_combinations = combinations(len_of_missing_vals, missing_vals)

            # check all_combinations and determine if it's a candidate key
            for comb in all_combinations:
                temp = "".join(sorted(k+"".join(comb)))
                tempval = "".join(sorted(k+"".join(comb)))
                for j in range(3):
                    for key in new_dependencies:
                        if all([i in tmp for i in key]):
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

    len_of_attributes = int(sys.argv[1])                            # get the length of attributes
    attributes = sys.argv[2:len_of_attributes+2]                    # grabs each attribute
    len_of_func_dep = int(sys.argv[2+len_of_attributes])            # length of functional dependencies
    dependencies = sys.argv[len_of_attributes+3:]                   # grabs each functional dependency
    
    dependencies = dep_into_dict(dependencies)                      # turn list of dependencies into a dictionary (key:value pair)
    keys_of_depencies = get_only_keys_of_dependencies(dependencies) # returns only the keys of functional dependencies
    new_dependencies = handle_dependencies(keys_of_depencies, dependencies)  # expands functional dependencies as a dictionary
    attributes = turn_attributes_to_string(attributes)                       # turns list of attributes to sorted string
    final_keys = find_possible_candidate_keys(attributes, new_dependencies) # This is where most of the work is done!!!!
                                                                            # 
    print_candidate_keys(final_keys)





    