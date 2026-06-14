document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("content").style.display = "none";
});

function updateTowns() {
    const district = document.getElementById("district").value;
    const townSelect = document.getElementById("town");


    townSelect.innerHTML = '<option selected disabled>Choose a Town</option>';
    townSelect.disabled = true; 

    const towns = {
        trivandrum: [
            { value: "neyyattinkara", name: "Neyyattinkara" },
            { value: "nedumangad", name: "Nedumangad" }
        ],
        kollam: [
            { value: "karunagappally", name: "Karunagappally" },
            { value: "kottarakkara", name: "Kottarakkara" },
            { value: "punalur", name: "Punalur" }
        ],
        alappuzha: [
            { value: "kayamkulam", name: "Kayamkulam" },
            { value: "cherthala", name: "Cherthala" }
        ]
    };

    if (district && towns[district]) {
        towns[district].forEach(town => {
            const option = document.createElement("option");
            option.value = town.value;
            option.textContent = town.name;
            townSelect.appendChild(option);
        });
        townSelect.disabled = false;
    }
}
function playVideo() {
    const lane = document.getElementById("lane").value;
    const video = document.getElementById("trafficVideo");
    
    console.log(lane)

    if (lane === "lane1") {
        video.src = "./Footage/Lane1.mp4"; 
        video.play();
    }
    else if (lane === "lane2") {
        video.src = "./Footage/Lane2.mp4"; 
        video.play();
    }
    else if (lane === "lane3") {
        video.src = "./Footage/Lane3.mp4"; 
        video.play();
    }
    else if (lane === "lane4") {
        video.src = "./Footage/Lane4.mp4"; 
        video.play();
    }
    else {
        alert("Couldn't find that lane!")
    }
}

function showContent() {
    const district = document.getElementById("district").value;
    const town = document.getElementById("town").value;

    if (district && town) {
        document.getElementById("content").style.display = "flex"; 
    } else {
        document.getElementById("content").style.display = "none"; 
    }
}

function updateLaneDeltas() {
    console.log("Should work now")
    function generateRandomDelta() {
        return Math.floor(Math.random() * (120 - 35 + 1)) + 35;
    }

    function updateDeltas() {
        document.getElementById("laneone").textContent = generateRandomDelta();
        document.getElementById("lanetwo").textContent = generateRandomDelta();
        document.getElementById("lanethree").textContent = generateRandomDelta();
        document.getElementById("lanefour").textContent = generateRandomDelta();
    }
    updateDeltas()
    setInterval(updateDeltas, 8000); 
}

let trafficLightRunning = false;

function cycleTrafficLights() {
    if (trafficLightRunning) return; // Prevent multiple instances
    trafficLightRunning = true;

    function getRandomTime() {
        return Math.floor(Math.random() * (15 - 8 + 1)) + 8;
    }

    function changeLightSequence() {
        let greenTime = getRandomTime() * 1000;
        let redTime = getRandomTime() * 1000;
        let yellowTime = 3000; // Yellow always 3s
        let isGreenToRed = true; // Direction flag: true for Green → Red, false for Red → Green

        console.log(`Green: ${greenTime / 1000}s, Red: ${redTime / 1000}s`);

        function changeLight(color) {
            console.log(`Changing to ${color}`);

            // Reset all lights
            document.getElementById("goLight").className = "bulb";
            document.getElementById("slowLight").className = "bulb";
            document.getElementById("stopLight").className = "bulb";
            // Remove any inline styles if they were set previously
            document.getElementById("goLight").style.background = "";
            document.getElementById("slowLight").style.background = "";
            document.getElementById("stopLight").style.background = "";

            // Turn on the selected light
            if (color === "green") {
                document.getElementById("goLight").classList.add("green-active");
                setTimeout(() => changeLight("yellow"), greenTime);
            } else if (color === "yellow") {
                document.getElementById("slowLight").classList.add("yellow-active");
                setTimeout(() => {
                    if (isGreenToRed) {
                        changeLight("red"); // Green → Yellow → Red
                    } else {
                        changeLight("green"); // Red → Yellow → Green
                    }
                }, yellowTime);
            } else if (color === "red") {
                document.getElementById("stopLight").classList.add("red-active");
                setTimeout(() => {
                    isGreenToRed = !isGreenToRed; // Toggle direction
                    changeLight("yellow");
                }, redTime);
            }
        }

        changeLight("green"); // Start with Green
    }

    changeLightSequence();
}
