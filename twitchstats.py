from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

i = 0

#url = "https://www.twitch.tv/uzra"
url = "https://www.twitch.tv/never_loses"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#打开参数面板
#driver.find_element_by_xpath("//button[@aria-label='设置']").click()
#driver.find_element_by_xpath("//button[@data-a-target='player-settings-menu-item-advanced']").click()
#driver.find_element_by_xpath("//div[@data-test-selector='video-stats-toggle']").click()

#wait for data loading
time.sleep(10)

#创建csv
headers = ['视频分辨率','显示分辨率','FPS','跳帧数','缓冲区大小','直播者延迟','延迟模式','回放速率']
with open('record.csv','w',newline='')as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)

while True:
    #回放视频时需要注释掉直播者延迟、延迟模式
    video_resolution = driver.find_element_by_xpath('//p[@aria-label="视频分辨率"]').text
    display_resolution = driver.find_element_by_xpath('//p[@aria-label="显示分辨率"]').text
    fps = driver.find_element_by_xpath('//p[@aria-label="FPS"]').text
    skipped_frames = driver.find_element_by_xpath('//p[@aria-label="跳帧数"]').text
    buffer_size = driver.find_element_by_xpath('//p[@aria-label="缓冲区大小"]').text
    latency_to_broadcaster = driver.find_element_by_xpath('//p[@aria-label="直播者延迟"]').text
    latency_mode = driver.find_element_by_xpath('//p[@aria-label="延迟模式"]').text
    playback_rate = driver.find_element_by_xpath('//p[@aria-label="回放速率"]').text
    
    rows = [video_resolution, display_resolution, fps, skipped_frames, buffer_size, latency_to_broadcaster, latency_mode, playback_rate]
    print(rows)
    
    #写入本地csv
    with open('record.csv','a',newline='')as f:
        f_csv = csv.writer(f)
        f_csv.writerow(rows)
    
    i = i+1
    print("总记录数：")
    print(i)
    
    time.sleep(1)
