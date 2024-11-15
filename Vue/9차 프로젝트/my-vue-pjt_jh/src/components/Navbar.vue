<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="logo">Movie App</router-link>
      <ul class="navbar-links">
        <li>
          <router-link to="/movies" class="nav-link">Top Rated Movies</router-link>
        </li>
        <li>
          <router-link to="/review-search" class="nav-link">Search Reviews</router-link>
        </li>
        <li>
          <router-link to="/recommended" class="nav-link">Recommended Movies</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
.navbar {
  background-color: #333;
  padding: 15px;
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  color: white;
  font-size: 1.8rem;
  text-decoration: none;
}

.navbar-links {
  list-style: none;
  display: flex;
  gap: 15px;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-size: 1.1rem;
}

.nav-link:hover {
  text-decoration: underline;
}
</style>
