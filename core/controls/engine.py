from djitellopy import tello
from dataclasses import dataclass
from core.exceptions.connection import ConnectionIssue
from abc import ABC
from time import sleep


class Drone(ABC):

    drone: tello = tello.Tello()


@dataclass
class BeforeStartup(Drone):

    def check_connection_status(self) -> None:
        try:
            self.drone.connect()
            print("\nCONNECTED")
        except ConnectionIssue:
            raise ConnectionIssue

    def check_data(self) -> None:
        temperature_fahrenheit = self.drone.get_temperature()
        temperature_celsius = round((temperature_fahrenheit - 35) * 5 / 9)
        battery = self.drone.get_battery()
        print(f'battery: { battery }%')
        print(f'temperature: approximately { temperature_celsius } C')


@dataclass
class AfterStartup:
    ...


@dataclass
class BeforeTakeOff:
    ...


@dataclass
class Controls(Drone):

    def takeoff(self) -> None:
        self.drone.takeoff()
        sleep(2)
        self.drone.send_rc_control(0,0,0,0)
        self.drone.land()


def begin(current_class: object, methods: list[str]) -> None:
    for each_method in methods:
        getattr(current_class, each_method)()


def test() -> None:
    begin(BeforeStartup(), ['check_connection_status',
                            'check_data'])
    begin(Controls(), ['takeoff'])


if __name__ == '__main__':
    test()
