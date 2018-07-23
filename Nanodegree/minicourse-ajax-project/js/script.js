
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview

    // YOUR CODE GOES HERE!
    var streetStr = $("#street").val();
    var cityStr = $("#city").val();
    var address = streetStr + ", " + cityStr

    var locationUrl = "http://maps.googleapis.com/maps/api/streetview?size=600x300&location=" + address

    $greeting.text('So, you want to live at ' + address + '?');

    $body.append('<img class="bgimg" src="' + locationUrl + '">')
    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
      'api-key': "7dee1b89aeff4714b7fc2ad32349f200",
      'q': cityStr
    });

    $nytHeaderElem.text("New York Times Articles About " + cityStr)

    $.getJSON( url, function( data ) {
        console.log(data);
        var items = [];
        data.response.docs.forEach(function( e ) {
            $nytElem.append(
                '<li class="article"> <a href="' + e.web_url + '">' + e.headline.main + '</a>' + '<p>' + e.snippet + '</p></li>');
            console.log(e.web_url);
        })
    })
    .fail(function() {
        $nytHeaderElem.text("New York Times Articles Could Not Be Loaded")
    });


    var wikiRequestTimeout = setTimeout(function(){
        $wikiElem.text("failed to get wikipedia resources");
    }, 8000);
    $.ajax({
        url: 'https://en.wikipedia.org/w/api.php?action=opensearch&search=' + cityStr,
        dataType: 'jsonp',
        success: function(data){
            console.log(data);
            var resultsNum = data[1].length;
            var links = data[3];
            var titles = data[1];
            for (i = 0; i < resultsNum; i++) {
                $wikiElem.append(
                '<li> <a href="' + links[i] + '">' + titles[i] + "</a></li>");
            };

            clearTimeout(wikiRequestTimeout);
        }
    });

    return false;
};

$('#form-container').submit(loadData);
