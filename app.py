import re
import streamlit as st
from words import word_list


def clean(old: str):
    return old[1:-1]


def check_apperance_times(string: str, times: dict):
    for i in times:
        count = string.count(i)
        if count > times[i]:
            return False
    return True


def search_words(pattern: str, wildcard: str) -> list:
    if wildcard is not None and len(wildcard) > 0:
        new_pattern = pattern.replace('?', f'[{wildcard}]')
    else:
        new_pattern = pattern.replace('?', '\w')
    new_pattern = ',' + new_pattern + ','
    pt = re.compile(new_pattern)

    result = pt.findall(word_list)
    result = list(map(clean, result))

    if wildcard is not None and len(wildcard) > 0:
        letter_times = dict()
        for i in wildcard:
            letter_times[i] = wildcard.count(i)
        filtered_result = [i for i in result if check_apperance_times(i, letter_times)]
    print(filtered_result)
    return(filtered_result)


st.set_page_config(page_title="Words")

pattern = st.text_input(label='Input the pattern, using ? for unkowns letters')
wildcard = st.text_input(label='Input the wildcard')

if st.button(label='Search'):
    result = search_words(pattern, wildcard)
    st.dataframe(result)

