from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

class ConnectivityScreen():
    def navigate_To(driver, connectivityName):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector()).scrollIntoView(text(\"%s\"))" % connectivityName)

    def tap_On_Toggle(driver, connectivityName): 
        driver.find_element(AppiumBy.XPATH, "(//android.widget.Switch[@content-desc='%s'])[2]" % connectivityName).click()
        sleep(1)
    
    def tap_On_Bluethooth_Confirmation_Popup(driver): 
        driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='OK']").click()
        sleep(1)

    def tap_On_Wifi_Confirmation_Popup(driver): 
        driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='OK']").click()
        sleep(1)

    def is_Toggle_Is_On(driver, connectivityName):
        toggle_status = driver.find_element(AppiumBy.XPATH,"(//android.widget.Switch[@content-desc='%s'])[2]" % connectivityName).get_attribute("checked")
        return toggle_status == "true"