lst1 = ["A", "B", "C"];

function calculateGPA(lst){
    lst = lst1;
    var sum = 0;
    var avg = 0;
    for(i of lst){
        if(i ==="A"){
            sum+=100;
        }
        if(i === "B"){
            sum+=80;
        }
        if(i === "C"){
            sum+=70;
        }
    }
    avg = sum/lst.length;

    console.log(avg);

    // document.getElementById("E1").innerHTML = avg;

}