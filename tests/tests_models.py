from unittest import TestCase
from datetime import date

from src.models import *


class TestContact(TestCase):

    serialized = """
    {
        "email": "john.doe@example.com",
        "phone": "+1 555 555 5555",
        "linkedin": "https://www.linkedin.com/in/johndoe",
        "github": "https://github.com/johndoe"
    }
    """

    def test_deserialisation(self):
        contact = Contact.parse_raw(self.serialized)
        self.assertEqual(contact.email, "john.doe@example.com")
        self.assertEqual(contact.phone, "+1 555 555 5555")
        self.assertEqual(contact.linkedin, "https://www.linkedin.com/in/johndoe")
        self.assertEqual(contact.github, "https://github.com/johndoe")


class TestAddress(TestCase):

    serialized = """
        {
            "street": "123 Main Street",
            "zipcode": "12345",
            "city": "New York",
            "state": "NY",
            "country": "USA"
        }
        """

    def test_deserialisation(self):
        address = Address.parse_raw(self.serialized)
        self.assertEqual(address.street, "123 Main Street")
        self.assertEqual(address.zipcode, "12345")
        self.assertEqual(address.city, "New York")
        self.assertEqual(address.state, "NY")
        self.assertEqual(address.country, "USA")


class TestPersonal(TestCase):

    serialized = """
        {
            "name": "John Doe",
            "dob": "1990-01-01",
            "address": {
                "street": "123 Main Street",
                "zipcode": "12345",
                "city": "New York",
                "state": "NY",
                "country": "USA"
            }
        }
        """

    def test_deserialisation(self):
        personal = Personal.parse_raw(self.serialized)
        self.assertEqual(personal.name, "John Doe")
        self.assertEqual(personal.dob, date(1990, 1, 1))
        self.assertEqual(personal.address.street, "123 Main Street")
        self.assertEqual(personal.address.zipcode, "12345")
        self.assertEqual(personal.address.city, "New York")
        self.assertEqual(personal.address.state, "NY")
        self.assertEqual(personal.address.country, "USA")


class TestLanguage(TestCase):

    serialized = """
        {
            "name": "English",
            "level": "Native"
        }
        """

    def test_deserialisation(self):
        language = Language.parse_raw(self.serialized)
        self.assertEqual(language.name, "English")
        self.assertEqual(language.level, "Native")


class TestTaggedItem(TestCase):

    serialized = """
    {
        "label": "Python",
        "tags": ["python", "programming", "scripting"]
    }
    """

    def test_deserialisation(self):
        tagged_item = TaggedItem.parse_raw(self.serialized)
        self.assertEqual(tagged_item.label, "Python")
        self.assertEqual(tagged_item.tags, set(["python", "programming", "scripting"]))


class TestEducation(TestCase):

    serialized = """
        {
            "title": "Bachelor of Science",
            "begin": "2010-01-01",
            "end": "2014-01-01",
            "location": "New York",
            "specialisation": "Computer Science",
            "classes": [
                {
                    "label": "Python",
                    "tags": ["python", "programming", "scripting"]
                }
            ],
            "projects": [
                {
                    "label": "Resume Generator",
                    "tags": ["python", "programming", "scripting", "cli"]
                }
            ]
        }
        """

    def test_deserialisation(self):
        education = Education.parse_raw(self.serialized)
        self.assertEqual(education.title, "Bachelor of Science")
        self.assertEqual(education.begin, date(2010, 1, 1))
        self.assertEqual(education.end, date(2014, 1, 1))
        self.assertEqual(education.location, "New York")
        self.assertEqual(education.specialisation, "Computer Science")
        self.assertEqual(education.classes[0].label, "Python")
        self.assertEqual(
            education.classes[0].tags, set(["python", "programming", "scripting"])
        )
        self.assertEqual(education.projects[0].label, "Resume Generator")
        self.assertEqual(
            education.projects[0].tags,
            set(["python", "programming", "scripting", "cli"]),
        )


class TestExperience(TestCase):

    serialized = """
        {
            "title": "Software Engineer",
            "begin": "2014-01-01",
            "end": "2018-01-01",
            "location": "New York",
            "achievements": [
                {
                    "label": "Resume Generator",
                    "tags": ["python", "programming", "scripting", "cli"]
                }
            ]
        }
        """

    def test_deserialisation(self):
        experience = Experience.parse_raw(self.serialized)
        self.assertEqual(experience.title, "Software Engineer")
        self.assertEqual(experience.begin, date(2014, 1, 1))
        self.assertEqual(experience.end, date(2018, 1, 1))
        self.assertEqual(experience.location, "New York")
        self.assertEqual(experience.achievements[0].label, "Resume Generator")
        self.assertEqual(
            experience.achievements[0].tags,
            set(["python", "programming", "scripting", "cli"]),
        )


class TestResume(TestCase):

    serialized = """
        {
            "objective": "To be the best software engineer in the world",
            "updated": "2018-01-01",
            "personal": {
                "name": "John Doe",
                "dob": "1990-01-01",
                "address": {
                    "street": "123 Main Street",
                    "zipcode": "12345",
                    "city": "New York",
                    "state": "NY",
                    "country": "USA"
                }
            },
            "contact": {
                "email": "john.doe@example.com",
                "phone": "+1 555 555 5555",
                "linkedin": "https://www.linkedin.com/in/johndoe",
                "github": "https://github.com/johndoe"
            },
            "languages": [
                {
                    "name": "English",
                    "level": "Native"
                }
            ],
            "education": [
                {
                    "title": "Bachelor of Science",
                    "begin": "2010-01-01",
                    "end": "2014-01-01",
                    "location": "New York",
                    "specialisation": "Computer Science",
                    "classes": [
                        {
                            "label": "Python",
                            "tags": ["python", "programming", "scripting"]
                        }
                    ],
                    "projects": [
                        {
                            "label": "Resume Generator",
                            "tags": ["python", "programming", "scripting", "cli"]
                        }
                    ]
                }
            ],
            "experiences": [
                {
                    "title": "Software Engineer",
                    "begin": "2014-01-01",
                    "end": "2018-01-01",
                    "location": "New York",
                    "achievements": [
                        {
                            "label": "Resume Generator",
                            "tags": ["python", "programming", "scripting", "cli"]
                        }
                    ]
                }
            ],
            "hard_skills": [
                {
                    "label": "Python",
                    "tags": ["python", "programming", "scripting"]
                }
            ],
            "soft_skills": [
                {
                    "label": "Teamwork",
                    "tags": ["teamwork", "collaboration", "communication"]
                }
            ]
        }
        """

    def test_deserialisation(self):
        resume = Resume.parse_raw(self.serialized)
        self.assertEqual(
            resume.objective, "To be the best software engineer in the world"
        )
        self.assertEqual(resume.updated, date(2018, 1, 1))
        self.assertEqual(resume.personal.name, "John Doe")
        self.assertEqual(resume.personal.dob, date(1990, 1, 1))
        self.assertEqual(resume.personal.address.street, "123 Main Street")
        self.assertEqual(resume.personal.address.zipcode, "12345")
        self.assertEqual(resume.personal.address.city, "New York")
        self.assertEqual(resume.personal.address.state, "NY")
        self.assertEqual(resume.personal.address.country, "USA")
        self.assertEqual(resume.contact.email, "john.doe@example.com")
        self.assertEqual(resume.contact.phone, "+1 555 555 5555")
        self.assertEqual(resume.contact.linkedin, "https://www.linkedin.com/in/johndoe")
        self.assertEqual(resume.contact.github, "https://github.com/johndoe")
        self.assertEqual(resume.languages[0].name, "English")
        self.assertEqual(resume.languages[0].level, "Native")
        self.assertEqual(resume.education[0].title, "Bachelor of Science")
        self.assertEqual(resume.education[0].begin, date(2010, 1, 1))
        self.assertEqual(resume.education[0].end, date(2014, 1, 1))
        self.assertEqual(resume.education[0].location, "New York")
        self.assertEqual(resume.education[0].specialisation, "Computer Science")
        self.assertEqual(resume.education[0].classes[0].label, "Python")
        self.assertEqual(
            resume.education[0].classes[0].tags,
            set(["python", "programming", "scripting"]),
        )
        self.assertEqual(resume.education[0].projects[0].label, "Resume Generator")
        self.assertEqual(
            resume.education[0].projects[0].tags,
            set(["python", "programming", "scripting", "cli"]),
        )
        self.assertEqual(resume.experiences[0].title, "Software Engineer")
        self.assertEqual(resume.experiences[0].begin, date(2014, 1, 1))
        self.assertEqual(resume.experiences[0].end, date(2018, 1, 1))
        self.assertEqual(resume.experiences[0].location, "New York")
        self.assertEqual(resume.experiences[0].achievements[0].label, "Resume Generator")
        self.assertEqual(
            resume.experiences[0].achievements[0].tags,
            set(["python", "programming", "scripting", "cli"]),
        )
        self.assertEqual(resume.hard_skills[0].label, "Python")
        self.assertEqual(
            resume.hard_skills[0].tags,
            set(["python", "programming", "scripting"]),
        )
        self.assertEqual(resume.soft_skills[0].label, "Teamwork")
        self.assertEqual(
            resume.soft_skills[0].tags,
            set(["teamwork", "collaboration", "communication"]),
        )
