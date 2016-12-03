console.log('loaded bmlet.js');

let doi;

document.getElementsByTagName('meta').forEach( metaTag => {
  const name = metaTag.getAttribute('name');
  if (name === 'citation_doi' || 'prism_doi') {
    console.log('found citation_doi metatag');
    doi = metaTag.getAttribute('content');
    console.log(doi);
  }
});

if (!doi) {
  // pubmed
  document.getElementsByTagName('dd').forEach( ddTag => {
    const doiTag = ddTag.child('a');
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

const url = 'rate.thediscoverengine.org' + '?doi=' + doi;
window.open(url);
