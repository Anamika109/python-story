async function getDogFact() {
    const response = await fetch("https://dogapi.dog/api/v2/facts");
    const data = await response.json();
    console.log(data);
}


getDogFact();

data = {
    data: []
}

ice = {
    temp: "COLD",
    color: "white"
}

console.log(ice.temp)