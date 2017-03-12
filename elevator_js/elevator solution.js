{
    init: function(elevators, floors) {
        function callElevator(floorNum){
            var lowestElevator = elevators[0];

            elevators.forEach(function(e1){
                if(e1.destinationQueue.length < lowestElevator.destinationQueue.length){
                    lowestElevator = e1;
                }
            });

            lowestElevator.goToFloor(floorNum);
        }

        elevators.forEach(function(e){
            e.on("idle", function() {
                e.goToFloor(0);
            });  

            e.on("passing_floor", function(floorNum, direction) { 
                var found = false;
                var i;

                while ((i = e.destinationQueue.indexOf(floorNum)) != -1) {
                    e.destinationQueue.splice(i, 1);
                    found = true;
                }

                if(found)
                    e.goToFloor(floorNum,true);

                e.checkDestinationQueue();

            });

            e.on("floor_button_pressed", function(floorNum) {                 
                e.goToFloor(floorNum);
            });
        });

        floors.forEach(function(f){
            f.on("up_button_pressed down_button_pressed", function() {
                callElevator(f.floorNum());
            });
        });
    },
    update: function(dt, elevators, floors) {
    }
}
