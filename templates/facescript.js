const videoElement = document.getElementById('video');
const startButton = document.getElementById('startButton');

// Access the user's webcam
navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
        videoElement.srcObject = stream;
    })
    .catch(function (error) {
        console.error('Error accessing the webcam: ' + error);
    });
