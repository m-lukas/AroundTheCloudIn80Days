function refresh() {
    tableContent = document.getElementById("table-content")

    awsChecked = document.getElementById("aws-radio").checked
    azureChecked = document.getElementById("azure-radio").checked
    gcpChecked = document.getElementById("gcp-radio").checked

    austriaChecked = document.getElementById("country-at").checked
    belgiumChecked = document.getElementById("country-be").checked
    swissChecked = document.getElementById("country-ch").checked
    germanyChecked = document.getElementById("country-de").checked
    denmarkChecked = document.getElementById("country-dk").checked
    spainChecked = document.getElementById("country-es").checked
    finlandChecked = document.getElementById("country-fi").checked
    franceChecked = document.getElementById("country-fr").checked
    irelandChecked = document.getElementById("country-ie").checked
    italyChecked = document.getElementById("country-it").checked
    netherlandsChecked = document.getElementById("country-nl").checked
    norwayChecked = document.getElementById("country-no").checked
    polandChecked = document.getElementById("country-pl").checked
    swedenChecked = document.getElementById("country-se").checked
    britainChecked = document.getElementById("country-uk").checked

    nuclearChecked = document.getElementById("nuclear").checked

    countries = []
    cloudProvider = ""
    nuclear = false

    tableContent.innerHTML = ""

    if(awsChecked){
        cloudProvider = "AWS"
    }else if(azureChecked){
        cloudProvider = "Azure"
    }else if(gcpChecked){
        cloudProvider = "GCP"
    }

    if(austriaChecked){
        countries.push("AT")
    }
    if(belgiumChecked){
        countries.push("BE")
    }
    if(swissChecked){
        countries.push("CH")
    }
    if(germanyChecked){
        countries.push("DE")
    }
    if(denmarkChecked){
        countries.push("DK")
    }
    if(spainChecked){
        countries.push("ES")
    }
    if(finlandChecked){
        countries.push("FI")
    }
    if(franceChecked){
        countries.push("FR")
    }
    if(irelandChecked){
        countries.push("IE")
    }
    if(italyChecked){
        countries.push("IT")
    }
    if(netherlandsChecked){
        countries.push("NL")
    }
    if(norwayChecked){
        countries.push("NO")
    }
    if(polandChecked){
        countries.push("PL")
    }
    if(swedenChecked){
        countries.push("SE")
    }
    if(britainChecked){
        countries.push("UK")
    }

    if(nuclearChecked){
        nuclear = true
    }

    var xhr = new XMLHttpRequest();
    xhr.open("POST", 'http://127.0.0.1:8000/ranking', true);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function() { // Call a function when the state changes.
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            response = JSON.parse(this.responseText)
            response.forEach(obj => {
                country = obj.country
                percentage = obj.percentage
                provider = obj.cloud_provider
                region = obj.region

                percentage = Number((percentage).toFixed(2));

                if(percentage === 0){
                    percentage = "unknown"
                }else{
                    percentage = `${percentage}%`
                }

                if(provider === "GCP"){
                    provider = "Google Cloud"
                }

                tableContent.innerHTML += `<tr class="alert" role="alert">
						      <th scope="row">${provider}</th>
						      <td>${region}</td>
						      <td>${country}</td>
						      <td>${percentage}</td>
						    </tr>`
            });
        }
    }

    xhr.send(JSON.stringify({
        "countries": countries,
        "cloud_provider": cloudProvider,
        "nuclear_is_green": nuclear
    }));
}

refresh()

