const interval = 1 * 1000; // milliseconds

const dataDiv = document.querySelector('#data');

function showData(response) {
  dataDiv.innerText = JSON.stringify(response, null, 2);
}

function processResponse(response) {
  showData(response);
  setTimeout(loadData, interval);
}

function loadData() {
  fetch('/data/').then(function (response) {
    return response.json();
  }).then(processResponse);
}

loadData();
