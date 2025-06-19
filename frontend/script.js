const API_URL = "http://localhost:8000/items";

document.getElementById("todo-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const text = document.getElementById("text").value;
    const description = document.getElementById("description").value;

    const response = await fetch(API_URL, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text, description, is_done: false})
    });

    if (response.ok) {
        document.getElementById("text").value = "";
        document.getElementById("description").value = "";
        loadTodos();
    }
});

async function loadTodos() {
    const res = await fetch(API_URL);
    const todos = await res.json();
    const list = document.getElementById("todo-list");
    list.innerHTML = "";

    todos.forEach(todo => {
        const li = document.createElement("li");
        li.className = todo.is_done ? "done" : "";

        li.innerHTML = `
            <span><strong>${todo.text}</strong> — ${todo.description || ""}</span>
            <div>
                <button onclick="toggleDone(${todo.id}, ${!todo.is_done})">
                    ${todo.is_done ? "Undo" : "Done"}
                </button>
                <button onclick="deleteTodo(${todo.id})">Delete</button>
            </div>
        `;

        list.appendChild(li);
    });
}

async function toggleDone(id, status) {
    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({is_done: status, text: "", description: ""})
    });
    loadTodos();
}

async function deleteTodo(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    loadTodos();
}

window.onload = loadTodos;
