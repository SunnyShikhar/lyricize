import argparse
from search import search
from parse_url import get_lyrics

def main(args):

    search_phrase = " ".join(args.input_search)
    a =search(search_phrase,args.output_filename,'n8zBK58YLA-WNRshur8hoNYDv8yabkjKQ7rNDhfK7MCUedV_hliH6aOcgFFq6jO2')
    urls = map(lambda t: t[3], a) #get urls

    f = open('lyrics/' + search_phrase, 'wb')
    lyrics = get_lyrics(urls[0])
    f.write(lyrics.encode("utf8"))
    f.close()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='quick and easy way to pull lyrics from Genius')

    parser.add_argument(
        '-f',
        '--search-query',
        help = 'Artist name or song name for query',
        type = str,
        nargs = '+',
        dest = 'input_search'
    )

    parser.add_argument(
        '-o',
        '--output-file',
        help = 'filename for output file',
        nargs = '?',
        default = 'out.csv',
        dest = 'output_filename'
    )

    args = parser.parse_args()
    main(parser.parse_args())
