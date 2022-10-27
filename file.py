MyTuple = ('css' , 'php' , 'js')
MyDict = { 
    'python': "90%",
    'c': "80%",
    'sql': "85%"
}

def show_details(name ,*skills , **skillswithprogress):
    print(f"hello {name} \nUr skills without progress:- ")
    
    for skill in skills:
        print(f" > {skill} ")

    print(f"Ur skills with progress:-") 

    for keyskill,valueskill in  skillswithprogress.items() :
        print(f"-{keyskill} => {valueskill} ")
show_details( "Ahmed" ,*MyTuple , **MyDict)



