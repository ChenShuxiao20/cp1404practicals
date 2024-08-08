import wikipedia

while True:
    search = input("Enter a page title: ")
    if not search:
        print("Thank you.")
        break

    try:
        page = wikipedia.page(search)
        print("Title:", page.title)
        print("Summary:", page.summary, "...")
        print(page.url)
    except wikipedia.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        options = e.options
        for i, option in enumerate(options,1):
            print(f"{i}. {option}")
        print()
    except wikipedia.PageError:
        print(f'Page id "{search}" does not match any pages. Try another id!')
        print()