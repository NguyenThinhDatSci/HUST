<script>
name: "MyApp";
</script>

<template>
  <div class="main">
    <div class="main_top">
      <div class="weather_top">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512">
          <!--! Font Awesome Pro 6.3.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
          <path
            d="M144 64c-26.5 0-48 21.5-48 48V276.5c0 17.3-7.1 31.9-15.3 42.5C70.2 332.6 64 349.5 64 368c0 44.2 35.8 80 80 80s80-35.8 80-80c0-18.5-6.2-35.4-16.7-48.9c-8.2-10.6-15.3-25.2-15.3-42.5V112c0-26.5-21.5-48-48-48zM32 112C32 50.2 82.1 0 144 0s112 50.1 112 112V276.5c0 .1 .1 .3 .2 .6c.2 .6 .8 1.6 1.7 2.8c18.9 24.4 30.1 55 30.1 88.1c0 79.5-64.5 144-144 144S0 447.5 0 368c0-33.2 11.2-63.8 30.1-88.1c.9-1.2 1.5-2.2 1.7-2.8c.1-.3 .2-.5 .2-.6V112zM192 368c0 26.5-21.5 48-48 48s-48-21.5-48-48c0-20.9 13.4-38.7 32-45.3V272c0-8.8 7.2-16 16-16s16 7.2 16 16v50.7c18.6 6.6 32 24.4 32 45.3z"
          />
        </svg>
      </div>
      <div class="weather_body">
        <div class="body_left"></div>
        <div class="body_right"></div>
      </div>
    </div>
    <div class="table">
      <table>
        <thead>
          <th>a</th>
          <th>b</th>
          <th>c</th>
        </thead>
        <tbody>
          <tr>
            a
          </tr>
          <tr>
            a
          </tr>
          <tr>
            a
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style >
.main {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.main_top {
  display: flex;
  flex-direction: column;
  background-color: #fff;
  height: 400px;
  width: 500px;
  border-radius: 15px;
}

.weather_top {
  display: flex;
  justify-content: center;
  align-items: center;
  flex: 1;
}

.weather_body {
  display: flex;
  flex: 1;
  width: 100%;
}

svg {
  height: 80px;
}

.body_left {
  background-color: #000;
  flex: 2;
  border-bottom-left-radius: 15px;
}

.body_right {
  background-color: #70c1b3;
  flex: 1;
  border-bottom-right-radius: 15px;
}
</style>
