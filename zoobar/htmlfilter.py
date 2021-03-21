import lxml.html
import lxml.html.clean
import slimit.ast
import slimit.parser
import lab6visitor

from debug import *

libcode = '''
<script>
    var dangerous_props = [
            "__proto__",
            "constructor",
            "__defineGetter__",
            "__defineSetter__"];
    var invalid_prop = "__invalid__";

    var sandbox_document = {
        getElementById: function(id) {
            var e = document.getElementById('sandbox-' + id);
            return {
                get onclick() { return e.onclick; },
                set onclick(h) { e.onclick = h; },
                get textContent() { return e.textContent; },
            }
        },
    };

    // Do not change these functions.
    function sandbox_grader(url) {
        window.location = url;
    }
    function sandbox_grader2() {
        eval("1 + 1".toString());  // What could possibly go wrong...
    }
    function sandbox_grader3() {
        try {
            eval(its_okay_no_one_will_ever_define_this_variable);
        } catch (e) {
        }
    }
    function is_dangerous_prop(s) {
        for (var i = 0; i < dangerous_props.length; ++i) {
            if (dangerous_props[i] === s ||
                dangerous_props[i] === s.toString() ||
                dangerous_props[i] === s.valueOf()) {
                return true;
            }
        }
        return false;
    }
    function bracket_check(s) {
        s.oldToString = s.toString;
        s.toString = function() {
            var toStringResult = s.oldToString();
            if (is_dangerous_prop(toStringResult)) {
                return null;
            }
            return s;
        };

        if (is_dangerous_prop(s)) {
            return null;
        }
        return s;
    }
    function this_check(t) {
        if (t === window) {
            return null;
        }
        return t;
    }
    function sandbox_setTimeout(callback, time) {
        if (typeof callback === "function") {
            return setTimeout(callback, time);
        }
        return null;
    }
</script>
'''

def filter_html_cb(s, jsrewrite):
    cleaner = lxml.html.clean.Cleaner()
    cleaner.scripts = False
    cleaner.style = True
    doc = lxml.html.fromstring(s)
    clean = cleaner.clean_html(doc)
    for el in clean.iter():
        if el.tag == 'script':
            el.text = jsrewrite(el.text)
            for a in el.attrib:
                del el.attrib[a]
        if 'id' in el.attrib:
            el.attrib['id'] = 'sandbox-' + el.attrib['id']
    return lxml.html.tostring(clean)

@catch_err
def filter_js(s):
    parser = slimit.parser.Parser()
    tree = parser.parse(s)
    visitor = lab6visitor.LabVisitor()
    return visitor.visit(tree)

@catch_err
def filter_html(s):
    return libcode + filter_html_cb(s, filter_js)

