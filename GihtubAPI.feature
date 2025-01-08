Feature: Interact with GitHub API

  Background:
    Given the API base URL is 'https://api.github.com'

  Scenario: Retrieve Public Repositories with Keyword "webdrivercamp-learning-python"
    When I send a 'GET' request to '/search/repositories?q=webdrivercamp-learning-python'
    Then the response status code is 200
    Then the response should have 'total_count' with length greater than 0

  Scenario: Get Authenticated User's Repository Count
    When I have a valid access token
    And I send a 'GET' request with authentication to '/user/repos'
    Then the response status code is 200
    Then the response should contain items

  Scenario: Create a New Private Repository
    When I have a valid access token
    And the request body is 'repository'
    When I send a 'POST' request with authentication to '/user/repos'
    Then the response status code is 201
    Then the response should have 'name' equal to 'repo-created-with-api'

  Scenario: Retrieve Details of a Created Repository
    When I have a valid access token
    And a repository named "repo-created-with-api" has been created
    When I send a 'GET' request with authentication to '/repos/OlgaLesser/repo-created-with-api'
    Then the response status code is 200
    Then the response should have 'name' equal to 'repo-created-with-api'

  Scenario: Update Description of a Created Repository
    When I have a valid access token
    And a repository named "repo-created-with-api" has been created
    And the request body is 'description'
    When I send a 'PATCH' request with authentication to '/repos/OlgaLesser/repo-created-with-api'
    Then the response status code is 200
    Then the response should have 'description' equal to 'I know Python Requests!'

  Scenario: Delete a Created Repository
    When I have a valid access token
    And a repository named "repo-created-with-api" has been created
    When I send a 'DELETE' request with authentication to '/repos/OlgaLesser/repo-created-with-api'
    Then the response status code is 204