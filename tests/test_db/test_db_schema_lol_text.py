import pytest

from discord_ritoman.db.schema import LoLText, LoLTextGroup
from discord_ritoman.db.session import session


@pytest.fixture
def lol_text_group_name() -> str:
    return "suffix"


@pytest.fixture
def lol_text_group_usage() -> str:
    return "text to be displayed at the end of a rich message"


@pytest.fixture
def lol_user() -> int:
    return 1234


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    # remove mock text
    session.query(LoLText).delete()
    session.commit()

    # remove mock text_groups
    session.query(LoLTextGroup).delete()
    session.commit()


def teardown_module(module):
    """teardown any state that was previously setup with a setup_module
    method.
    """

    # remove mock text
    session.query(LoLText).delete()
    session.commit()

    # remove mock text_groups
    session.query(LoLTextGroup).delete()
    session.commit()


def test_create_lol_text_group(
    lol_text_group_name, lol_text_group_usage, lol_user
):
    """
    Tests that a lol text group can be created successfully
    """
    assert len(session.query(LoLTextGroup).all()) == 0

    text_group = LoLTextGroup(
        lol_text_group_name, lol_text_group_usage, lol_user
    )
    session.add(text_group)
    session.commit()

    assert len(session.query(LoLTextGroup).all()) == 1


def test_create_lol_text(lol_text_group_name, lol_user):
    """
    Tests that a lol text can be created successfully
    """
    assert len(session.query(LoLText).all()) == 0

    text = LoLText(lol_text_group_name, "ending.", lol_user)
    session.add(text)
    session.commit()

    assert len(session.query(LoLText).all()) == 1


def test_delete_lol_text():
    """
    Tests that deleting a LoLText object works successfully
    """
    assert len(session.query(LoLText).all()) == 1

    text_uuid = session.query(LoLText).all()[0].uuid
    session.query(LoLText).filter(LoLText.uuid == text_uuid).delete()
    session.commit()

    assert len(session.query(LoLText).all()) == 0


def test_delete_lol_text_group(
    lol_text_group_name, lol_text_group_usage, lol_user
):
    """
    Tests that a lol text group can be deleted successfully
    """
    queried_groups = session.query(LoLTextGroup).all()
    group = None
    if len(queried_groups) != 1:
        group = LoLTextGroup(
            lol_text_group_name, lol_text_group_usage, lol_user
        )
        session.add(group)
        session.commit()
    else:
        group = queried_groups[0]

    session.query(LoLTextGroup).filter(
        LoLTextGroup.name == lol_text_group_name
    ).delete()
    session.commit()

    assert len(session.query(LoLTextGroup).all()) == 0
