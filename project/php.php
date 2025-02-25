<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input fields
    $suspectName = $_POST['suspect_name'];
    $crimeDetails = $_POST['crime_details'];
    $suspectDetails = $_POST['suspect_details'];
    
    // Handle image upload
    if (isset($_FILES['suspect_images']) && $_FILES['suspect_images']['error'] == 0) {
        $targetDir = "uploads/";
        $targetFile = $targetDir . basename($_FILES["suspect_images"]["name"]);
        
        // Move the uploaded image to the server directory
        if (move_uploaded_file($_FILES["suspects_image"]["tmp_name"], $targetFile)) {
            echo "The file has been uploaded.";
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }

    // Insert data into the database (this assumes you have set up a database connection)
    $conn = new mysqli("localhost", "username", "password", "suspect_db");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $stmt = $conn->prepare("INSERT INTO suspects (name, crime_details, suspect_details, image_path) VALUES (?, ?, ?, ?)");
    $stmt->bind_param("ssss", $suspectName, $crimeDetails, $suspectDetails, $targetFile);
    $stmt->execute();
    
    echo "Suspect details saved successfully!";
    $stmt->close();
    $conn->close();
}
?>
