/**
 * WEBSITE: https://themefisher.com
 * TWITTER: https://twitter.com/themefisher
 * FACEBOOK: https://www.facebook.com/themefisher
 * GITHUB: https://github.com/themefisher/
 */

const itemsContainerSelector = 'sliderItemsContainer';

const getItemTemplate = ({
   name,
   tlg,
   tlg_link,
   tlg_percent,
   worker,
   worker_link,
   worker_percent
}) => parseInt(tlg) || parseInt(worker) ? `
    <h3 class="text-white ml-2">Supporting IBC by ${name} society</h3>
    ${parseInt(worker) ?
    `<p class="text-muted ml-4"><a href="${worker_link}" target="_blank">${worker} token holders</a></p>
    <div class="progress mb-4">
      <div class="progress-bar bg-warning" role="progressbar" style="width: ${worker_percent}%" aria-valuenow="${worker_percent}" aria-valuemin="0" aria-valuemax="100"></div>
    </div>` : ''}
    ${parseInt(tlg) ?
    `<div class="progress mb-3">
      <div class="progress-bar bg-warning" role="progressbar" style="width: ${tlg_percent}%" aria-valuenow="${tlg_percent}" aria-valuemin="0" aria-valuemax="100"></div>
    </div>
    <p class="text-muted ml-4"><a href="${tlg_link}" target="_blank">${tlg} telegram members</a></p>` : ''}
` : null;

function setData(data) {
  Object.keys(data).map((item) => {
    const elementInner = getItemTemplate({ name: item, ...data[item] });
    const element = document.createElement('div');
    element.innerHTML = elementInner;
    document.getElementById(itemsContainerSelector).appendChild(element);
  });
}

function setError(error) {
  console.error('err', error); // add some visible message
}

function getData() {
  fetch('http://81.200.148.147:8888/ibc_voting_data')
    .then(response=> response.json())
    .then(json => setData(json))
    .catch(result => setError(result));
}

window.addEventListener('load', function () { // init script after page loaded
  console.log('<f> doc loaded');
  getData();
});
