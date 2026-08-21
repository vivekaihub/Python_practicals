print("===== TEXT MODERATION FILTER =====")

feedback = input("Enter your feedback: ")

target_words = ["badword", "stupid", "hate"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print("\n----- MODERATED FEEDBACK -----")
print(feedback)