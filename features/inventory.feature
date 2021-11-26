# Populate the feature file
# Then write the needed steps in *_steps.py
Feature: The Inventory service back-end
    As an Inventory Manager
    I need a RESTful product list service
    So that I can keep track of my inventory

    # Runs for each scenario
    Background:
        Given the following inventory
            | name      | condition     | quantity | restock_level |
            | Chocolate | new           | 10       | 5             |
            | iPhone    | used          | 20       | 25            |
            | Mug       | slightly_used | 30       | 30            |
            | Computer  | unknown       | 50       | 20            |

    Scenario: The server is running
        When I visit the "Home Page"
        Then I should see "Inventory REST API Service" in the title
        And I should not see "404 Not Found"

    Scenario: Create an Inventory
        When I visit the "Home Page"
        And I set the "Name" to "Banana"
        And I set the "Quantity" to "20"
        And I set the "Restock_level" to "10"
        And I select "New" in the "Condition" dropdown
        And I press the "Create" button
        Then I should see the message "Success"
        When I copy the "Id" field
        And I press the "Clear" button
        Then the "Id" field should be empty
        And the "Name" field should be empty
        And the "Condition" field should be empty
        When I paste the "Id" field
        And I press the "Retrieve" button
        Then I should see the message "Success"
        And I should see "Banana" in the "Name" field
        And I should see "20" in the "Quantity" field
        And I should see "10" in the "Restock_level" field
        And I should see "New" in the "Condition" dropdown

    Scenario: Read an Inventory
        When I visit the "Home Page"
        And I set the "Id" to the first item in table
        And I press the "Retrieve" button
        Then I should see the message "Success"
        And I should see "Chocolate" in the "Name" field
        And I should see "10" in the "Quantity" field
        And I should see "5" in the "Restock_level" field
        And I should see "New" in the "Condition" dropdown

    Scenario: Update an Inventory
        When I visit the "Home Page"
        And I set the "Id" to the first item in table
        And I press the "Retrieve" button
        Then I should see the message "Success"
        And I should see "Chocolate" in the "Name" field
        And I should see "10" in the "Quantity" field
        And I should see "5" in the "Restock_level" field
        And I should see "New" in the "Condition" dropdown
        When I change "Name" to "Banana"
        And I select "Unknown" in the "Condition" dropdown
        And I press the "Update" button
        Then I should see the message "Success"
        When I copy the "Id" field
        And I press the "Clear" button
        And I paste the "Id" field
        And I press the "Retrieve" button
        Then I should see the message "Success"
        And I should see "Banana" in the "Name" field
        And I should see "10" in the "Quantity" field
        And I should see "5" in the "Restock_level" field
        And I should see "Unknown" in the "Condition" dropdown
