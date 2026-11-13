#
# This file created by Claude Code (AI) plug-in to IntelliJ IDEA
#

"""A tiny inventory "repository" backed by SQLite, used to demonstrate fixtures."""

import sqlite3


def create_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        "CREATE TABLE inventory (name TEXT PRIMARY KEY, quantity INTEGER NOT NULL)"
    )


def add_item(conn: sqlite3.Connection, name: str, quantity: int) -> None:
    """Add quantity of an item, creating the item if it doesn't exist."""
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    conn.execute(
        "INSERT INTO inventory (name, quantity) VALUES (?, ?) "
        "ON CONFLICT(name) DO UPDATE SET quantity = quantity + excluded.quantity",
        (name, quantity),
    )


def remove_item(conn: sqlite3.Connection, name: str, quantity: int) -> None:
    """Remove quantity of an item; raises ValueError if there isn't enough."""
    current = get_quantity(conn, name)
    if quantity > current:
        raise ValueError(f"only {current} of {name!r} in stock")
    conn.execute(
        "UPDATE inventory SET quantity = quantity - ? WHERE name = ?",
        (quantity, name),
    )


def get_quantity(conn: sqlite3.Connection, name: str) -> int:
    row = conn.execute(
        "SELECT quantity FROM inventory WHERE name = ?", (name,)
    ).fetchone()
    return row[0] if row else 0