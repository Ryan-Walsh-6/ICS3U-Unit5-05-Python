#!/usr/bin/env python3

# created by: Ryan Walsh
# created on: January 2021
# this program formats a mailing address


def format_address(addressee_from_user, street_number_from_user,
                   street_name_from_user, city_from_user, province_from_user,
                   postal_code_from_user, apt_number_from_user=None):
    # formates mailing address

    # process
    if apt_number_from_user is not None:
        mailing_address = (addressee_from_user + "\n" + apt_number_from_user +
                           "-" + street_number_from_user + " "
                           + street_name_from_user + "\n"
                           + city_from_user + " " + province_from_user + "  " +
                           postal_code_from_user)
    else:
        mailing_address = (addressee_from_user + "\n" +
                           street_number_from_user + " " +
                           street_name_from_user + "\n" + city_from_user +
                           " " + province_from_user + "  " +
                           postal_code_from_user)

    return mailing_address


def main():
    # this program formats a mailing address
    apt_number_from_user = None

    addressee_from_user = input("Enter your name:")
    street_number_from_user = input("Enter a street number:")
    street_name_from_user = input("Enter a street name:")
    city_from_user = input("Enter a city:")
    province_from_user = input("Enter a province:")
    postal_code_from_user = input("Enter a postal code:")
    live_apt_from_user = input("Do you live in a apartment? (Y/N):")
    if (live_apt_from_user.upper() == "Y" or live_apt_from_user.upper() ==
       "YES"):
        apt_number_from_user = input("Enter an apartment number:")
    print("\n", end="")

    # call function
    if apt_number_from_user is not None:
        address = format_address(addressee_from_user,
                                 street_number_from_user,
                                 street_name_from_user,
                                 city_from_user, province_from_user,
                                 postal_code_from_user, apt_number_from_user)
    else:
        address = format_address(addressee_from_user, street_number_from_user,
                                 street_name_from_user,
                                 city_from_user, province_from_user,
                                 postal_code_from_user)

    print(address)


if __name__ == "__main__":
    main()
