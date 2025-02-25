<?php
// Assuming you have already established a MySQL connection ($conn)
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $suspectName = $_POST['suspect_name'];
    $crimeDetails = $_POST['crime_details'];
    $suspectDetails = $_POST['suspect_details'];

    // Insert suspect details into the suspects table
    $sql = "INSERT INTO suspects (suspect_name, crime_details, suspect_details) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $suspectName, $crimeDetails, $suspectDetails);
    $stmt->execute();
    $suspectId = $stmt->insert_id; // Get the inserted suspect ID

    // Handle image upload
    if (isset($_FILES['suspect_image']) && $_FILES['suspect_image']['error'] == 0) {
        $imageTmpName = $_FILES['suspect_image']['tmp_name'];
        $imageName = basename($_FILES['suspect_image']['name']);
        $imagePath = 'uploads/suspect_images/' . $imageName;

        // Move the uploaded image to the designated folder
        if (move_uploaded_file($imageTmpName, $imagePath)) {
            // Insert image details into suspect_images table
            $sql = "INSERT INTO suspect_images (suspect_id, image_path) VALUES (?, ?)";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("is", $suspectId, $imagePath);
            $stmt->execute();
        }
    }

    // Redirect or show success message
    echo "Suspect submitted successfully!";
}
?>
