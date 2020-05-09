from pathlib import Path
from unittest import TestCase, skipIf
import doc_safer
import platform
from readme_renderer import rst

README_TEXT = Path(doc_safer.README_FILE).read_text()


class TestDoc(TestCase):
    @skipIf(platform.python_version() < '3.6', 'Needs Python 3.6 or greater')
    def test_make_doc(self):
        actual = doc_safer.make_doc()
        assert actual.rstrip() == README_TEXT.rstrip()

    def test_rendering(self):
        actual = rst.render(README_TEXT)
        assert actual is not None
