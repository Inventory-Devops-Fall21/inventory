# Populate the feature file
# Then write the needed steps in *_steps.py
Feature: The Inventory service back-end
    As an Inventory Manager
    I need a RESTful product list service
    So that I can keep track of my inventory

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

# Scenario: Create a Pet
#     When I visit the "Home Page"
#     And I set the "Name" to "Happy"
#     And I set the "Category" to "Hippo"
#     And I select "False" in the "Available" dropdown
#     And I press the "Create" button
#     Then I should see the message "Success"
#     When I copy the "Id" field
#     And I press the "Clear" button
#     Then the "Id" field should be empty
#     And the "Name" field should be empty
#     And the "Category" field should be empty
#     When I paste the "Id" field
#     And I press the "Retrieve" button
#     Then I should see "Happy" in the "Name" field
#     And I should see "Hippo" in the "Category" field
#     And I should see "False" in the "Available" dropdown