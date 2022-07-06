# Variables
book = []
chapters = []
standard_work = []
highest_number_of_chapters = 0
highest_chapters_book = ""
input_book_list = []
input_chapter_list = []

# Read File
with open("books_and_chapters.txt") as file:
    for line in file:
        book_and_chapter = line.strip()
        parts = book_and_chapter.split(":")
        standard_work.append(parts[2])
        chapters.append(parts[1])
        book.append(parts[0])
file.close()

# Find highest number of chapters

# for i in range(len(chapters)):
#     if int(chapters[i]) > highest_number_of_chapters:
#         highest_number_of_chapters = int(chapters[i])
#         highest_chapters_book = book[i]

# print(
#     f"The highest number of chapters is {highest_number_of_chapters} in {highest_chapters_book}"
# )

### Stretch ###
swInput = input("Enter a standard work: ")


for i in range(len(standard_work)):
    if standard_work[i] == swInput:
        input_book_list.append(book[i])
        input_chapter_list.append(chapters[i])
    else:
        pass
# Find highest number of chapters in input_book_list

for i in range(len(input_chapter_list)):
    if int(input_chapter_list[i]) > highest_number_of_chapters:
        highest_number_of_chapters = int(input_chapter_list[i])
        highest_chapters_book = input_book_list[i]

print(
    f"The highest number of chapters is {highest_number_of_chapters} in {highest_chapters_book}"
)
