def review():
    print("Please add your review")
    rev_user=input("Enter your review: ") #storing the review from the user
    if len(rev_user.strip())>5:
        print("\nReview added successfully.")
        print(f">>>{rev_user.strip()}")
        print("Thank You for your valuable feedback.")
    else:
        print("Review was too short. No feedback submitted")