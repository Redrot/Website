particlesJS.load('particles-js', 'static/assets/particles.json', () => {
  console.log('callback - particles.js config loaded');
});

var scroll = new SmoothScroll('a[href*="#"]');
