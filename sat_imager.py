#Bing Images -> horiztontal translation == 8 key presses; vertical translation == 4 key presses;
#Start at 100 meter resolution satellite image
#Each horizontal pan covers ~1,450 meters
#Each vertical pan covers ~650 meters

#Country Georegion horizontal square == 173,690 meters
#Country Georegion vertical square == 441,380 meters

#Bing Starting coords -> 29.510579, 34.191551 (lower left)

h_block = 1450
v_block = 650
h_dist = 173690
v_dist = 441380

h_pan_count = h_dist / h_block
v_pan_count = v_dist / v_block

print('\nBing\n')
hline = '-'*12
print(f'Horizontal pans: {h_pan_count:.2f}\nVertical pans: {v_pan_count:.2f}')

pan_tot_count = v_pan_count * h_pan_count
print(f'Total pan count: {pan_tot_count:,.2f}')

print(hline)

################################################


#Google Earth Images -> Horizontal press == ~4.5 second hold; Vertical press == 6 second hold
#Camera Height -> ~1,640 meters
#Starting Coords -> https://earth.google.com/web/@29.51598064,34.27119323,708.6334802a,950.89642911d,35y,0h,0t,0r (lower left)
#Pan right all the pan_counts, then pan vertical one pan_count, then pan left all pan_counts, pan vert one, etc.
print('\nGoogle Earth\n')
h_block = 7718.53
v_block = 3934.72
h_pan_count = h_dist / h_block
v_pan_count = v_dist / v_block

print(f'Horizontal pans: {h_pan_count:.2f}\nVertical pans: {v_pan_count:.2f}')

pan_tot_count = v_pan_count * h_pan_count
print(f'Total pan count: {pan_tot_count:,.2f}')
print(hline)



# Chromedriver location = /usr/local/bin/chromedriver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pgui
PATH = '/usr/local/bin/chromedriver'
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=PATH, options=option)
driver.maximize_window()
with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'r') as f:
    coords = str(f.read().split('\n')[-1])
driver.get(coords)
# print(driver.current_url)
# driver.set_window_size(1024, 600)
sleep(20)

screen_width, screen_height = pgui.size()

#Screenshot
#Upper left: (x=0, y=149)
#Lower left: (x=0, y=839)
#Upper right: (x=1459, y=149)
#Lower right: (x=1459, y=839)

# with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/i.txt', 'r') as f:
#     i_start = int(f.read())

for j in range(113):
    for i in range(23):
        pgui.moveTo(x=(screen_width/2), y=(screen_height/2))
        pgui.leftClick()
        pgui.screenshot(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.png')
        # with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'a') as f:
        #     f.write(f'\n{driver.current_url}')
        pgui.keyDown(pgui.RIGHT)
        sleep(1.65)
        pgui.keyUp(pgui.RIGHT)
        sleep(5)
        sat_name = driver.current_url.split('@')[-1]
        latitude = sat_name.split(',')[0]
        longitude = sat_name.split(',')[1]
        # elevation = sat_name.split(',')[2].split('a')[0]
        label = [latitude, longitude]
        with open(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.txt', 'w') as f:
            f.write(str(label))
        # with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/i.txt', 'w') as f:
        #     f.write(i)

        #TEST VERT MOVEMENT CODE
        # pgui.moveTo(x=(screen_width/2), y=(screen_height/2))
        # pgui.leftClick()
        # pgui.keyDown('up')
        # sleep(1.65)
        # pgui.keyUp('up')
        # sleep(5)
        # pgui.screenshot(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.png')
        # # sleep(3)
        # with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'a') as f:
        #     f.write(f'\n{driver.current_url}')
        # sat_name = driver.current_url.split('@')[-1]
        # latitude = sat_name.split(',')[0]
        # longitude = sat_name.split(',')[1]
        # # elevation = sat_name.split(',')[2].split('a')[0]
        # label = [latitude, longitude]
        # with open(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.txt', 'w') as f:
        #     f.write(str(label))

    pgui.moveTo(x=(screen_width/2), y=(screen_height/2))
    pgui.leftClick()
    pgui.keyDown('up')
    sleep(1.65)
    pgui.keyUp('up')
    sleep(5)
    pgui.screenshot(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.png')
    # sleep(3)
    with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'a') as f:
        f.write(f'\n{driver.current_url}')
    sat_name = driver.current_url.split('@')[-1]
    latitude = sat_name.split(',')[0]
    longitude = sat_name.split(',')[1]
    # elevation = sat_name.split(',')[2].split('a')[0]
    label = [latitude, longitude]
    with open(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_R_{i}_{j}.txt', 'w') as f:
        f.write(str(label))

    for i in range(23):
        pgui.moveTo(x=(screen_width/2), y=(screen_height/2))
        pgui.leftClick()
        pgui.screenshot(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_L_{i}_{j}.png')
        sleep(3)
        # with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'a') as f:
        #     f.write(f'\n{driver.current_url}')
        sat_name = driver.current_url.split('@')[-1]
        latitude = sat_name.split(',')[0]
        longitude = sat_name.split(',')[1]
        # elevation = sat_name.split(',')[2].split('a')[0]
        label = [latitude, longitude]
        with open(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_L_{i}_{j}.txt', 'w') as f:
            f.write(str(label))
        pgui.keyDown(pgui.LEFT)
        sleep(1.65)
        pgui.keyUp(pgui.LEFT)
        sleep(5)

    pgui.moveTo(x=(screen_width/2), y=(screen_height/2))
    pgui.leftClick()
    pgui.keyDown('up')
    sleep(1.65)
    pgui.keyUp('up')
    sleep(5)
    pgui.screenshot(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_L_{i}_{j}.png')
    # sleep(3)
    with open('/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/tracked_coords.txt', 'a') as f:
        f.write(f'\n{driver.current_url}')
    sat_name = driver.current_url.split('@')[-1]
    latitude = sat_name.split(',')[0]
    longitude = sat_name.split(',')[1]
    # elevation = sat_name.split(',')[2].split('a')[0]
    label = [latitude, longitude]
    with open(f'/Users/jordanianjoker/Desktop/Code/Py/Satellite Images/sat_L_{i}_{j}.txt', 'w') as f:
        f.write(str(label))