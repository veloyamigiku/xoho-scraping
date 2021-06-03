import os
import sys

from scraping import scraping_coming_soon, scraping_now_playing_share
from scraping import scraping_now_playing
from download import download_file


now_playing_txt_path = sys.argv[1]
now_playing_img_dir = sys.argv[2]
coming_soon_txt_path = sys.argv[3]
coming_soon_img_dir = sys.argv[4]
now_playing_share_txt_path = sys.argv[5]


if not os.path.isdir(now_playing_img_dir):
  os.makedirs(now_playing_img_dir)

if not os.path.isdir(coming_soon_img_dir):
  os.makedirs(coming_soon_img_dir)

now_playing_html_str = None
with open(now_playing_txt_path, mode="r", encoding="UTF-8") as html_f:
  now_playing_html_str = html_f.read()

now_playing_list = scraping_now_playing(now_playing_html_str)
# print(now_playing_list)

coming_soon_html_str = None
with open(coming_soon_txt_path, mode="r", encoding="UTF-8") as html_f:
  coming_soon_html_str = html_f.read()

coming_soon_list = scraping_coming_soon(coming_soon_html_str)
# print(coming_soon_list)

now_playing_share_html_str = None
with open(now_playing_share_txt_path, mode="r", encoding="UTF-8") as html_f:
  now_playing_share_html_str = html_f.read()

now_playing_share_list = scraping_now_playing_share(now_playing_share_html_str)


"""
now_playing_img_name_prefix = "now_playing_"
now_playing_img_idx = 1
for now_playing in now_playing_list:
  now_playing_img_url = now_playing["img_url"]
  now_playing_img_name = now_playing_img_name_prefix + str(now_playing_img_idx) + ".jpg"
  now_playing_img_path = now_playing_img_dir + os.sep + now_playing_img_name
  #print("now_playing_img_path:", now_playing_img_path)
  download_file(
      now_playing_img_url,
      now_playing_img_path)
  now_playing_img_idx += 1

coming_soon_img_name_prefix = "coming_soon_"
coming_soon_img_idx = 1
for coming_soon in coming_soon_list:
  coming_soon_img_url = coming_soon["img_url"]
  coming_soon_img_name = coming_soon_img_name_prefix + str(coming_soon_img_idx) + ".jpg"
  coming_soon_img_path = coming_soon_img_dir + os.sep + coming_soon_img_name
  #print("coming_soon_img_path:", coming_soon_img_path)
  download_file(
      coming_soon_img_url,
      coming_soon_img_path)
  coming_soon_img_idx += 1
"""
