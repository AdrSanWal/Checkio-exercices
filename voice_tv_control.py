CHANNELS = ["BBC", "Discovery", "TV1000"]


class VoiceCommand():
    def __init__(self, channels):
        self.channels = channels
        self.cur_channel = 0

    def first_channel(self):
        self.cur_channel = 0
        return self.channels[0]

    def last_channel(self):
        self.cur_channel = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, c):
        self.cur_channel = c - 1
        return self.channels[c - 1]

    def next_channel(self):
        if self.cur_channel == len(self.channels) - 1:
            self.cur_channel = 0
        else:
            self.cur_channel += 1
        return self.channels[self.cur_channel]

    def previous_channel(self):
        if self.cur_channel == 0:
            self.cur_channel = len(self.channels) - 1
        else:
            self.cur_channel -= 1
        return self.channels[self.cur_channel]

    def current_channel(self):
        return self.channels[self.cur_channel]

    def is_exist(self, channel):
        if isinstance(channel, int):
            return 'Yes' if channel <= len(self.channels) else 'No'
        return 'Yes' if channel in self.channels else 'No'

controller = VoiceCommand(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
