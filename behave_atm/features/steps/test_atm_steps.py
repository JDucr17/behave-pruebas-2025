from behave import given, when, then
from hamcrest import assert_that, equal_to
from atm import ATM, AccountLockedError, InvalidPINError


@given('an account with initial balance of {amount:d}')
def step_given_initial_balance(context, amount):
    context.atm = ATM(amount)
    context.output = None
    context.error = None


@given('a destination account with initial balance of {amount:d}')
def step_given_destination_account(context, amount):
    context.destination_atm = ATM(amount)


@given('a daily withdrawal limit of {limit:d}')
def step_given_limit(context, limit):
    context.atm.daily_limit = limit


@when('the user checks the balance')
def step_when_check_balance(context):
    context.output = context.atm.check_balance()


@when('the user deposits {amount:d}')
def step_when_deposit(context, amount):
    try:
        context.atm.deposit(amount)
        context.output = context.atm.check_balance()
    except Exception as e:
        context.error = str(e)


@when('the user withdraws {amount:d}')
def step_when_withdraw(context, amount):
    try:
        context.atm.withdraw(amount)
        context.output = context.atm.check_balance()
    except Exception as e:
        context.error = str(e)


@when('the user attempts to withdraw {amount:d}')
def step_when_attempt_withdraw(context, amount):
    try:
        context.atm.withdraw(amount)
        context.output = context.atm.check_balance()
    except Exception as e:
        context.error = str(e)


@when('the user transfers {amount:d} to the destination account')
def step_when_transfer(context, amount):
    try:
        context.atm.transfer(amount, context.destination_atm)
        context.output = context.atm.check_balance()
    except Exception as e:
        context.error = str(e)
           

@when('the user attempts to transfer {amount:d} to the destination account')
def step_when_attempt_transfer(context, amount):
    try:
        context.atm.transfer(amount, context.destination_atm)
        context.output = context.atm.check_balance()
    except Exception as e:
        context.error = str(e)


@when('the user checks the transaction history')
def step_when_check_history(context):
    context.history = context.atm.get_transaction_history()


@when('the user changes PIN from "{old_pin}" to "{new_pin}"')
def step_when_change_pin(context, old_pin, new_pin):
    try:
        context.output = context.atm.change_pin(old_pin, new_pin)
    except Exception as e:
        context.error = str(e)


@when('the user attempts to change PIN from "{old_pin}" to "{new_pin}"')
def step_when_attempt_change_pin(context, old_pin, new_pin):
    try:
        context.output = context.atm.change_pin(old_pin, new_pin)
    except Exception as e:
        context.error = str(e)


@when('the user enters incorrect PIN "{pin}"')
def step_when_incorrect_pin(context, pin):
    try:
        context.atm.change_pin(pin, "5678")
    except (InvalidPINError, AccountLockedError) as e:
        context.last_error = str(e)


@when('the user attempts to withdraw {amount:d} again')
def step_when_withdraw_again(context, amount):
    try:
        context.atm.withdraw(amount)
    except Exception as e:
        context.last_error = str(e)


@then('the displayed balance should be {expected:d}')
def step_then_balance(context, expected):
    assert context.output == expected, f"Expected balance {expected}, but got {context.output}"


@then('the destination account balance should be {expected:d}')
def step_then_destination_balance(context, expected):
    actual = context.destination_atm.check_balance()
    assert actual == expected, f"Expected destination balance {expected}, but got {actual}"


@then('an insufficient funds error should be displayed')
def step_then_insufficient_funds_error(context):
    assert context.error is not None, "Expected an error but none occurred"
    assert 'insufficient' in context.error.lower(), "Error message does not mention insufficient funds"


@then('the history should contain {count:d} transactions')
def step_then_history_count(context, count):
    assert len(context.history) == count, f"Expected {count} transactions, but got {len(context.history)}"


@then('the PIN change should be successful')
def step_then_pin_change_successful(context):
    assert context.output is True, "PIN change was not successful"


@then('an invalid PIN error should be displayed')
def step_then_invalid_pin_error(context):
    assert context.error is not None, "Expected an error but none occurred"
    assert 'pin' in context.error.lower(), "Error message does not mention PIN"


@then('the account should be locked')
def step_then_locked(context):
    assert_that(context.atm.locked, equal_to(True))


@then('an "Account locked due to multiple failed attempts" error should be raised')
def step_then_error_message(context):
    assert_that(context.last_error, equal_to("Account locked due to multiple failed attempts"))


@then('a "Daily withdrawal limit exceeded" error should be raised')
def step_then_error(context):
    assert_that(context.last_error, equal_to("Daily withdrawal limit exceeded"))

@then('the displayed balance should remain {balance:d}')
def step_then_balance_remain(context, balance):
    assert_that(context.atm.balance, equal_to(balance))