document.addEventListener('DOMContentLoaded', () => {
  const helloElement = document.getElementById('hello');

  const fetchHello = async () => {
    try {
      const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
      const data = await response.json();
      const helloText = data.hello;
      helloElement.textContent = helloText;
    } catch (error) {
      console.error('Error fetching hello:', error);
    }
  };

  fetchHello();
});
