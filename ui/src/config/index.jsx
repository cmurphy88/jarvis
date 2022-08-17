function getApiUrl() {
    const test = process.env.REACT_APP_API_URL || "http://127.0.0.1:8000/";
    console.log("URL...", test)
    return test;
    // return "https://jarvis-1.5a25j6q6mjvnu.eu-west-1.cs.amazonlightsail.com/";

}

export {getApiUrl}; 
