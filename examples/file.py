class FileManager(TaggedClass):
    """In this setup, the exists method will be called before each call to
    open"""

    def __init__(self, filename):
        self.filename = filename

    @tag("pre_open")
    def exists(self):
        if not os.path.exists(self.filename):
            raise ValueError

    @apply_pre_processor
    def open(self):
        pass


class FileManager(TaggedClass):

    @tag("pre_open")
    def exists(self):
        pass

    def open(self):
        hooks = self.get_tag_processors("pre_open")
        hooks = self.get_preprocessor("open")

pre_open = tag_processor("pre_open")
post_open = post_processor("open")
class ABC():
    @pre_open
    def exists(self):
        pass
    @apply_hooks
    def open(self):
        pass
    @post_open
    def close(self):
        pass
