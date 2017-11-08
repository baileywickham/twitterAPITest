var OAuth = require('oauth');
var fs = require('fs');
// keys for oauth
var CONSUMER_KEY = 'KCpd1MjS4AKTh2vS0poWq9Plp';
var CONSUMER_SECRET = 'EJYRMJRg1tGDvemYJsf1ou9jgcvEP8zRVnL66VJisRn0yBldf3';
var ACCESS_TOKEN = '2751102888-8HKrPfo6zfBc4vwhD0qGRzl0O1XnE8HhkL2cWuM';
var ACCESS_TOKEN_SECRET = 'F7Vw2Qf40DUpmfUqlbc5Wtrv5ZQJtNBB7mRcDnkmpJv9C';



// Instantiate the client
var twitterClient = new OAuth.OAuth(
    'https://api.twitter.com/oauth/request_token',
    'https://api.twitter.com/oauth/access_token',
    CONSUMER_KEY,
    CONSUMER_SECRET,
    '1.0A',
    null,
    'HMAC-SHA1'
);


//request

var ID = ['753783025712771072']; //tweet id
var URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=jackwarszalek&count=199&incude_rts=false';
twitterClient.get( 
    URL,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    function (err, data, res) {
        if (err) {
            console.log(err);
            return; //error logging
        }
        if (res.statusCode != 200) {
            console.log('Got non 200 status: ', res.statusCode);
            return; //url status code
        }

        var obj = JSON.parse(data);
	
	for (var i = 0; i < obj.length; i++) {
	    fs.appendFile("tmp/log", JSON.stringify(obj[i].text, "", 2), function(err) {
		    if (err) {
			return console.log(err);
		    }
		    console.log("success");

		i++;
		});
	    }	     
});
