window.addEventListener('scroll', function() {
    var sections = document.getElementsByTagName('section');
    var currentPosition = window.pageYOffset;
    
    for (var i = 0; i < sections.length; i++) {
      var section = sections[i];
      var sectionTop = section.offsetTop;
      
      if (currentPosition >= sectionTop && currentPosition < sectionTop + section.offsetHeight) {
        section.classList.add('active');
      } else {
        section.classList.remove('active');
      }
    }
  });
  