from appium.webdriver.common.appiumby import AppiumBy

class GestureScreen():
    def is_Touch_To_Wake_Is_On(driver):
        touch_to_wake_status = driver.find_element(AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='Touch-to-wake'])[2]").get_attribute("checked")
        return touch_to_wake_status == "true"

    def is_Tilt_To_Wake_Is_Off(driver):
        tilt_to_wake_status = driver.find_element(AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='Tilt-to-wake'])[2]").get_attribute("checked")
        return tilt_to_wake_status == "false"