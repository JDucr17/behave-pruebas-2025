from behave import given, when, then
from atm import ATM


@given('an account with initial balance of {amount:d}')
def step_given_initial_balance(context, amount):
    context.atm = ATM(amount)
    context.output = None
    context.error = None


@given('a destination account with initial balance of {amount:d}')
def step_given_destination_account(context, amount):
    context.destination_atm = ATM(amount)


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