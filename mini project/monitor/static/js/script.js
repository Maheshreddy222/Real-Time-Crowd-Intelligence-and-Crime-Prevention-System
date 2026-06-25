// ===== AI Sentinel - Shared Script =====
// 🔍 Toggle search dropdown
function toggleSearchDropdown(event) {
    event.stopPropagation(); // prevents closing instantly

    let dropdown = document.getElementById("searchDropdown");

    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
    } else {
        dropdown.style.display = "block";
    }
}

// CLOSE when clicking outside
document.addEventListener("click", function (event) {
    let dropdown = document.getElementById("searchDropdown");
    let searchBox = document.querySelector(".search-input");

    if (!searchBox.contains(event.target) && !dropdown.contains(event.target)) {
        dropdown.style.display = "none";
    }
});
function goToDashboard() {
    if (window.location.pathname === "/") {
        location.reload(); // already on dashboard
    } else {
        window.location.href = "/";
    }
}
// Live clock
function updateClock() {
  const now = new Date();
  const dateEl = document.getElementById('header-date');
  const timeEl = document.getElementById('header-time');
  if (dateEl) dateEl.textContent = now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
  if (timeEl) timeEl.textContent = now.toLocaleTimeString('en-US');
}
setInterval(updateClock, 1000);

// Highlight active nav
document.addEventListener('DOMContentLoaded', () => {
  updateClock();
  lucide.createIcons();
  const page = location.pathname.split('/').pop() || '/';
  document.querySelectorAll('.nav-item').forEach(el => {
    if (el.getAttribute('href') === page) el.classList.add('active');
  });
  // Animate stat counters
  document.querySelectorAll('[data-count]').forEach(el => {
    const target = parseInt(el.dataset.count);
    if (isNaN(target)) { el.textContent = el.dataset.countText || '0'; return; }
    let current = 0;
    const step = Math.ceil(target / 40);
    const timer = setInterval(() => {
      current += step;
      if (current >= target) { current = target; clearInterval(timer); }
      el.textContent = current.toLocaleString();
    }, 30);
  });
  // Filter buttons
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const group = btn.closest('.filter-group');
      group.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      const target = btn.closest('.filter-group').dataset.target;
      if (target) {
        document.querySelectorAll(target).forEach(item => {
          if (filter === 'all' || item.dataset.status === filter || item.dataset.severity === filter || item.dataset.type === filter) {
            item.style.display = '';
          } else {
            item.style.display = 'none';
          }
        });
      }
    });
  });
  // Search
  const searchInput = document.getElementById('page-search');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase();
      const target = searchInput.dataset.target;
      if (target) {
        document.querySelectorAll(target).forEach(item => {
          item.style.display = item.textContent.toLowerCase().includes(q) ? '' : 'none';
        });
      }
    });
  }
});
