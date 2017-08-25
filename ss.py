import tika
from tika import parser
import re


class ResumeParsing:
    def parseResume():
        parsed = parser.from_file("resume.pdf")
        email= re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}",re.IGNORECASE)
        x = re.search(email, parsed["content"])
        print(x)

        phone= re.compile(r"[+0-9 ]{10,14}", re.IGNORECASE)
        x = re.search(phone, parsed["content"])
        print(x)

        gpa= re.compile(r"[0-9]+\.[0-9]{1,3}", re.IGNORECASE)
        x = re.search(gpa, parsed["content"])
        print(x)

ResumeParsing.parseResume()