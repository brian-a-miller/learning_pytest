#
# This file created by Claude Code (AI) plug-in to IntelliJ IDEA
# with some modifications / additions by Brian A. Miller
# after initial creation
#

import sqlite3

import pytest
from inventory import add_item, create_schema, get_quantity, remove_item


@pytest.fixture
def db(request):

    test_name = request.node.name
    # print(f"\n[fixture] *** entering db(request), for the test: {test_name} ***")

    # --- setup: runs before each test that asks for "db" ---
    conn = sqlite3.connect(":memory:")  # brand-new, empty database
    create_schema(conn)
    print("\n[fixture] opened database")

    # print("**** in the fixture before yield ***")
    yield conn  # the test runs here, receiving conn as its "db" argument
    # print("**** in the fixture after yield ***")

    # --- teardown: runs after the test, even if the test failed ---
    conn.close()
    print("\n[fixture] closed database")


@pytest.fixture
def stocked_db(db):
    # print("entering method stocked_db(db)")
    # Fixtures can build on other fixtures: this one reuses "db"
    # (including its teardown) and adds some starting data.
    add_item(db, "apple", 10)
    add_item(db, "banana", 5)
    return db  # no cleanup of its own, so a plain return is enough


def test_new_database_is_empty(db):
    # print("\nentering test_new_database_is_empty(db)")
    assert get_quantity(db, "apple") == 0


def test_add_item(db):
    # print("\nentering test_add_item(db)")
    add_item(db, "apple", 3)
    assert get_quantity(db, "apple") == 3


def test_add_same_item_twice_accumulates(db):
    # print("\nentering test_add_same_item_twice_accumulates(db)")
    add_item(db, "apple", 3)
    add_item(db, "apple", 4)
    assert get_quantity(db, "apple") == 7


def test_each_test_gets_a_fresh_database(db):
    # print("\nentering test_each_test_gets_a_fresh_database(db)")
    # Earlier tests added apples, but this test gets its own new database
    assert get_quantity(db, "apple") == 0


def test_remove_item(stocked_db):
    # print("\nentering test_remove_item(stocked_db)")
    remove_item(stocked_db, "apple", 4)
    assert get_quantity(stocked_db, "apple") == 6


def test_cannot_remove_more_than_in_stock(stocked_db):
    # print("\nentering test_cannot_remove_more_than_in_stock(stocked_db)")
    with pytest.raises(ValueError, match="only 5"):
        remove_item(stocked_db, "banana", 6)