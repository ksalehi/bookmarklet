'use strict';

console.log('loaded bookmarklet');

let doi;

Array.from(document.getElementsByTagName('meta')).forEach( metaTag => {
  let name = metaTag.getAttribute('name');
  if (name === ('citation_doi' || 'prism_doi')) {
    doi = metaTag.getAttribute('content');
    console.log('found doi metatag:');
    console.log(doi);
  }
});

if (!doi) {
  // pubmed
  Array.from(document.getElementsByTagName('dd')).forEach( ddTag => {
    let doiTag = ddTag.child('a');
    if (doiTag) {
      if (doiTag.getAttribute('ref') === 'aid_type=doi') {
        doi = doiTag.getAttribute('href');
        console.log('found pubmed doi:');
        console.log(doi);
      }
    }
  });
}

let url = 'http://rate.thediscoveryengine.org' + '?doi=' + doi;
window.open(url);
