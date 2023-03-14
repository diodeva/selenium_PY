const expect = require("chai".expect)
const request = require("supertest")("https://reqres.in")

describe("reqres test", () => {
    it('get list user', async function(){
        const response = await request
        .get('/api/users?page=2')
        .send(response)
    })
})