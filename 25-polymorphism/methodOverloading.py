class TextProcessor:
    def format_text(self, text1: str, text2: str = None) -> str:
        if text2 is None:
            return text1.upper()
        else:
            return text1 + text2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
    