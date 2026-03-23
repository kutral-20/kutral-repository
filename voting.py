class invalidageexception(exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self,message)
    def validate_vote_age(age):
        if age<18:
            raise invalidageexception ("Age is below 18,not eligibleto vote")
        else:
            print("you are eligible to vote")
try:
    age=int(input("Enter your age :"))
    validate_voter_age(age)
except invalidageexception as e:
    print(f"Error:{e}")
except valueerror:
    print("Invalid input! please a enter integer for age")
