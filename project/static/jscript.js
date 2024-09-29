function testFunc(){
    selectedValue = document.querySelector('input[name = "exeRad"]:checked').value
    air = "AI summary:"
    
    if (selectedValue == 10){
        document.getElementById("ratedExe").textContent =  air.concat(' ', "YO MOOD FIREEEE!!!!!");
    }else if (selectedValue <= 9 && selectedValue >= 7){ 
        document.getElementById("ratedExe").textContent  = air.concat(' ', "your mood alr")
    }else if (selectedValue < 8 && selectedValue  > 1){
         document.getElementById("ratedExe").textContent  = air.concat(' ', "your mood could be better") 
    }else{
        document.getElementById("ratedExe").textContent  = air.concat(' ', "suicide")
    }
}