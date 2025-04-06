from terraform_compliance import step

@step('I have resource that supports tags defined')
def check_resource_has_tags(step):
    # This step checks that the resource in the Terraform plan supports tags.
    step.variable("resource").has_key("tags")

@step('I have resource that is not type "azapi_resource.subnet"')
def check_resource_is_not_subnet(step):
    # This step checks that the resource type is not "azurerm_subnet".
    if step.variable("resource")["type"] == "azapi_resource.subnet":
        step.skip("Skipping subnet resource")
    else:
        step.pass_()

@step('it must contain tags')
def check_tags_not_null(step):
    # This step ensures that the resource has tags and they are not null.
    tags = step.variable("resource")["tags"]
    if tags is None or tags == {}:
        step.fail("Resource does not have tags or tags are empty")
    else:
        step.pass_()

@step('its value must not be null')
def check_tag_values_not_null(step):
    # This step ensures that the tags' values are not null.
    for key, value in step.variable("resource")["tags"].items():
        if value is None or value == "":
            step.fail(f"Tag {key} has a null or empty value")
    step.pass_()

@step('it must contain {tag}')
def check_tag_exists(step, tag):
    # This step checks that a specific tag is present in the resource's tags.
    tags = step.variable("resource")["tags"]
    if tag not in tags:
        step.fail(f"Tag {tag} is missing from resource")
    else:
        step.pass_()

@step('its value must match the "{value}" regex')
def check_tag_value_regex(step, value):
    # This step checks that the tag's value matches the regex.
    import re
    tags = step.variable("resource")["tags"]
    for key, tag_value in tags.items():
        if not re.match(value, str(tag_value)):
            step.fail(f"Tag {key} value {tag_value} does not match regex {value}")
    step.pass_()
