import requests
from random_word import RandomWords
import json

presentation_count = 0
score_count = 0
TOTAL_PRESENTATION_COUNT = 5
headers = {
    'x-rapidapi-host': "<RAPIDAPI_HOST>",
    'x-rapidapi-key': "<RAPIDAPI_KEY>"
}


def fetch_synonyms(word):
    url = "https://wordsapiv1.p.rapidapi.com/words/" + word + "/synonyms"
    api_response = requests.request("GET", url, headers=headers)
    return json.loads(api_response.text)


if __name__ == "__main__":
    print("WELCOME TO SYNONYM WORD GAME \n")
    print("||||| LET'S PLAY ||||| \n")
    r = RandomWords()
    while presentation_count < TOTAL_PRESENTATION_COUNT:
        words = [r.get_random_word() for _ in range(15)]
        for word in words:
            response = fetch_synonyms(word)
            if word in response:

                if len(response["synonyms"]) > 0:
                    presentation_count = presentation_count + 1

                    print("Enter a synonym for the word: " + word)
                    answer = input()
                    match_found = False
                    for matcheval in response["synonyms"]:
                        if matcheval == answer:
                            match_found = True
                            score_count = score_count + 1
                            break
                    if match_found:
                        print("Hurray !!! You Are Right n")
                    else:
                        print("Bad luck, That's A Wrong Answer n")
                    print("Your Current Score : " + str(score_count) + "n")
                    if presentation_count == TOTAL_PRESENTATION_COUNT:
                        break
                    else:
                        print(str(TOTAL_PRESENTATION_COUNT - presentation_count) + " More To Go n")
    print("||||| GAME OVER ||||| n")
    if score_count == TOTAL_PRESENTATION_COUNT:
        print("Voila!! You got all synonyms correct. n")
    print("Your Final Score: " + str(score_count) + " out of " + str(presentation_count))