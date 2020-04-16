import sys

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

        for j in range(3):
            for k in tmp_list:
                if all([i in tmp_value for i in k]) == True:
                    tmp_value += dependencies[k]
        
        # sort values and remove duplicates
        # a set is useful because it does not allow duplicates
        new_dependency[keys_of_depencies[i]] = ''.join(sorted(set(tmp_value)))

    return new_dependency


    

    
    

    


# this function will find the candidate keys
# and return it as a list
def find_candidate_key(attributes, dependencies):
    pass




if __name__ == '__main__':

    len_of_attributes = int(sys.argv[1])
    attributes = sys.argv[2:len_of_attributes+2]
    len_of_func_dep = int(sys.argv[2+len_of_attributes])
    dependencies = sys.argv[len_of_attributes+3:]

    dependencies = dep_into_dict(dependencies)

    keys_of_depencies = get_only_keys_of_dependencies(dependencies)

    new_dependencies = handle_dependencies(keys_of_depencies, dependencies)
    print(new_dependencies)

    # dependencies = find_candidate_key(attributes, dependencies)





    