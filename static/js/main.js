// Theme management with cosmic effects
function setTheme(color) {
    document.documentElement.setAttribute('data-theme', color);
    localStorage.setItem('writeups-theme', color);
    
    // Add theme switch animation
    document.body.style.transition = 'all 0.5s ease';
    setTimeout(() => {
        document.body.style.transition = '';
    }, 500);
}

// Load saved theme on startup
window.addEventListener('load', function() {
    const savedTheme = localStorage.getItem('writeups-theme') || 'blue';
    setTheme(savedTheme);
});

// Machine navigation system
function showMachine(machineId) {
    // Hide all page contents
    document.querySelectorAll('.page-content').forEach(page => {
        page.style.display = 'none';
        page.classList.remove('active');
    });
    
    // Show selected machine page
    const machinePage = document.getElementById('machine-' + machineId);
    if (machinePage) {
        machinePage.style.display = 'block';
        setTimeout(() => {
            machinePage.classList.add('active');
        }, 10);
    }
    
    // Update machine button states
    document.querySelectorAll('.machine-item').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Highlight selected machine
    event.target.closest('.machine-item').classList.add('active');
}

// Create floating particles dynamically
function createSpaceParticles() {
    const particleCount = 15;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'space-particle';

		const direction = Math.random() < 0.5 ? 'up' : 'down';
        
        if (direction === 'up') {
            particle.style.animationName = 'float-up';
        } else {
            particle.style.animationName = 'float-down';
        }
        
        particle.style.left = Math.random() * 100 + '%';
        particle.style.width = (Math.random() * 3 + 1) + 'px';
        particle.style.height = particle.style.width;
        particle.style.animationDelay = Math.random() * 20 + 's';
        particle.style.animationDuration = (Math.random() * 10 + 15) + 's';
        document.body.appendChild(particle);
    }
}

// Initialize the cosmic interface
document.addEventListener('DOMContentLoaded', function() {
    createSpaceParticles();
    
    // Add smooth scrolling for code blocks
    document.querySelectorAll('.code-block').forEach(block => {
        block.addEventListener('wheel', function(e) {
            if (this.scrollWidth > this.clientWidth) {
                e.preventDefault();
                this.scrollLeft += e.deltaY;
            }
        });
    });
});

// Keyboard shortcuts for navigation
document.addEventListener('keydown', function(e) {
    if (e.ctrlKey || e.metaKey) {
        switch(e.key) {
            case '1':
                e.preventDefault();
                showPage('home');
                break;
            case '2':
                e.preventDefault();
                showPage('about');
                break;
            case 'b':
                e.preventDefault();
                showMachine('beep');
                break;
            case 'l':
                e.preventDefault();
                showMachine('lame');
                break;
        }
    }
});
/*
const sidebar = document.querySelector('.sidebar');
		const toggleBtn = document.querySelector('.sidebar-toggle');

		toggleBtn.addEventListener('click', () => {
		  sidebar.classList.toggle('hidden');
		  toggleBtn.textContent = sidebar.classList.contains('hidden') ? '>' : '✖';
		});
*/
