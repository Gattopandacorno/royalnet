from ..utils.commands import Command, Call


class PingCommand(Command):
    def _common(self, c: Call):
        c.reply("Ping!")
