{
    init: function(elevators, floors) {
        function enqueueFloor(e, floorNum) {
            if (e.destinationQueue.indexOf(floorNum) == -1) {
                e.goToFloor(floorNum);
            }
        }

        function dequeueFloor(e, floorNum) {
            removeElement(e.destinationQueue, floorNum);
        }

        function isInQueue(e, floorNum) {
            return e.destinationQueue.indexOf(floorNum) != -1;
        }

        function isInPressedFloors(e, floorNum) {
            return e.getPressedFloors().indexOf(floorNum) != -1;
        }

        function queueSort(e) {
            var currFloor = e.currentFloor();
            var goingUp = e.goingUpIndicator();

            var floorsUp = [];
            var floorsDown = [];

            e.destinationQueue.forEach(function(fn) {
                if (fn < currFloor) {
                    floorsUp.push(fn);
                } else {
                    floorsDown.push(fn);
                }
            });

            floorsUp.sort(function(a, b) { return a - b; })
            floorsDown.sort(function(a, b) {return a - b; })

            if (currFloor == 0) {
                newQueue = floorsUp;
                goingUp = true;  
            } else if (goingUp && floorsUp.length > 0) {
                newQueue = floorsUp.concat(floorsDown.reverse());
                goingUp = true;
            } else if (!goingUp && floorsDown.length > 0) {
                newQueue = floorsDown.reverse().concat(floorsUp);
                goingUp = false;
            } else if (goingUp) {
                newQueue = floorsDown;
                goingUp = false;
            } else {
                newQueue = floorsUp;
                goingUp = true;
            }
            
            alert(currFloor);

            e.destinationQueue = newQueue;
            e.goingUpIndicator(goingUp);
            e.goingDownIndicator(!goingUp);

            e.checkDestinationQueue();
        }

        function removeElement(arr, el) {
            while ((i = arr.indexOf(el)) != -1) {
                arr.splice(i, 1);
            }
            return arr;
        }

        function callBestElevator(floorNum) {
            var best = elevators[0];
            var diff = Math.abs(best.currentFloor() - floorNum);
            elevators.forEach(function(e) {
                if ((e.currentFloor() > floorNum && e.goingDownIndicator())||e.goingUpIndicator()) {
                    var this_diff = Math.abs(e.currentFloor() - floorNum);
                    if (this_diff < diff) {
                        best = e;
                        diff = this_diff;
                    }
                }
            })
            enqueueFloor(best, floorNum);
        }

        elevators.forEach(function(e){
            e.on("idle", function() {
                e.goToFloor(0);
            });  

            e.on("passing_floor", function(floorNum, direction) { 
                if (isInQueue(e, floorNum) || isInPressedFloors(e, floorNum)) {
                    e.goToFloor(floorNum, true);
                    dequeueFloor(e, floorNum);
                }
            });

            e.on("stopped_at_floor", function(floorNum) {
                queueSort(e);
            });

            e.on("floor_button_pressed", function(floorNum) {                 
                e.goToFloor(floorNum);
            });
        });

        floors.forEach(function(f){
            f.on("up_button_pressed down_button_pressed", function() {
                callBestElevator(f.floorNum());
            });
        });
    },
        
        update: function(dt, elevators, floors) {
        }
}