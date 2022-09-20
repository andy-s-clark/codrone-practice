import logging
import time

import CoDrone

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

drone = CoDrone.CoDrone()

logging.info('Pairing to nearest')
drone.pair(drone.Nearest)
logging.info('Pairing complete')

battery_percentage = drone.get_battery_percentage()
logging.info(f'Battery level {battery_percentage:.2f}%')


logging.info('Ready to fly?')
ready_count = 0
while not drone.is_ready_to_fly():
    if ready_count > 10:
        logging.error('Not ready to fly')
        exit()
    ready_count += ready_count
    time.sleep(0.5)

for i in range(3):
    logging.info(f'Pushup #{i}')
    drone.takeoff()
    drone.land()


drone.close()
logging.info('Connection closed')
