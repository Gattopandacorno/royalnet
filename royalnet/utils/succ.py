class Succ:
    """All calls to this class return itself."""

    def __bool__(self):
        return False

    def __getattr__(self, attr):
        return Succ()

    def __call__(self, *args, **kwargs):
        return Succ()

    def __str__(self):
        return "succ"

    def __repr__(self):
        return "<Succ>"
