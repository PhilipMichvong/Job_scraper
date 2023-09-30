# -*- coding: windows-1250 -*-
import requests
from bs4 import BeautifulSoup
from data import TEST_LINK
import os
import signal
from handler import handler
import pyshorteners
PAGE_LINK = ""


class JobScraper:
    def __init__(self) -> None:
        self.page_link = ""
        self.job_offerts_links = []

    def get_source_code(self, source_page_link: str) -> BeautifulSoup:
        """ function that get the source code from website using requests """
        self.page_link = source_page_link
        response = requests.get(source_page_link)

        if response.status_code != 200:
            print("Website is not responding")
            return None

        return BeautifulSoup(response.text, "html.parser")

    def get_job_offert_links(self):
        """ Looping over popular job searching pages to find job offers """
        if "pracuj.pl" in self.page_link:
            listings = self.get_source_code(TEST_LINK).find_all(
                'div', class_="listing_c1dc6in8")

            href_links = set()

            for listing in listings:
                links = listing.find_all('a')
                for link in links:
                    href_value = link.get('href')
                    if "pracodawcy" not in href_value:
                        href_links.add(href_value)

            self.job_offerts_links = list(href_links)

    def create_job_dict(ad_title, location, salary, working_time, workplace, position, offer_link) -> dict:

        job_dict = {
            "ad title": ad_title,
            "location": location,
            "salary": salary,
            "amount of working time": working_time,
            "workplace": workplace,
            "position": position,
            "link to offer": offer_link
        }
        return job_dict

    def is_pracuj_pl(self):
        return 'pracuj.pl' in self.page_link

    def extract_salary(self, salary_element):
        if salary_element:

            source = self.get_source_code(self.page_link)

            salary_from = source.find(
                'span', class_='offer-viewZGJhIB').text

            salary_to = source.find('span', class_='offer-viewYo2KTr').text

            salary_from = ''.join(filter(str.isdigit, salary_from))

            salary_to = ''.join(filter(str.isdigit, salary_to))

            salary = f"{salary_from} - {salary_to} (PLN)"

            return salary

        return "Salary not included in offer".center(70)

    def extract_working_time(self, source):
        working_time_element = source.find(
            attrs={'data-test': 'sections-benefit-work-schedule-text'})
        return working_time_element.text if working_time_element else "NOT FOUND".center(70)

    def extract_ad_title(self, source):

        if self.is_pracuj_pl():
            return source.find('h1', class_="offer-viewkHIhn3").text if source else 'TITLE NOt INCLUDED'.center(70)

    def extract_location(self, source):

        if self.is_pracuj_pl():

            location = source.find(
                'a', class_="offer-viewnqE8MW") or source.find('p', class_="offer-viewAV75Zu")
            return location.text if location else 'NOT FOUND'

    def extract_workplace(self, source):

        if self.is_pracuj_pl():
            workplace = source.find(
                attrs={'data-test': 'sections-benefit-work-modes-text'})
            return workplace.text if workplace else 'NOT FOUND'.center(70)

    def extract_position(self, source):

        if self.is_pracuj_pl():
            position = source.find(
                attrs={'data-test': 'sections-benefit-employment-type-name-text'})
            return position.text if position else 'NOT FOUND'.center(70)

    def process_job_offert(self, offert):

        source = self.get_source_code(offert)

        ad_title = self.extract_ad_title(source)

        location_element = self.extract_location(source)

        salary_element = source.find('span', class_='offer-viewZGJhIB')

        salary = self.extract_salary(salary_element)

        working_time = self.extract_working_time(source)

        workplace = self.extract_workplace(source)

        place = self.extract_position(source)

        print((f"Offer title: {ad_title}\n").center(70))

        print((f"Location: {location_element} " + '\n').center(70))

        print(salary.center(70) + '\n')

        print(working_time.center(70) + '\n')

        print(workplace.center(70) + '\n')

        print(place.center(70) + '\n')


def main():

    signal.signal(signal.SIGINT, handler)
    job_scraper = JobScraper()
    job_scraper.get_source_code(TEST_LINK)
    job_scraper.get_job_offert_links()

    num_of_offerts = len(job_scraper.job_offerts_links)
    print("\n")

    for i, offert in enumerate(job_scraper.job_offerts_links):

        print(f"Offer number: {i+1} / {num_of_offerts}".center(70, "-"))
        print("\n")

        job_scraper.process_job_offert(offert)

        type_tiny = pyshorteners.Shortener()
        shorter_link = type_tiny.tinyurl.short(offert)

        print((f"offert link: {shorter_link}\n").center(70))

        input()
        os.system('cls')


if __name__ == "__main__":
    main()
