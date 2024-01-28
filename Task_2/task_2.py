import sys

def entry_num():

        with open(sys.argv[1], "rt") as file:
            entry_number = []

            for line in file:

                if line.strip() == "END":
                    break
                entry_time = line.strip().split(",")
                if len(entry_time) >= 2:
                    entry_number.append(int(entry_time[1]))
                else:
                    print(f"Invalid line: {line}")

        return entry_number

    # except FileNotFoundError:
    #     print(f"The file {path_file} was not found.")

def exit_num():

        with open(sys.argv[1], "rt") as file:
            exit_number = []

            for line in file:

                if line.strip() == "END":
                    break
                exit_time = line.strip().split(",")
                if len(exit_time) >= 2:
                    exit_number.append(int(exit_time[2]))
                else:
                    print(f"Invalid line: {line}")

        return exit_number

    # except FileNotFoundError:
    #     print(f"The file {path_file} was not found.")

def owner_cat():

        with open(sys.argv[1], "rt") as file:
            cat_owner = []

            for line in file:

                if line.strip() == "END":
                    break
                ownership = line.strip().split(",")
                if len(ownership) >= 2:
                    cat_owner.append(ownership[0])
                else:
                    print(f"Invalid line: {line}")

        return cat_owner
    #
    # except FileNotFoundError:
    #     print(f"The file {path_file} was not found.")

def time_diff(enter,left):
    time_different = []
    for i in range(len(left)):
        time_different.append(left[i]-enter[i])

    return time_different

def entries_count(cat_owner):
    ours = 0
    theirs = 0

    for i in range(len(cat_owner)):
        if cat_owner[i] == "THEIRS":
            theirs += 1

        if cat_owner[i] == "OURS":
            ours += 1

    return theirs, ours

def time_cat_stayed(time_difference,cat_owner):
    stayed_time = 0

    for i in range(len(time_difference)):
        if cat_owner[i] == "OURS":
            stayed_time += time_difference[i]

    hours = stayed_time//60
    minutes = stayed_time%60

    return hours,minutes

def long_short(time_difference,cat_owner):
    longest = max(time_difference)
    new_time_diff = time_difference[:]
    for i in range(len(time_difference)):
        if cat_owner[i] == "THEIRS":
            new_time_diff[i] = 1500
    # # for i,j in enumerate(time_difference):
    #         if cat_owner[i] == "THEIRS":
    #             new_time_diff[i]= 1500

    shortest = min(new_time_diff)
    return new_time_diff,longest,shortest

def time_average(new_time_difference):
    num_sum = 0
    count = 0

    for i in new_time_difference:
        if i<1500:
            num_sum +=i
            count +=1
    average = num_sum / count
    average = round(average,2)

    return average

def input_output(theirs,ours,hour,minute,longest,shortest,average):
    print(f"Cat visits:{ours}")
    print(f"Other cats: {theirs}")
    print(f"Total Time in House: {hour} hours {minute} minutes\n")
    print(f"Longest visit: {longest} minutes")
    print(f"Shortest visit: {shortest} minutes")
    print(f"Average visit: {average} minutes")
print()
print("Log File Analysis")
print("=================")
print()
# path_file = 'shelter_2023-08-25.log'
list_entry = entry_num()
list_exit = exit_num()
difference_time = time_diff(list_entry,list_exit)
cat_ownership = owner_cat()
entry_cat, exit_cat = entries_count(cat_ownership)
cat_stay_hour, cat_stay_min = time_cat_stayed(difference_time,cat_ownership)
long_short_time = long_short(difference_time,cat_ownership)
new_diff_time , large , short = long_short(difference_time,cat_ownership)
average_number = time_average(new_diff_time)
final_display = input_output(entry_cat,exit_cat,cat_stay_hour,cat_stay_min,large,short,average_number)
# print(final_display)
# print(long_short_time)
# print(exit_cat,entry_cat)
# print(time_diff(list_entry,list_exit))
# result = owner_cat(file_path)
# print(result)
# print(list_exit)

