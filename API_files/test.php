#!/usr/bin/php
<?php


$jsonFile = fopen("MenShirtsReady.json", "r") or die("Unable to open file!");
$jsonText = fread($jsonFile, filesize("MenShirtsReady.json"));
var_dump(json_decode($jsonText));

