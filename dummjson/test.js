// baseURL = "https://restful-booker.herokuapp.com"
const request = require("supertest")("https://dummyjson.com")
const expect = require("chai").expect

describe("get products", function () { // test scenario
    it("succes get all products", async function() { // test cases 1
        const response = await request
        .get("/booking") // HTTP method + endpoint
        .send();
        // expect(response.status).to.eql(200)
    })
   
})

// it.only , it.skip