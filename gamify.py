import os
import fnmatch
import re

from collections import defaultdict


class BookSolutionStatistics:
    def __init__(self, dir_book):
        self.dir_book     = dir_book
        self.authors      = self.find_authors()
        self.books        = self.get_current_books()
        self.distribution = self.solution_statistics()

    def find_authors(self):
        authors = set()
        pattern = re.compile(r'ex\d+\.(\w+)\.tex$')

        for dirpath, dirnames, filenames in os.walk(self.dir_book):
            for filename in filenames:
                result = pattern.match(filename)
                if result:
                    authors.add(result.group(1))
        return sorted(list(authors))

    def get_current_books(self):
        return [name for name in os.listdir(self.dir_book) 
                        if os.path.isdir(os.path.join(self.dir_book, name))]

    def find_solution_files(self, file_pattern):
        result_files = []
        for root, dirs, files in os.walk(self.dir_book):
            for name in files:
                if fnmatch.fnmatch(name, file_pattern):
                    result_files.append(os.path.join(root, name))
        return result_files

    def solution_statistics(self):
        result_files = self.find_solution_files('ex*.tex')
        distribution = defaultdict(lambda: defaultdict(int))

        for file in result_files:
            book   = file.split('/')[1]
            author = file.split('/')[-1].split('.')[1]
            distribution[author][book] += 1
        return distribution

    def __str__(self):
        wm, wn, wl = 7, 9, 5

        output = ""
        header = f'{" ":<{wm}}|'
        for book in self.books:
            header += f'{book:<{wn}}|'
        header += f'{"Total":<{wl}}|'
        output += header + "\n"

        separator_line = '-' * wm + '+' + ('-' * wn + '+') * len(self.books) + '-' * wl + '+'
        output += separator_line + "\n"

        for author in self.authors:
            row   = f'{author:>{wm}}|'
            total = 0
            for book in self.books:
                outcome = self.distribution[author][book]
                total  += outcome
                row    += f'{outcome:>{wn}}|'
            row    += f'{total:>{wl}}|'
            output += row + "\n"
        return output[:-1] if output[-1] == '\n' else output


if __name__ == "__main__":
    dir_book = "Books"
    print(BookSolutionStatistics(dir_book))
