from . import const, utils

class GaroStatus:

    def __init__(self, json = None):
        self._connector = const.Connector.UNKNOWN
        self._mode = const.Mode.Off
        self._current_limit = 0
        self._factory_current_limit = 0
        self._switch_current_limit = 0
        self._power_mode = const.PowerMode.Off
        self._current_charging_current = 0.0
        self._current_charging_power = 0
        self._acc_session_energy = 0
        self._acc_session_millis = 0
        self._latest_reading = 0
        self._charge_status = 0
        self._current_temperature = 0
        self._number_of_phases = 1
        self._pilot_level = 0

        self._has_changed = False        
        self.load(json)

    def load(self, json = None) -> bool:
        if not json:
            return False
        
        self.connector = utils.read_enum(json,'connector', const.Connector, self._connector)
        self.mode = utils.read_enum(json,'mode', const.Mode, self._mode)
        self.current_limit = utils.read_value(json,'currentLimit', self._current_limit)
        self.factory_current_limit = utils.read_value(json,'factoryCurrentLimit', self._factory_current_limit)
        self.switch_current_limit = utils.read_value(json,'switchCurrentLimit', self._switch_current_limit)
        self.power_mode = utils.read_enum(json,'powerMode', const.PowerMode, self._power_mode)
        self.current_charging_current = utils.read_value(json,'currentChargingCurrent', self._current_charging_current)
        self.current_charging_power = utils.read_value(json,'currentChargingPower', self._current_charging_power)
        self.acc_session_energy = utils.read_value(json,'accSessionEnergy', self._acc_session_energy)
        self.acc_session_millis = utils.read_value(json,'accSessionMillis', self._acc_session_millis)
        self.latest_reading = utils.read_value(json,'latestReading', self._latest_reading)
        self.charge_status = utils.read_value(json,'chargeStatus', self._charge_status)
        self.current_temperature = utils.read_value(json,'currentTemperature', self._current_temperature)
        self.number_of_phases = utils.read_value(json,'nrOfPhases', self._number_of_phases)
        self.pilot_level = utils.read_value(json,'pilotLevel', self._pilot_level)

        has_changed = self._has_changed
        self._has_changed = False
        return has_changed
    
    @property
    def connector(self):        
        return self._connector
    @connector.setter
    def connector(self, value):
        if self._connector == value:
            return
        self._connector = value
        self._has_changed = True

    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, value):
        if self._mode == value:
            return
        self._mode = value
        self._has_changed = True

    @property
    def current_limit(self):
        return self._current_limit
    @current_limit.setter
    def current_limit(self, value):
        if self._current_limit == value:
            return
        self._current_limit = value
        self._has_changed = True

    @property
    def factory_current_limit(self):
        return self._factory_current_limit
    @factory_current_limit.setter
    def factory_current_limit(self, value):
        if self._factory_current_limit == value:
            return
        self._factory_current_limit = value
        self._has_changed = True

    @property
    def switch_current_limit(self):
        return self._switch_current_limit
    @switch_current_limit.setter
    def switch_current_limit(self, value):
        if self._switch_current_limit == value:
            return
        self._switch_current_limit = value
        self._has_changed = True

    @property
    def power_mode(self):
        return self._power_mode
    @power_mode.setter
    def power_mode(self, value):
        if self._power_mode == value:
            return
        self._power_mode = value
        self._has_changed = True

    @property
    def current_charging_current(self):
        return self._current_charging_current
    @current_charging_current.setter
    def current_charging_current(self, value):
        value = max(0, value / 1000)
        if self._current_charging_current == value:
            return
        self._current_charging_current = value
        self._has_changed = True

    @property
    def current_charging_power(self):
        return self._current_charging_power
    @current_charging_power.setter
    def current_charging_power(self, value):
        if value > 32000:
            value = 0
        if self._current_charging_power == value:
            return
        self._current_charging_power = value
        self._has_changed = True

    @property
    def acc_session_energy(self):
        return self._acc_session_energy
    @acc_session_energy.setter
    def acc_session_energy(self, value):
        if self._acc_session_energy == value:
            return
        self._acc_session_energy = value
        self._has_changed = True

    @property
    def acc_session_millis(self):
        return self._acc_session_millis
    @acc_session_millis.setter
    def acc_session_millis(self, value):
        if self._acc_session_millis == value:
            return
        self._acc_session_millis = value
        self._has_changed = True

    @property
    def latest_reading(self):
        return self._latest_reading
    @latest_reading.setter
    def latest_reading(self, value):
        if self._latest_reading == value:
            return
        if self._latest_reading > 0 and value - self._latest_reading > 500000:
            return
        self._latest_reading = value
        self._has_changed = True

    @property
    def charge_status(self):
        return self._charge_status
    @charge_status.setter
    def charge_status(self, value):
        if self._charge_status == value:
            return
        self._charge_status = value
        self._has_changed = True

    @property
    def current_temperature(self):
        return self._current_temperature
    @current_temperature.setter
    def current_temperature(self, value):
        if self._current_temperature == value:
            return
        self._current_temperature = value
        self._has_changed = True

    @property
    def number_of_phases(self):
        return self._number_of_phases
    @number_of_phases.setter
    def number_of_phases(self, value):
        if self._number_of_phases == value:
            return
        self._number_of_phases = value
        self._has_changed = True

    @property
    def pilot_level(self):
        return self._pilot_level
    @pilot_level.setter
    def pilot_level(self, value):
        if self._pilot_level == value:
            return
        self._pilot_level = value
        self._has_changed = True
