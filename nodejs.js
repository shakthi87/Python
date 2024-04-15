const setRateLimit = require("express-rate-limit");

// Rate limit middleware
const rateLimitMiddleware = setRateLimit({
  windowMs: 60 * 1000,
  max: 5,
  message: "You have exceeded your 5 requests per minute limit.",
  headers: true,
});

module.exports = rateLimitMiddleware;
/* This middleware enforces our rate limit based on the provided options, where:

    windowMs: This is the window (time frame) size in milliseconds.
    max: Maximum number of requests which can be allowed in the given window size.
    message: This option is optional, we can customize the error message or use the default message provided by the middleware.
    headers: The headers option is essential, as it automatically adds crucial HTTP headers to responses. 
             These headers include X-RateLimit-Limit (indicating the rate limit), X-RateLimit-Remaining (showing the remaining requests within the window), 
             and Retry-After (indicating the time to wait before retrying). 
             These headers provide clients with vital rate-limiting information.
 
*/



//app.js

const express = require("express");
const rateLimitMiddleware = require("./middlewares/ratelimit");
const app = express();

app.use(rateLimitMiddleware);

//Using Rate Limiter on a specific route
app.get("/api/blog/post", rateLimitMiddleware, (req, res) => {
  res.send({
    success: true,
    author: "Mike Abdul",
    "title": "Creating NodeJs Rate Limiter",
    "post": "..."
  });
});
