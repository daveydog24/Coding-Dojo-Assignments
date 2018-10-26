// add more data here for more items
data = [
    {
        title: "iPhone",
        image: "https://amp.businessinsider.com/images/59c29dcb2488492b395ca43e-960-623.jpg",
        description: " Movie Description would normally go here"
    },
    {
        title: "Macbook",
        image: "https://cnet4.cbsistatic.com/img/s7OzxR8Y3xxOlegTpRQW3CuZPuk=/830x467/2017/06/06/349b7e65-a855-44f0-ae0a-6610ebca0809/apple-macbook-pro-12-inch-2017-4181.jpg",
        description: " Movie Description would normally go here"
    },
    {
        title: "Car",
        image: "https://imgct2.aeplcdn.com/img/800x600/car-data/big/honda-city-image-9579.png?v=29",
        description: " Movie Description would normally go here"
    },
    {
        title: "Television",
        image: "http://imshopping.rediff.com/imgshop/300-400/shopping/pixs/25424/b/bush32._bush-32-inch-curved-led-tv.jpg",
        description: " Movie Description would normally go here"
    },
    {
        title: "Bike",
        description: " Movie Description would normally go here"
    },
    {
        title: "Test",
        image: undefined,
        description: undefined
    },
    {
        title: "The Book of Eli",
        trailer: "bookOfEli.mp4",
        description: " Movie Description would normally go here"
    }
]

function openModal(title){
    itemContent = document.getElementById(title);
    itemContent.style.display = "block";
}

function closeModal(title){
    itemContent = document.getElementById(title);
    itemContent.style.display = "none";
}

