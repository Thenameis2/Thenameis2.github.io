
  // Sample image URLs
const imageUrls = [
    "IMG_5949.jpg",
    'Headshot.JPG',
    'IMG_5865.jpg',
    'IMG_5949.jpg',
    'jeopardy.png',
    'path/to/image6.jpg',
    'path/to/image7.jpg',
    'path/to/image8.jpg',
    // Add more image URLs here
  ];
  
  // Function to create gallery images
  function createGallery() {
    const galleryElement = document.getElementById('gallery');
  
    imageUrls.forEach((url, index) => {
      const imageElement = document.createElement('img');
      imageElement.src = url;
      imageElement.className = 'image';
  
      // Add event listener for image click
      imageElement.addEventListener('click', () => {
        // Add your custom logic here for image click event
        console.log(`Image clicked: ${url}`);
      });
  
      // Set initial rotation angle for each image
      const angle = (index / imageUrls.length) * 360;
      imageElement.style.transform = `rotateY(${angle}deg) translateZ(100px)`;
  
      galleryElement.appendChild(imageElement);
    });
  }
  
  // Call the createGallery function when the page loads
  window.addEventListener('load', createGallery);
  