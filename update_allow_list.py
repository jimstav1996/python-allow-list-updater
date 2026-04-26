# List of IP addresses that should be removed from the allow list
remove_list = ["192.168.1.11", "192.168.1.13"]

# File that contains the allow list
import_file = "allow_list.txt"

# Open the file and read its contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Remove IP addresses that are on the remove list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert the updated list back into a string
ip_addresses = "\n".join(ip_addresses)

# Write the updated list back to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)
