const proseMirror = (function () {
    "use strict";

    const initProseEditor = function (textarea) {
        let options = JSON.parse(textarea.dataset.prosemirror);
        PMEditor.initProse(textarea, options);
    };

    document.addEventListener("DOMContentLoaded", () => {
        document.querySelectorAll("textarea[data-prosemirror]").forEach(initProseEditor);
    });

    return {
        initProse: initProseEditor,
    };
})();
