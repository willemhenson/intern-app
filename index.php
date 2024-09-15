<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="style.css">
	    <script>
	        let currentSlide = 0;

	        // Function to change the slide
	        function changeSlide(direction) {
	            const slides = document.querySelectorAll('.slide');
	            slides[currentSlide].classList.remove('active'); // Hide current slide

	            // Calculate the new slide index
	            currentSlide = (currentSlide + direction + slides.length) % slides.length;

	            // Show the new slide
	            slides[currentSlide].classList.add('active');
	        }
	    </script>
	</head>
	<body>
		<div class="container">
        	<!-- Arrows for navigation -->
        	<span class="arrow left" onclick="changeSlide(-1)">&#10094;</span>
        	<span class="arrow right" onclick="changeSlide(1)">&#10095;</span>
	        <div class="slide active">
	            <h2>Welcome</h2>
	            <p>Use the arrows to navigate</p>
	        </div>
<?php
// Path to the local file
$filename = './jobs.json';

// Read the file contents
$fileContents = file_get_contents($filename);

// Decode the JSON string into an associative array
$array = json_decode($fileContents, true);

foreach ($array as $element) {
	echo "<div class='slide'>\n";
	echo "<div class='card'>\n";
	echo "<img src=" . $element["Logo"] . ">\n";
	echo "<br>";
	echo "<b>" . $element["Name"] . "</b>\n";
	echo "<br>\n";
	echo "<ul>\n";
	echo "<br>\n";

	echo "<li>Salary: " . $element["Salary"] . "</li>\n";
	echo "<li>Location: " . $element["Location"] . "</li>\n";
	echo "<li>Duration: " . $element["Duration"] . "</li>\n";
	echo "<li>Starting: " . $element["Starting"] . "</li>\n";
	echo "<li><b>Deadline: " . $element["Deadline"] . "</b></li>\n";

	echo "<br>\n";
	echo "</ul>\n";
	echo "<a href=" . $element["Link"] . ">Apply Here</a>\n";
	echo "<br>\n";
	echo "<i>Hosted at: " . $element["Host"] . "</i>\n";
	echo "</div>\n";
	echo "</div>\n";
}
?>
		</div>
	</body>
</html>
