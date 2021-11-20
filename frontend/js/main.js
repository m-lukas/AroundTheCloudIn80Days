awsField = document.getElementById("aws-radio")
azureField = document.getElementById("azure-radio")
gcpField = document.getElementById("gcp-radio")

austriaField = document.getElementById("country-at")
belgiumField = document.getElementById("country-be")
swissField = document.getElementById("country-ch")
germanyField = document.getElementById("country-de")
denmarkField = document.getElementById("country-dk")
spainField = document.getElementById("country-es")
finlandField = document.getElementById("country-fi")
franceField = document.getElementById("country-fr")
irelandField = document.getElementById("country-ie")
italyField = document.getElementById("country-it")
netherlandsField = document.getElementById("country-nl")
norwayField = document.getElementById("country-no")
polandField = document.getElementById("country-pl")
swedenField = document.getElementById("country-se")
britainField = document.getElementById("country-uk")

nuclearField = document.getElementById("nuclear")

function refresh() {
    tableContent = document.getElementById("table-content")
    timestampField = document.getElementById("timestamp-field")

    awsChecked = awsField.checked
    azureChecked = azureField.checked
    gcpChecked = gcpField.checked

    austriaChecked = austriaField.checked
    belgiumChecked = belgiumField.checked
    swissChecked = swissField.checked
    germanyChecked = germanyField.checked
    denmarkChecked = denmarkField.checked
    spainChecked = spainField.checked
    finlandChecked = finlandField.checked
    franceChecked = franceField.checked
    irelandChecked = irelandField.checked
    italyChecked = italyField.checked
    netherlandsChecked = netherlandsField.checked
    norwayChecked = norwayField.checked
    polandChecked = polandField.checked
    swedenChecked = swedenField.checked
    britainChecked = britainField.checked

    nuclearChecked = nuclearField.checked

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
            timestamp = response.timestamp
            data = response.data

            timestampField.innerHTML = timestamp

            data.forEach(obj => {
                country = obj.country
                percentage = obj.percentage
                provider = obj.cloud_provider
                region = obj.region

                percentage = Number((percentage).toFixed(2));

                fontColorClass = ""

                if(percentage >= 95){
                    fontColorClass = "percentage-95"
                }else if(percentage >= 80){
                    fontColorClass = "percentage-80"
                }else if(percentage >= 70){
                    fontColorClass = "percentage-70"
                }else if(percentage >= 60){
                    fontColorClass = "percentage-60"
                }else if(percentage >= 50){
                    fontColorClass = "percentage-50"
                }else if(percentage >= 40){
                    fontColorClass = "percentage-40"
                }else if(percentage >= 30){
                    fontColorClass = "percentage-30"
                }else if(percentage >= 20){
                    fontColorClass = "percentage-20"
                }else if(percentage >= 10){
                    fontColorClass = "percentage-10"
                }else if(percentage > 0){
                    fontColorClass = "percentage-0"
                }else{
                    fontColorClass = "percentage-unknown"
                }

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
						      <td class="${fontColorClass} font-weight-bold">${percentage}</td>
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

