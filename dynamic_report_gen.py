# --- Style decorators ---
def wrap_bold(func):
    def inner(self):
        return "** " + func(self) + " **"
    return inner


def wrap_box(func):
    def inner(self):
        text = func(self)
        line = "=" * (len(text) + 4)
        return f"{line}\n| {text} |\n{line}"
    return inner


def announce(func):
    def inner(self):
        print("\n[INFO] Generating summary...")
        return func(self)
    return inner


# --- Simple uppercase formatter, used as a callable object ---
class UpperCaser:
    def __call__(self, text):
        return text.upper()


# --- A single block/section of a document ---
class Section:
    def __init__(self, title):
        self.title = title
        self.body = ""

    def fill(self, body_text):
        self.body = body_text

    def __str__(self):
        return f"--- {self.title} ---\n{self.body}"


# --- The document itself ---
class Document:
    blueprints = {}

    @classmethod
    def add_blueprint(cls, name, section_titles):
        cls.blueprints[name] = section_titles

    @classmethod
    def build_from_blueprint(cls, name):
        doc = cls(name, "Unknown")
        for title in cls.blueprints.get(name, []):
            doc.add_section(Section(title))
        return doc

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    @wrap_bold
    def heading_line(self):
        return f"{self.title} | Author : {self.author}"

    @announce
    @wrap_box
    def summary(self):
        return f"Total Sections : {len(self.sections)}"

    def __str__(self):
        out = self.heading_line() + "\n\n"
        for section in self.sections:
            out += str(section) + "\n\n"
        return out.strip()

    def __len__(self):
        return len(self.sections)

    def __getitem__(self, idx):
        return self.sections[idx]

    def __iter__(self):
        return iter(self.sections)

    def __add__(self, other):
        merged = Document(f"{self.title} & {other.title}", f"{self.author} & {other.author}")
        merged.sections = self.sections + other.sections
        return merged

    def __eq__(self, other):
        return self.title == other.title


# --- Driver code ---
def main():
    print("=" * 40)
    print("        DOCUMENT BUILDER TOOL")
    print("=" * 40)

    Document.add_blueprint("Student Report", ["Introduction", "Results", "Conclusion"])
    Document.add_blueprint("Project Report", ["Abstract", "Methodology", "Outcome"])

    print("\nAvailable Blueprints:")
    for name in Document.blueprints:
        print(f"  • {name}")

    chosen = input("\nPick a blueprint : ").title()

    if chosen not in Document.blueprints:
        print(f'\n[Error] "{chosen}" is not a known blueprint.')
        return

    doc = Document.build_from_blueprint(chosen)
    doc.author = input("Author name : ")

    print("\n" + "-" * 40)
    print(" FILL IN EACH SECTION ")
    print("-" * 40)
    for section in doc:
        text = input(f"Text for [{section.title}] : ")
        section.fill(text)

    print("\n" + "-" * 40)
    print(" CHOOSE A DISPLAY STYLE ")
    print("-" * 40)
    print("  1. Bold heading, plain body")
    print("  2. Whole thing in uppercase")
    print("  3. Just the boxed summary")

    option = int(input("\nChoice (1-3) : "))

    print("\n" + "=" * 40)
    print("                RESULT")
    print("=" * 40 + "\n")

    if option == 1:
        print(doc)
    elif option == 2:
        upper = UpperCaser()
        print(upper(str(doc)))
    elif option == 3:
        print(doc.summary())

    print("\n" + "-" * 40)
    print(" DOCUMENT INFO ")
    print("-" * 40)
    print(f"Section count : {len(doc)}")
    print(f"\nFirst section:\n{doc[0]}")

    print("\nSection titles in order:")
    for s in doc:
        print(f"  ➜ {s.title}")

    side_doc = Document("Bonus Report", "Admin")
    side_doc.add_section(Section("Bonus Section"))

    joined = doc + side_doc
    print(f"\nMerged document has {len(joined)} sections.")

    if doc == side_doc:
        print("Note: both documents share the same title.")
    else:
        print("Note: documents have different titles.")

    print("=" * 40)


if __name__ == "__main__":
    main()