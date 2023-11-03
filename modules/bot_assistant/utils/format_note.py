def format_note(note):
    tags_str = "; ".join(p.value for p in note.tags)
    return f"{note.id:<4}\t{note.title.value:<15}\t{tags_str:<30}\t{note.creation_date.value:<20}\t{note.edited.value:<20}\t{note.status.value:<12}\t{note.text:<100}"
