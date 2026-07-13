import time

passage="This is a basic typing speed tester I will have the worlds most amazing and\n" \
"this is not even what I would Like to have in the world that is the most important thing oh yeah."
print(passage)

start_time = time.perf_counter()
text=input("Start typing the text above :")
end_time = time.perf_counter()

A=set(passage)
B=set(text)
wrong_letters=A-A.intersection(B)


# 3. Calculate elapsed time
elapsed_time = end_time - start_time

gross_wpm=(len(text)/5)/(elapsed_time/60)

correct_words=len(passage)-len(wrong_letters)

accuracy_percentage = (correct_words/len(passage))*100

wpm=len(wrong_letters)/(elapsed_time/60)

net_wpm=gross_wpm-wpm
print(f"Wrong letters that you got: {wrong_letters}",)
print(f"Gross WPM:{int(gross_wpm)}")
print(f"Accuracy percentage:{int(accuracy_percentage)}%")
print(f"Net WPM:{int(gross_wpm)}")

