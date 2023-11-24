import requests

RESOURCE = r"http://192.168.1.12:5000/api/v2/resources/books"

def get_resource(url):

    response = requests.get(RESOURCE + url)

    return response

def get_resource_json(url):

    return get_resource(url).json()

def get_resource_text(url):

    return get_resource(url).text

def print_resource_json(url):

    res = get_resource_json(url)

    print(*[x for x in res], sep="\n")

def add_book(author, title, first_sentence, published):

    requests.post(RESOURCE, json={"author":author,"title":title,"first_sentence":first_sentence,"published":published})

def print_resource_text(url):

    print(get_resource_text(url))

if __name__ == "__main__":

    data = get_resource_json(r"/all")
    print(*sorted({x["author"] for x in data}), sep="\n")

    #add_book(
    #    author="Robert Jordan",
    #    title="The Eye of the World",
    #    first_sentence="The palace still shook occasionally as the earth rumbled in memory, groaning as if it would deny what had happened.",
    #    published="1990")
    
