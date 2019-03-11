import typing


class Call:
    source: str = NotImplemented

    def _sendmessage(self, text):
        raise NotImplementedError()

    sendmessage: typing.Callable = _sendmessage


class Command:
    """A generic command, called from any source."""

    def call(self, call: Call):
        method_name = f"_{call.source}"
        try:
            method: typing.Callable = getattr(self, method_name)
            # Ci va il self. ?
            method(call)
        except AttributeError:
            self._common(call)

    def _common(self, cd: Call):
        raise NotImplementedError()
