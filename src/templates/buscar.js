import axios from "axios";

const options = {
  method: 'GET',
  url: 'https://ryanair-all-api.p.rapidapi.com/',
  headers: {
    'X-RapidAPI-Key': '6ae587a3bdmsh021d9a94bcaf13bp14ef7ejsn146886682b43',
    'X-RapidAPI-Host': 'ryanair-all-api.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});