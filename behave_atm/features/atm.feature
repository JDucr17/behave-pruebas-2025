Feature: ATM basic operations
  As an ATM user
  I want to perform banking operations
  To manage my account

  @balance @query
  Scenario: Check initial balance
    Given an account with initial balance of 10000
    When the user checks the balance
    Then the displayed balance should be 10000

  @deposit
  Scenario Outline: Make a valid deposit
    Given an account with initial balance of <initial_balance>
    When the user deposits <deposit_amount>
    Then the displayed balance should be <resulting_balance>

    Examples:
      | initial_balance | deposit_amount | resulting_balance |
      | 5000            | 2000           | 7000              |
      | 10000           | 500            | 10500             |

  @withdrawal
  Scenario: Withdrawal with sufficient balance
    Given an account with initial balance of 10000
    When the user withdraws 5000
    Then the displayed balance should be 5000

  @withdrawal_failed
  Scenario: Attempt to withdraw more than available balance
    Given an account with initial balance of 1000
    When the user attempts to withdraw 5000
    Then an insufficient funds error should be displayed

  @transfer
  Scenario: Transfer between accounts
    Given an account with initial balance of 10000
    And a destination account with initial balance of 5000
    When the user transfers 3000 to the destination account
    Then the displayed balance should be 7000
    And the destination account balance should be 8000

  @transfer_failed
  Scenario: Attempt to transfer with insufficient funds
    Given an account with initial balance of 1000
    And a destination account with initial balance of 5000
    When the user attempts to transfer 2000 to the destination account
    Then an insufficient funds error should be displayed

  @history
  Scenario: View transaction history
    Given an account with initial balance of 10000
    When the user deposits 2000
    And the user withdraws 1000
    And the user checks the transaction history
    Then the history should contain 3 transactions

  @pin
  Scenario: Successfully change PIN
    Given an account with initial balance of 5000
    When the user changes PIN from "1234" to "5678"
    Then the PIN change should be successful

  @pin_failed
  Scenario: Attempt to change PIN with incorrect current PIN
    Given an account with initial balance of 5000
    When the user attempts to change PIN from "0000" to "5678"
    Then an invalid PIN error should be displayed