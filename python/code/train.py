def get_people_scores(name="",**score):

    if name != "" and len(score.items()) != 0:
        print(f"hello {name} this is your score table: ")
        for  k,v in score.items():
            print(f"{k} => {v}")

    elif name!="" and len(score.items()) == 0:
        print(f"hello {name} you have no scores to show")

    else:
        for  k,v in score.items():
            print(f"{k} => {v}")

get_people_scores()