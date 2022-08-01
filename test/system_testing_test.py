from appium import webdriver
from screens.setting_screen import SettingScreen
from screens.gesture_screen import GestureScreen
from screens.connectivity_screen import ConnectivityScreen
from screens.display_screen import DisplayScreen
import pytest


def launchApp(host="http://127.0.0.1:4723/wd/hub", udid='K6E5001121B0007', **kwargs):
    desired_caps = {}
    desired_caps['udid'] = udid
    desired_caps['platformName'] = 'android'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps.update(kwargs)
    return webdriver.Remote(host, desired_caps)


@pytest.fixture(scope="function")
def driver():
    driver = launchApp(appPackage="com.google.android.apps.wearable.settings",
                       appActivity="com.google.android.clockwork.settings.MainSettingsActivity")
    return driver


def test_touch_to_wake_default_setting_should_be_ON(driver):
    SettingScreen.navigate_To(driver, "Gestures")
    assert GestureScreen.is_Touch_To_Wake_Is_On(driver)


def test_tilt_to_wake_default_setting_should_be_OFF(driver):
    SettingScreen.navigate_To(driver, "Gestures")
    assert GestureScreen.is_Tilt_To_Wake_Is_Off(driver)


def test_adjust_brightness(driver):
    SettingScreen.navigate_To(driver, "Display")
    DisplayScreen.navigate_To(driver, "Adjust brightness")

    DisplayScreen.reset_Brightness_To_Minium(driver)
    before_increase = DisplayScreen.get_Brightness_Level(driver)
    DisplayScreen.tap_On_Brightness_Button(driver, "Increase brightness")
    after_increase = DisplayScreen.get_Brightness_Level(driver)
    assert before_increase < after_increase

    DisplayScreen.tap_On_Brightness_Button(driver, "Decrease brightness")
    after_decrease = DisplayScreen.get_Brightness_Level(driver)
    assert after_increase > after_decrease


def test_toggle_bluethooth(driver):
    SettingScreen.navigate_To(driver, "Connectivity")
    SettingScreen.navigate_To(driver, "Bluetooth")

    ConnectivityScreen.navigate_To(driver, "Bluetooth")
    before_status = ConnectivityScreen.is_Toggle_Is_On(driver, "Bluetooth")
    ConnectivityScreen.tap_On_Toggle(driver, "Bluetooth")
    ConnectivityScreen.tap_On_Bluethooth_Confirmation_Popup(driver)
    after_status = ConnectivityScreen.is_Toggle_Is_On(driver, "Bluetooth")
    assert before_status != after_status


def test_toggle_wifi(driver):
    SettingScreen.navigate_To(driver, "Connectivity")
    SettingScreen.navigate_To(driver, "Wi-Fi")

    before_status = ConnectivityScreen.is_Toggle_Is_On(driver, "Wi-Fi")
    ConnectivityScreen.tap_On_Toggle(driver, "Wi-Fi")
    ConnectivityScreen.tap_On_Wifi_Confirmation_Popup(driver)
    after_status = ConnectivityScreen.is_Toggle_Is_On(driver, "Wi-Fi")
    assert before_status != after_status


def test_toggle_always_on_display(driver):
    DisplayScreen.open_Display_Settings(driver, "Display")
    DisplayScreen.navigate_To(driver, "Always-on screen")

    before_status = DisplayScreen.is_Always_On_Screen_Is_On(driver)
    DisplayScreen.tap_On_Toggle(driver)
    after_status = DisplayScreen.is_Always_On_Screen_Is_On(driver)
    assert before_status != after_status
