from urllib import quote
from urllib import urlopen
import argparse
import json

def getWikipedia(term):
    page_title = None
    revisions = None
    ns = None
    page_id = None
    text = None
    term = quote(term)
    url = "https://en.wikipedia.org/w/api.php?action=query&titles="+term+"&prop=revisions&rvprop=content&format=json"
    try:
        response = urlopen(url)
        res = json.load(response)
        if "query" in res.keys():
            if "pages" in res["query"].keys():
                ids = res["query"]["pages"].keys()
                page_title = res["query"]["pages"][ids[0]].keys()
                revisions = res["query"]["pages"][ids[0]]["revisions"]
                page_id = res["query"]["pages"][ids[0]]["pageid"]
                ns = res["query"]["pages"][ids[0]]["ns"]
                l = res["query"]["pages"].keys()
                info = res["query"]["pages"][l[0]]["revisions"][0]
                text = info["*"]

    except IOError:
        print "Error: check network connectivity"
    except ValueError:
        print "Error: Unfamiliar result"
    print "__________________________________"
    print page_id, page_title
    print text

def main():
    parser = argparse.ArgumentParser(description="Query")
    parser.add_argument("query")
    args = parser.parse_args()
    getWikipedia(args.query)

if __name__ == "__main__":
    main()
