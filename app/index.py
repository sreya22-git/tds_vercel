
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# JSON data with 100 students (Example)
students_data = [{"name":"zcmrNfp5","marks":23},{"name":"8T5V74FE9","marks":90},{"name":"AbXv7BR2y9","marks":60},{"name":"lp","marks":40},{"name":"SQMte","marks":31},{"name":"MsMb2a3Zbk","marks":43},{"name":"4Tq","marks":97},{"name":"9aB","marks":59},{"name":"bx3J","marks":35},{"name":"Fu5HXc8Ne","marks":40},{"name":"RBICrn","marks":64},{"name":"78Z89NBAn","marks":2},{"name":"AAU13kJzV","marks":2},{"name":"cm7w","marks":61},{"name":"H7Us7Xrjlo","marks":21},{"name":"VyNB","marks":64},{"name":"BPoUVDD","marks":33},{"name":"7O1qNcj","marks":19},{"name":"FCHKEhlGJ3","marks":20},{"name":"TuxOk","marks":36},{"name":"Af","marks":14},{"name":"QOw5othhS","marks":54},{"name":"LpnQh","marks":65},{"name":"vMr9jmbCE","marks":49},{"name":"K","marks":10},{"name":"ya5qQJcvQx","marks":24},{"name":"Vb","marks":95},{"name":"WVT3","marks":75},{"name":"6vRK0","marks":91},{"name":"r1gZ5hJ86","marks":38},{"name":"A","marks":6},{"name":"3vzI3uUwv","marks":78},{"name":"5hHWPy","marks":64},{"name":"NBe2","marks":12},{"name":"aFIafkzZ6e","marks":11},{"name":"UNiEDRVr","marks":17},{"name":"Mwzfd","marks":88},{"name":"fK3V7Vd","marks":92},{"name":"2umoMTwaaF","marks":91},{"name":"Gz","marks":92},{"name":"XT","marks":37},{"name":"ds5k","marks":11},{"name":"71Ic9i","marks":20},{"name":"YOzr55V","marks":86},{"name":"16kXxceB","marks":80},{"name":"R","marks":12},{"name":"52","marks":90},{"name":"Pn8L","marks":56},{"name":"Ina","marks":6},{"name":"0mARb4oyt","marks":99},{"name":"tuZ","marks":93},{"name":"0Xqo1ricR","marks":86},{"name":"O65kWQmh","marks":68},{"name":"RBmM","marks":73},{"name":"cXmloFrl","marks":4},{"name":"HLKMAXBI","marks":14},{"name":"qoMi","marks":17},{"name":"DsN","marks":75},{"name":"g6nuZ","marks":90},{"name":"O","marks":75},{"name":"g1HtOkO","marks":14},{"name":"RtW","marks":77},{"name":"b9F7bstONH","marks":32},{"name":"jiE","marks":25},{"name":"c","marks":9},{"name":"Km8v5","marks":16},{"name":"JM","marks":8},{"name":"G","marks":14},{"name":"4Ddv","marks":63},{"name":"nleZMpv","marks":42},{"name":"wHZA6V2i6Y","marks":36},{"name":"ilvgQpezu","marks":17},{"name":"DEr312","marks":66},{"name":"cSTx","marks":24},{"name":"UtYkX3LTXe","marks":19},{"name":"TJ","marks":64},{"name":"ntglUBMs","marks":92},{"name":"XCyE4K","marks":30},{"name":"6L00UPuzC","marks":79},{"name":"RE8r","marks":74},{"name":"GTYq6UMQY","marks":73},{"name":"9WK8","marks":76},{"name":"cOzJ","marks":22},{"name":"efxSaZyl","marks":31},{"name":"W5BoxM","marks":93},{"name":"3Ofqb8","marks":37},{"name":"lehImdF","marks":50},{"name":"cl7Y","marks":8},{"name":"5UvO4ziiOk","marks":14},{"name":"Xt2c","marks":21},{"name":"tm67XXk","marks":48},{"name":"0FwoddW","marks":73},{"name":"jq","marks":53},{"name":"TEv","marks":94},{"name":"WC","marks":39},{"name":"oamsu","marks":72},{"name":"Oi","marks":55},{"name":"xCfjiDpJ","marks":49},{"name":"M","marks":82},{"name":"0VHXZQSsP","marks":26}]
@app.get("/api")
async def get_marks(name: list[str] = Query(None)):
    """
    Fetch marks of students by name.
    Example usage:
    - `/api?name=ho8ePmxFs` -> {"marks": [70]}
    - `/api?name=ho8ePmxFs&name=Zfmi` -> {"marks": [70, 55]}
    """
    if name:
        marks = [next((s["marks"] for s in students_data if s["name"] ==n), None) for n in name]
        return {"marks": marks}
    return {"marks": []}
