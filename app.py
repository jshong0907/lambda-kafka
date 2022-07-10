from schemas import InputSchema


def handler(event, context):
    input = InputSchema(**event)
    return input.json()


if __name__ == '__main__':
    print(InputSchema(**{
        "request_id": "10",
        "message": "message",
        "request_date": "2022-07-13"
    }).json())