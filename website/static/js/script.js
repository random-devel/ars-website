// Add to script.js or <script> tags
document.addEventListener('DOMContentLoaded', () => {
    // Animate terminal prompts on page load
    const prompts = document.querySelectorAll('.prompt:not(.typing)');
    prompts.forEach((prompt, i) => {
    setTimeout(() => {
        prompt.classList.add('typing');
        setTimeout(() => prompt.classList.remove('typing'), 3000);
    }, i * 800);
    });

    // Add blinking cursor effect to inputs
    const inputs = document.querySelectorAll('.terminal-input');
    inputs.forEach(input => {
    const cursor = document.createElement('span');
    cursor.className = 'cursor';
    cursor.innerHTML = '_';
    input.parentNode.insertBefore(cursor, input.nextSibling);
    
    input.addEventListener('focus', () => cursor.style.opacity = '1');
    input.addEventListener('blur', () => cursor.style.opacity = '0');
    });
});