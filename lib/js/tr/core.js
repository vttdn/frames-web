document.addEventListener('DOMContentLoaded',function(){const schemaFiles=['/lib/schema/tr/software.json','/lib/schema/tr/video.json','/lib/schema/tr/faq.json','/lib/schema/tr/organization.json','/lib/schema/tr/webpage-homepage.json','/lib/schema/tr/howto.json'];schemaFiles.forEach((url)=>{fetch(url).then(response=>{if(!response.ok){throw new Error(`Failed to fetch ${url}: ${response.status}`);}
return response.json();}).then(jsonData=>{const script=document.createElement('script');script.type='application/ld+json';script.textContent=JSON.stringify(jsonData);document.head.appendChild(script);}).catch(error=>{console.error('Error injecting JSON-LD:',error);});});});document.addEventListener('DOMContentLoaded',()=>{const overlay=document.getElementById('overlay');const modalContainer=document.getElementById('modal-container');const body=document.body;let lastFocusedElement=null;if(!overlay||!modalContainer)return;function openOverlay({type,titleText,contentHTML}){lastFocusedElement=document.activeElement;modalContainer.innerHTML=contentHTML;const titleEl=modalContainer.querySelector('h3');if(titleEl){const titleId=`overlay-title-${type}`;titleEl.id=titleId;overlay.setAttribute('aria-labelledby',titleId);}else{overlay.removeAttribute('aria-labelledby');}
overlay.hidden=false;overlay.classList.add('show');body.classList.add('body-no-scroll');const trigger=document.querySelector(`[data-overlay-trigger="${type}"]`);if(trigger)trigger.setAttribute('aria-expanded','true');overlay.setAttribute('aria-hidden','false');}
function closeOverlay(){overlay.classList.remove('show');body.classList.remove('body-no-scroll');setTimeout(()=>{overlay.hidden=true;modalContainer.innerHTML='';if(lastFocusedElement)lastFocusedElement.focus();},200);document.querySelectorAll('[data-overlay-trigger][aria-expanded="true"]').forEach(btn=>btn.setAttribute('aria-expanded','false'));overlay.setAttribute('aria-hidden','true');}
overlay.addEventListener('click',(e)=>{if(e.target===overlay)closeOverlay();});document.addEventListener('keydown',(e)=>{if(e.key==='Escape'&&!overlay.hidden)closeOverlay();});const socialBtn=document.getElementById('button-social-share');if(socialBtn){socialBtn.dataset.overlayTrigger='social';socialBtn.addEventListener('click',()=>{const contentHTML=`
          <div class="modal-header flex flex-justify-between flex-center">
            <h3>Paylaş</h3>
            <button class="overlay-button-close flex flex-center flex-justify-center"
                    aria-label="Kapat">
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
              <img src="/lib/img/icn/paperplane.svg" alt="E-posta Icon" width="14" height="14" loading="lazy">
            </a>
        </div>`;openOverlay({type:'social',titleText:'Paylaş',contentHTML});modalContainer.querySelector('.overlay-button-close').addEventListener('click',closeOverlay);});}
const menuBtn=document.getElementById('menu-toggle');if(menuBtn){menuBtn.dataset.overlayTrigger='menu';menuBtn.addEventListener('click',()=>{const contentHTML=`
      <div class="wrapper">
        <button class="overlay-button-close flex flex-center flex-justify-center"
                aria-label="Kapat">
            <img src="/lib/img/icn/xmark.svg" alt="x Mark Icon" width="32" height="32" loading="lazy" aria-hidden="true">
        </button>

        <nav class="mobile-menu-nav" aria-label="Mobil navigasyon">
          <ul class="flex flex-col">
            <li><a href="#features">Özellikler</a></li>
            <li><a href="/docs/">Dokümantasyon</a></li>
            <li><a href="/tr/changelog/">Değişiklik Günlüğü</a></li>
            <li><a href="/tr/gizlilik-politikasi/">Gizlilik</a></li>
          </ul>
        </nav>
      </div>
    `;openOverlay({type:'menu',titleText:'Mobil navigasyon',contentHTML});modalContainer.classList.add('modal-menu');const closeBtn=modalContainer.querySelector('.overlay-button-close');if(closeBtn){closeBtn.addEventListener('click',()=>{modalContainer.classList.remove('modal-menu');closeOverlay();});}
const anchors=modalContainer.querySelectorAll('a[href^="#"]');anchors.forEach(anchor=>{anchor.addEventListener('click',(e)=>{modalContainer.classList.remove('modal-menu');closeOverlay();});});});}
const playBtn=document.getElementById('youtube-video-toggle');if(playBtn){playBtn.dataset.overlayTrigger='youtube';playBtn.addEventListener('click',()=>{const videoId=playBtn.dataset.videoId;if(!videoId)return;const iframeHTML=`
      <iframe src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&mute=1&rel=0&modestbranding=1"
              title="YouTube video player"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; fullscreen"
              referrerpolicy="no-referrer-when-downgrade"
              style="position:absolute;inset:0;width:100%;height:100%;border:0;"></iframe>`;const contentHTML=`
      <div class="modal-header flex flex-justify-between flex-center">
            <h3>İzle</h3>
        <button class="overlay-button-close flex flex-center flex-justify-center"
                aria-label="Kapat">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
              viewBox="0 0 24 24" fill="none" stroke="currentColor"
              stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="size-4">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>
      <div class="video-wrapper" style="position:relative;padding-top:56.25%;">
        ${iframeHTML}
      </div>`;openOverlay({type:'youtube',titleText:'Demo videoyu oynat',contentHTML});modalContainer.classList.add('large');modalContainer.querySelector('.overlay-button-close').addEventListener('click',()=>{closeOverlay();setTimeout(()=>{modalContainer.classList.remove('large');},350);});});}});function shareOn(platform){const url=encodeURIComponent(window.location.href);const title=encodeURIComponent(document.title);const text=encodeURIComponent("Analog fotoğrafçılar için film fotoğrafçılık uygulaması. Kamera ayarlarını kaydedin, rulolar düzenleyin ve EXIF meta verisi ekleyin. Ücretsiz deneme iPhone.");let shareUrl='';switch(platform){case'facebook':shareUrl=`https://www.facebook.com/sharer/sharer.php?u=${url}`;break;case'twitter':shareUrl=`https://twitter.com/intent/tweet?url=${url}&text=${text}`;break;case'linkedin':shareUrl=`https://www.linkedin.com/sharing/share-offsite/?url=${url}`;break;case'whatsapp':shareUrl=`https://wa.me/?text=${text}%20${url}`;break;case'reddit':shareUrl=`https://reddit.com/submit?url=${url}&title=${title}`;break;case'email':shareUrl=`mailto:?subject=${title}&body=${text}%20${url}`;break;}
if(shareUrl){window.open(shareUrl,'_blank','width=600,height=400');}}
document.addEventListener('DOMContentLoaded',()=>{const howtoFigures=document.querySelectorAll('.howto figure.tile, .preview figure.tile');if(howtoFigures.length===0)return;howtoFigures.forEach(figure=>{figure.setAttribute('tabindex','0');figure.style.cursor='pointer';figure.setAttribute('role','button');figure.setAttribute('aria-pressed','false');const toggleContent=()=>{const img=figure.querySelector('img');const figcaption=figure.querySelector('figcaption');if(img&&figcaption){howtoFigures.forEach(otherFigure=>{if(otherFigure!==figure){const otherImg=otherFigure.querySelector('img');const otherFigcaption=otherFigure.querySelector('figcaption');if(otherImg&&otherFigcaption){otherImg.classList.remove('ruh');otherFigcaption.classList.add('ruh');otherFigure.setAttribute('aria-pressed','false');}}});const isDefaultState=figcaption.classList.contains('ruh');if(isDefaultState){figcaption.classList.remove('ruh');img.classList.add('ruh');}else{img.classList.remove('ruh');figcaption.classList.add('ruh');}
figure.setAttribute('aria-pressed',(!isDefaultState).toString());}};figure.addEventListener('click',toggleContent);figure.addEventListener('keydown',(e)=>{if(e.key===' '||e.key==='Enter'){e.preventDefault();toggleContent();}});});});