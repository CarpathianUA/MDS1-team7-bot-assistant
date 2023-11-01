import tests.bot_assistant.test_address_book as test_address_book

if __name__ == "__main__":
    # test address book model
    test_address_book.test_add_contact()
    test_address_book.test_add_contact_phone()
    test_address_book.test_edit_contact_phone()
    test_address_book.test_get_contact_phone()
    test_address_book.test_delete_contact()
    test_address_book.test_remove_contact_phone()
    test_address_book.test_add_contact_email()
    test_address_book.test_edit_contact_email()
    test_address_book.test_get_all_contacts()
    test_address_book.test_add_birthday()
    test_address_book.test_get_birthday()

    print("All tests passed!")
