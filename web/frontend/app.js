(() => {
  const emailInput = document.getElementById('email');
  const runBtn = document.getElementById('run');
  const stopBtn = document.getElementById('stop');
  const log = document.getElementById('log');

  let ws = null;

  function appendLine(text) {
    log.textContent += text;
    log.scrollTop = log.scrollHeight;
  }

  runBtn.addEventListener('click', () => {
    const email = emailInput.value.trim();
    if (!email) {
      appendLine('Please enter an email.\n');
      return;
    }

    if (ws && ws.readyState === WebSocket.OPEN) {
      appendLine('Already running.\n');
      return;
    }

    const scheme = location.protocol === 'https:' ? 'wss' : 'ws';
    const url = `${scheme}://${location.host}/ws/search`;
    ws = new WebSocket(url);

    ws.addEventListener('open', () => {
      appendLine(`Starting search for ${email}...\n`);
      ws.send(JSON.stringify({ email }));
      runBtn.disabled = true;
      stopBtn.disabled = false;
    });

    ws.addEventListener('message', (ev) => {
      appendLine(ev.data);
    });

    ws.addEventListener('close', () => {
      appendLine('\nConnection closed.\n');
      runBtn.disabled = false;
      stopBtn.disabled = true;
      ws = null;
    });

    ws.addEventListener('error', (ev) => {
      appendLine('\nWebSocket error\n');
    });
  });

  stopBtn.addEventListener('click', () => {
    if (ws) {
      ws.close();
    }
  });

  // allow enter to run
  emailInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') runBtn.click();
  });
})();
