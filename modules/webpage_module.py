from selenium import webdriver
from PIL import Image

def printaTabela(liga):
    #browser exposes an executable file
    #Through Selenium test we will invoke the executable file which will then
    #invoke actual browser
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    if liga == "CBLOL":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/CBLOL/2021_Season/Split_1")
        
    elif liga == "LCS":
         #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LCS/2021_Season/Spring_Season")
        
    elif liga == "LEC":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LEC/2021_Season/Spring_Season")
        
    elif liga == "LCK":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LCK/2021_Season/Spring_Season")
        
    elif liga == "LPL":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LPL/2021_Season/Spring_Season")
        

    # identifying the logo to capture the screenshot
    element= driver.find_element_by_class_name('standings')
    # to get the element location
    location = element.location_once_scrolled_into_view
    # to get the dimension the element
    size = element.size
    # moving to the element location
    driver.execute_script("arguments[0].scrollIntoView();", element)
    #to save the screenshot of complete page
    p = driver.get_screenshot_as_file("completo.png")
    #to get the x axis
    l = location['x']
    #to get the y axis
    t = location['y']
    # to get the length the element
    b = location['y']+size['height']
    # to get the width the element
    r = location['x']+size['width']
    # to open the captured image with PIL
    imgOpen = Image.open("completo.png")
    # to crop the captured image to size of the logo
    imgLogo = imgOpen.crop((l, t, r, b))
    # to save the cropped image
    imgLogo.save("cortado.png")
    #to close the browser
    driver.close()