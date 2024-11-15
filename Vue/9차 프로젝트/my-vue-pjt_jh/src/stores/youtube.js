// src/api/youtube.js
import axios from 'axios';

const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY;
const YOUTUBE_BASE_URL = 'https://www.googleapis.com/youtube/v3/search';

// YouTube에서 영화 리뷰 영상을 검색하는 함수
export const searchYouTubeVideos = async (query) => {
  try {
    const response = await axios.get(YOUTUBE_BASE_URL, {
      params: {
        part: 'snippet',
        q: `${query} review`,
        key: YOUTUBE_API_KEY
      }
    });
    return response.data.items;  // 검색된 유튜브 영상 목록을 반환
  } catch (error) {
    console.error('Failed to fetch YouTube videos:', error);
    return [];
  }
};
