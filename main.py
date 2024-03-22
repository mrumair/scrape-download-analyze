import scrape_filename
import download_file
import analyze_file


def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    file_download_path = 'downloads'

    url_of_file_to_download, file_name = scrape_filename.main(url)

    download_file.main(url_of_file_to_download, file_download_path)

    analyze_file.main(f"{file_download_path}/{file_name}")


if __name__ == "__main__":
    main()
