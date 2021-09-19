import pytest
from mongoPageObject import mongoPageObject as POM
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('.\mongo_steps.feature', 'changing the data')
def test_changing_the_data():
    pass

@pytest.fixture(scope='function')
def context():
    return {}


@given('the mail is gary@gmail.com')
def the_mail_is_garygmailcom(context):
    """the mail is gary@gmail.com."""
    context['obj'] = POM()
    context['obj'].edit_mongo_mail("gary@gmail.com")

@when('I change mail to garygary@gmail')
def i_change_mail_to_garygarygmail(context):
    """I change mail to garygary@gmail."""
    context["obj"].edit_mongo_mail("garygary@gmail.com")


@then('mongoDB mail also is updated')
def mongodb_mail_also_is_updated(context):
    context["obj"].navigate_to_mongo_express_mail()
    assert (context["obj"].get_mongo_express_mail() == 'garygary@gmail.com')
