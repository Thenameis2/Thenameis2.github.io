// Function to navigate to a section and show/hide the appropriate content
function navigateToSection(sectionId) {
    // Hide all sections
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
      section.classList.add('hidden');
    });
  
    // Show the selected section
    const selectedSection = document.getElementById(sectionId);
    selectedSection.classList.remove('hidden');
  }
  
  // Function to show only the home section initially
  function showHomeOnly() {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
      section.classList.add('hidden');
    });
  
    const homeSection = document.getElementById('home');
    homeSection.classList.remove('hidden');
  }
  
  // Get all navigation links and add click event listeners
  const navLinks = document.querySelectorAll('nav a');
  navLinks.forEach(link => {
    link.addEventListener('click', (event) => {
      event.preventDefault(); // Prevent default link behavior
      const sectionId = link.getAttribute('href').substring(1); // Get section id from href attribute
      navigateToSection(sectionId);
    });
  });
  
  // Show only the home section initially when the page loads
  window.addEventListener('load', showHomeOnly);
  