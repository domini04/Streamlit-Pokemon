import streamlit as st

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="./images/pokeball.webp",
)

st.title('streamlit 포켓몬 도감')
st.header('이 앱은 포켓몬 도감을 보여주는 앱입니다.')
st.markdown('**포켓몬**을 도감에 추가해보세요!')
# change color of span to red
st.markdown("""
            <style>
            h1 {
                color: red;
            }
            
            img {
                max-height : 300px;
            }
            .st-expander {
                display: flex;
                justify-content: center;
            }
            
            </style>
            """, unsafe_allow_html=True)

type_dict = {
    '풀': "🍃",
    '물': "💧",
    '불꽃': "🔥",
    '벌레': "🐛",
    '노말': "🐭",
    '전기': "⚡",
    '얼음': "❄️",
    '독': "☠️",
    '비행': "🕊",
    '격투': "🥊",
    '땅': "🏜️",
    '바위': "🪨",
    '에스퍼': "🔮",
    '드래곤': "🐉",
    '고스트': "👻",
    '악': "🦹",
    '강철': "⚙️",
    '페어리': "🧚"
}    

# pokemon = {
#     "name": "피카츄",
#     "types": ["전기"],
#     "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
# }

# col1, col2, col3 = st.columns(3)
# with col1:
#     with st.expander(label=pokemon['name'], expanded=True):
#         st.subheader(f"{pokemon['name']} : {type_dict[pokemon['types'][0]]}")
#         st.image(pokemon['img'], width=200, use_column_width=True)
# with col2:
#     #갸라도스
#     with st.expander(label="갸라도스", expanded=True):
#         st.subheader("갸라도스 : 🐉💧")
#         st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/130.png", width=200, use_column_width=True)
# with col3:
#     #번치코
#     with st.expander(label="번치코", expanded=True):
#         st.subheader("번치코 : 🥊🔥")
#         st.image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/257.png", width=200, use_column_width=True)
        
# #위 코드 반복문으로 변경하기

# #포켓몬 dict 리스트화
# pokemon_list = ["피카츄", "라이츄", "번치코"]
# type_list = [["전기"], ["전기"], ["격투", "불꽃"]]
# pokemon_number = [25, 26, 257]

# cols = st.columns(3)

# for i in range(3):
#     with cols[i]:
#         with st.expander(label=pokemon_list[i], expanded=True):
#             st.subheader(f"{pokemon_list[i]} : {type_dict[type_list[i][0]]} {type_dict[type_list[i][1]] if len(type_list[i]) == 2 else ''}")
#             st.image(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_number[i]}.png", width=200, use_column_width=True)
            
            
#A list containing 9 pokemons. Each pokemon is a dictionary containing the name, types, and image of the pokemon. Use pokemons that are not already used in the previous examples.
initial_pokemons = [
    {
        "name": "파이리",
        "types": ["불꽃"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png"
    },
    {
        "name": "꼬부기",
        "types": ["물"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png"
    },
    {
        "name": "이상해씨",
        "types": ["풀", "독"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png"
    },
    {
        "name": "피죤",
        "types": ["노말", "비행"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/17.png"
    },
    {
        "name": "또가스",
        "types": ["독"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/109.png"
    },
    {
        "name": "픽시",
        "types": ["노말", "페어리"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/35.png"
    },
    {
        "name": "뮤",
        "types": ["에스퍼"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png"
    },
    {
        "name": "뮤츠",
        "types": ["에스퍼"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png"
    },
    {
        "name": "피카츄",
        "types": ["전기"],
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    }
]

#Session state는 일종
if 'pokemons' not in st.session_state:
    st.session_state['pokemons'] = initial_pokemons

#toggle을 사용한 autocomplete 연습
auto_complete = st.toggle("자동으로 채우기", True)
exmaple_pokemon = {
   "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/51.png" 
}


#streamlit form 연습
with st.form(key='my_form'):
    name = st.text_input(label='포켓몬 이름을 입력하세요',
                         value=exmaple_pokemon['name'] if auto_complete else None)
    types = st.multiselect(label='포켓몬 타입을 선택하세요', 
                           options=list(type_dict.keys()),
                           max_selections=2,
                           default=exmaple_pokemon['types'] if auto_complete else None)
    img = st.text_input(label='포켓몬 이미지 URL을 입력하세요',
                        value=exmaple_pokemon['img'] if auto_complete else None)
    submit_button = st.form_submit_button(label='도감에 추가하기')
    if submit_button:
        #입력 체크
        if not name:
            st.error('포켓몬 이름을 입력하세요')
        elif not types:
            st.error('포켓몬 타입을 선택하세요')
        elif not img:
            st.error('포켓몬 이미지 URL을 입력하세요')
        else :    
            st.success('도감에 추가되었습니다!')
            st.session_state['pokemons'].append({
                'name': name,
                'types': types,
                'img': img
            })
    

    
    ##columns 사용법


    # cols = st.columns(3)
    # for i in range(len(pokemons)):
    #     with cols[i % 3]:
    #         pokemon = pokemons[i]
    #         with st.expander(label=pokemon['name'], expanded=True):
    #             st.subheader(f"{pokemon['name']} : {type_dict[pokemon['types'][0]]} {type_dict[pokemon['types'][1]] if len(pokemon['types']) == 2 else ''}")
    #             st.image(pokemon['img'], width=200, use_column_width=True)


    #위 코드와는 다르게 포켓몬 3개씩 묶어서 column을 생성하기에, 화면을 줄이더라도 순서가 꼬이지 않음
for i in range(0, len(st.session_state['pokemons']), 3):
    row_pokemons = st.session_state['pokemons'][i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]   
            with st.expander(label=pokemon['name'], expanded=True):
                st.subheader(f"{pokemon['name']} : {type_dict[pokemon['types'][0]]} {type_dict[pokemon['types'][1]] if len(pokemon['types']) == 2 else ''}")
                st.image(pokemon['img'], width=200, use_column_width=True)
                
                #삭제 버튼 추가
                delete_button = st.button(label='삭제', key=f'delete_{i+j}', use_container_width=True)
                if delete_button:
                    st.session_state['pokemons'].remove(pokemon)
                    st.experimental_rerun()
                
                
                
