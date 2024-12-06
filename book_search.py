def main():
    title_list = [['Windtalker','Jones'],['Godfather','Smith'],['Winds of war','Brown']]
    on = True
    while on == True:
        found = False
        search_term = input("Enter the title of book to search: ")
        for x in title_list:
            if search_term.lower() == x[0].lower():
                found = True
                print(f"The author of '{x[0]}' is {x[1]}.")
        if found == False:
            print(f"Title '{search_term.title()}' not found in the list.")
        choice = input("Continue y/n: ")
        if choice == 'n':
            on = False
main()
