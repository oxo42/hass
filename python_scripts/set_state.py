# --------------------------------------------------------------------------------------------------
# Set the state or other attributes for the entity specified in the Automation Action
# --------------------------------------------------------------------------------------------------

# The action could be
# action:
#     service: python_script.set_state
#     data_template:
#       entity_id: Binary_sensor.sensor1
#       state: ON


inputEntity = data.get("entity_id")
inputStateObject = hass.states.get(inputEntity)
inputState = inputStateObject.state
inputAttributesObject = inputStateObject.attributes.copy()

newState = data.get("state")
if newState is not None:
    inputState = newState

newIcon = data.get("icon")
if newIcon is not None:
    inputAttributesObject["icon"] = newIcon

hass.states.set(inputEntity, inputState, inputAttributesObject)
