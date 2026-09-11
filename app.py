import streamlit as st
import pandas as pd
import numpy as np
import random
import time 
import matplotlib.pyplot as plt
st.set_page_config("📽️Stardust")#change the app name froome streamlit to the desired name and it should be wrtten as the first function in the code

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home","🎬 Movies","📺 TV Shows","📊 Insights","🎮STARDUST Arcade","💫 Movie Match"]
)
st.sidebar.divider()
st.sidebar.subheader("👩‍💻 Developed by")
st.sidebar.write("Jasmeet Kaur")

if page == "🏠 Home": 
    df = pd.read_csv('netflix.csv')
    st.title("📽️STAR DUST")#adds the title of the app
    st.caption("Where every story finds its audience.")#write the caption under the title we can also use write() but to make it elegant we use caption()
    st.info("✨ Welcome to STARDUST! Explore trending movies, TV shows, and discover hidden gems.")
    
    st.container()
    st.subheader("✨ Vibe Check")
    st.caption("What's today's mood? We'll find the perfect watch.")
    
    movie_posters = [ 
        "dickjohnson.jpg",
         "mylittlepony.jpg",
         "sankofa.jpg",
         "thestarling.jpg",
         "jesuis.jpg",
         "confessions.jpg",
         "europe.jpg",
         "intrusion.jpg",
         "avvai.jpg",
         "gogo.jpg",
         "jeans.jpg",
         "minsara.jpg",
         "grown.jpg",
         "dark.jpg",
         "paranoia.jpg",
         "ankahi.jpg",
         "father.jpg",
         "stronghold.jpg",
         "birthofdragon.jpg",
         "jaws.jpg"
         ]
    movie_trailers = [
    "https://www.youtube.com/watch?v=wfTmT6C5DnM&pp=ygUUZGljayBqb2huc29uIGlzIGRlYWQ%3D",
    "https://www.youtube.com/watch?v=Pa_PRDVpjSk&pp=ygUhbXkgbGl0dGxlIHBvbnkgOiBhIG5ldyBnZW5lcmF0aW9u",
    "https://www.youtube.com/watch?v=jUWLAXHj2SU&pp=ygUHc2Fua29mYQ%3D%3D",
    "https://www.youtube.com/watch?v=fYyImx_KXm4&pp=ygUMdGhlIHN0YXJsaW5n",
    "https://www.youtube.com/watch?v=oFQel_8SZ6M&pp=ygUMamUgc3VpcyBrYXJs",
    "https://www.youtube.com/watch?v=uGJBHueplss&pp=ygUgQ29uZmVzc2lvbnMgb2YgYW4gSW52aXNpYmxlIEdpcmw%3D",
    "https://www.youtube.com/watch?v=DObP6W8b6ck&pp=ygUzRXVyb3BlJ3MgTW9zdCBEYW5nZXJvdXMgTWFuOiBPdHRvIFNrb3J6ZW55IGluIFNwYWlu",
    "https://www.youtube.com/watch?v=tAJVDe205tY&pp=ygUJSW50cnVzaW9u",
    "https://www.youtube.com/watch?v=LioSgVXzFdI&pp=ygUXQXZ2YWkgU2hhbm11Z2hpIHRyYWlsYXI%3D",
    "https://www.youtube.com/watch?v=cjWqbzSoYuA&pp=ygU0R28hIEdvISBDb3J5IENhcnNvbjogQ2hyaXNzeSBUYWtlcyB0aGUgV2hlZWwgdHJhaWxhcg%3D%3D",
    "https://www.youtube.com/watch?v=g6mmqzbjNXQ&pp=ygUWSmVhbnMgb2ZmaWNpbGEgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=UrCs31xkz2A&pp=ygUeTWluc2FyYSBLYW5hdnVvZmZpY2lsYSB0cmFpbGVy",
    "https://www.youtube.com/watch?v=wzImCSfTlgY&pp=ygUSCUdyb3duIFVwcyB0cmFpbGVy0gcJCUwLAYcqIYzv",
    "https://www.youtube.com/watch?v=K8iLp1xQtPQ&pp=ygUSZGFyayBza2llcyB0cmFpbGVy0gcJCUwLAYcqIYzv",
    "https://www.youtube.com/watch?v=2T1RLye5Z_w&pp=ygUQcGFyYW5vaWEgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=pw1WuzTYM3Q&pp=ygUXQW5rYWhpIEthaGFuaXlhIHRyYWlsZXLSBwkJTgsBhyohjO8%3D",
    "https://www.youtube.com/watch?v=VX2b52unYdw&pp=ygUnCVRoZSBGYXRoZXIgV2hvIE1vdmVzIE1vdW50YWlucyB0cmFpbGVy",
    "https://www.youtube.com/watch?v=2jp3YYw8hT4&pp=ygUWVGhlIFN0cm9uZ2hvbGQgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=soLlxteBbNA&pp=ygUbQmlydGggb2YgdGhlIERyYWdvbiB0cmFpbGVy",
    "https://www.youtube.com/watch?v=U1fu_sA7XhE&pp=ygUMamF3cyB0cmFpbGVy"
    ]
    tv_posters = [
    "blood&water.jpg",
    "gangland.jpg",
    "jailbirds.jpg",
    "kotafactory.jpg",
    "midnightmass.jpg",
    "thegreatbritishbakingshow.jpg",
    "vendetta.jpg",
    "bangkok.jpg",
    "crimestories.jpg",
    "dearwhitepeople.jpg",
    "false.jpg",
    "monster.jpg",
    "resurrection.jpg",
    "love.jpg",
    "chicago.jpg",
    "squid.jpg",
    "tayo.jpg",
    "angry.jpg",
    "heman.jpg",
    "smart.jpg"
     ]
    tvshows_trailers = [
    "https://www.youtube.com/watch?v=2m0Cm2kMOBU&pp=ygUVYmxvb2QgJiB3YXRlciB0cmFpbGVy",
    "https://www.youtube.com/watch?v=0VZ2Nbx8gHI&pp=ygURR2FuZ2xhbmRzIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=G6vrmPQ50qs&pp=ygUeSmFpbGJpcmRzIE5ldyBPcmxlYW5zICB0cmFpbGVy",
    "https://www.youtube.com/watch?v=pNZQ6msbOvM&pp=ygUVS290YSBGYWN0b3J5ICB0cmFpbGVy",
    "https://www.youtube.com/watch?v=89UV8vmWXlY&pp=ygUWTWlkbmlnaHQgTWFzcyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=BnOZ9BNUTtk&pp=ygUmVGhlIEdyZWF0IEJyaXRpc2ggQmFraW5nIFNob3cgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=78qOHrILufk&pp=ygUsVmVuZGV0dGE6IFRydXRoLCBMaWVzIGFuZCBUaGUgTWFmaWEgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=JAfHOxm2Xhs&pp=ygUZQmFuZ2tvayBCcmVha2luZyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=ErB-Fm77gso&pp=ygUoQ3JpbWUgU3RvcmllczogSW5kaWEgRGV0ZWN0aXZlcyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=JMgWMzbM2Pk&pp=ygUaRGVhciBXaGl0ZSBQZW9wbGUgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=AugXC36Xml8&pp=ygUfZmFsc2EgaWRlbnRpZGFkIG9yZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=gUjtViCsb8E&pp=ygU_TW9uc3RlcnMgSW5zaWRlOiBUaGUgMjQgRmFjZXMgb2YgQmlsbHkgTWlsbGlnYW4gb3JnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=FfdXu9jZFKs&pp=ygUmUmVzdXJyZWN0aW9uOiBFcnR1Z3J1bCBvcmdpbmFsIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=kX-QbcXyZug&pp=ygUkTG92ZSBvbiB0aGUgU3BlY3RydW0gb3JnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=o90l2auMiUs&pp=ygUiQ2hpY2FnbyBQYXJ0eSBBdW50IG9yZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=oqxAJKy0ii4&pp=ygUbU3F1aWQgR2FtZSBvcmlnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=fS38dyRA0kE&pp=ygUoVGF5byBhbmQgTGl0dGxlIFdpemFyZHMgb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=QRmKa7vvct4&pp=ygUcQW5ncnkgQmlyZHMgb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=ZmEx7wQI6RY&pp=ygU3SGUtTWFuIGFuZCB0aGUgTWFzdGVycyBvZiB0aGUgVW5pdmVyc2Ugb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=No6052an_Zw&pp=ygUxSGUtTWFuIGFuZCBUaGUgU21hcnQgTW9uZXkgV29tYW4gb3JpZ2luYWwgdHJhaWxlctIHCQlOCwGHKiGM7w%3D%3D"
     ]
    
    col1, col2 = st.columns(2)
    with col1:
        chill = st.button("😌 Chill")
        laugh = st.button("😂 Need a Laugh")
    with col2:
        emotional = st.button("😭 In My Feelings")
        thriller = st.button("😱 Plot Twists Please")
    search = st.text_input( "", placeholder="What story are you looking for tonight?")
    if search:
        result=df[df['title'].str.contains(search , case = False , na = False)]
        st.dataframe(result)
    if chill:
        st.success("😌 Time to relax!")
        result = df[df["listed_in"].str.contains("Documentaries|Children|Family", case=False, na=False)]
    elif laugh:
        st.success("😂 Here's something to make you laugh!")
        result = df[df["listed_in"].str.contains("Comedies", case=False, na=False)]
    elif emotional:
        st.success("😭 Grab some tissues...")
        result = df[df["listed_in"].str.contains("Drama|Romantic", case=False, na=False)]
    elif thriller:
        st.success("😱 Plot twists incoming!")
        result = df[df["listed_in"].str.contains("Thrillers|Crime", case=False, na=False)]
    if chill or laugh or emotional or thriller:
            recommendations = result.head(5)
            for i in range(len(recommendations)):
                st.subheader(recommendations.iloc[i]["title"])
                st.write("⭐", recommendations.iloc[i]["rating"])
                st.write("🎭", recommendations.iloc[i]["listed_in"])
                st.write("📅", recommendations.iloc[i]["release_year"])
                st.divider()
    st.divider()
    with st.container():
        st.header("Featured this week")
        st.info("🍿 Discover trending movies and TV shows selected just for you!")
        col1,col2 = st.columns(2)
    with col1:
        st.button("Watch Trailer🎬")
    with col2:
        st.link_button("🌐 Explore Netflix","https://www.netflix.com")

    st.success("🎬 Echoes of the Moment")
    st.caption("Top 10 movies of the week")
    movies_df = df[df['type'] == 'Movie']
    
    cols  = st.columns(5)
    for i in  range(5):
        with cols[i]:
            st.image("D:/PROJECT/assests/Posters/"+ movie_posters[i], width=210)
            st.link_button(
               "▶ Watch Trailer",
                 movie_trailers[i]
             )
            st.markdown(
             f"""**{movies_df.iloc[i]["title"]}**
             ⭐ {movies_df.iloc[i]["rating"]}
              🕒 {movies_df.iloc[i]["duration"]}
             """
             )
    st.divider()
    movie = df[df["type"]=="Movie"].shape[0]
    tv = df[df["type"]=="TV Show"].shape[0]
    country = df["country"].nunique()
    rating = df["rating"].nunique()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric("🎬 Movies",movie)
    with col2:
        st.metric("📺 TV Shows",tv)
    with col3:
        st.metric("🌍 Countries",country)
    with col4:
        st.metric("⭐ Ratings",rating)
    
    st.subheader("🎬 Echoes of the Moment")
    st.caption("Top 10 TV shows of the week")
    tv_shows_df = df[df['type'] == 'TV Show']
    
    cols  = st.columns(5)
    for i in  range(5):
         with cols[i]:
             st.image("D:/PROJECT/assests/Posters/"+ tv_posters[i], width=210)
             st.link_button(
             "▶ Watch Trailer",
              tvshows_trailers[i]
             )
             st.markdown(
        f"""**{tv_shows_df.iloc[i]["title"]}**
        ⭐ {tv_shows_df.iloc[i]["rating"]}
        🕒 {tv_shows_df.iloc[i]["duration"]}
         """
         )
    st.divider()
    st.subheader("🎲 Surprise Me!")
    if st.button("Recommend a Random Movie"):
        random_index = random.randint(0,9)
        st.image(
            "D:/PROJECT/assests/Posters/" +
            movie_posters[random_index],
            width=250
        )

        st.write("###",movies_df.iloc[random_index]["title"])

        st.link_button(
        "▶ Watch Trailer",
        movie_trailers[random_index]
        )
    quotes = [
    "🎬 Movies touch our hearts and awaken our vision.",
    "🍿 Every movie is a journey waiting to begin.",
    "🌟 Great stories never really end.",
    "🎥 Cinema is a mirror of life.",
    "📺 Every frame tells a story."
    ]
    st.subheader("💬 Quote of the Day")
    st.success(random.choice(quotes))
    
    facts = [
    "🍿 Netflix started as a DVD rental company.",
    "🎬 The average movie contains over 1000 camera shots.",
    "🌍 India produces more films than any other country.",
    "📺 Binge-watching became popular because of streaming platforms.",
    "🎥 Animation can take hundreds of hours for just one minute of film."
     ]
    st.subheader("🎉 Did You Know?")
    st.info(random.choice(facts))
    st.divider()
    st.caption("Made with ❤️ using Python, Pandas, Matplotlib and Streamlit.")
    st.caption("© 2026 STARDUST")
if page == "📊 Insights":
    
    df = pd.read_csv('netflix.csv')
    st.title("📽️STAR DUST")
    
    st.title("🎶Explore Box Office Trends🎶")
    movie = df[df['type']=="Movie"].shape[0]
    TVshow = df[df['type']=="TV Show"].shape[0]
    
    total = len(df)
    countries = df["country"].nunique()
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.metric("🎬 Movies", movie)

    with col2:
        st.metric("📺 TV Shows", TVshow)

    with col3:
        st.metric("📚 Total Titles", total)

    with col4:
        st.metric("🌍 Countries", countries)
    
    plt.style.use('ggplot')
    plt.style.use('dark_background')

    fig, ax = plt.subplots()
    df["country"].value_counts().head(10).plot(kind="barh",ax=ax)
    ax.set_title("🌍 Top 10 Countries")
    ax.set_xlabel("Number of Titles")
    st.pyplot(fig)
    
    fig0, ax = plt.subplots()
    df['country'].value_counts().head(15).plot(kind = 'bar',ax=ax)
    ax.set_title("Top 15 Countries")
    st.pyplot(fig0)

    fig1,ax= plt.subplots()
    df['release_year'].value_counts().sort_index().plot(kind='line', ax=ax)
    ax.set_title("📅 Release Year Trend")
    st.pyplot(fig1)
    st.divider()

    fig2, ax = plt.subplots()
    df["type"].value_counts().plot(kind="bar",ax=ax)
    ax.set_title("🎬 Movies vs TV Shows")
    st.pyplot(fig2)
    st.divider()

    fig3, ax = plt.subplots()
    df["director"].value_counts().head(10).plot(kind="barh",ax=ax)
    ax.set_title("🎥 Top Directors")
    st.pyplot(fig3)
    st.divider()

    st.success("📊 Dashboard generated successfully!")
    st.caption("Data Source: Netflix Dataset")
    st.subheader("📌 Fun Facts")

    oldest = df["release_year"].min()

    latest = df["release_year"].max()

    col1,col2 = st.columns(2)

    with col1:

        st.info(f"🎬 Oldest Release : {oldest}")

    with col2:

        st.info(f"🚀 Latest Release : {latest}")

if page == "🎬 Movies":
    st.title("Movies")
    
    df = pd.read_csv('netflix.csv')
    st.title("📽️STAR DUST")
    search = st.text_input( "",
          placeholder="What story are you looking for tonight?"
    )
    if search:
        result=df[df['title'].str.contains(search , case = False , na = False)]#case ignore capital letters and na ignore null values
        st.dataframe(result)
    st.divider()
    movies_df = df[df['type'] == 'Movie']
    genre = st.selectbox(
    "🎭 Choose Genre",
    ["All", "Action", "Comedy", "Drama", "Documentaries", "Horror"]
    )
    years = ["All"]
    for year in sorted(movies_df["release_year"].unique(), reverse=True):
        years.append(year) #sorted() function arrange the values,reverse=true make the newest movie appear                 
    selected_year = st.selectbox(
        "📅 Choose Release Year",
        years
    )
    if genre != "All":
        movies_df = movies_df[
            movies_df["listed_in"].str.contains(genre,case=False,na=False)
        ]
    if selected_year != "All":
         movies_df = movies_df[
        movies_df["release_year"] == selected_year
         ]
    st.success(f"🎬 Showing {len(movies_df)} Movies")#success shows green msg
    movie_count = len(movies_df)
    rating_count = len(movies_df["rating"].unique())#unique remove duplication
    duration_count = len(movies_df["duration"].unique())

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎬 Movies", movie_count)

    with col2:
        st.metric("⭐ Ratings", rating_count)

    with col3:
        st.metric("⏱️ Durations", duration_count)

    st.divider()
    movie_posters = [ 
         "dickjohnson.jpg",
         "mylittlepony.jpg",
         "sankofa.jpg",
         "thestarling.jpg",
         "jesuis.jpg",
         "confessions.jpg",
         "europe.jpg",
         "intrusion.jpg",
         "avvai.jpg",
         "gogo.jpg",
         "jeans.jpg",
         "minsara.jpg",
         "grown.jpg",
         "dark.jpg",
         "paranoia.jpg",
         "ankahi.jpg",
         "father.jpg",
         "stronghold.jpg",
         "birthofdragon.jpg",
         "jaws.jpg"
         ]
    movie_trailers = [
    "https://www.youtube.com/watch?v=wfTmT6C5DnM&pp=ygUUZGljayBqb2huc29uIGlzIGRlYWQ%3D",
    "https://www.youtube.com/watch?v=Pa_PRDVpjSk&pp=ygUhbXkgbGl0dGxlIHBvbnkgOiBhIG5ldyBnZW5lcmF0aW9u",
    "https://www.youtube.com/watch?v=jUWLAXHj2SU&pp=ygUHc2Fua29mYQ%3D%3D",
    "https://www.youtube.com/watch?v=fYyImx_KXm4&pp=ygUMdGhlIHN0YXJsaW5n",
    "https://www.youtube.com/watch?v=oFQel_8SZ6M&pp=ygUMamUgc3VpcyBrYXJs",
    "https://www.youtube.com/watch?v=uGJBHueplss&pp=ygUgQ29uZmVzc2lvbnMgb2YgYW4gSW52aXNpYmxlIEdpcmw%3D",
    "https://www.youtube.com/watch?v=DObP6W8b6ck&pp=ygUzRXVyb3BlJ3MgTW9zdCBEYW5nZXJvdXMgTWFuOiBPdHRvIFNrb3J6ZW55IGluIFNwYWlu",
    "https://www.youtube.com/watch?v=tAJVDe205tY&pp=ygUJSW50cnVzaW9u",
    "https://www.youtube.com/watch?v=LioSgVXzFdI&pp=ygUXQXZ2YWkgU2hhbm11Z2hpIHRyYWlsYXI%3D",
    "https://www.youtube.com/watch?v=cjWqbzSoYuA&pp=ygU0R28hIEdvISBDb3J5IENhcnNvbjogQ2hyaXNzeSBUYWtlcyB0aGUgV2hlZWwgdHJhaWxhcg%3D%3D",
    "https://www.youtube.com/watch?v=g6mmqzbjNXQ&pp=ygUWSmVhbnMgb2ZmaWNpbGEgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=UrCs31xkz2A&pp=ygUeTWluc2FyYSBLYW5hdnVvZmZpY2lsYSB0cmFpbGVy",
    "https://www.youtube.com/watch?v=wzImCSfTlgY&pp=ygUSCUdyb3duIFVwcyB0cmFpbGVy0gcJCUwLAYcqIYzv",
    "https://www.youtube.com/watch?v=K8iLp1xQtPQ&pp=ygUSZGFyayBza2llcyB0cmFpbGVy0gcJCUwLAYcqIYzv",
    "https://www.youtube.com/watch?v=2T1RLye5Z_w&pp=ygUQcGFyYW5vaWEgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=pw1WuzTYM3Q&pp=ygUXQW5rYWhpIEthaGFuaXlhIHRyYWlsZXLSBwkJTgsBhyohjO8%3D",
    "https://www.youtube.com/watch?v=VX2b52unYdw&pp=ygUnCVRoZSBGYXRoZXIgV2hvIE1vdmVzIE1vdW50YWlucyB0cmFpbGVy",
    "https://www.youtube.com/watch?v=2jp3YYw8hT4&pp=ygUWVGhlIFN0cm9uZ2hvbGQgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=soLlxteBbNA&pp=ygUbQmlydGggb2YgdGhlIERyYWdvbiB0cmFpbGVy",
    "https://www.youtube.com/watch?v=U1fu_sA7XhE&pp=ygUMamF3cyB0cmFpbGVy"
    ]
    random_index = random.randint(0, len(movie_posters)-1)
    st.subheader("🌟 Movie of the Day")
    col1, col2 = st.columns(2)
    with col1:
        st.image(
        "D:/PROJECT/assests/Posters/" +
        movie_posters[random_index],
        width=250
        )

    with col2:
       st.write("###", movies_df.iloc[random_index]["title"])
       st.write("⭐", movies_df.iloc[random_index]["rating"])
       st.write("🕒", movies_df.iloc[random_index]["duration"])

       st.link_button(
        "▶ Watch Trailer",
        movie_trailers[random_index]
      )

    st.divider()
    st.subheader("🏆 Top Rated Movies")

    top_movies = movies_df.sort_values(
    by="title" 
    ).head(5)

    for i in range(len(top_movies)):
        st.write(
        f"{i+1}. {top_movies.iloc[i]['title']} ⭐ {top_movies.iloc[i]['rating']}"
       )

    st.divider()
    st.subheader("🎲 Can't Decide?")

    recommend = st.button("Recommend Me a Movie")

    if recommend:

         random_index = random.randint(0, len(movie_posters)-1)
         col1, col2 = st.columns(2)

         with col1:

            st.image(
            "D:/PROJECT/assests/Posters/" +
            movie_posters[random_index],
            width=250
            )

         with col2:

            st.write("###", movies_df.iloc[random_index]["title"])

            st.write("⭐", movies_df.iloc[random_index]["rating"])

            st.write("🕒", movies_df.iloc[random_index]["duration"])

            st.link_button(
            "▶ Watch Trailer",
            movie_trailers[random_index]
            )

    st.divider()
    st.subheader("🎬 Browse Movies")
    st.caption("Click any trailer button to watch the official trailer on YouTube.")
    for row in range(5):           #gives the rows
        cols = st.columns(4)       #gives the columns

        for col in range(4):
            index = row * 4 + col 
            if index >= len(movie_posters):
                break
   
            with cols[col]:
                st.image(
                "D:/PROJECT/assests/Posters/" + movie_posters[index],width = 220
            )
                st.divider()
                st.link_button(
                    "▶ Watch Trailer",
                    movie_trailers[index]
                )

                st.markdown(f"**{movies_df.iloc[index]['title']}**")

                st.caption(f"⭐ {movies_df.iloc[index]['rating']}")

                st.caption(f"🕒 {movies_df.iloc[index]['duration']}")
        st.write("")
    
    st.success("🍿 Enjoy Exploring STARDUST!")
    st.info("✨ More movies are waiting on the next page!")

if page == "📺 TV Shows":
    st.title("📺 TV Shows")

    df = pd.read_csv('netflix.csv')
    st.title("📽️STAR DUST")
    search = st.text_input( "",
          placeholder="What story are you looking for tonight?"
    )
    if search:
        result=df[df['title'].str.contains(search , case = False , na = False)]
        st.dataframe(result)
    st.divider()
    tv_shows_df = df[df['type'] == 'TV Show']
    tv_posters = [
    "blood&water.jpg",
    "gangland.jpg",
    "jailbirds.jpg",
    "kotafactory.jpg",
    "midnightmass.jpg",
    "thegreatbritishbakingshow.jpg",
    "vendetta.jpg",
    "bangkok.jpg",
    "crimestories.jpg",
    "dearwhitepeople.jpg",
    "false.jpg",
    "monster.jpg",
    "resurrection.jpg",
    "love.jpg",
    "chicago.jpg",
    "squid.jpg",
    "tayo.jpg",
    "angry.jpg",
    "heman.jpg",
    "smart.jpg"
     ]
    tvshows_trailers = [
    "https://www.youtube.com/watch?v=2m0Cm2kMOBU&pp=ygUVYmxvb2QgJiB3YXRlciB0cmFpbGVy",
    "https://www.youtube.com/watch?v=0VZ2Nbx8gHI&pp=ygURR2FuZ2xhbmRzIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=G6vrmPQ50qs&pp=ygUeSmFpbGJpcmRzIE5ldyBPcmxlYW5zICB0cmFpbGVy",
    "https://www.youtube.com/watch?v=pNZQ6msbOvM&pp=ygUVS290YSBGYWN0b3J5ICB0cmFpbGVy",
    "https://www.youtube.com/watch?v=89UV8vmWXlY&pp=ygUWTWlkbmlnaHQgTWFzcyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=BnOZ9BNUTtk&pp=ygUmVGhlIEdyZWF0IEJyaXRpc2ggQmFraW5nIFNob3cgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=78qOHrILufk&pp=ygUsVmVuZGV0dGE6IFRydXRoLCBMaWVzIGFuZCBUaGUgTWFmaWEgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=JAfHOxm2Xhs&pp=ygUZQmFuZ2tvayBCcmVha2luZyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=ErB-Fm77gso&pp=ygUoQ3JpbWUgU3RvcmllczogSW5kaWEgRGV0ZWN0aXZlcyAgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=JMgWMzbM2Pk&pp=ygUaRGVhciBXaGl0ZSBQZW9wbGUgIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=AugXC36Xml8&pp=ygUfZmFsc2EgaWRlbnRpZGFkIG9yZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=gUjtViCsb8E&pp=ygU_TW9uc3RlcnMgSW5zaWRlOiBUaGUgMjQgRmFjZXMgb2YgQmlsbHkgTWlsbGlnYW4gb3JnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=FfdXu9jZFKs&pp=ygUmUmVzdXJyZWN0aW9uOiBFcnR1Z3J1bCBvcmdpbmFsIHRyYWlsZXI%3D",
    "https://www.youtube.com/watch?v=kX-QbcXyZug&pp=ygUkTG92ZSBvbiB0aGUgU3BlY3RydW0gb3JnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=o90l2auMiUs&pp=ygUiQ2hpY2FnbyBQYXJ0eSBBdW50IG9yZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=oqxAJKy0ii4&pp=ygUbU3F1aWQgR2FtZSBvcmlnaW5hbCB0cmFpbGVy",
    "https://www.youtube.com/watch?v=fS38dyRA0kE&pp=ygUoVGF5byBhbmQgTGl0dGxlIFdpemFyZHMgb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=QRmKa7vvct4&pp=ygUcQW5ncnkgQmlyZHMgb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=ZmEx7wQI6RY&pp=ygU3SGUtTWFuIGFuZCB0aGUgTWFzdGVycyBvZiB0aGUgVW5pdmVyc2Ugb3JpZ2luYWwgdHJhaWxlcg%3D%3D",
    "https://www.youtube.com/watch?v=No6052an_Zw&pp=ygUxSGUtTWFuIGFuZCBUaGUgU21hcnQgTW9uZXkgV29tYW4gb3JpZ2luYWwgdHJhaWxlctIHCQlOCwGHKiGM7w%3D%3D"
     ]
    
    for row in range(2):           #gives the rows
        cols = st.columns(5)       #gives the columns

        for col in range(5):
            index =  row * 5 + col    
            with cols[col]:
                st.image(
                "D:/PROJECT/assests/Posters/" + tv_posters[index],width = 300
            )
                st.divider()
                st.link_button(
                    "▶ Watch Trailer", 
                    tvshows_trailers[index]
                )

                st.markdown(
                    f"""⭐ {tv_shows_df.iloc[index]["rating"]}
                    🕒 {tv_shows_df.iloc[index]["duration"]}
                    """
                )
    st.divider()
    

if page == "💫 Movie Match":
    df = pd.read_csv('netflix.csv')
    st.title("💫 Movie Match")
    st.caption("Answer a few fun questions and let STARDUST discover your perfect watch.")
    st.divider()
    st.subheader("🌙 It's Friday Night...")

    q1 = st.radio(
       "What's the plan?",
       [
        "🍿 Staying in with snacks",
        "🎉 Going out with friends",
        "😴 Sleeping early",
        "🌍 Trying something new"
       ],
       index=None
    )

    st.divider()

    st.subheader("🎵 Pick Your Soundtrack")
    q2 = st.radio(
        "Which one matches your vibe?",
       [
        "🎹 Calm Piano",
        "🎸 Rock",
        "🎻 Emotional Orchestra",
        "🎧 Pop Hits"
        ],
        index=None
    )

    st.divider()

    st.subheader("🍿 Movie Snacks Matter!")
    q3 = st.radio(
        "Choose your snack:",
        [
        "🍕 Pizza",
        "🍫 Chocolate",
        "🍿 Popcorn",
        "🍟 Fries"
        ],
        index=None
    )

    st.divider()
    st.subheader("🎬 What Ending Do You Love?")
    q4 = st.radio(
       "Pick one:",
       [
        "❤️ Happy Ending",
        "🤯 Mind Blowing",
        "😭 Emotional",
        "😈 Unexpected Twist"
        ],
        index=None
    )

    st.divider()
    st.subheader("✨ Finally... What's Today's Vibe?")
    q5 = st.radio(
       "Choose one:",
       [
        "😂 Funny",
        "😭 Emotional",
        "😱 Thriller",
        "🚀 Adventure"
        ],
        index=None
    )

    st.divider()

    st.subheader("🌍 Pick Your Dream Destination")
    q6 = st.radio(
        "Where would you rather be?",
      [
        "🏖 Beach",
        "🏙 Big City",
        "🌌 Space",
        "🏕 Mountains"
       ],
       index=None
    )

    st.divider()
    match = st.button("✨ Reveal My Match")
    if match:
        if None in [q1, q2, q3, q4, q5, q6]:
            st.warning("⚠️ Please answer all the questions before revealing your match.")
        else:
            st.snow()
            st.header("🌌 The Stars Have Spoken...")
            st.write("Here's what STARDUST thinks about you 💫")
            st.divider()
            if q5 == "😂 Funny":
                st.success("🏆 STARDUST Badge Unlocked")
                st.markdown("## 😂 The Comedy King/Queen")
                st.write(
                "You love light-hearted stories, unforgettable laughs, and movies that make every night more fun."
                )
            elif q5 == "😭 Emotional":
                st.success("🏆 STARDUST Badge Unlocked")
                st.markdown("## 💖 The Hopeless Romantic")
                st.write(
            "You enjoy emotional journeys, meaningful characters, and stories that stay with you."
                )
            elif q5 == "😱 Thriller":
                st.success("🏆 STARDUST Badge Unlocked")
                st.markdown("## 🕵️ The Detective")
                st.write(
            "You enjoy suspense, mystery, and plot twists that keep everyone guessing."
                )
            elif q5 == "🚀 Adventure": 
                st.success("🏆 STARDUST Badge Unlocked")
                st.markdown("## 🚀 The Explorer")
                st.write(
                "You love discovering new worlds, exciting adventures, and unforgettable journeys."
                )
            if q5 == "😂 Funny":
                 result = df[df["listed_in"].str.contains("Comedies", case=False, na=False)]
            elif q5 == "😭 Emotional":
                result = df[df["listed_in"].str.contains("Dramas|Romantic", case=False, na=False)]
            elif q5 == "😱 Thriller":
                result = df[df["listed_in"].str.contains("Thrillers|Crime", case=False, na=False)]
            elif q5 == "🚀 Adventure":
                result = df[df["listed_in"].str.contains("Action|Adventure|Sci-Fi", case=False, na=False)]
        
            recommendations = result.sample(min(5, len(result)))
            st.divider()
            st.subheader("🍿 Your STARDUST Picks")
            for i in range(len(recommendations)):
                st.markdown(f"### 🎬 {recommendations.iloc[i]['title']}")
                st.write(f"⭐ Rating : {recommendations.iloc[i]['rating']}")
                st.write(f"🎭 Genre : {recommendations.iloc[i]['listed_in']}")
                st.write(f"📅 Release Year : {recommendations.iloc[i]['release_year']}")
                st.write(f"⏱ Duration : {recommendations.iloc[i]['duration']}")
                st.divider()
        st.info("✨ Not feeling these? Click 'Reveal My Match' again for a fresh set of recommendations!")

if page == "🎮STARDUST Arcade" :
    
    st.subheader("🎞️ Guess the Blockbuster")
    st.write("Can you guess the movie from the emojis?")
    st.divider()
    emoji_quiz = [

        {
        "emoji":"🦁👑",
        "options":["The Lion King","Frozen","Madagascar","Kung Fu Panda"],
        "answer":"The Lion King"
        },

       {
        "emoji":"🕷️🕸️🧑",
        "options":["Batman","Spider-Man","Superman","Iron Man"],
        "answer":"Spider-Man"
        },

        {
        "emoji":"🧊👸❄️",
        "options":["Moana","Frozen","Brave","Encanto"],
        "answer":"Frozen"
        },

        {  
        "emoji":"🧑‍🎓👨‍🎓👨‍🎓📚",
        "options":["3 Idiots","Chhichhore","Munna Bhai M.B.B.S.","Fukrey"],
        "answer":"3 Idiots"
        },

        {"emoji":"👻😎👳‍♂️",
         "options":["Sardaar Ji","Carry On Jatta","Shadaa","Qismat"],
        "answer":"Sardaar Ji"
        },
        {
        "emoji":"🥅😆",
        "options":["Golmaal","Dhamaal","Housefull","Welcome"],
        "answer":"Golmaal"
        },

        {
        "emoji":"🏠😄😄😄",
        "options":["Bhool Bhulaiyaa","Dhamaal","Housefull","Welcome"],
        "answer":"Housefull"
        },

        {
        "emoji":"✈️👊",
        "options":["Fighter","WAR","Pathaan","Bang Bang"],
        "answer":"Fighter"
        },
        {
        "emoji":"🏃🏁",
        "options":["Golmaal","Krrish","Dhoom","Race"],
        "answer":"Race"
        },

        ]

    if "question" not in st.session_state:
        st.session_state.question = random.choice(emoji_quiz)
    question = st.session_state.question
    st.markdown(f"## {question['emoji']}")
    guess = st.radio("Choose your answer",question["options"], index=None,key = "guess")
    if st.button("🎬 Reveal Answer"):
        if guess is None:
            st.warning("⚠️ Please choose an answer first!")
        elif guess == question["answer"]:

            st.success("🎉 Correct! You're a movie genius!")
            st.balloons()
        else:

            st.error("❌ Wrong Answer!")
            st.info(f"✅ Correct Answer: **{question['answer']}**")
    
    if st.button("🔄 Next Question"):
        st.session_state.question = random.choice(emoji_quiz)
        st.rerun()