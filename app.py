import re
import streamlit as st
from words import word_list


def clean(old: str):
    return old[1:-1]


def check_apperance_times(string: str, times: dict):
    for i in times:
        count = string.lower().count(i)
        if count > times[i]:
            return False
    return True


def search_words(pattern: str, wildcard: str) -> list:
    pattern = pattern.lower().strip()
    wildcard = wildcard.lower().strip()
    if wildcard != "":
        new_pattern = pattern.replace('?', f'[{wildcard}]')
    else:
        new_pattern = pattern.replace('?', '\w')
    new_pattern = ',' + new_pattern + ','
    pt = re.compile(new_pattern, re.IGNORECASE)

    result = pt.findall(word_list)
    result = list(map(clean, result))
    if wildcard is not None and len(wildcard) > 0:
        letter_times = dict()
        for i in wildcard:
            letter_times[i] = wildcard.count(i)
        filtered_result = [i for i in result if check_apperance_times(i, letter_times)]
        return filtered_result

    return result


st.set_page_config(page_title="Words")

pattern = st.text_input(label='Input the pattern, ? for unkowns letters. Example: a?b??c')
wildcard = st.text_input(label='Input the possible letters for ?. Blank means any letters could be used.')

if st.button(label='Search'):
    result = search_words(pattern, wildcard)
    st.table(result)

