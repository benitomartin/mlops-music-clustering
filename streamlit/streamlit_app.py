import streamlit as st
import pandas as pd
import joblib
from sklearn.utils import shuffle
import pywhatkit as kit

def main():
    # Set page title and configure layout
    st.set_page_config(page_title="Playlist Generator App", page_icon="🎷", layout="wide")
    st.title('📻MUSIC PLAYLIST GENERATOR📻')

    # Header for selecting song features
    st.header("Select your song features")

    # Create two columns for the song feature sliders
    col1, col2 = st.columns(2)

    with col1:
        acousticness = st.slider("Acousticness", min_value=0., max_value=1., step=0.01)
        danceability = st.slider("Danceability", min_value=0., max_value=1., step=0.01)
        duration_ms = st.slider("Duration (min)", min_value=0, max_value=10)
        energy = st.slider("Energy", min_value=0., max_value=1., step=0.01)
        instrumentalness = st.slider("Instrumentalness", min_value=0., max_value=1., step=0.01)

    with col2:
        liveness = st.slider("Liveness", min_value=0., max_value=1., step=0.01)
        loudness = st.slider("Loudness", min_value=-60., max_value=0., step=0.5)
        speechiness = st.slider("Speechiness", min_value=1., max_value=10., step=0.1)
        tempo = st.slider("Tempo", min_value=0., max_value=1., step=0.01)
        valence = st.slider("Valence", min_value=0., max_value=1., step=0.01)

    # Popularity slider
    popularity = st.slider("Popularity", min_value=0, max_value=100, step=1)

    # Create a DataFrame with selected song features
    df = pd.DataFrame({
        'popularity': [popularity],
        'acousticness': [acousticness],
        'danceability': [danceability],
        'duration_ms': [duration_ms * 50],
        'energy': [energy],
        'instrumentalness': [instrumentalness],
        'liveness': [liveness],
        'loudness': [loudness],
        'speechiness': [speechiness],
        'tempo': [tempo],
        'valence': [valence]
    })

    # Sidebar information about the app
    st.sidebar.subheader("About the App")
    st.sidebar.info("This App is based on the following Spotify Dataset from [Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db).")
    st.sidebar.info("PCA and KMeans have been performed to cluster the songs into 5 groups (playlists) based on the song features.")
    st.sidebar.info("First, you can generate the playlist based on the selected features. Then, you can search for a random song from the list, which will redirect to YouTube.")
    st.sidebar.image("../images/cassette.jpg")

    # Use st.session_state to persist variables across button clicks
    if 'filtered_playlist_df' not in st.session_state:
        st.session_state.filtered_playlist_df = pd.DataFrame()

    if 'selected_song' not in st.session_state:
        st.session_state.selected_song = ""

    # Generate Playlist button
    if st.button("Generate Playlist"):
        model = joblib.load('../model/best_model.pkl')
        predict = model.predict(df)
        st.write("Let's Rock!🎸🎸🎸")

        # Read the dataset and rename columns
        playlist_file = pd.read_csv("../data/labelled_dataset.csv")
        playlist_df = pd.DataFrame(playlist_file)
        new_column_names = {
            "genre": "Genre",
            "artist_name": "Artist Name",
            "track_name": "Track Name",
            "cluster": "cluster",
        }
        playlist_df = playlist_df.rename(columns=new_column_names)

        # Filter and shuffle the playlist
        st.session_state.filtered_playlist_df = playlist_df[playlist_df['cluster'] == predict[0]]
        shuffled_playlist = shuffle(st.session_state.filtered_playlist_df.drop(labels=["cluster"], axis=1))

        # Display the shuffled playlist
        st.dataframe(shuffled_playlist, use_container_width=True, hide_index=True)

    # Search on YouTube button
    st.header("Search on YouTube a random song from your list")
    if st.button("Search on YouTube"):
        if not st.session_state.filtered_playlist_df.empty:
            # Get a random song and artist from the filtered playlist
            selected_row = st.session_state.filtered_playlist_df.sample(n=1)
            selected_artist = selected_row["Artist Name"].values[0]
            st.session_state.selected_song = selected_row["Track Name"].values[0]

            # Perform a YouTube search for the selected song and artist
            search_query = f"{st.session_state.selected_song} {selected_artist}"
            kit.playonyt(search_query)

if __name__ == '__main__':
    main()
   
