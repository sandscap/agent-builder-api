import pytest
from agentbuilder.llm import extract_after_slash


def test_extract_after_slash_with_model():
    assert extract_after_slash("openai/gpt-4o") == ("openai", "gpt-4o")


def test_extract_after_slash_without_model():
    assert extract_after_slash("openai") == ("openai", None)
