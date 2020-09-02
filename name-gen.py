import sys
import random
import yaml


def H(n: int) -> float:
    if n == 1:
        return 1
    else:
        return H(n-1) + (1/n)


def generate_probabilities(number_of_terms: int) -> list:
    probabilities = []

    P = H(number_of_terms)
    probabilities.append(1/P)

    for i in range(2, number_of_terms+1):
        probabilities.append(1/(i*P))

    return probabilities


def generate_cdf(probabilities: list) -> list:
    cdf = []

    for i in range(len(probabilities)):
        sublist = probabilities[0:i+1]
        new_cdf_entry = sum(sublist)
        cdf.append(new_cdf_entry)

    return cdf


def get_zipfian_index(input_list: list) -> int:
    length_of_input_list = len(input_list)

    probs = generate_probabilities(length_of_input_list)
    cdf = generate_cdf(probs)

    x = random.random()
    cdf_candidates = [upper_bound for upper_bound in cdf if upper_bound > x]
    x_upper_bound = min(cdf_candidates)

    final_result_index = cdf.index(x_upper_bound)
    return final_result_index


def zipfer(input_list: list) -> any:
    random_index = get_zipfian_index(input_list)
    return input_list[random_index]


selected_lang = sys.argv[1]
number_of_names = int(sys.argv[2])

with open(f"lang/{selected_lang}.yaml", "r", encoding="utf-8") as file:
    lang_specs = yaml.safe_load(file)
    file.close

name_shapes = lang_specs["name_shapes"]
syllable_structures = lang_specs["syllable_structures"]
separator = lang_specs["separator"]

cats = {
    k: lang_specs[k]
    for k in lang_specs.keys()
    if k not in ['syllable_structures', 'separator']
}

generated_names = []
for _ in range(number_of_names):
    new_name = ""
    shape = int(zipfer(name_shapes))
    for syl in range(shape):
        new_syllable = ""
        current_syllable_structure = zipfer(syllable_structures)
        for pcat in current_syllable_structure:
            current_cat = cats[pcat]
            new_phoneme = zipfer(current_cat)
            new_syllable += new_phoneme
        new_syllable += (separator if syl+1 < shape else "")
        new_name += new_syllable
    print(new_name)