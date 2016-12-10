'use strict';

console.log('loaded bookmarklet');

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
  // can flesh this section out with any specific sites that don't store doi metatags
  // just implementing for pubmed for now
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
