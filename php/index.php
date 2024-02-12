<?php
$connection = new mysqli("mysql", "root", "password", "information_schema");

$query = "SELECT * FROM CHARACTER_SETS";
$result = $connection->query($query);

echo "<ul>";
while($row = $result->fetch_assoc()) {
    echo "<li>" . $row['CHARACTER_SET_NAME'] . " - " . $row['DEFAULT_COLLATE_NAME'] . "</li>";
}
echo "</ul>";

$connection->close();
?>

