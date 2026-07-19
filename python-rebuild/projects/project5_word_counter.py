# Project 5: Word Counter
# Author: Gül İfdal ALDEMİR
# Date: 19 July 2026

print()
print("Welcome to the Word Counter! ")

#Kullanıcıdan bir metin alıyoruz
text = input("Enter a sentence: ")

#Metni kelimelere ayırıyoruz
words = text.split()

#Kelime ve karakter sayılarını hesaplıyoruz
word_count = len(words)
character_count = len(text)

#En uzun kelimeyi buluyoruz
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Kelimelerdeki toplam harf sayısını hesaplıyoruz
total_letters = 0

for word in words:
    total_letters += len(word)

# Ortalama kelime uzunluğunu hesaplıyoruz
average_length = total_letters / word_count



print()
print("================================ RESULT ===========================================")
print(f"Words        : {word_count}")
print(f"Characters   : {character_count}")
print(f"Longest Word : {longest_word}")
print(f"Average Word Length : {average_length:2f}")





