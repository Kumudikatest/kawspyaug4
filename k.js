const Swagger = require('swagger-client');

exports.handler = async (event) => {
    debugger;
    try {
        let response = await Swagger.http({
            url: `https://api.stripe.com/v1/balance`,
            method: 'get',
            query: {},
            headers: { "Accept": "application/json" }
        });
        console.log(response)
        // your code goes here

    } catch (err) {
        console.log(err)
        // error handling goes here
    }

    return { "message": "Successfully executed" };
};