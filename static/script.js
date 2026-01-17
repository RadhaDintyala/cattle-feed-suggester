function sendMessage() {
    let gobar = document.getElementById('gobar').value;
    let eating = document.getElementById('eating').value;
    let activity = document.getElementById('activity').value;
    let milk = document.getElementById('milk').value;
    let temp = document.getElementById('temp').value;
    let dung = document.getElementById('dung').value;
    let body_condition = document.getElementById('body_condition').value;

    if(!gobar || !eating || !activity || !milk || !temp || !dung || !body_condition){
        alert("Please fill all fields!");
        return;
    }

    // Show user input
    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="chat-message user-msg">You: Gobar=${gobar}, Eating=${eating}, Activity=${activity}, Milk=${milk}, Temp=${temp}, Dung=${dung}, Body=${body_condition}</div><div class="clearfix"></div>`;

    // Clear inputs
    document.getElementById('gobar').value = '';
    document.getElementById('eating').value = '';
    document.getElementById('activity').value = '';
    document.getElementById('milk').value = '';
    document.getElementById('temp').value = '';
    document.getElementById('dung').value = '';
    document.getElementById('body_condition').value = '';

    fetch('/get_response', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({gobar, eating, activity, milk, temp, dung, body_condition})
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="chat-message bot-msg">${data.response.replace(/\n/g,"<br>")}</div><div class="clearfix"></div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
