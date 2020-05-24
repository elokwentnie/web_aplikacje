# answer options
age_options = {1: '<18', 2: '18-25', 3: '25-40', 4: '>40'}
home_options = {1: "Wieś", 2: "Miasto (do 50 tys.)", 3: "Miasto (50 - 500 tys.)", 4: "Miasto (+ 500 tys."}
gender_options = {1: "Mężczyzna", 2: "Kobieta", 3: "Nie chcę podawać"}
education_options = {1: "Podstawowe", 2: "Zawodowe", 3: "Średnie", 4: "Wyższe", 5: "Inne"}
view_options = {1: ">1/dzień", 2: "1/dzień", 3: "<1/dzień", 4: "Nigdy"}
badfeeling_options = {1: "Ryzyko zachorowania", 2: "Kryzys gospodarczy", 3: "Zmiany w relacjach społecznych",
                      4: "Brak niepokoju"}
corona_options = {1: "Znam", 2: "Nie znam", 3: "Nie wiem"}
# sentiment dict
sentiments_dict = [{"Positive": [2], "Negative": [1]}, {"Positive": [1], "Negative": [2]},
                   {"Positive": [1], "Negative": [2]}, {"Positive": [2], "Negative": [3]},
                   {"Positive": [3], "Negative": [2]}, {"Positive": [1, 2], "Negative": [3]},
                   {"Positive": [2], "Negative": [1]}]
