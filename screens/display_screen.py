from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
import os

class DisplayScreen():    
    def open_Display_Settings(driver, pageName):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector()).scrollIntoView(text(\"%s\"))" % pageName)
        driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='%s']" % pageName).click()
        sleep(1)

    def navigate_To(driver, connectivityName):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector()).scrollIntoView(text(\"%s\"))" % connectivityName)

    def is_Always_On_Screen_Is_On(driver):
        aos_status = driver.find_element(AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='Always-on screen'])[2]").get_attribute("checked")
        return aos_status == "true"

    def tap_On_Toggle(driver): 
        driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@content-desc='Always-on screen'])[2]").click()
        sleep(1)

    def reset_Brightness_To_Minium(driver):
        DisplayScreen.tap_On_Brightness_Button(driver, "Decrease brightness")

    def tap_On_Brightness_Button(driver, buttonName):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID,'%s' %buttonName).click()

    def get_Brightness_Level(driver):
        for level in os.system("adb shell settings get system screen_brightness").read():
            brightness_level = level
        return brightness_level