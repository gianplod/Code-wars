def solution(ints):

    ints.sort()
    temp_ints = []
    format_ints = ""
    i = 0
    j = 0
    num_counter = 1

    while True:

        if i < (len(ints) - 1):
            if abs(ints[i+1]) == (abs(ints[i]) - 1 if ints[i] < 0 else abs(ints[i]) + 1):
                i += 1
                num_counter += 1
            else:
                if num_counter >= 3:
                    temp_ints = [num for num in ints[j:i+1]]
                    format_ints += f"{min(temp_ints)}-{max(temp_ints)},"
                    j = i + 1
                    i += 1
                    num_counter = 1
                elif num_counter == 2:
                    format_ints += f"{ints[j]},{ints[i]},"
                    j = i + 1
                    i += 1
                    num_counter = 1
                else:
                    format_ints += f"{ints[i]},"
                    i += 1
                    j += 1
        else:
            if num_counter >= 3:
                temp_ints = [num for num in ints[j:i+1]]
                format_ints += f"{min(temp_ints)}-{max(temp_ints)}"
            elif num_counter == 2:
                format_ints += f"{ints[j]},{ints[i]}"
            else:
                format_ints += f"{ints[i]}"

            break

    return format_ints
