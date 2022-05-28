pc_agents = [
    "Windows 10/ Edge browser: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    "Windows 7/ Chrome browser: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
    "Mac OS X10/Safari browser: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    "Linux PC/Firefox browser: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"
    "Chrome OS/Chrome browser: Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36"
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
]


IGNORED_MEMBER_EXPRESSIONS = [
    {
        "object": r"^self|top|window|parent$",
        "property": r"^addEventListener|alert|atob|blur|btoa|cancelAnimationFrame|cancelIdleCallback|captureEvents|clearInterval|clearTimeout|clientInformation|close|closed|confirm|createImageBitmap|crypto|customElements|defaultStatus|defaultstatus|devicePixelRatio|dispatchEvent|document|external|fetch|find|focus|frameElement|frames|getComputedStyle|getSelection|history|indexedDB|innerHeight|innerWidth|isSecureContext|length|localStorage|location|locationbar|matchMedia|menubar|moveBy|moveTo|name|navigator|open|openDatabase|opener|origin|outerHeight|outerWidth|pageXOffset|pageYOffset|parent|performance|personalbar|postMessage|print|prompt|queueMicrotask|releaseEvents|removeEventListener|requestAnimationFrame|requestIdleCallback|resizeBy|resizeTo|screen|screenLeft|screenTop|screenX|screenY|scroll|scrollBy|scrollTo|scrollX|scrollY|scrollbars|self|sessionStorage|setInterval|setTimeout|speechSynthesis|status|statusbar|stop|styleMedia|toolbar|top|visualViewport|window$",
    },
    {"property": "prototype"},
    {
        object: "document",
        "property": r"^body|documentElement|head|getElementById|querySelector|querySelectorAll$",
    },
    {
        object: "Object",
        "property": r"^length|name|prototype|assign|getOwnPropertyDescriptor|getOwnPropertyDescriptors|getOwnPropertyNames|getOwnPropertySymbols|is|preventExtensions|seal|create|defineProperties|defineProperty|freeze|getPrototypeOf|setPrototypeOf|isExtensible|isFrozen|isSealed|keys|entries|fromEntries|values$",
    },
]
