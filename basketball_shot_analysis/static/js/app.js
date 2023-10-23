## static/js/app.js

// Function to handle file upload
function handleFileUpload() {
  // Get the file input element
  const fileInput = document.getElementById("file");

  // Check if a file is selected
  if (fileInput.files.length > 0) {
    // Get the selected file
    const file = fileInput.files[0];

    // Create a FormData object
    const formData = new FormData();

    // Append the file to the FormData object
    formData.append("file", file);

    // Send a POST request to the API endpoint
    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // Display the video analysis page
        showAnalysis(data.video_id);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
}

// Function to display the video analysis page
function showAnalysis(videoId) {
  // Hide the upload video form
  const uploadForm = document.getElementById("upload-form");
  uploadForm.style.display = "none";

  // Show the video analysis page
  const analysisPage = document.getElementById("analysis-page");
  analysisPage.style.display = "block";

  // Send a POST request to the API endpoint to analyze the video
  fetch("/analyze", {
    method: "POST",
    body: JSON.stringify({ video_id: videoId }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      // Display the analysis results
      displayAnalysis(data.analyzed_shots);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Function to display the analysis results
function displayAnalysis(shots) {
  // Display the accuracy chart
  const accuracyChart = document.getElementById("accuracy-chart");
  // Generate the accuracy chart using Chart.js
  // ...

  // Display the angle chart
  const angleChart = document.getElementById("angle-chart");
  // Generate the angle chart using Chart.js
  // ...

  // Display the trajectory chart
  const trajectoryChart = document.getElementById("trajectory-chart");
  // Generate the trajectory chart using Chart.js
  // ...
}

// Event listener for file upload
const fileInput = document.getElementById("file");
fileInput.addEventListener("change", handleFileUpload);
