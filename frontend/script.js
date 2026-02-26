const video = document.getElementById("camera");

let emotionInterval;

// Start camera
async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: true,
            audio: true
        });
        video.srcObject = stream;

        // Start emotion detection loop
        startEmotionDetection();

    } catch (err) {
        console.error("Camera error:", err);
        alert("Camera permission denied!");
    }
}

// Capture frame & send to backend
function startEmotionDetection() {
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    emotionInterval = setInterval(async () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0);

        const imageData = canvas.toDataURL("image/jpeg");

        try {
            const response = await fetch("http://127.0.0.1:8000/detect-emotion/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ image: imageData })
            });

            const data = await response.json();
            document.getElementById("emotionLabel").innerText =
                "Current Emotion: " + data.emotion;

        } catch (error) {
            console.error("Emotion API error:", error);
        }

    }, 3000); // every 3 seconds (optimized for performance)
}

// Upload Resume
async function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch("http://127.0.0.1:8000/upload-resume/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    alert("Detected Skills: " + data.detected_skills);
}

// Start Interview
async function startInterview() {
    await startCamera();

    const response = await fetch("http://127.0.0.1:8000/start-interview/", {
        method: "POST"
    });

    const data = await response.json();
    console.log(data);
    alert("AI Interview Started!");
}