import requests
import validators
import os, shutil
from glob import glob
import concurrent.futures


def fetch_file(url, file_path):
    if validators.url(url):
        r = requests.get(url)
        if r.status_code == 200:
            if glob(file_path):
                print('WARNING: File already exists')
            else:
                with open(file_path, 'wb') as w:
                    w.write(r.content)
            return True
        else:
            return False
    else:
        False


def get_local_file_path(url, path_downloads):
    file_name = url.split('/')[-1] 
    file_path = os.path.join(path_downloads, file_name)
    return file_path


def download_file(URL, path_downloads, workers):
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_url = {executor.submit(fetch_file, URL, get_local_file_path(URL,path_downloads)): (URL, get_local_file_path(URL,path_downloads))}
        for future in concurrent.futures.as_completed(future_to_url):
            url, file_path = future_to_url[future]
            print("Downloading file from: ", url)
            try:
                result = future.result()
                if result:
                    print("File downloaded successfully and saved to:", path_downloads)
                else:
                    print("FAILED to download file from: ", url)
            except Exception as exc:
                print(f"FAILED to download file from {url}: {exc}")



def main(url, path_downloads):
    workers = 5

    if not os.path.exists(path_downloads):
        os.mkdir(path_downloads)
    
    download_file(url, path_downloads, workers)
      

# if __name__ == "__main__":
#     start_time = time.time()
#     main()
#     print("--- {} seconds ---".format(time.time() - start_time))
