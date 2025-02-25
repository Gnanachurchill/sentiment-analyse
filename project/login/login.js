function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('login-error');

    // Clear any previous error message
    errorMessage.style.display = 'none';

    // Simulate login check (you could replace this with a real API call)
    const users = [
        { username: 'user1', password: 'password123' },
        { username: 'user2', password: 'password456' }
    ];

    const user = users.find(u => u.username === username && u.password === password);

    if (user) {
        // Successful login, redirect to sentiment analysis page
        window.location.href = 'website.html'; // Redirect to the sentiment analysis page
    } else {
        // Invalid credentials
        errorMessage.style.display = 'block';
    }
}
