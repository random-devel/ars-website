document.addEventListener('DOMContentLoaded', function() {
  // Terminal typing effect
  const prompts = document.querySelectorAll('.typing');
  prompts.forEach(prompt => {
    const text = prompt.textContent;
    prompt.textContent = '';
    let i = 0;
    const typing = setInterval(() => {
      if (i < text.length) {
        prompt.textContent += text.charAt(i);
        i++;
      } else {
        clearInterval(typing);
        // Add cursor after typing completes
        const cursor = document.createElement('span');
        cursor.className = 'cursor';
        cursor.textContent = '_';
        prompt.appendChild(cursor);
      }
    }, 100);
  });

  // Terminal command interaction
  const terminalInputs = document.querySelectorAll('.terminal-input');
  terminalInputs.forEach(input => {
    input.addEventListener('keyup', function(e) {
      if (e.key === 'Enter') {
        const command = this.value.trim();
        this.value = '';

        // Create new prompt line
        const newPrompt = document.createElement('div');
        newPrompt.className = 'prompt';
        newPrompt.innerHTML = `<span class="prompt-prefix">root@ars-sec:~$</span> ${command}`;

        // Create response
        const response = document.createElement('div');
        response.className = 'response';

        // Process commands
        if (command === 'clear') {
          document.querySelector('.terminal-body').innerHTML = '';
          return;
        } else if (command === 'help') {
          response.innerHTML = `> Available commands: clear, help, contact, services, status`;
        } else if (command === 'contact') {
          response.innerHTML = `> Redirecting to contact page...<meta http-equiv="refresh" content="2;url=/contact">`;
        } else if (command === 'services') {
          response.innerHTML = `> PENETRATION TESTING<br>> RED TEAM OPERATIONS<br>> SECURITY TRAINING`;
        } else if (command === 'status') {
          response.innerHTML = `> SYSTEM STATUS: OPERATIONAL<br>> THREAT LEVEL: ELEVATED`;
        } else {
          response.innerHTML = `> Command not found: ${command}`;
        }

        // Append to terminal
        const terminalBody = document.querySelector('.terminal-body');
        terminalBody.appendChild(newPrompt);
        terminalBody.appendChild(response);

        // Scroll to bottom
        terminalBody.scrollTop = terminalBody.scrollHeight;
      }
    });
  });

  // Product quantity controls
  const quantityControls = document.querySelectorAll('.quantity-control');
  quantityControls.forEach(control => {
    const minus = control.querySelector('.quantity-minus');
    const plus = control.querySelector('.quantity-plus');
    const input = control.querySelector('.quantity-input');

    minus.addEventListener('click', () => {
      let value = parseInt(input.value);
      if (value > 1) {
        input.value = value - 1;
      }
    });

    plus.addEventListener('click', () => {
      let value = parseInt(input.value);
      input.value = value + 1;
    });
  });

  // Certificate verification
  const verifyButtons = document.querySelectorAll('.verify-btn');
  verifyButtons.forEach(button => {
    button.addEventListener('click', function() {
      const certId = this.getAttribute('data-cert-id');
      const verificationResult = document.querySelector(`#verification-${certId}`);

      // Simulate verification
      verificationResult.innerHTML = '<span class="status status-online"></span> Verifying...';

      setTimeout(() => {
        verificationResult.innerHTML = `
          <span class="status status-online"></span>
          VERIFIED: ${certId.toUpperCase()}
          <br>ISSUER: OFFENSIVE SECURITY
          <br>DATE: 2023-01-15
        `;
      }, 1500);
    });
  });

  // Animate cards on scroll
  const animateOnScroll = () => {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
      const cardPosition = card.getBoundingClientRect().top;
      const screenPosition = window.innerHeight / 1.3;

      if (cardPosition < screenPosition) {
        card.style.opacity = '1';
        card.style.transform = 'translateY(0)';
      }
    });
  };

  // Initialize cards for animation
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = 'all 0.6s ease';
  });

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll(); // Run once on load
});