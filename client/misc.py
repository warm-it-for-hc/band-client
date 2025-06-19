RESULT_CODES = {
    211: {
        "message": "Invalid Parameters",
        "description": None,
        "resolution": None
    },
    212: {
        "message": "Insufficient Parameters",
        "description": None,
        "resolution": "Check for required parameters and add it (if applicable)."
    },
    1001: {
        "message": "App quota has been exceeded",
        "description": "API quota exceeds the limit",
        "resolution": None
    },
    1002: {
        "message": "User quota has been exceeded",
        "description": "User quota exceeds the limit",
        "resolution": None
    },
    1003: {
        "message": "Cool down time restriction",
        "description": "Continuous API calls for a short period of time is not available",
        "resolution": "Try again after timeout interval has expire."
    },
    2142: {
        "message": "Only Band Leaders are allowed to do this",
        "description": "Only Band owners are allowed",
        "resolution": None
    },
    2300: {
        "message": "Invalid response",
        "description": "Error in server response",
        "resolution": "Undefined error. Send us your client ID, request URL, and parameter info."
    },
    3000: {
        "message": "Invalid request",
        "description": "Invalid call",
        "resolution": "Check the path and parameters and try again."
    },
    3001: {
        "message": "Exceeded chareacter limit",
        "description": "Content length exceeds the limit",
        "resolution": "Shorten the length and try again."
    },
    3002: {
        "message": "Image file size has been exceeded",
        "description": "Image file size exceeds the limit",
        "resolution": "Reduce the image file size and try again."
    },
    3003: {
        "message": "Number of image files has been exceeded",
        "description": "The number of attachments exceeds the limit",
        "resolution": "Reduce the number of attachments and try again."
    },
    10401: {
        "message": "Unauthorized",
        "description": "Authentication failure; no access token exists or it has expired",
        "resolution": "Get a new access token after login and try again."
    },
    10403: {
        "message": "Forbidden",
        "description": "Access is denied; no permissions",
        "resolution": "Check your permissions and contact Customer Center to request permission."
    },
    60000: {
        "message": "Invalid Parameter",
        "description": "Invalid parameter is used",
        "resolution": "Check for required parameters and parameter types and try again."
    },
    60100: {
        "message": "Invalid member",
        "description": "User does not exist",
        "resolution": None
    },
    60101: {
        "message": "Not my friend",
        "description": "User is not found in the friend list",
        "resolution": None
    },
    60102: {
        "message": "Not Band member",
        "description": "The API called is only valid for Bands that a user has joined",
        "resolution": None
    },
    60103: {
        "message": "This user is not connected",
        "description": "The API called is only valid for users whose BAND account is connected with the app",
        "resolution": None
    },
    60104: {
        "message": "This user has already been connected",
        "description": "The API called is only valid for users whose BAND account is not connected with the app",
        "resolution": None
    },
    60105: {
        "message": "You are Band Leader. Band has members.",
        "description": "Band owner tries to leave a Band",
        "resolution": None
    },
    60106: {
        "message": "This function is granted to the specified member.",
        "description": "Only specific members are given permission to use this function",
        "resolution": None
    },
    60200: {
        "message": "This Band is invalid or not connected.",
        "description": "Band does not exist or is invalid",
        "resolution": None
    },
    60201: {
        "message": "You have already joined Band",
        "description": "The API called is only valid for Bands that a user has not joined",
        "resolution": None
    },
    60202: {
        "message": "Exceeded Band Max.",
        "description": "Exceeded the maximum number of Bands a user is allowed to join",
        "resolution": None
    },
    60203: {
        "message": "Invalid Band type",
        "description": "The API called is valid for either guild Bands or official Bands",
        "resolution": None
    },
    60204: {
        "message": "This Band did not allow access by the user.",
        "description": "Try to access a Band that is not accessible",
        "resolution": None
    },
    60300: {
        "message": "Receiving message is blocked",
        "description": "Message is not accepted by the recipient",
        "resolution": None
    },
    60301: {
        "message": "Invalid message format",
        "description": None,
        "resolution": None
    },
    60302: {
        "message": "Message service failure",
        "description": None,
        "resolution": None
    },
    60400: {
        "message": "Only designated member(s) can write post",
        "description": "No write permission",
        "resolution": None
    },
    60401: {
        "message": "Post is not connected with the app",
        "description": None,
        "resolution": None
    },
    60402: {
        "message": "Post is not editable; images or its sub posts may be deleted.",
        "description": None,
        "resolution": None
    },
    60700: {
        "message": "This invitation is invalid",
        "description": "Invalid invitation",
        "resolution": None
    },
    60800: {
        "message": "Image URL is invalid or the format is not supported",
        "description": "Invalid image URL format",
        "resolution": None
    },
    60801: {
        "message": "Album not exists",
        "description": "Album ID does not exist",
        "resolution": None
    }
}
