"""
// Infection Problem //
Write a program that reports the names and number of club members infected up to each
meeting from the first meeting where anyone was infected.
"""

filename = input("Enter the file name: ")
file = open(filename, "r")  # Opening file
lines = file.read().splitlines()  # Converting file into list of lines


def fever_finder(list_of_lines):
    infected_list = []  # Making a infection list
    for line in list_of_lines:
        temp_infected_list = []  # Splitting the line with whitespace
        tokens = line.split()
        line_number = tokens[0]
        names = tokens[1:]
        index = 0
        for name in names:  # If the name ends with *, it is the source of the fever
            if name.endswith("*"):
                # Adding self and neighbours as infected
                temp_infected_list.append(name.strip("*"))
                temp_infected_list.append(names[index - 1])
                if index == (len(names) - 1):
                    index = -1
                temp_infected_list.append(names[index + 1])
                break

            for infected in infected_list:  # If the current person is found in the infection list
                if name == infected:
                    temp_infected_list.append(names[index - 1])
                    if index == (len(names) - 1):
                        index = -1  # adding the neighbours
                    temp_infected_list.append(names[index + 1])  # Now break
            index += 1
        infected_list = list(set(infected_list + temp_infected_list))

        if len(infected_list):
            print(line_number, " ".join(infected_list), len(infected_list))


file.close()
fever_finder(lines)
