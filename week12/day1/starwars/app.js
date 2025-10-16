'use strict';

// DOM retrieval
const elements = {
  button: document.getElementById('fetchBtn'),
  audioBtn: document.getElementById('audioBtn'),
  audioIcon: document.getElementById('audioIcon'),
  themeAudio: document.getElementById('themeAudio'),
  loading: document.getElementById('loading'),
  error: document.getElementById('error'),
  errorMsg: document.getElementById('errorMsg'),
  placeholder: document.getElementById('placeholder'),
  content: document.getElementById('content'),
  name: document.getElementById('name'),
  height: document.getElementById('height'),
  gender: document.getElementById('gender'),
  birthYear: document.getElementById('birthYear'),
  homeworld: document.getElementById('homeworld')
};

const TOTAL_CHARACTERS = 83; // as per instructions
let isAudioPlaying = false;

// Audio controls
function toggleAudio() {
  if (isAudioPlaying) {
    elements.themeAudio.pause();
    elements.audioIcon.className = 'fa-solid fa-volume-xmark';
    isAudioPlaying = false;
  } else {
    elements.themeAudio.play().catch(e => console.log('Audio play failed:', e));
    elements.audioIcon.className = 'fa-solid fa-volume-high';
    isAudioPlaying = true;
  }
}

// Hyperspace animation
function triggerHyperspace() {
  // Canvas-based star streaks from center
  const canvas = document.createElement('canvas');
  canvas.className = 'hyperspace-canvas';
  const ctx = canvas.getContext('2d');
  document.body.appendChild(canvas);

  const dpr = Math.max(1, window.devicePixelRatio || 1);
  function resize() {
    canvas.width = Math.floor(window.innerWidth * dpr);
    canvas.height = Math.floor(window.innerHeight * dpr);
    canvas.style.width = window.innerWidth + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();

  const centerX = () => window.innerWidth / 2;
  const centerY = () => window.innerHeight / 2;

  const numStars = Math.min(600, Math.floor((window.innerWidth * window.innerHeight) / 3500));
  const stars = Array.from({ length: numStars }).map(() => {
    const angle = Math.random() * Math.PI * 2;
    const speed = 6 + Math.random() * 10; // px per frame base
    const length = 6 + Math.random() * 18;
    return {
      angle,
      speed,
      length,
      distance: 0.2 + Math.random() * 1.2,
      opacity: 0.6 + Math.random() * 0.4
    };
  });

  let start; let rafId;
  const duration = 1100; // ms

  function step(ts) {
    if (!start) start = ts;
    const elapsed = ts - start;

    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    ctx.fillStyle = 'rgba(0,0,0,0.15)';
    ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);

    for (const s of stars) {
      // accelerate with time to mimic warp
      const t = Math.min(1, elapsed / duration);
      const accel = 0.5 + 4.5 * t * t; // quadratic acceleration
      s.distance += s.speed * accel;

      const x0 = centerX() + Math.cos(s.angle) * (s.distance - s.length);
      const y0 = centerY() + Math.sin(s.angle) * (s.distance - s.length);
      const x1 = centerX() + Math.cos(s.angle) * s.distance;
      const y1 = centerY() + Math.sin(s.angle) * s.distance;

      const grad = ctx.createLinearGradient(x0, y0, x1, y1);
      grad.addColorStop(0, `rgba(255,255,255,0)`);
      grad.addColorStop(1, `rgba(255,255,255,${s.opacity})`);
      ctx.strokeStyle = grad;
      ctx.lineWidth = Math.max(1, t * 3);
      ctx.beginPath();
      ctx.moveTo(x0, y0);
      ctx.lineTo(x1, y1);
      ctx.stroke();
    }

    if (elapsed < duration) {
      rafId = requestAnimationFrame(step);
    } else {
      cancelAnimationFrame(rafId);
      canvas.remove();
    }
  }

  window.addEventListener('resize', resize, { once: true });
  rafId = requestAnimationFrame(step);
}


function randomCharacterId() {
  return Math.floor(Math.random() * TOTAL_CHARACTERS) + 1;
}

function showLoading() {
  elements.loading.classList.remove('hidden');
  elements.error.classList.add('hidden');
  elements.placeholder.classList.add('hidden');
  elements.content.classList.add('hidden');
  elements.button.disabled = true;
}

function hideLoading() {
  elements.loading.classList.add('hidden');
  elements.button.disabled = false;
}

function showError(message) {
  elements.errorMsg.textContent = message || 'Something went wrong. Please try again.';
  elements.error.classList.remove('hidden');
  elements.placeholder.classList.add('hidden');
  elements.content.classList.add('hidden');
}

function renderCharacter({ name, height, gender, birthYear, homeworldName }) {
  elements.name.textContent = name;
  elements.height.textContent = height;
  elements.gender.textContent = gender;
  elements.birthYear.textContent = birthYear;
  elements.homeworld.textContent = homeworldName;

  elements.content.classList.remove('hidden');
  elements.error.classList.add('hidden');
  elements.placeholder.classList.add('hidden');
}

async function fetchJson(url) {
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`);
  }
  return response.json();
}

async function fetchRandomCharacter() {
  showLoading();
  try {
    const id = randomCharacterId();
    const personUrl = `https://www.swapi.tech/api/people/${id}`;
    const personData = await fetchJson(personUrl);

    if (!personData || !personData.result) {
      throw new Error('Invalid character payload');
    }

    const props = personData.result.properties;
    const { name, height, gender, birth_year: birthYear, homeworld } = props;

    let homeworldName = 'Unknown';
    try {
      if (homeworld) {
        const worldData = await fetchJson(homeworld);
        homeworldName = worldData?.result?.properties?.name || 'Unknown';
      }
    } catch (_) {
      homeworldName = 'Unknown';
    }

    renderCharacter({
      name: name || 'Unknown',
      height: height || 'Unknown',
      gender: gender || 'Unknown',
      birthYear: birthYear || 'Unknown',
      homeworldName
    });
  } catch (err) {
    showError(`Failed to retrieve character. ${err.message || ''}`.trim());
  } finally {
    hideLoading();
  }
}

async function fetchRandomCharacter() {
  showLoading();
  triggerHyperspace(); // Add hyperspace effect
  
  try {
    const id = randomCharacterId();
    const personUrl = `https://www.swapi.tech/api/people/${id}`;
    const personData = await fetchJson(personUrl);

    if (!personData || !personData.result) {
      throw new Error('Invalid character payload');
    }

    const props = personData.result.properties;
    const { name, height, gender, birth_year: birthYear, homeworld } = props;

    let homeworldName = 'Unknown';
    try {
      if (homeworld) {
        const worldData = await fetchJson(homeworld);
        homeworldName = worldData?.result?.properties?.name || 'Unknown';
      }
    } catch (_) {
      homeworldName = 'Unknown';
    }

    renderCharacter({
      name: name || 'Unknown',
      height: height || 'Unknown',
      gender: gender || 'Unknown',
      birthYear: birthYear || 'Unknown',
      homeworldName
    });
  } catch (err) {
    showError(`Failed to retrieve character. ${err.message || ''}`.trim());
  } finally {
    hideLoading();
  }
}

// Wire events
if (elements.button) {
  elements.button.addEventListener('click', fetchRandomCharacter);
}

if (elements.audioBtn) {
  elements.audioBtn.addEventListener('click', toggleAudio);
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
  // Try to start audio on first user interaction
  document.addEventListener('click', function() {
    if (!isAudioPlaying && elements.themeAudio) {
      elements.themeAudio.play().catch(e => console.log('Auto-play blocked:', e));
    }
  }, { once: true });
});


