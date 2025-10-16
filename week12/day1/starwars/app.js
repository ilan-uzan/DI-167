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
  if (!elements.themeAudio) {
    console.log('Audio element not found');
    return;
  }
  
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
  // Canvas-based 3D starfield with perspective and streaks
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

  const cx = () => window.innerWidth / 2;
  const cy = () => window.innerHeight / 2;
  const fov = Math.min(window.innerWidth, window.innerHeight) * 0.8; // perspective scale

  const count = Math.min(1200, Math.floor((window.innerWidth * window.innerHeight) / 2000));
  function makeStar() {
    // x,y in a unit disk for even distribution
    const r = Math.sqrt(Math.random());
    const theta = Math.random() * Math.PI * 2;
    const x = r * Math.cos(theta);
    const y = r * Math.sin(theta);
    const z = 0.2 + Math.random() * 1.8; // depth (near -> far)
    return { x, y, z, px: null, py: null, o: 0.7 + Math.random() * 0.3 };
  }
  const stars = Array.from({ length: count }, makeStar);

  let rafId; let lastTs; let startTs; let shouldStop = false;
  const duration = 1400; // ms

  // Ease: smoother accel then slight decel
  function easeCubic(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }

  function render(ts) {
    if (!startTs) startTs = ts;
    if (!lastTs) lastTs = ts;
    const elapsed = ts - startTs;
    const dt = Math.min(32, ts - lastTs) / 16.67; // ~frames
    lastTs = ts;

    const t = Math.min(1, elapsed / duration);
    const accel = 0.6 + 5.0 * easeCubic(t); // speed factor over time

    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

    // Subtle flash at start
    if (elapsed < 120) {
      const alpha = 1 - elapsed / 120;
      ctx.fillStyle = `rgba(255,255,255,${alpha * 0.35})`;
      ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
    }

    for (const s of stars) {
      // advance toward camera by reducing z
      s.z -= (0.02 + 0.035 * s.o) * accel * dt;
      if (s.z <= 0.05) {
        // recycle star to back
        const ns = makeStar();
        s.x = ns.x; s.y = ns.y; s.z = ns.z; s.px = null; s.py = null; s.o = ns.o;
      }

      // project to screen
      const scale = fov / s.z;
      const x = cx() + s.x * scale;
      const y = cy() + s.y * scale;

      if (s.px != null && s.py != null) {
        const grad = ctx.createLinearGradient(s.px, s.py, x, y);
        grad.addColorStop(0, `rgba(255,255,255,0)`);
        grad.addColorStop(1, `rgba(255,255,255,${s.o})`);
        ctx.strokeStyle = grad;
        ctx.lineWidth = Math.min(4, Math.max(1, (fov / (s.z + 0.001)) * 0.003));
        ctx.beginPath();
        ctx.moveTo(s.px, s.py);
        ctx.lineTo(x, y);
        ctx.stroke();
      }

      s.px = x; s.py = y;
    }

    // Stop immediately when requested
    if (shouldStop) {
      cancelAnimationFrame(rafId);
      canvas.remove();
      return;
    }

    if (elapsed < duration) {
      rafId = requestAnimationFrame(render);
    } else {
      cancelAnimationFrame(rafId);
      canvas.remove();
    }
  }

  window.addEventListener('resize', resize, { once: true });
  rafId = requestAnimationFrame(render);

  // Return function to stop animation immediately
  return () => {
    shouldStop = true;
  };
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
  const stopHyperspace = triggerHyperspace(); // Get stop function
  
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

    // Stop hyperspace animation smoothly when character loads
    stopHyperspace();
    
    renderCharacter({
      name: name || 'Unknown',
      height: height || 'Unknown',
      gender: gender || 'Unknown',
      birthYear: birthYear || 'Unknown',
      homeworldName
    });
  } catch (err) {
    // Stop hyperspace animation on error too
    stopHyperspace();
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
  // Debug audio element
  console.log('Audio element:', elements.themeAudio);
  console.log('Audio button:', elements.audioBtn);
  
  // Check if audio file loads
  if (elements.themeAudio) {
    elements.themeAudio.addEventListener('loadstart', () => console.log('Audio loading started'));
    elements.themeAudio.addEventListener('canplay', () => console.log('Audio can play'));
    elements.themeAudio.addEventListener('error', (e) => console.log('Audio error:', e));
    elements.themeAudio.addEventListener('loadeddata', () => console.log('Audio data loaded'));
  }
  
  // Try to start audio on first user interaction
  document.addEventListener('click', function() {
    if (!isAudioPlaying && elements.themeAudio) {
      console.log('Attempting to play audio...');
      elements.themeAudio.play().catch(e => console.log('Auto-play blocked:', e));
    }
  }, { once: true });
});


