import { initProseEditor } from "./editor.js";

window.PMEditor = {
    initProse: function (textarea, options) {
        return initProseEditor(textarea, options);
    },
};
