'use strict';

console.log('Welcome to the Discovery Engine via the amazing bookmarklet! Please email feedback@thediscoveryengine.org with any suggestions!');

function perform() {
  let doi;
  const possibleDoiTagNames = {
    'citation_doi': true,
    'prism_doi': true,
    'dc.identifier.doi': true,
    'bepress_citation_doi': true,
    'ppl.doi': true,
    'doi': true
  };

  Array.from(document.getElementsByTagName('meta')).forEach( metaTag => {
    let tagName = metaTag.getAttribute('name');
    if (possibleDoiTagNames[tagName]) {
      doi = metaTag.getAttribute('content');
    }
  });

  if (!doi) {
    /*** CUSTOM SITE PARSERS ***/
    // PubMed
    if (window.location.hostname === 'www.ncbi.nlm.nih.gov') {
      console.log('PubMed custom parser');
      const ddTags = document.getElementsByTagName('dd');
      doi = ddTags[1].childNodes[0].innerText;
    } else {
      doi = 'DOI_NOT_FOUND';
    }
  }

  console.log(doi);
  let url = 'http://rate.thediscoveryengine.org' + '?doi=' + doi;
  var result = window.open(url);
  if (result === undefined) {
    showPopupMessage(doi);
  }
}

function showPopupMessage(doi) {
  let template = ' \
    <div id="deBookmarkletPopupBlocker" style="position: absolute; top: 0; right: 0; left: 0; background: #FF3366; color: white; text-align: center; padding: 10px;"> \
      <img src="http://rate.thediscoveryengine.org/static/img/favicon.png" /> \
      <span>Please disable your popup blocker for the bookmarklet to work. Click <a href="http://rate.thediscoveryengine.org/?doi='+doi+'" target="_blank">here</a> to rate this paper.</span> \
    </div> \
  '

  var container = document.createElement('div');
  container.innerHTML = template;
  var popupMessage = container.firstChild
  document.getElementsByTagName('body')[0].appendChild(popupMessage);

  setTimeout(function() {
    popupMessage.style.display = 'none';
  }, 10000);
}

perform();
