'use strict';

console.log('loaded bmlet.js');

let doi;

Array.from(document.getElementsByTagName('meta')).forEach( metaTag => {
  let name = metaTag.getAttribute('name');
  if (name === ('citation_doi' || 'prism_doi')) {
    console.log('found citation_doi metatag');
    doi = metaTag.getAttribute('content');
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
        console.log('found dd / a tag');
        console.log(doi);
      }
    }
  });
}

console.log('this is updating!');

let url = 'http://rate.thediscoveryengine.org' + '?doi=' + doi;
window.open(url);
