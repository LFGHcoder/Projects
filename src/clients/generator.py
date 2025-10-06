import random, re

def spintax(text: str) -> str:
    def repl(match):
        return random.choice(match.group(1).split('|'))
    return re.sub(r"\{([^{}]+)\}", repl, text)

TEMPLATES = [
    "{Love|Really like|Nice} this! {Great|Solid} work.",
    "{Awesome|Cool} post — {thanks for sharing|learned something new}."
]

def generate_comment() -> str:
    return spintax(random.choice(TEMPLATES))
