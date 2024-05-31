from rich import print
def parseCLI():
    csv_mapping_list = []
    row_dict = dict()
    interfaceDict = dict()
    with open("/workspaces/network-interview-prep/show_ip_int_brief.txt") as my_data:
        line_count = 0
        for line in my_data:
            row_list = [val.strip() for val in line.split()]
            if line_count == 0:
                header = row_list[1:]
            else:
                row_dict = {key: value for key, value in zip(header, row_list[1:])}
                csv_mapping_list.append(row_dict)
                interfaceDict[row_list[0]] = row_dict
            line_count += 1
    return interfaceDict
result = parseCLI()
print(result)
