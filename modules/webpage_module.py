from selenium import webdriver
from PIL import Image

def pesquisaImagem(link:str, className:str, nome1:str, nome2:str):
    nome = ""
    
    #invoke actual browser
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    #driver = webdriver.Firefox()
    driver.get(link)
    driver.maximize_window()
    driver.execute_script("document.body.style.zoom='40%'")
    nome = 'images/'+nome1+'_'+nome2+'.png'
    # identifying the logo to capture the screenshot
    element= driver.find_element_by_class_name(className)
    # to get the element location
    location = element.location_once_scrolled_into_view
    # to get the dimension the element
    size = element.size
    # moving to the element location
    driver.execute_script("arguments[0].scrollIntoView();", element)
    #to save the screenshot of complete page
    p = driver.get_screenshot_as_file("images/completo.png")
    #to get the x axis
    l = location['x']
    #to get the y axis
    t = location['y']
    # to get the length the element
    b = location['y']+size['height']
    # to get the width the element
    r = location['x']+size['width']
    # to open the captured image with PIL
    imgOpen = Image.open("images/completo.png")
    # to crop the captured image to size of the logo
    imgLogo = imgOpen.crop((l, t, r, b))
    # to save the cropped image
    imgLogo.save(nome)
    #to close the browser
    driver.close()

def pesquisaTabela(liga:str):
    nome = ""
    
    #invoke actual browser
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    # driver = webdriver.Firefox()
    if liga == "CBLOL":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/CBLOL/2021_Season/Split_1")
        nome = "images/cblol.png"
        
    elif liga == "LCS":
         #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LCS/2021_Season/Spring_Season")
        nome = "images/lcs.png"
        
    elif liga == "LEC":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LEC/2021_Season/Spring_Season")
        nome = "images/lec.png"
        
    elif liga == "LCK":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LCK/2021_Season/Spring_Season")
        nome = "images/lck.png"
        
    elif liga == "LPL":
        #get method to launch the URL
        driver.get("https://lol.gamepedia.com/LPL/2021_Season/Spring_Season")
        nome = "images/lpl.png"
        
    # identifying the logo to capture the screenshot
    element= driver.find_element_by_class_name('standings')
    # to get the element location
    location = element.location_once_scrolled_into_view
    # to get the dimension the element
    size = element.size
    # moving to the element location
    driver.execute_script("arguments[0].scrollIntoView();", element)
    #to save the screenshot of complete page
    p = driver.get_screenshot_as_file("images/completo.png")
    #to get the x axis
    l = location['x']
    #to get the y axis
    t = location['y']
    # to get the length the element
    b = location['y']+size['height']
    # to get the width the element
    r = location['x']+size['width']
    # to open the captured image with PIL
    imgOpen = Image.open("images/completo.png")
    # to crop the captured image to size of the logo
    imgLogo = imgOpen.crop((l, t, r, b))
    # to save the cropped image
    imgLogo.save(nome)
    #to close the browser
    driver.close()

def pesquisaCStats(liga:str, role:str):
    nome = ""

    if liga == "CBLOL":
        if role == "":
            return "https://cutt.ly/nj1vFdU"
        else:
            link = "https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByChampionRole&TS%5Btournament%5D=CBLOL%2F2021+Season%2FSplit+1&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D="+role+"&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, role)
            return 'images/'+liga+"_"+role+'.png'
        
    if liga == "LCS":
        if role == "":
            return "O Torneio não começou ainda!"
        else:
            return
                
    if liga == "LEC":
        if role == "":
            return "https://cutt.ly/Gj1v2C2"
        else:
            link = "https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByChampionRole&TS%5Btournament%5D=LEC%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D="+role+"&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, role)
            return 'images/'+liga+"_"+role+'.png'
        
        
    if liga == "LCK":
        if role == "":
            return "https://cutt.ly/9j2vX6W"
        else:
            link = "https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByChampionRole&TS%5Btournament%5D=LCK%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D="+role+"&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, role)
            return 'images/'+liga+"_"+role+'.png'
        
        
    if liga == "LPL":
        if role == "":
            return "https://cutt.ly/Qj2v83z"
        else:
            link = "https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByChampionRole&TS%5Btournament%5D=LPL%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D="+role+"&TS%5Bteam%5D=&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, role)
            return 'images/'+liga+"_"+role+'.png'

def pesquisaPStats(liga:str, time:str):
    nome = ""

    if liga == "CBLOL":
        if time == "":
            return "https://bit.ly/3sYsm0s"
        else:
            link="https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByPlayer&TS%5Btournament%5D=CBLOL%2F2021+Season%2FSplit+1&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D="+time+"&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, time)
            return 'images/'+liga+"_"+time+'.png'

    if liga == "LCS":
        if time == "":
            return "O Torneio não começou ainda!"
        else:
        #link="https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByPlayer&TS%5Btournament%5D=CBLOL%2F2021+Season%2FSplit+1&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D="+time+"&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
        #pesquisaImagem(link, 'spstats', liga, time)
        #return 'images/'+time+'.png'
            pass
                
    if liga == "LEC":
        if time == "":
            return "https://bit.ly/3okCc92"
        else:
            link="https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByPlayer&TS%5Btournament%5D=LEC%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D="+time+"&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, time)
            return 'images/'+liga+"_"+time+'.png'
        
    if liga == "LCK":
        if time == "":
            return "https://bit.ly/2MkOalX"

        else:
            link="https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByPlayer&TS%5Btournament%5D=LCK%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D="+time+"&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, time)
            return 'images/'+liga+"_"+time+'.png'
        
    if liga == "LPL":
        if time == "":
            return "https://bit.ly/3ojtGaz"

        else:
            link="https://lol.gamepedia.com/Special:RunQuery/TournamentStatistics?pfRunQueryFormName=TournamentStatistics&TS%5Bpreload%5D=TournamentByPlayer&TS%5Btournament%5D=LPL%2F2021+Season%2FSpring+Season&TS%5Blink%5D=&TS%5Bchampion%5D=&TS%5Brole%5D=&TS%5Bteam%5D="+time+"&TS%5Bpatch%5D=&TS%5Byear%5D=&TS%5Bregion%5D=&TS%5Btournamentlevel%5D=&TS%5Bwhere%5D=&TS%5Bincludelink%5D%5Bis_checkbox%5D=true&TS%5Bshownet%5D%5Bis_checkbox%5D=true&wpRunQuery=Run+query&pf_free_text="
            pesquisaImagem(link, 'spstats', liga, time)
            return 'images/'+liga+"_"+time+'.png'
