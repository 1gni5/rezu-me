from datetime import date

from pydantic import BaseModel


class Address(BaseModel):
    """Address model."""

    street: str
    zipcode: str
    city: str
    state: str
    country: str


class Contact(BaseModel):
    """Contact model."""

    email: str
    phone: str
    linkedin: str
    github: str


class Personal(BaseModel):
    """Personal informations model."""

    name: str
    dob: date
    address: Address


class Language(BaseModel):
    """Language model."""

    name: str
    level: str


class TaggedItem(BaseModel):
    """Tagged item model."""

    label: str
    tags: set[str]


class Education(BaseModel):
    """Education model."""

    title: str
    begin: date
    end: date
    location: str
    specialisation: str
    classes: list[TaggedItem]
    projects: list[TaggedItem]


class Experience(BaseModel):
    """Experience model."""

    title: str
    begin: date
    end: date
    location: str
    actions: list[TaggedItem]


class Resume(BaseModel):
    """Resume model."""

    objective: str
    updated: date
    contact: Contact
    personal: Personal
    education: list[Education]
    experiences: list[Experience]
    languages: list[Language]
    skills: list[TaggedItem]


    def get_tags(self) -> set[str]:
        """Return a set of all tags in the resume."""
        tags = set()

        for education in self.education:
            for item in education.classes:
                tags |= item.tags
            for item in education.projects:
                tags |= item.tags

        for experience in self.experiences:
            for item in experience.actions:
                tags |= item.tags
        
        for skill in self.skills:
            tags |= skill.tags

        return tags
