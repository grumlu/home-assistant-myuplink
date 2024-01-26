"""Test for the myUplink integration."""

from custom_components.myuplink.const import DOMAIN as MYUPLINK_DOMAIN


# from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component

async def test_setup_with_no_config(hass) -> None:
    """Test that we do not discover anything or try to set up a controller."""
    assert await async_setup_component(hass, MYUPLINK_DOMAIN, {}) is True
    assert MYUPLINK_DOMAIN not in hass.data