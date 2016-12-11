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
      const ddTags = document.getElementsByTagName('dd');
      doi = ddTags[1].childNodes[0].innerText;
      console.log('pubmed doi:');
      console.log(doi);
    } else {
      doi = 'DOI_NOT_FOUND';
    }
  }

  let url = 'http://rate.thediscoveryengine.org' + '?doi=' + doi;
  window.open(url);
}

perform();
