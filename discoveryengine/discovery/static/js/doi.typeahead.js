var doiBloodhound = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
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
                messages[i] = item
            }
            console.log(messages)
            return messages;
        }
    }
});

$('#doi').typeahead(null, {
    name: 'doi',
    display: 'doi',
    source: doiBloodhound,
    templates: {
        suggestion: Handlebars.compile('<div><strong>{{title}}</strong> - {{authors}}</div>')
    }
});