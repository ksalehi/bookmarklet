/*******************
**** SETUP AJAX ****
*******************/
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            var csrftoken = Cookies.get('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
/*******************
***** END SETUP ****
*******************/

var rating = {};
var dvSelected = false;
var acSelected = false;
var crSelected = false;
var exSelected = false;

function resetRating() {
    var rating = {};
    var dvSelected = false;
    var acSelected = false;
    var crSelected = false;
    var exSelected = false;

    $('#dv-slider').val($("#dv-slider").attr("max")/2);
    $('#ac-slider').val($("#ac-slider").attr("max")/2);
    $('#cr-slider').val($("#cr-slider").attr("max")/2);
    $('#ex-slider').val($("#ex-slider").attr("max")/2);

    $('#allInputError').hide();
    $('#ratingSubmitted').hide();
    $('#errorSubmitting').hide();
}

resetRating();

function hideAlerts() {
    $('#allInputError').hide();
    $('#ratingSubmitted').hide();
    $('#errorSubmitting').hide();
}

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

// GET DOI FROM QUERY PARAM
function doiFromQuery() {
    var doi = (location.search.match(new RegExp('doi' + "=(.*?)($|\&)", "i")) || [])[1]
    if (doi != undefined) {
        $('#doi').val(doi);
        searchByDOI();
    }
}
doiFromQuery();

function searchByDOI() {
    loading(true);
    var doi = $('#doi').val();
    if (!doi) {
        loading(false);
        return;
    }
    history.pushState(null, '', '/?doi='+doi);
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
            $('#article-authors').text("Please try again or enter the DOI manually");
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
    hideAlerts();
    if (!(dvSelected && acSelected && crSelected && exSelected)) {
        $('#allInputError').show();
        return;
    }

    $.post('/api/discovery/ratings/', rating, function(data, status, xhr) {
        if (status=="success") {
            $('#ratingSubmitted').show();
        } else {
            $('#errorSubmitting').show();
        }
    });
}
