from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://gentle-bay-0e4e13803.azurestaticapps.net/videos.html")
    html5video = driver.find_element_by_id("html5video")
    # Video screenshot betöltés után!
    html5video.screenshot('html5video_builtin_load_screenshot.png')
    html5video.click()
    time.sleep(4)
    # Video screenshot 4 másodperccel az indítás után!
    html5video.screenshot('html5video_builtin_play_screenshot.png')
    time.sleep(2)
    html5video.click()
    time.sleep(2)

    video1 = driver.find_element_by_id("video1")
    # Video screenshot betöltés után!
    video1.screenshot('video1_vcc_load_screenshot.png')
    video1_play_pause = driver.find_element_by_xpath('//button[@onclick="playPause()"]')
    video1_play_pause.click()
    time.sleep(4)
    # Video screenshot 4 másodperccel az indítás után!
    video1.screenshot('video1_vcc_play_screenshot.png')
    video1_play_pause.click()
    time.sleep(2)

    youtube_frame = driver.find_element_by_id("youtubeframe")
    driver.switch_to.frame(youtube_frame)
    time.sleep(1)
    youtube_play = driver.find_element_by_xpath('//button[@class="ytp-large-play-button ytp-button"]')
    # Video screenshot betöltés után!
    youtube_play.screenshot('youtube_iframe_load.png')
    youtube_play.click()
    time.sleep(20)
    youtube_pause = driver.find_element_by_xpath('//button[@class="ytp-play-button ytp-button"]')
    # Video screenshot 20 másodperccel az indítás után!
    youtube_pause.screenshot('youtube_iframe_play.png')
    youtube_pause.click()
    time.sleep(4)


finally:
    driver.close()
