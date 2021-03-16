import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    pass


class TextComparer():
    def __init__(self, url_list=[]):
        self.url_list = url_list
        
    def download(self, url, filename):
        self.filenames = []
        response = requests.get(url)
        
        if response.ok:
            with open(filename, 'wb') as file_object:
                self.filenames.append(filename)
                for chunk in response.iter_content(chunk_size=1024):
                    file_object.write(chunk)

                
        elif response.status_code == 404:
            raise NotFoundException('Status code 404')
            

    
    

    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        index = self.n
        if index != len(self.filenames):
            self.n += 1
            return self.filenames[index]
        else:
            raise StopIteration
            
    def url_list_generator(self):
        for url in self.url_list:
            yield url
            
    
    def avg_vowels(self, book):
        vowel_list = ['A', 'E', 'I', 'O', 'U', 'Y']
        
        with open(book) as file:
            read_file = file.read()
        
        number_of_words = read_file.split()
        number_of_words_count = len(number_of_words)
        amount_of_vowels = 0
        
        for word in number_of_words:
            for char in word:
                if char.upper() in vowel_list:
                    amount_of_vowels += 1
        average_vowels = round(amount_of_vowels / number_of_words_count, 2)
        return average_vowels, book
    

    
    
    
    
    
            