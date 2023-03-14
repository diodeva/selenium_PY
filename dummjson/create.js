const request = require("supertest")("https://dummyjson.com")
const expect = require("chai").expect

describe("create products", function () { // test scenario
    it("success create product", async function() { // test case 2
        const response = await request
        .post("/products/add")
        .send({
            title: 'BMW Pencil' // body request
        });
        expect(response.status).to.eql(200)
        expect(response.body).to.have.property('title')
        expect(response.body.title).to.eql('BMW Pencil')
        expect(response.body.id).to.eql(101)
        var title = response.body.title
        console.log(title)
    })
    it("get token", async function () {
        const response = await request
        .post("/auth/login")
        .send({
            username: 'kminchelle',
            password: '0lelplR'
        });
        var token = response.body.token
        console.log(token)
        
    })
})