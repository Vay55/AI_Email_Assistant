function setLoading(isLoading) {
  const buttons = document.querySelectorAll("button");

  buttons.forEach(btn => {
    btn.disabled = isLoading;
  });

  const output = document.getElementById("output");
  if (isLoading) {
    output.innerText = "⏳ Loading...";
  }
}

async function summarize() {
  const text = document.getElementById("email").value;
  const output = document.getElementById("output");

  if (!text) {
  document.getElementById("output").innerText = "⚠️ Please enter an email first.";
  return;
}

  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:5000/summarize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    output.innerText = data.result;

  } catch (error) {
    output.innerText = "❌ Error connecting to server.";
  }

  setLoading(false);
}


async function reply() {
  const text = document.getElementById("email").value;
  const output = document.getElementById("output");

  if (!text) {
  document.getElementById("output").innerText = "⚠️ Please enter an email first.";
  return;
}

  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:5000/reply", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    });

    const data = await res.json();
    output.innerText = data.result;

  } catch (error) {
    output.innerText = "❌ Error: Could not connect to server.";
  }

  setLoading(false);
}

async function intent() {
  const text = document.getElementById("email").value;
  const output = document.getElementById("output");

  if (!text) {
  document.getElementById("output").innerText = "⚠️ Please enter an email first.";
  return;
}

  setLoading(true);

  output.innerText = "⏳ Loading...";

  const res = await fetch("http://127.0.0.1:5000/intent", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  output.innerText = data.result;

  setLoading(false);
}

async function urgency() {
  const text = document.getElementById("email").value;
  const output = document.getElementById("output");

  if (!text) {
  document.getElementById("output").innerText = "⚠️ Please enter an email first.";
  return;
}

  setLoading(true);

  output.innerText = "⏳ Loading...";

  const res = await fetch("http://127.0.0.1:5000/urgency", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  output.innerText = data.result;

  setLoading(false);
}

async function improve() {
  const text = document.getElementById("email").value;
  const output = document.getElementById("output");

  if (!text) {
  document.getElementById("output").innerText = "⚠️ Please enter an email first.";
  return;
}

  setLoading(true);

  output.innerText = "⏳ Loading...";

  const res = await fetch("http://127.0.0.1:5000/improve", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text })
  });

  const data = await res.json();
  output.innerText = data.result;
  
  setLoading(false);
}

async function useLast() {
  const textarea = document.getElementById("email");
  const output = document.getElementById("output");

  setLoading(true);

  try {
    const res = await fetch("http://127.0.0.1:5000/last");
    const data = await res.json();

    if (data.result === "No previous output found.") {
      output.innerText = data.result;
    } else {
      textarea.value = data.result;
      output.innerText = "✅ Loaded last output into input.";
    }

  } catch (error) {
    output.innerText = "❌ Error fetching last output.";
  }

  setLoading(false);
}