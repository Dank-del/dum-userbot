import html

def bold(text: str) -> str:
    """Returns the given text in bold"""
    return "<b>" + text + "</b>"

def italic(text: str) -> str:
    """Returns the given text in italics"""
    return "<i>" + text + "</i>"

def code(text: str) -> str:
    """Returns the given text in code"""
    return "<code>" + text + "</code>"

def underline(text: str) -> str:
    """Returns the given text underlined"""
    return "<u>" + text + "</u>"

def strikethrough(text: str) -> str:
    """Returns the given text with a strikethrough"""
    return "<s>" + text + "</s>"

def mention(text: str, id: int) -> str:
    """Returns a mention"""
    return "<a href='tg://user?id={}'>{}</a>".format(id, html.escape(text))