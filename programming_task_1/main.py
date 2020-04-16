import sys

# def user_input():
#     len_of_attributes = int(input('Please input the length of attributes of your entity: '))
#     attributes = input('Please enter how many attributes you would like to have, each attribute'
#                         ' can only be represented by a single character, and each char should'
#                         ' should be seperated by a space in between: ')


if __name__ == '__main__':
    
    # len_of_attributes = int(sys.argv[1])
    # print(len_of_attributes)
    # # print(type(len_of_attributes))
    # # attributes = []
    # # for att in len_of_attributes-2:
    # #     attributes.append(sys.)
    # # print(attributes)

    # attributes = sys.argv[2:len_of_attributes]
    # print(attributes)

    # len_of_frenquency_dependency = int(sys.argv[1])
    
    len_of_attributes = int(input('\nPlease enter the length of attributes of your entity: '))
    print()
    attributes = list(input('Please enter how many attributes you would like to have, each attribute'
                        ' can only be represented by a single character, and each char should'
                        ' should be seperated by a space in between: '))

    for char in attributes:
        if char == ' ':
            attributes.remove(char)

    print(attributes)

