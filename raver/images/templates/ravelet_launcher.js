(
    function(){
        if(!window.ravelet) {
            ravelet_js = document.body.appendChild(document.createElement('script'));
            ravelet_js.src = '//127.0.0.1:8000/static/js/ravelet.js?r='+Math.floor(Math.random()*9999999999999999);
            window.ravelet = true;
        }
        else {
            raveletLaunch();
        }
    }
)