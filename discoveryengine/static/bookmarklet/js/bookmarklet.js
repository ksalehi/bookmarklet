'use strict';

console.log('Welcome to the Discovery Engine via the amazing bookmarklet! Please email feedback@thediscoveryengine.org with any suggestions!');

function DE_BOOKMARKLET_perform() {
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
    DE_BOOKMARKLET_showPopupMessage(doi);
  }
}

function DE_BOOKMARKLET_showPopupMessage(doi) {
  let template = ' \
    <div id="deBookmarkletPopupBlocker" style="position: fixed; top: 0; right: 0; left: 0; background: #FF3366; color: white; text-align: center; padding: 10px; z-index: 1001; display: flex; flex-direction: horizontal; align-items: center; justify-content: center;"> \
      <img src="http://rate.thediscoveryengine.org/static/img/logo_white.png" style="width: 24px; margin-right: 5px;" /> \
      <span style="margin-right: 5px;">Please disable your popup blocker and refresh the page for the bookmarklet to work. Click <a href="http://rate.thediscoveryengine.org/?doi='+doi+'" target="_blank" style="color: #163158; font-weight: bold; text-decoration: underline;">here</a> to rate this paper.</span> \
      <small><a href="#" onclick="DE_BOOKMARKLET_closePopup()" style="color: #163158">Close</a></small> \
    </div> \
  '

  if (document.getElementById('deBookmarkletPopupBlocker')) {
    document.getElementById('deBookmarkletPopupBlocker').style.display = 'flex';
  } else {
    var container = document.createElement('div');
    container.innerHTML = template;
    document.getElementsByTagName('body')[0].appendChild(container);
  }

  setTimeout(DE_BOOKMARKLET_closePopup, 10000);
}

function DE_BOOKMARKLET_closePopup() {
  document.getElementById('deBookmarkletPopupBlocker').style.display = 'none';
}

DE_BOOKMARKLET_perform();
