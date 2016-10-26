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

// $('#doi').typeahead(null, {
//     name: 'doi',
//     display: 'doi',
//     source: doiBloodhound,
//     templates: {
//         suggestion: Handlebars.compile('<div><strong>{{title}}</strong> - {{authors}}</div>')
//     }
// });