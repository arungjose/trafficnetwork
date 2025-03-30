function searchLocation() {
    var location = document.getElementById("location").value.trim().toLowerCase();
    var validLocations = ["kayamkulam", "nooranad", "pandalum"];
    if (validLocations.includes(location)) {
        document.getElementById("cameraButtons").style.display = "block";
    } else {
        alert("Invalid location! Please enter Kayamkulam, Nooranad, or Pandalum.");
        document.getElementById("cameraButtons").style.display = "none";
    }
}

function showCamera(camera) {
    document.getElementById("cameraView").style.display = "block";
    document.getElementById("cameraFeed").src = "camera_feed.html?camera=" + camera;
    loadTableData();
}

function loadTableData() {
    var tableBody = document.getElementById("tableBody");
    tableBody.innerHTML = "";
    var data = [
        { time: "08:00 AM", count: 20 },
        { time: "09:00 AM", count: 35 },
        { time: "10:00 AM", count: 40 }
    ];
    data.forEach(function(row) {
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + row.time + "</td><td>" + row.count + "</td>";
        tableBody.appendChild(tr);
    });
}