// var CB = require('cloudboost');
var a=CB.CloudApp.init("anuchdiujlug", "ff59f960-5982-479c-81dc-e3b1f7856a96");
console.log(a);
//Data Storage : Create a CloudObject of type 'Custom' (Note: You need to create a table 'Custom' on CloudBoost Dashboard)

var obj = new CB.CloudObject('User');
var json_=CB.toJSON(obj);
console.log(json_)
console.log(obj);

//Set the property 'name' (Note: Create a column 'name' of type text on CloudBoost Dashboard)
obj.set('a1', 'newone');

//Save the object
obj.save({
    success: function(res) {
        console.log("object saved successfully");
    },
    error: function(err) {
        console.log("error while saving object");
    }
});
