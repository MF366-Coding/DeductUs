# difficulty manager for DeductUs

class Difficulty:
    def __init__(self, value: int, tags: dict[str, tuple[int, int] | str], default_tags: dict[str, tuple[int, int]] = None) -> None:
        self._DIFF_VALUE: int = value
        self._DIFF_NAME: str = tags.pop("NAME", "Unknown Difficulty")
        self._DIFF_TAGS: dict[str, tuple[int, int]] = tags.copy() # [i] we separated the name to avoid further trouble :/
        self._DEFAULT_TAGS = None

        if default_tags is None:
            self._DEFAULT_TAGS: dict[str, tuple[int, int]] = tags.copy()

        else:
            self._DEFAULT_TAGS: dict[str, tuple[int, int]] = default_tags

    def get_tag(self, tag: str) -> tuple[int, int] | None:
        return self._DIFF_TAGS.get(tag, self._DEFAULT_TAGS.get(tag, None)) # [i] No, I was not gonna enter a loop
        # [i] It's only a second chance for me not to screw it up :) - or the player, if they try to modify the source...

    @property
    def name(self) -> str:
        return self._DIFF_NAME

    @property
    def difficulty_id(self) -> int:
        return self._DIFF_VALUE

    @property
    def full_copy(self) -> dict[str, tuple[int, int] | str]:
        # [*] full version with the tag NAME
        return {"NAME": self._DIFF_NAME, **self._DIFF_TAGS.copy()}

    @property
    def regular_copy(self) -> dict[str, tuple[int, int]]:
        return self._DIFF_TAGS.copy()
