document.addEventListener('DOMContentLoaded',function(){const schemaFiles=['/lib/schema/hi/breadcrumb-privacy.json','/lib/schema/hi/organization.json','/lib/schema/hi/webpage-privacy.json'];schemaFiles.forEach((url)=>{fetch(url).then(response=>{if(!response.ok){throw new Error(`Failed to fetch ${url}: ${response.status}`);}
return response.json();}).then(jsonData=>{const script=document.createElement('script');script.type='application/ld+json';script.textContent=JSON.stringify(jsonData);document.head.appendChild(script);}).catch(error=>{console.error('Error injecting JSON-LD:',error);});});});function shareOn(platform){const url=encodeURIComponent(window.location.href);const title=encodeURIComponent(document.title);const metaDescription=document.querySelector('meta[name="description"]');const text=encodeURIComponent(metaDescription?metaDescription.getAttribute('content'):"");let shareUrl='';switch(platform){case'facebook':shareUrl=`https://www.facebook.com/sharer/sharer.php?u=${url}`;break;case'twitter':shareUrl=`https://twitter.com/intent/tweet?url=${url}&text=${text}`;break;case'linkedin':shareUrl=`https://www.linkedin.com/sharing/share-offsite/?url=${url}`;break;case'whatsapp':shareUrl=`https://wa.me/?text=${text}%20${url}`;break;case'reddit':shareUrl=`https://reddit.com/submit?url=${url}&title=${title}`;break;case'email':shareUrl=`mailto:?subject=${title}&body=${text}%20${url}`;break;}
if(shareUrl){window.open(shareUrl,'_blank','width=600,height=400');}}
document.addEventListener('DOMContentLoaded',()=>{const overlay=document.getElementById('overlay');const modalContainer=document.getElementById('modal-container');const body=document.body;let lastFocusedElement=null;if(!overlay||!modalContainer)return;function openOverlay({type,titleText,contentHTML}){lastFocusedElement=document.activeElement;modalContainer.innerHTML=contentHTML;const titleEl=modalContainer.querySelector('h3');if(titleEl){const titleId=`overlay-title-${type}`;titleEl.id=titleId;overlay.setAttribute('aria-labelledby',titleId);}else{overlay.removeAttribute('aria-labelledby');}
overlay.hidden=false;overlay.classList.add('show');body.classList.add('body-no-scroll');const trigger=document.querySelector(`[data-overlay-trigger="${type}"]`);if(trigger)trigger.setAttribute('aria-expanded','true');overlay.setAttribute('aria-hidden','false');}
function closeOverlay(){overlay.classList.remove('show');body.classList.remove('body-no-scroll');setTimeout(()=>{overlay.hidden=true;modalContainer.innerHTML='';if(lastFocusedElement)lastFocusedElement.focus();},200);document.querySelectorAll('[data-overlay-trigger][aria-expanded="true"]').forEach(btn=>btn.setAttribute('aria-expanded','false'));overlay.setAttribute('aria-hidden','true');}
overlay.addEventListener('click',(e)=>{if(e.target===overlay)closeOverlay();});document.addEventListener('keydown',(e)=>{if(e.key==='Escape'&&!overlay.hidden)closeOverlay();});const socialBtn=document.getElementById('button-social-share');if(socialBtn){socialBtn.dataset.overlayTrigger='social';socialBtn.addEventListener('click',()=>{const contentHTML=`
          <div class="modal-header flex flex-justify-between flex-center">
            <h3>साझा करें</h3>
            <button class="overlay-button-close flex flex-center flex-justify-center"
                    aria-label="बंद करें">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
                   viewBox="0 0 24 24" fill="none" stroke="currentColor"
                   stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4">
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </button>
          </div>

          <div class="modal-social-buttons grid grid-3col">
            <a href="#" onclick="shareOn('facebook');return false;">
              <img src="/lib/img/icn/facebook.svg" alt="Facebook Icon" width="14" height="14" loading="lazy">
            </a>
            <a href="#" onclick="shareOn('twitter');return false;">
              <img src="/lib/img/icn/twitter.svg" alt="Twitter / X Icon" width="14" height="14" loading="lazy">
            </a>
            <a href="#" onclick="shareOn('linkedin');return false;">
              <img src="/lib/img/icn/linkedin.svg" alt="LinkedIn Icon" width="14" height="14" loading="lazy">
            </a>
            <a href="#" onclick="shareOn('whatsapp');return false;">
              <img src="/lib/img/icn/whatsapp.svg" alt="WhatsApp Icon" width="14" height="14" loading="lazy">
            </a>
            <a href="#" onclick="shareOn('reddit');return false;">
              <img src="/lib/img/icn/reddit.svg" alt="Reddit Icon" width="14" height="14" loading="lazy">
            </a>
            <a href="#" onclick="shareOn('email');return false;">
              <img src="/lib/img/icn/paperplane.svg" alt="ईमेल Icon" width="14" height="14" loading="lazy">
            </a>
        </div>`;openOverlay({type:'social',titleText:'साझा करें',contentHTML});modalContainer.querySelector('.overlay-button-close').addEventListener('click',closeOverlay);});}
const menuBtn=document.getElementById('menu-toggle');if(menuBtn){menuBtn.dataset.overlayTrigger='menu';menuBtn.addEventListener('click',()=>{const contentHTML=`
      <div class="wrapper">
        <button class="overlay-button-close flex flex-center flex-justify-center"
                aria-label="बंद करें">
            <img src="/lib/img/icn/xmark.svg" alt="x Mark Icon" width="32" height="32" loading="lazy" aria-hidden="true">
        </button>

        <nav class="mobile-menu-nav" aria-label="मोबाइल नेविगेशन">
          <ul class="flex flex-col">
            <li><a href="https://withframes.com/hi/#features">विशेषताएं</a></li>
            <li><a href="/docs/">दस्तावेज़ीकरण</a></li>
            <li><a href="/hi/changelog/">परिवर्तन सूची</a></li>
            <li><a href="/hi/privacy/">गोपनीयता</a></li>
          </ul>
        </nav>
      </div>
    `;openOverlay({type:'menu',titleText:'मोबाइल नेविगेशन',contentHTML});modalContainer.classList.add('modal-menu');const closeBtn=modalContainer.querySelector('.overlay-button-close');if(closeBtn){closeBtn.addEventListener('click',()=>{modalContainer.classList.remove('modal-menu');closeOverlay();});}
const anchors=modalContainer.querySelectorAll('a[href^="#"]');anchors.forEach(anchor=>{anchor.addEventListener('click',(e)=>{modalContainer.classList.remove('modal-menu');closeOverlay();});});});}});