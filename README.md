# Garo Wallbox (EVSE) - HomeAssistant Integration

[![GitHub Release][releases-shield]][releases]
[![License][license-shield]](LICENSE)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![Integration Usage](https://img.shields.io/badge/dynamic/json?color=41BDF5&style=for-the-badge&logo=home-assistant&label=usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.garo_wallbox.total)](https://analytics.home-assistant.io/)


This is a custom component to allow control of Garo Wallboxes in [HomeAssistant](https://home-assistant.io).

<p>
    <img src="https://github.com/sockless-coding/panasonic_cc/raw/master/doc/fixed_controls.png" alt="Example controls" style="vertical-align: top;max-width:100%" align="top" />
    <img src="https://github.com/sockless-coding/panasonic_cc/raw/master/doc/fixed_sensors.png" alt="Example sensors" style="vertical-align: top;max-width:100%" align="top" />
    <img src="https://github.com/sockless-coding/panasonic_cc/raw/master/doc/twin_controls.png" alt="Example controls" style="vertical-align: top;max-width:100%" align="top" />
</p>

#### Support Development
- :coffee:&nbsp;&nbsp;[Buy me a coffee](https://www.buymeacoffee.com/sockless)


## Installation

### Install using HACS (recomended)
If you do not have HACS installed yet visit https://hacs.xyz for installation instructions.
In HACS go to the Integrations section hit the big + at the bottom right and search for **Garo Wallbox**.

### Install manually
Clone or copy this repository and copy the folder 'custom_components/garo_wallbox' into '<homeassistant config>/custom_components/garo_wallbox'

## Configuration

Once installed the Garo Wallbox integration can be configured via the Home Assistant integration interface 
where you can enter the IP address of the device.

## Services

### Set the mode of the EVSE
Service: `garo_wallbox.set_mode`
| Parameter | Description | Example |
| - | - | - |
| entity_id | Name of the entity to change | sensor.garage_charger |
| mode | The new mode available modes: `On`, `Off`, `Schema` | On |

### Set the charge limit
Service: `garo_wallbox.set_current_limit`
| Parameter | Description | Example |
| - | - | - |
| entity_id | Name of the entity to change | sensor.garage_charger |
| limit | The new limit in Ampare | 10 |


[license-shield]: https://img.shields.io/github/license/sockless-coding/garo_wallbox.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/sockless-coding/garo_wallbox.svg?style=for-the-badge
[releases]: https://github.com/sockless-coding/garo_wallbox/releases
