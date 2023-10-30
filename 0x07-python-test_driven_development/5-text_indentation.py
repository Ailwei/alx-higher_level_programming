#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    cleaned_lines = [line.strip() for line in lines]
    formatted_text = "\n".join(cleaned_lines)
    return formatted_text
