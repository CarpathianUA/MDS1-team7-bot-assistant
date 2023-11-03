def format_note(note):
    tags_str = "; ".join(p.value for p in note.tags)
    return f"{note.id:<4}\t{note.title.value:<15}\t{tags_str:<30}\t{note.creation_date.value:<20}\t{note.edited.value:<20}\t{note.status.value:<12}\t{note.text:<100}"


def format_text(text, max_line_width):
    lines = text.split("\n")
    formatted_lines = []

    for line in lines:
        words = line.split()
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_width:
                current_line += f"{word} "
            else:
                formatted_lines.append(current_line)
                current_line = f"{word} "

        if current_line:
            formatted_lines.append(current_line)

    return "\n".join(formatted_lines)
