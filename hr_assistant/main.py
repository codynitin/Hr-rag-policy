
from hr_assistant.pipeline import ask ,building_hr_agent


def main():
    print("building hr aggent")
    agent = building_hr_agent()
    print("ready hr aggent\n")

    questions = [" how many hours i need to work on holiay?",
                 "how many leaves  do i have ?" , 
                 "can i work from home ?"]

    for question in questions:
        print("*"*60)
        print(" this is question", question)
        answer= ask(agent , question)
        print(" this is answer", answer)
        print("-"*60)
        print()

if __name__ =="__main__" :
    main()




