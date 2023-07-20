import os

def break_down_large_file(file, context_window_size):
    chunks = []
    chunk = ""
    with open(file, 'r') as f:
        for line in f:
            if len(chunk) + len(line) > context_window_size:
                chunks.append(chunk)
                chunk = ""
            chunk += line
        if chunk:
            chunks.append(chunk)
    return chunks