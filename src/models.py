from datetime import date
from copy import deepcopy

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
    mission: str
    achievements: list[TaggedItem]


class Resume(BaseModel):
    """Resume model."""

    objective: str
    updated: date
    contact: Contact
    personal: Personal
    education: list[Education]
    experiences: list[Experience]
    languages: list[Language]
    hard_skills: list[TaggedItem]
    soft_skills: list[TaggedItem]

    def get_tags(self) -> set[str]:
        """Return a set of all tags in the resume."""
        tags = set()

        for education in self.education:
            for item in education.classes:
                tags |= item.tags
            for item in education.projects:
                tags |= item.tags

        for experience in self.experiences:
            for item in experience.achievements:
                tags |= item.tags

        for skill in self.soft_skills + self.hard_skills:
            tags |= skill.tags

        return tags

    def render(self, tags: set[str]) -> "Resume":
        """Return a copy of the resume with only the given tags."""
        resume = deepcopy(self)

        def filter_tags(items: list[TaggedItem], tags: set[str]) -> set[str]:
            """Filter and order items based on given tags."""
            return sorted(
                [item for item in items if item.tags & tags],
                key=lambda item: len(item.tags),
                reverse=True,
            )

        for education in resume.education:
            education.classes = filter_tags(education.classes, tags)
            education.projects = filter_tags(education.projects, tags)

        for experience in resume.experiences:
            experience.achievements = filter_tags(experience.achievements, tags)

        resume.hard_skills = filter_tags(resume.hard_skills, tags)
        resume.soft_skills = filter_tags(resume.soft_skills, tags)

        return resume
