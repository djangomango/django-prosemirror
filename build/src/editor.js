import { EditorState } from "prosemirror-state";
import { EditorView } from "prosemirror-view";
import { DOMParser as PMDOMParser, DOMSerializer, Schema } from "prosemirror-model";
import { schema } from "prosemirror-schema-basic";
import { addListNodes } from "prosemirror-schema-list";
import { exampleSetup } from "prosemirror-example-setup";

const mySchema = new Schema({
    nodes: addListNodes(schema.spec.nodes, "paragraph block*", "block"),
    marks: schema.spec.marks,
});

function serializeDocToHTML(doc, schema) {
    const fragment = DOMSerializer.fromSchema(schema).serializeFragment(doc.content);
    const div = document.createElement("div");
    div.appendChild(fragment);
    return div.innerHTML;
}

function initProseEditor(textarea, options) {
    const el = document.createElement("div");
    el.classList = textarea.classList;
    textarea.parentNode.insertBefore(el, textarea);
    textarea.style.display = "none";

    const parser = new DOMParser();
    const content = parser.parseFromString(textarea.value, "text/html").body;

    const view = new EditorView(el, {
        state: EditorState.create({
            doc: PMDOMParser.fromSchema(mySchema).parse(content),
            plugins: exampleSetup({ schema: mySchema, menuBar: true, history: true }),
        }),
        dispatchTransaction(tr) {
            const { state } = view.state.applyTransaction(tr);
            view.updateState(state);
            if (tr.docChanged) {
                textarea.value = serializeDocToHTML(view.state.doc, view.state.schema);
            }
        },
    });
}

export { initProseEditor };
