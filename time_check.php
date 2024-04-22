<?php

$url = 'http://localhost:5000/get_time';

$response = file_get_contents($url);
$data = json_decode($response, true);
$time = $data['time'];

echo "Current time is: " . $time;

?>