import csv
import copy


class Methods:

    @staticmethod
    def remove_quotation(s):  # removes quotations from a string or just returns a string if it has no quotations

        string = s

        if s[0] == '"' and s[len(s)-1] == '"':

            string = s[1:len(s)-1]

        return string

    @staticmethod
    def represents_int(s):

        try:

            int(s)

            return True

        except ValueError:

            return False

    @staticmethod
    def get_possible_string_values(double_array):
        possible_values = []

        for x in range(0, len(double_array[0])):  # Adds an array for each type of data

            possible_values.append([])

        for arr in double_array:

            for idx, value in enumerate(arr):

                if Methods.represents_int(value):  # Excludes integer data values

                    possible_values[idx] = [None]

                elif value not in possible_values[idx]:  # Appends all new pieces of data

                    possible_values[idx].append(value)

        return possible_values

    @staticmethod
    def standardise(possible):  # This probably shouldn't be as static method
        return_list = possible

        for idx, options in enumerate(possible):

            if options == ['yes', 'no']:

                return_list[idx] = ['no', 'yes']

            elif 'other' in options:

                return_list[idx][options.index('other')], return_list[idx][0] = options[0], options[options.index('other')]

        return return_list

    @staticmethod
    def remove_list_quotes(list_data):
        return_list = []

        for idx, student in enumerate(list_data):

            return_list.append([])  # adds a list for each student

            for data in student:  # goes through each piece of data

                tempdata = Methods.remove_quotation(data)  # removes quotation marks if there are any

                try:
                    return_list[idx].append(int(tempdata))  # appends in type integer

                except ValueError:
                    return_list[idx].append(tempdata)  # appends string without quotation marks;

        return return_list

    @staticmethod
    def integerise(values_list, possible_values_list):
        return_list = []

        for idx1, student in enumerate(values_list):
            return_list.append([])

            for idx2, data in enumerate(student):

                if possible_values_list[idx2] != [None]:

                    return_list[idx1].append(possible_values_list[idx2].index(data))
                else:
                    return_list[idx1].append(data)

        return return_list

    @staticmethod
    def dec_to_bin(non_binary):
        return int(bin(non_binary)[2:])

    @staticmethod
    def dec_to_tally(non_tally):
        return_string = ''
        for x in range(0, non_tally):
            return_string+='1'
        return int(return_string)


    @staticmethod
    def integer_binary_list(int):
        binary_string = str(Methods.dec_to_bin(int))
        return Methods.string_to_list(binary_string)

    @staticmethod
    def integer_tally_list(int):
        tally_string = str(Methods.dec_to_tally(int))
        return Methods.string_to_list(tally_string)

    @staticmethod
    def string_to_list(binary_string):

        temp_list = []

        for idx in range(0, len(binary_string)):
            temp_list.append(binary_string[idx: idx+1])

        return_list = []

        for element in temp_list:
            return_list.append(int(element))

        return return_list

    @staticmethod
    def lengthen(double_binary_list):
        length_list = []
        return_list = []
        for binary_list in double_binary_list:
            length_list.append(len(binary_list))

        maximum_length = max(length_list)

        for binary_list in double_binary_list:
            temp_list = binary_list
            for n in range(0, maximum_length-len(binary_list)):
                temp_list.insert(0, 0)
            return_list.append(temp_list)

        return return_list


class Preprocessing:

    @staticmethod
    def preprocess(path):

        integer_list = []

        with open(path, 'rb') as csvfile:

            data_list = list(csv.reader(csvfile, delimiter=';', quotechar='|'))  # converts from csv file to list

            student_list = Methods.remove_list_quotes(data_list[1:])

            possible_values = Methods.standardise(Methods.get_possible_string_values(student_list))

            integer_list = Methods.integerise(student_list, possible_values)

        return integer_list

    @staticmethod
    def preprocess_inputs(path):

        integer_list = Preprocessing.preprocess(path)

        return_list = []

        for student in integer_list:

            student_input = student[0:len(student)-3]
            return_list.append(student_input)

        return return_list

    @staticmethod
    def preprocess_outputs_1(path):

        integer_list = Preprocessing.preprocess(path)

        return_integer_list = []

        for student in integer_list:

            student_input = student[len(student)-3:len(student)-2]
            return_integer_list.append(Methods.integer_tally_list(student_input[0]))

        return Methods.lengthen(return_integer_list)


#Binary not changed yet
    @staticmethod
    def preprocess_outputs_2(path):

        integer_list = Preprocessing.preprocess(path)

        return_integer_list = []

        for student in integer_list:

            student_input = student[len(student)-2:len(student)-1]
            return_integer_list.append(Methods.integer_binary_list(student_input[0]))

        return Methods.lengthen(return_integer_list)

path = 'Data Sets\student-mat.csv'


#print(Preprocessing.preprocess_outputs_1(path))
'''print(Preprocessing.preprocess_inputs(path))



print(Preprocessing.preprocess(path))

print(Preprocessing.preprocess_inputs(path))

print(Preprocessing.preprocess_outputs_1(path))

print(Preprocessing.preprocess_outputs_2(path))'''







