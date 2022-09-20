# codrone-practice

## Set up

1. Install Python 3.10 and virtualenv
2. Change to the directory of your local clone of this repository

        cd ~/work/codrone-practice
3. Create python virtual environment

        python3 -m venv venv
4. Activate python virtual environment

        source venv/bin/activate
5. Install required packages

        pip install -r requirements.txt

## Usage

1. Turn on the drone.
2. Unplug the controller cable from the BLE board.
3. Plug the BLE board into a USB port.
3. Run a script.

        python pushups.py
