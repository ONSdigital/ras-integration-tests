import nose
import re


def substitute_context_values(context, raw_string):
    """scans the raw string looking for {context.value} or {value}, replaces each instance with the corresponding
    value from context. Will ignore spaces after '{' and before '}'
     """
    new_string = raw_string.replace('{context.', '{')
    matches = re.findall('{[\sa-zA-Z0-9_]+}', raw_string)

    for match_str in matches:
        context_attr = match_str.replace('{', '').replace('}', '').strip()
        replacement = getattr(context, context_attr, None)
        nose.tools.assert_is_not_none(replacement, f"Unable to to find value for {context_attr} on context object")
        new_string = re.sub(match_str, replacement, new_string)

    return new_string
