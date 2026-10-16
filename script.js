async function getDogFact() {
    document.getElementById("facts").textContent = "Loading..."
    const response = await fetch("https://dogapi.dog/api/v2/facts");
    const data = await response.json();
    // console.log(data);
    const fact = data.data[0].attributes.body;
    document.getElementById("facts").textContent = fact
    // console.log(data)
    // console.log(fact)   
}








































































// getDogFact();

// const stuff = {data: [
//     {id:"4487fc9c-5f20-4b07-af4b-5a02662e78ce",type:"fact",
        
//         attributes:
//     {body:"Chocolate contains a substance known as theobromine (similar to caffeine) which can kill dogs or, at the very least, make them violently ill."}
// }]};
// console.log(stuff.data)

// console.log(stuff.data[0].type)

// ice = {
//     temp: ["hair", {country: "canada"}],
//     color: "white"
// }

// console.log(ice.temp[1].country)