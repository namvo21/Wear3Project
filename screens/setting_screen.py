from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

class SettingScreen():
    def navigate_To(driver, pageName):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector()).scrollIntoView(text(\"%s\"))" % pageName)
        driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='%s']" % pageName).click()
        sleep(1)