from typing import List

from pydantic import BaseModel


class BaseGitaModel(BaseModel):
    id: int

    class Config:
        orm_mode = True


class GitaTranslation(BaseGitaModel):
    description: str
    author_name: str
    language: str


class GitaTransliteration(BaseGitaModel):

    description: str
    language: str
    verse_id: int
    language_id: int


class GitaCommentary(BaseGitaModel):
    description: str
    author_name: str
    language: str


class GitaVerse(BaseGitaModel):
    verse_number: int
    chapter_number: int
    slug: str
    text: str
    sanskrit_recitation_url: str
    word_meanings: str
    translations: List[GitaTranslation] = []
    commentaries: List[GitaCommentary] = []
    transliterations: List[GitaTransliteration] = []


class GitaChapter(BaseGitaModel):
    name: str
    slug: str
    name_transliterated: str
    name_translated: str
    verses_count: int
    chapter_number: int
    name_meaning: str
    chapter_summary: str


class VerseOfDay(BaseGitaModel):
    id: int
    verse_order: int
