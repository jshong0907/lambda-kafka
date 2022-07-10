from schemas import InputSchema


def handler(event, context):
    input = InputSchema(**event)
    return input.json()
