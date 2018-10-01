information = [
    {
        name: "iPhone",
        url: "https://amp.businessinsider.com/images/59c29dcb2488492b395ca43e-960-623.jpg",
    },
    {
        name: "Macbook",
        url: "https://cnet4.cbsistatic.com/img/s7OzxR8Y3xxOlegTpRQW3CuZPuk=/830x467/2017/06/06/349b7e65-a855-44f0-ae0a-6610ebca0809/apple-macbook-pro-12-inch-2017-4181.jpg"
    },
    {
        name: "Car",
        url: "https://imgct2.aeplcdn.com/img/800x600/car-data/big/honda-city-image-9579.png?v=29"
    },
    {
        name: "Television",
        url: "http://imshopping.rediff.com/imgshop/300-400/shopping/pixs/25424/b/bush32._bush-32-inch-curved-led-tv.jpg",
    },
    {
        name: "Bike",
        url: "https://imgd.aeplcdn.com//1056x594//bw/models/tvs-apache-rtr-160-4v.jpg?20180813151835"
    }
]

function openModal(name){
    itemContent = document.getElementById(name);
    itemContent.style.display = "block";
}

function closeModal(name){
    itemContent = document.getElementById(name);
    itemContent.style.display = "none";
}

