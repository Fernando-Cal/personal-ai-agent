from db.models import Message 


def format_messages_for_gpt(messages):
    """
    Takes a list of Message ORM objects and converts them 
    into the format expected by OpenAI's API 

    Args:
        messages (ORM objects): _description_
    """
    return[{"role": m.role, "content": m.content} for m in messages]