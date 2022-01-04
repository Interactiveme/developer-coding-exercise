class PostParentDTO:
    def __init__(self, content):
        self.content = content


class PostDTO(PostParentDTO):
    def __init__(self, tags, content):
        self.tags = tags
        super().__init__(content)


class PostStubDTO(PostParentDTO):
    def __init__(self, title, slug, author, content):
        self.title = title
        self.author = author
        self.slug = slug
        super().__init__(content)
