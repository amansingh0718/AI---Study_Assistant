def load_css():
    return """
    <style>

    /* ===========================
       Main App
    ============================ */

    .stApp{
        background:#f5f7fb;
    }

    .block-container{
        padding-top:1.5rem;
        padding-bottom:2rem;
        max-width:1200px;
    }

    /* ===========================
       Header Card
    ============================ */

    .header-card{
        background:linear-gradient(135deg,#2563eb,#4f46e5);
        padding:28px;
        border-radius:18px;
        color:white;
        box-shadow:0px 10px 30px rgba(0,0,0,0.15);
        margin-bottom:25px;
    }

    .header-title{
        font-size:36px;
        font-weight:700;
        margin-bottom:8px;
    }

    .header-subtitle{
        font-size:17px;
        opacity:0.95;
    }

    /* ===========================
       Section Cards
    ============================ */

    .card{

        background:white;

        border-radius:16px;

        padding:20px;

        box-shadow:0 6px 18px rgba(0,0,0,.08);

        margin-bottom:18px;

        border:1px solid #eeeeee;
    }

    .card-title{

        font-size:22px;

        font-weight:bold;

        color:#1f2937;

        margin-bottom:12px;
    }

    /* ===========================
       Buttons
    ============================ */

    .stButton>button{

        width:100%;

        background:#2563eb;

        color:white;

        border:none;

        border-radius:10px;

        padding:12px;

        font-weight:bold;

        transition:.3s;
    }

    .stButton>button:hover{

        background:#1d4ed8;

        transform:translateY(-2px);

        box-shadow:0px 8px 18px rgba(37,99,235,.3);
    }

    /* ===========================
       Inputs
    ============================ */

    .stTextInput input{

        border-radius:10px;

        border:1px solid #d1d5db;
    }

    div[data-baseweb="select"]{

        border-radius:10px;
    }

    /* ===========================
       Upload Box
    ============================ */

    [data-testid="stFileUploader"]{

        border:2px dashed #2563eb;

        border-radius:15px;

        padding:12px;

        background:#f8fbff;
    }

    /* ===========================
       Success
    ============================ */

    .success-card{

        background:#dcfce7;

        color:#166534;

        border-radius:12px;

        padding:15px;

        font-weight:bold;

        border:1px solid #22c55e;
    }

    /* ===========================
       Result
    ============================ */

    .result-card{

        background:white;

        padding:25px;

        border-radius:16px;

        border-left:6px solid #2563eb;

        box-shadow:0px 5px 15px rgba(0,0,0,.08);

        margin-top:20px;
    }

    /* ===========================
       Sidebar
    ============================ */

    section[data-testid="stSidebar"]{

        background:#ffffff;

        border-right:1px solid #e5e7eb;
    }

    </style>
    """