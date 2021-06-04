import json
import os
import re
import sys

from scraping import scraping_coming_soon
from scraping import scraping_now_playing
from download import download_file


def extract_mm_dd_day(mm_dd_day):
  match_res = re.match('^(\d{1,2})/(\d{1,2})\((.+)\)', mm_dd_day)
  mm = match_res.group(1)
  dd = match_res.group(2)
  day = match_res.group(3)
  return (mm, dd, day)


def dump_now_playing_json(now_playing_download_list, output_dir):
  now_playing_list = []
  for now_playing_download in now_playing_download_list:
    now_playing_list.append({
        "title": now_playing_download["title"],
        "url": "",
        "img_url": ""})
  now_playing_json = json.dumps(
      now_playing_list,
      ensure_ascii=False,
      indent=2)
  with open(output_dir + os.sep + "now_playing_json.txt", mode="w", encoding="UTF-8") as f:
    f.write(now_playing_json)


def dump_coming_soon_json(coming_soon_download_list, output_dir):
  coming_soon_list = []
  pre_mm_dd_day = None
  movie_list = []
  for coming_soon_download in coming_soon_download_list:
    mm_dd_day = coming_soon_download["mm_dd_day"]
    movie = {
        "title": coming_soon_download["title"],
        "url": "",
        "img_url": ""}
    if pre_mm_dd_day is None or pre_mm_dd_day == mm_dd_day:
      movie_list.append(movie)
      pre_mm_dd_day = mm_dd_day
    else:
      (mm, dd, day) = extract_mm_dd_day(pre_mm_dd_day)
      coming_soon_list.append({
          "mm": int(mm),
          "dd": int(dd),
          "day": day,
          "movie_list": movie_list})
      pre_mm_dd_day = mm_dd_day
      movie_list = [movie]
  if len(movie_list) > 0:
    (mm, dd, day) = extract_mm_dd_day(pre_mm_dd_day)
    coming_soon_list.append({
        "mm": int(mm),
        "dd": int(dd),
        "day": day,
        "movie_list": movie_list})

  coming_soon_json = json.dumps(
      coming_soon_list,
      ensure_ascii=False,
      indent=2)
  with open(output_dir + os.sep + "coming_soon_json.txt", mode="w", encoding="UTF-8") as f:
    f.write(coming_soon_json)


now_playing_txt_path = sys.argv[1]
now_playing_img_dir = sys.argv[2]
coming_soon_txt_path = sys.argv[3]
coming_soon_img_dir = sys.argv[4]


if not os.path.isdir(now_playing_img_dir):
  os.makedirs(now_playing_img_dir)

if not os.path.isdir(coming_soon_img_dir):
  os.makedirs(coming_soon_img_dir)

now_playing_html_str = None
with open(now_playing_txt_path, mode="r", encoding="UTF-8") as html_f:
  now_playing_html_str = html_f.read()

now_playing_download_list = scraping_now_playing(now_playing_html_str)

dump_now_playing_json(
    now_playing_download_list,
    now_playing_img_dir)

coming_soon_html_str = None
with open(coming_soon_txt_path, mode="r", encoding="UTF-8") as html_f:
  coming_soon_html_str = html_f.read()

coming_soon_download_list = scraping_coming_soon(coming_soon_html_str)

dump_coming_soon_json(
    coming_soon_download_list,
    coming_soon_img_dir)

now_playing_img_name_prefix = "now_playing_"
now_playing_img_idx = 1
for now_playing_download in now_playing_download_list:
  now_playing_img_url = now_playing_download["img_url"]
  now_playing_img_name = now_playing_img_name_prefix + str(now_playing_img_idx) + ".jpg"
  now_playing_img_path = now_playing_img_dir + os.sep + now_playing_img_name
  #print("now_playing_img_path:", now_playing_img_path)
  download_file(
      now_playing_img_url,
      now_playing_img_path)
  now_playing_img_idx += 1

coming_soon_img_name_prefix = "coming_soon_"
coming_soon_img_idx = 1
for coming_soon_download in coming_soon_download_list:
  coming_soon_img_url = coming_soon_download["img_url"]
  coming_soon_img_name = coming_soon_img_name_prefix + str(coming_soon_img_idx) + ".jpg"
  coming_soon_img_path = coming_soon_img_dir + os.sep + coming_soon_img_name
  download_file(
      coming_soon_img_url,
      coming_soon_img_path)
  coming_soon_img_idx += 1
