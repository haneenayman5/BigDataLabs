HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>HDFS Control Panel</title>
<style>

/* ── RESET ── */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* ── BASE ── */
body {
    background-color: #0d0d0d;
    color: #c8c8c8;
    font-family: "Courier New", Courier, monospace;
    font-size: 13px;
    height: 100vh;
    overflow: hidden;
}

/* ── HEADER ── */
#header {
    background-color: #1a1a1a;
    border-bottom: 2px solid #e8a900;
    padding: 10px 18px;
    display: table;
    width: 100%;
}
#header-left  { display: table-cell; vertical-align: middle; }
#header-right { display: table-cell; vertical-align: middle; text-align: right; }

#header h1 {
    font-size: 16px;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #e8a900;
}
#header-right span {
    font-size: 11px;
    color: #555;
    letter-spacing: 2px;
    text-transform: uppercase;
}

/* ── MAIN SPLIT ── */
#main {
    display: table;
    width: 100%;
    height: calc(100vh - 46px);
}

/* ── LEFT PANEL ── */
#left {
    display: table-cell;
    width: 38%;
    vertical-align: top;
    background-color: #111;
    border-right: 2px solid #e8a900;
    overflow-y: auto;
    padding: 12px 10px;
}

/* ── RIGHT TERMINAL ── */
#right {
    display: table-cell;
    vertical-align: top;
    background-color: #050505;
}

/* ── CARDS ── */
.card {
    background-color: #161616;
    border: 1px solid #2a2a2a;
    border-left: 3px solid #e8a900;
    margin-bottom: 10px;
    padding: 10px 12px;
}

.card-title {
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #e8a900;
    margin-bottom: 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid #2a2a2a;
}

/* ── INPUTS ── */
.field-label {
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #666;
    display: block;
    margin-top: 7px;
    margin-bottom: 3px;
}

input[type="text"] {
    width: 100%;
    padding: 6px 8px;
    background-color: #0d0d0d;
    border: 1px solid #333;
    border-bottom: 2px solid #444;
    color: #e0e0e0;
    font-family: "Courier New", Courier, monospace;
    font-size: 12px;
    outline: none;
}

input[type="text"]:focus {
    border-bottom: 2px solid #e8a900;
    color: #fff;
}

/* ── BUTTON ROW ── */
.btn-row {
    margin-top: 9px;
}

/* ── BUTTONS ── */
button {
    display: inline-block;
    padding: 6px 11px;
    margin-right: 5px;
    margin-bottom: 4px;
    font-family: "Courier New", Courier, monospace;
    font-size: 11px;
    letter-spacing: 1px;
    text-transform: uppercase;
    border: none;
    cursor: pointer;
    border-bottom: 3px solid transparent;
}

button:active {
    border-bottom-width: 1px;
    margin-top: 2px;
}

.btn-amber {
    background-color: #e8a900;
    color: #0d0d0d;
    font-weight: bold;
    border-bottom-color: #a57800;
}
.btn-amber:hover { background-color: #ffbb00; }

.btn-green {
    background-color: #1a7a1a;
    color: #aaffaa;
    border-bottom-color: #0d4a0d;
}
.btn-green:hover { background-color: #228822; }

.btn-red {
    background-color: #7a1a1a;
    color: #ffaaaa;
    border-bottom-color: #4a0d0d;
}
.btn-red:hover { background-color: #882222; }

.btn-slate {
    background-color: #1e2a38;
    color: #88aacc;
    border-bottom-color: #111b25;
}
.btn-slate:hover { background-color: #253347; }

/* ── TERMINAL RIGHT ── */
#term-bar {
    background-color: #111;
    border-bottom: 1px solid #2a2a2a;
    padding: 8px 14px;
    font-size: 11px;
    letter-spacing: 1px;
    color: #555;
}

#term-bar span {
    color: #e8a900;
    letter-spacing: 0;
}

#term-prompt {
    background-color: #0a0a0a;
    border-bottom: 1px solid #1a1a1a;
    padding: 6px 14px;
    font-size: 11px;
    color: #444;
}

#term-prompt span { color: #3a6e3a; }
#term-prompt b    { color: #c8c8c8; font-weight: normal; }

#term-output {
    padding: 14px;
    overflow-y: auto;
    height: calc(100vh - 46px - 34px - 30px);
    font-family: "Courier New", Courier, monospace;
    font-size: 13px;
    color: #3dba5a;
    white-space: pre-wrap;
    word-break: break-all;
    line-height: 1.6;
}

/* ── SCROLLBARS (Firefox old) ── */
#left       { scrollbar-color: #e8a900 #111; scrollbar-width: thin; }
#term-output{ scrollbar-color: #3dba5a #050505; scrollbar-width: thin; }

/* ── CURSOR BLINK ── */
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
#cursor {
    display: inline-block;
    width: 8px;
    height: 14px;
    background-color: #3dba5a;
    vertical-align: middle;
    animation: blink 1s step-end infinite;
    margin-left: 2px;
}

/* ── ERROR COLOR ── */
.err { color: #e05555; }

</style>
</head>

<body>

<!-- HEADER -->
<div id="header">
    <div id="header-left">
        <h1>&#9654; HDFS Control Panel</h1>
    </div>
    <div id="header-right">
        <span>Offline Mode &bull; Hadoop Distributed FS</span>
    </div>
</div>

<!-- MAIN -->
<div id="main">

    <!-- ═══════════ LEFT CONTROLS ═══════════ -->
    <div id="left">

        <!-- Cluster Control -->
        <div class="card">
            <div class="card-title">&#9632; Cluster Control</div>
            <div class="btn-row">
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="command" value="start-dfs.sh">
                    <button class="btn-green">&#9650; Start DFS</button>
                </form>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="command" value="start-yarn.sh">
                    <button class="btn-green">&#9650; Start YARN</button>
                </form>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="command" value="stop-dfs.sh">
                    <button class="btn-red">&#9660; Stop DFS</button>
                </form>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="command" value="stop-yarn.sh">
                    <button class="btn-red">&#9660; Stop YARN</button>
                </form>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="command" value="jps">
                    <button class="btn-slate">&#9670; JPS Check</button>
                </form>
            </div>
        </div>

        <!-- Browse -->
        <div class="card">
            <div class="card-title">&#9632; Browse HDFS</div>
            <form method="POST">
                <label class="field-label">Path</label>
                <input type="text" name="path_entry" value="{{ last_path }}">
                <div class="btn-row">
                    <button class="btn-amber" name="action" value="ls">&#9658; List</button>
                    <button class="btn-slate" name="action" value="cat">&#9658; View File</button>
                </div>
            </form>
        </div>

        <!-- File Ops -->
        <div class="card">
            <div class="card-title">&#9632; File Operations</div>
            <form method="POST">
                <label class="field-label">Source Path</label>
                <input type="text" name="src_entry" placeholder="/hdfs/source/path">
                <label class="field-label">Destination Path</label>
                <input type="text" name="dst_entry" placeholder="/hdfs/dest/path">
                <div class="btn-row">
                    <button class="btn-amber" name="action" value="cp">&#9660; Copy</button>
                    <button class="btn-slate" name="action" value="mv">&#8594; Move</button>
                </div>
            </form>
        </div>

        <!-- Directory -->
        <div class="card">
            <div class="card-title">&#9632; Directory</div>
            <form method="POST">
                <label class="field-label">Path</label>
                <input type="text" name="rm_path" placeholder="/hdfs/target/path">
                <div class="btn-row">
                    <button class="btn-green" name="action" value="mkdir">+ Create Dir</button>
                    <button class="btn-red" name="action" value="rm">&#215; Delete</button>
                </div>
            </form>
        </div>

    </div>
    <!-- ═══════════ end LEFT ═══════════ -->

    <!-- ═══════════ RIGHT TERMINAL ═══════════ -->
    <div id="right">

        <div id="term-bar">
            LAST CMD &nbsp;&#9658;&nbsp; <span>{{ cmd_text }}</span>
        </div>

        <div id="term-prompt">
            <span>hdfs@cluster</span>:<b>~$</b> _
        </div>

        <div id="term-output">{{ output }}<span id="cursor"></span></div>

    </div>
    <!-- ═══════════ end RIGHT ═══════════ -->

</div>

</body>
</html>
"""
