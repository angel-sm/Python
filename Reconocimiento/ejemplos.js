const products = [{
    "item": "DELUXE COOKED HAM",
    "price": " $5.15 ",
    "productId": "102",
"img": "https://cdn.hyperdev.com/paste-me.svg?v=1477325869954"
},
{
    "item": "DELUXE LOW-SODIUM COOKED HAM ",
    "price": " $5.15 ",
    "productId": "159",
"img": "https://cdn.hyperdev.com/paste-me.svg?v=1477325869954"
},
{
    "item": "DELUXE LOW-SODIUM WHOLE HAM",
    "price": " $5.15 ",
    "productId": "105",
"img": "https://cdn.hyperdev.com/paste-me.svg?v=1477325869954"
}];

let id = 159
products.forEach(ele => {
    ele.productId == id ? console.log(ele) : console.log('falso')
})
