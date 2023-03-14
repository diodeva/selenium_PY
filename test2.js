// baseURL = "https://restful-booker.herokuapp.com"
const request = require("supertest")("https://restful-booker.herokuapp.com")
const expect = require("chai").expect

describe("get booking", function () { // test scenario
    it("succes get booking", async function() { // test cases 1
        const response = await request
        .get("/booking") // HTTP method + endpoint
        .send();
        expect(response.status).to.eql(200)
    })
})