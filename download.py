import urllib.request


def download_file(url, dst_path):
  print("download_url:", url)
  print("download_dst_path:", dst_path)
  with urllib.request.urlopen(url) as web_file:
    data = web_file.read()
    with open(dst_path, mode="wb") as local_file:
      local_file.write(data)
