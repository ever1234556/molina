// Simple efecto de "latido" al pasar el mouse por el corazón
const heart = document.querySelector('.heart');

heart.addEventListener('mouseenter', () => {
    heart.style.animationPlayState = 'paused';
});

heart.addEventListener('mouseleave', () => {
    heart.style.animationPlayState = 'running';
});