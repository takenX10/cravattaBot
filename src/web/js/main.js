
eel.expose(message_received);
function message_received(msg, autoscroll) {
    var body = document.getElementById('body');
    var newp = document.createElement('p');
    newp.setAttribute('class','msg')
    var today = new Date();
    var time = '['+today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds()+'] - ';
    newp.innerText = time+msg;
    var newdiv = document.createElement('div');
    newdiv.setAttribute('class','div-msg');
    newdiv.appendChild(newp);
    body.appendChild(newdiv);
    if(autoscroll == true){
        window.scrollTo(0,document.body.scrollHeight);
    }
    console.log(msg);
}

  