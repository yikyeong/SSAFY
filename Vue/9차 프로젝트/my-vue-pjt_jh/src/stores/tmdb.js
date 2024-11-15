import axios from 'axios';

const API_KEY = import.meta.env.VITE_TMDB_API_KEY;
const BASE_URL = 'https://api.themoviedb.org/3';

export const fetchTopRatedMovies = async () => {
  try {
    const response = await axios.get(`${BASE_URL}/movie/top_rated`, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    });
    return response.data.results;  // 영화 목록 반환
  } catch (error) {
    console.error('Failed to fetch top rated movies:', error);
  }
};

export const fetchMovieDetails = async (movieId) => {
  try {
    const response = await axios.get(`${BASE_URL}/movie/${movieId}`, {
      params: {
        api_key: API_KEY,
        language: 'ko-KR',
      }
    });
    return response.data;  // 영화 세부정보 반환
  } catch (error) {
    console.error('Failed to fetch movie details:', error);
  }
};
