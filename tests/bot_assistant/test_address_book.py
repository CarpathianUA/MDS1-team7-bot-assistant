import modules.bot_assistant.models.address_book as ab


def test_add_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    assert book.find("AlanWake") is not None

    print("test: add contact: passed! [Module: {}]".format(ab.__name__))


def test_change_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    book.find("AlanWake").edit_phone("1111111111", "3333333333")
    assert book.find("AlanWake").find_phone("3333333333") is not None

    print("test: change contact: passed! [Module: {}]".format(ab.__name__))


def test_get_contact_phone():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    assert book.find("AlanWake").find_phone("1111111111") is not None

    print("test: get contact phone: passed! [Module: {}]".format(ab.__name__))


def test_remove_contact_phone():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    book.find("AlanWake").remove_phone("1111111111")
    assert book.find("AlanWake").find_phone("1111111111") is None

    print("test: remove contact phone: passed! [Module: {}]".format(ab.__name__))


def test_delete_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    book.delete("AlanWake")
    assert book.data == {}

    print("test: delete contact: passed! [Module: {}]".format(ab.__name__))


def test_get_all_contacts():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    book.add_record(ab.Record("Jane"))
    book.find("Jane").add_phone("3333333333")

    assert len(book.data) == 2

    result = [(str(name), str(record)) for name, record in book.data.items()]
    assert result == [
        (
            "AlanWake",
            "Contact name: AlanWake, phones: 1111111111; 2222222222, birthday: No birthday available",
        ),
        (
            "Jane",
            "Contact name: Jane, phones: 3333333333, birthday: No birthday available",
        ),
    ]

    print("test: get all contacts: passed! [Module: {}]".format(ab.__name__))


def test_add_birthday():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_birthday("30.10.1982")

    assert book.find("AlanWake").get_birthday() == "30.10.1982"

    print("test: add birthday: passed! [Module: {}]".format(ab.__name__))


def test_get_birthday():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_birthday("30.10.1982")

    assert book.find("AlanWake").get_birthday() == "30.10.1982"

    print("test: get birthday: passed! [Module: {}]".format(ab.__name__))


# TO-DO: cover rest of the methods with tests
