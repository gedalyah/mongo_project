Feature: editProfile

  Edits site running on port 3000

  Scenario: changing the data
    Given the mail is gary@gmail.com
    When I change mail to garygary@gmail
    Then mongoDB mail also is updated