import modules.bot_assistant.models.address_book as ab


def test_add_contact():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    assert book.find("AlanWake") is not None

    print("test: add contact: passed! [Module: {}]".format(ab.__name__))


def test_add_contact_phone():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")

    assert book.find("AlanWake").find_phone("1111111111") is not None
    print("test: add contact phone: passed! [Module: {}]".format(ab.__name__))


def test_edit_contact_phone():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_phone("1111111111")
    book.find("AlanWake").add_phone("2222222222")

    book.find("AlanWake").edit_phone("1111111111", "3333333333")
    assert book.find("AlanWake").find_phone("3333333333") is not None

    print("test: edit contact phone: passed! [Module: {}]".format(ab.__name__))


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


def test_add_contact_email():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_email("alan.wake@remedy.com")

    assert book.find("AlanWake").find_email("alan.wake@remedy.com") is not None

    print("test: add contact email: passed! [Module: {}]".format(ab.__name__))


def test_add_invalid_contact_email():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))

    try:
        book.find("AlanWake").add_email("alan.wakeremedy.com")
    except ValueError:
        pass

    print("test: add invalid contact email: passed! [Module: {}]".format(ab.__name__))


def test_edit_contact_email():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_email("alan.wake@remedy.com")

    book.find("AlanWake").edit_email("alan.wake@remedy.com", "wake@remedy.com")

    assert book.find("AlanWake").find_email("wake@remedy.com") is not None

    print("test: edit contact email: passed! [Module: {}]".format(ab.__name__))


def test_remove_contact_email():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_email("alan.wake@remedy.com")

    book.find("AlanWake").remove_email("alan.wake@remedy.com")

    assert book.find("AlanWake").find_email("alan.wake@remedy.com") is None

    print("test: remove contact email: passed! [Module: {}]".format(ab.__name__))


def test_add_contact_address():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_address("6A Bright Falls Ave")

    assert book.find("AlanWake").find_address("6A Bright Falls Ave") is not None

    print("test: add contact address: passed! [Module: {}]".format(ab.__name__))


def test_edit_contact_address():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_address("6A Bright Falls Ave")

    book.find("AlanWake").edit_address(
        "6A Bright Falls Ave", "6A Bright Falls Ave, Bright Falls, WA"
    )

    assert (
            book.find("AlanWake").find_address("6A Bright Falls Ave, Bright Falls, WA")
            is not None
    )

    print("test: edit contact address: passed! [Module: {}]".format(ab.__name__))


def test_get_contact_address():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_address("6A Bright Falls Ave")

    assert book.find("AlanWake").find_address("6A Bright Falls Ave") is not None

    print("test: get contact address: passed! [Module: {}]".format(ab.__name__))


def test_remove_contact_address():
    book = ab.AddressBook()
    book.add_record(ab.Record("AlanWake"))
    book.find("AlanWake").add_address("6A Bright Falls Ave")

    book.find("AlanWake").remove_address("6A Bright Falls Ave")

    assert book.find("AlanWake").find_address("6A Bright Falls Ave") is None

    print("test: remove contact address: passed! [Module: {}]".format(ab.__name__))


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
    book.find("AlanWake").add_birthday("30.10.1982")
    book.find("AlanWake").add_email("alan.wake@remedy.com")

    book.add_record(ab.Record("Jane"))
    book.find("Jane").add_phone("3333333333")
    book.find("Jane").add_birthday("03.11.1989")
    book.find("Jane").add_email("jane.doe@example.com")

    assert len(book.data) == 2

    result = [
        (str(name), str(record).rstrip("-\n"))
        for name, record in book.data.items()
    ]

    expected = [
        (
            "AlanWake",
            "Contact name: AlanWake, phones: 1111111111; 2222222222, "
            "birthday: 30.10.1982, emails: alan.wake@remedy.com, "
            "addresses: no addresses available"
        ),
        (
            "Jane",
            "Contact name: Jane, phones: 3333333333, birthday: 03.11.1989, "
            "emails: jane.doe@example.com, addresses: no addresses available"
        ),
    ]

    assert result == expected

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
