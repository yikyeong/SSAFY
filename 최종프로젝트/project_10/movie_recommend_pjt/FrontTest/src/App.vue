<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mt-3">
      <div class="container">
        <!-- 로고에 왼쪽 간격 추가 -->
        <img src="./img/logo/ssafy_logo.png" alt="logo" class="logo">
        <!-- 네비게이션 항목들을 오른쪽으로 정렬 -->
        <div class="ms-auto nav-links">
          <RouterLink :to="{ name: 'home' }" class="nav-link" active-class="active-link">홈</RouterLink>
          <RouterLink :to="{ name: 'searchReview' }" class="nav-link" active-class="active-link">리뷰검색</RouterLink>
          <RouterLink :to="{ name: 'signUp' }" class="nav-link" active-class="active-link">회원가입</RouterLink>
          <RouterLink :to="{ name: 'login' }" class="nav-link" active-class="active-link">로그인</RouterLink>
          <form @submit.prevent="logOut">
            <input type="submit" value="로그아웃" class="nav-link">
          </form>
          <RouterLink :to="{ name: 'searchMovie' }" class="nav-link" active-class="active-link">
            <img src="./img/search_icon/white_search_icon2-removebg-preview.png" alt="search_icon" class="nav-img">
          </RouterLink>
          <RouterLink :to="{ name: 'movieRecommend' }" class="nav-link" active-class="active-link">영화추천</RouterLink>
        </div>
      </div>
    </nav>
  </header>

  <!-- 라우터 뷰 영역 -->
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const logOut = function () {
  store.logOut()
}

</script>

<style>
/* 페이지 배경에 어두운 그라데이션 추가 */
html,
body {
  background: linear-gradient(to bottom, #1a1a1a, #514848);
  /* 그라데이션 설정 */
  color: white;
  /* 텍스트를 흰색으로 설정 */
  height: 100%;
  /* 페이지 높이를 100%로 설정 */
  margin: 0;
  /* 기본 마진 제거 */
  font-family: Arial, sans-serif;
  /* 기본 폰트 설정 */
}

/* 네비게이션 항목 사이에 일정한 간격을 두고, 마우스 오버와 클릭 시 색상 변경 */
.nav-link {
  cursor: pointer;
  /* 클릭할 수 있음을 나타내는 커서 */
  font-size: 16px;
  /* 기본 글자 크기 */
  color: white;
  /* 기본 텍스트 색상 흰색 */
  text-decoration: none;
  /* 밑줄 제거 */
  margin-right: 15px;
  /* 항목 간의 간격 */
}

/* 이미지 크기를 텍스트 크기에 맞게 설정 */
.nav-img {
  width: 30px;
  /* 원하는 크기로 조정 */
  height: auto;
  /* 비율 유지 */
  vertical-align: middle;
  /* 텍스트와 수평 정렬 */
  margin-left: 5px;
  /* 이미지와 텍스트 간 간격 */
}

/* 네비게이션 항목을 한 줄로 정렬하고, 간격을 일정하게 설정 */
.nav-links {
  display: flex;
  /* 수평으로 정렬 */
  justify-content: flex-end;
  /* 오른쪽으로 정렬 */
  align-items: center;
  /* 수직 중앙 정렬 */
  gap: 20px;
  /* 항목 간 간격 */
}

/* 마우스 오버 시 색상 */
.nav-link:hover {
  color: #007bff;
}

/* 활성화된 링크 색상 */
.active-link {
  color: #ff6347;
  /* 활성화된 링크 색상 (예: 토마토 색) */
}

/* 네비게이션 바 스타일 */
.navbar {
  display: flex;
  justify-content: flex-start;
  /* 기본적으로 왼쪽 정렬 */
  align-items: center;
  padding-top: 20px;
  /* 네비게이션 바의 위쪽 여백 */
  width: 100%;
  box-sizing: border-box;
}

/* 네비게이션 바 내의 컨테이너 스타일 */
.navbar .container {
  display: flex;
  justify-content: flex-start;
  width: 100%;
  align-items: center;
}

/* 네비게이션 항목들을 오른쪽으로 몰기 */
.ms-auto {
  margin-left: auto;
  /* 오른쪽으로 몰아주는 클래스 */
}

/* 로고의 왼쪽 여백 */
.logo {
  margin-left: 0px;
  width: 75px;
  /* 로고의 기본 크기 */
  height: auto;
  /* 비율 유지 */
  transition: width 0.3s ease;
  /* 로고 크기 조정 시 부드럽게 전환 */
}

/* 작은 화면에서 로고 크기 줄이기 */
@media (max-width: 768px) {
  .logo {
    width: 50px;
    /* 화면이 작아지면 로고 크기 줄이기 */
  }

  .nav-links {
    gap: 15px;
    /* 작은 화면에서 네비게이션 항목 간 간격을 좁히기 */
  }
}

/* 매우 작은 화면에서 네비게이션을 세로로 쌓기 */
@media (max-width: 480px) {
  .nav-links {
    flex-direction: column;
    /* 세로로 쌓기 */
    gap: 10px;
    /* 항목 간 간격 좁히기 */
    text-align: center;
    /* 텍스트 중앙 정렬 */
  }

  .logo {
    width: 50px;
    /* 작은 화면에서 로고 크기 줄이기 */
  }
}
</style>
