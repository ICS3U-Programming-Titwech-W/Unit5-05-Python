#!/usr/bin/env python3

# Created by: Titwech Wal
# Created on: May.26.2022
# accepts an address and
# then prints it again


def adress_name(full_name, aprtment, street_num, street_name, city,
                province, postal_code, apt_num=None):

    # format the adress
    adress_display = full_name.upper() + "\n" + street_num + " " \
                   + street_name.upper() + "\n" + city.upper() \
                   + " " + province.upper() + " " + postal_code.upper()

    # if user lives in a apartment
    if aprtment == "y":
        adress_display = full_name.upper() + "\n" + apt_num \
                       + "-" + street_num + " " + street_name.upper() \
                       + "\n" + city.upper() + " " + province.upper() \
                       + " " + postal_code.upper()

        return adress_display

    return adress_display


def main():

    apt_num_user = None

    # prints what the program does
    print("This program creates an address to a Canadian mailing address!")
    print("")

    # get user input
    user_name = input("Enter your full name: ")
    question_apt = input("Do you live in an apartment (y/n): ")\

    # check if user lives in an apartment
    if question_apt == "y":
        apt_num_user = input("Enter your apartment number: ")

    # gets input from the user
    street_num_user = input("Enter your street number: ")
    street_name_user = input("Enter your street name and "
                             "type (Main St., Flower Cres., etc.): ")

    # get city and province
    city_user = input("Enter your city: ")
    province_user = input("Enter your province (as an abbreviation "
                          "i.e ON, AB, etc.): ")

    # postal code
    postal_user = input("Enter your postal code (i.e A1B 2C3): ")

    # assigns varaible to function that formats the address
    if apt_num_user is not None:
        user_address = adress_name(user_name, question_apt,
                                   street_num_user, street_name_user,
                                   city_user, province_user,
                                   postal_user, apt_num_user)
    else:
        user_address = adress_name(user_name, question_apt,
                                   street_num_user, street_name_user,
                                   city_user, province_user,
                                   postal_user)
    print("")
    print("Your Canadian mailing address is:\n")
    print(user_address)


if __name__ == "__main__":
    main()
