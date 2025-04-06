Feature: Tagging Compliance

  # Scenario for ensuring that all non-subnet resources have tags
  Scenario: Ensure all non-subnet resources have tags (if supported)
    Given I have resource that supports tags defined
    And I have resource that is not type "azapi_resource.subnet"
    Then it must contain tags
    And its value must not be null

  # Scenario outline for ensuring that specific tags are defined
  Scenario Outline: Ensure resources have specific tags (excluding subnets)
    Given I have resource that supports tags defined
    And I have resource that is not type "azapi_resource.subnet"
    When it has tags
    Then it must contain <tag>
    And its value must match the "<value>" regex

    Examples:
      | tag              | value                 |
      | Application Name | .+                    |
      | GL Code          | .+                    |
      | IT Owner         | .+                    |
      | Onboard Date     | .+                    |
      | Modified Date    | .+                    |
      | Organization     | .+                    |
      | Implemented by   | .+                    |
      | Resource Owner   | .+                    |
      | Resource Posture | .+                    |
      | Resource Type    | .+                    |
      | Business Owner   | .+                    |
      | Built Using      | .+                    |
      | Environment      | ^(sandbox|uat|dev)$   |
