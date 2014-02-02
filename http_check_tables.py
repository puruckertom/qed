from django.template import Context, Template
from django.utils.safestring import mark_safe
import logging
import time
import datetime

def getdjtemplate():
    dj_template ="""
    <table class="out_">
    {# headings #}
        <tr>
        {% for heading in headings %}
            <th>{{ heading }}</th>
        {% endfor %}
        </tr>
    {# data #}
    {% for row in data %}
    <tr>
        {% for val in row %}
        <td>{{ val|default:'' }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
    </table>
    """
    return dj_template

def gethttpheader():
	headings = ["#", "Page", "Status", "Reason"]
	return headings

def gethttpdata(counter, page, status, reason):
    data = { 
        "#": counter,
        "Page": page,
        "Status": status,
        "Reason": reason,
    }
    return data

def timestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%A, %Y-%B-%d %H:%M:%S')
    html="""
    <div class="out_">
        Web Page Functionality Check<br>
    """
    html = html + st
    html = html + " (UTC)</b>"
    html = html + """
    </div>"""
    return html

def gethtmlrowsfromcols(data, headings):
    columns = [data[heading] for heading in headings]

    # get the length of the longest column
    max_len = len(max(columns, key=len))

    for col in columns:
        # padding the short columns with None
        col += [None,] * (max_len - len(col))

    # Then rotate the structure...
    rows = [[col[i] for col in columns] for i in range(max_len)]
    return rows

djtemplate = getdjtemplate()
tmpl = Template(djtemplate)

def table_1(httpheadings, counter, page, status, reason, counter_total, counter_ok):
    ok_score = str(counter_ok + "/" + counter_total)
    html1 = """
    <H3 class="out_1 collapsible" id="section1"><span></span>Test Results (
    """
    html2 = """
    </H3>
    <div class="out_">
        <H4 class="out_1 collapsible" id="section2"><span></span>Integration Test of Non-Output Pages (<a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html">Status Code Definitions</a>)</H4>
            <div class="out_ container_output">
    """
    html = html1 + ok_score + html2
    t1data = gethttpdata(counter, page, status, reason)
    t1rows = gethtmlrowsfromcols(t1data,httpheadings)
    html = html + tmpl.render(Context(dict(data=t1rows, headings=httpheadings)))
    html = html + """
            </div>
    </div>
    """
    return html

