var rating = {};
var dvSelected = false;
var acSelected = false;
var crSelected = false;
var exSelected = false;

var doiBloodhound = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    sufficient: 1,
    remote: {
        url: 'http://api.crossref.org/works/%QUERY',
        wildcard: '%QUERY',
        transform: function(response) {
            var messageType = response["message-type"];
            var messages = response.message;
            if (messageType == "work") {
                messages = [messages];
            }
            for (i=0; i<messages.length; i++) {
                var message = messages[i];
                var item = {};
                rating.doi = message.DOI
                item.doi = message.DOI
                item.title = message.title[0];
                item.authors = [];
                for (j=0; j<message.author.length; j++) {
                    var firstName = message.author[j].given;
                    var lastName = message.author[j].family;
                    item.authors.push(firstName+" "+lastName);
                }
                item.authors = item.authors.join(', ');
                item.date = moment(message.created['date-time']).format('YYYY');
                messages[i] = item;
            }
            return messages;
        }
    }
});

function loading(isLoading) {
    $('#searchButton').attr('disabled', isLoading);
}

function searchByDOI() {
    loading(true);
    var doi = $('#doi').val();
    if (!doi) {
        loading(false);
        return;
    }
    function sync(results) {
        return;
    }
    function async(results) {
        if (results.length > 0) {
            var article = results[0];
            $('#article-title').text(article.title);
            $('#article-authors').text(article.authors);
            $('#inputs').css('visibility', 'visible');
            $('#rate').css('visibility', 'visible');
        } else {
            $('#article-title').text("Could not locate document");
            $('#article-authors').text("Please try again");
            $('#inputs').css('visibility', 'hidden');
            $('#rate').css('visibility', 'visible');
        }
        loading(false);
    }
    doiBloodhound.search(doi, sync, async);
}

function dvRangeUpdated(value) {
    dvSelected = true;
    var slider = $('#dv-slider');
    rating.dv = slider.val()
}
function acRangeUpdated(value) {
    acSelected = true;
    var slider = $('#ac-slider');
    rating.ac = slider.val()
}
function crRangeUpdated(value) {
    crSelected = true;
    var slider = $('#cr-slider');
    rating.cr = slider.val()
}
function exRangeUpdated(value) {
    exSelected = true;
    var slider = $('#ex-slider');
    rating.ex = slider.val()
}

function submitRating() {
    $('#allInputError').hide();
    console.log(rating);
    if (!(dvSelected && acSelected && crSelected && exSelected)) {
        $('#allInputError').show();
    }
}