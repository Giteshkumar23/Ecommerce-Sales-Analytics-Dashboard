def load_css():
    return """
    <style>

    .stApp{
        background-color:#0E1117;
    }

    .main-title{
        color:white;
        font-size:42px;
        font-weight:700;
    }

    .subtitle{
        color:#A0AEC0;
        font-size:18px;
        margin-bottom:25px;
    }

    div[data-testid="metric-container"]{
        background:#1E293B;
        border:1px solid #334155;
        padding:18px;
        border-radius:16px;
        box-shadow:0 0 15px rgba(0,0,0,.25);
    }

    div[data-testid="metric-container"]:hover{
        transform:translateY(-4px);
        transition:0.3s;
        border:1px solid #3B82F6;
    }

    h1,h2,h3{
        color:white;
    }

    </style>
    """