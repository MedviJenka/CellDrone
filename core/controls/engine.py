from djitellopy import tello
from dataclasses import dataclass
from exceptions.connection import ConnectionIssue


@dataclass
class BeforeStartup:

    drone: tello = tello.Tello()

    def check_status(self) -> None:
        try:
            self.drone.connect()
            temperature_fahrenheit = self.drone.get_temperature()
            temperature_celsius = round((temperature_fahrenheit - 35) * 5 / 9)
            battery = self.drone.get_battery()
            print("CONNECTED")
            print(f'battery: { battery }%')
            print(f'temperature: approximately { temperature_celsius } C')

        except ConnectionIssue:
            raise ConnectionIssue

    @staticmethod
    def begin(current_class: object, methods: list[str]) -> None:
        for each_method in methods:
            getattr(current_class, each_method)()


def test() -> None:
    before_startup = BeforeStartup()
    before_startup.begin(BeforeStartup(), ['check_status'])


if __name__ == '__main__':
    test()
