import logging


class event:
    def __init__(self, start_time: int, end_time, name) -> None:
        self.start_time = start_time
        self.end_time = end_time
        self.name = name
        logging.info("event instance is created")

    def duration(self):
        return self.end_time - self.start_time

    def overlaps(self, other) -> bool:
        return other.start_time <= self.start_time <= other.endtime \
            or self.start_time <= other.start_time <= self.end_time

    def __str__(self) -> str:
        return "{0}: from {1} to {2}".format(self.name, self.start_time, self.end_time)

    def __eq__(self, __o: object) -> bool:
        if self.start_time == __o.start_time and self.end_time == __o.end_time and self.name == __o.name:
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
