from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_py import binary_path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(url):

    date_to_find = '2024-01-19 10:25'.strip()
    file_size = '3.8M'
    # it would pick the first one
    #86624099999.csv	2024-01-19 10:25	3.8M	 
    #86818099999.csv	2024-01-19 10:25	3.8M
    
    svc = Service(executable_path=binary_path)
    driver = webdriver.Chrome(service=svc)

    driver.get(url)
    assert "climatological" in driver.title, "Not the climatological website"

    e = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, 
            f"//td[contains(normalize-space(), '{date_to_find}')]/following-sibling::td[contains(normalize-space(), '{file_size}')]"
            ))
    )
    file_name = e.find_element(By.XPATH, "preceding-sibling::*[2]/a").text
    driver.close()
    print("File name: ", file_name)
    
    url_of_file_to_download = url + file_name
    print("URL to download the file: ", url_of_file_to_download)
    return url_of_file_to_download, file_name



# if __name__ == "__main__":
#     main()
