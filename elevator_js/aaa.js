{
    init: function(elevators, floors) {
        function enqueue(e, floorNum) {
            if (e.destinationQueue.indexOf(floorNum) == -1) {
                e.goToFloor(floorNum);
            }
        }
        
        function dequeue(e, floorNum) {
            remove(e.destinationQueue, floorNum);
        }
        
        function isInQueue(e, floorNum) {
            return e.destinationQueue.indexOf(floorNum) != -1;
        }
        
        function isInPressedFloors(e, floorNum) {
            return e.getPressedFloors().indexOf(floorNum) != -1;
        }
        
        function queueSort(e) {
            var currFloor = e.currentFloor;
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
            
            if (goingUp && floorsUp.length > 0) {
                newQueue = floorsUp.concat(floorsDown.reverse());
                goingUp = true;
            } else if (!goingUp && floorsDown.length > 0) {
                newQueue = floorsDown.concat(floorsUp.reverse());
                goingUp = false;
            } else if (goingUp) {
                newQueue = floorsDown;
                goingUp = false;
            } else {
                newQueue = floorsUp;
                goingUp = true;
            }
            
            e.destinationQueue = newQueue;
            e.goingUpIndicator(goingUp);
            e.goingDownIndicator(!goingUp);
            
            e.checkDestinationQueue();
        }
        
        function remove(arr, el) {
            while ((var i = arr.indexOf(el)) != -1) {
                arr.splice(i, 1);
            }
            return arr;
        }
        
        function callBestElevator(floorNum) {
            var best = elevators[0];
            var diff = Math.abs(best.currentFloor - floorNum);
            elevators.forEach(function(e) {
                if ((e.currentFloor > floorNum && e.goingDownIndicator())||e.goingUpIndicator()) {
                    var this_diff = Math.abs(e.currentFloor - floorNum);
                    if (this_diff < diff) {
                        best = e;
                        diff = this_diff;
                    }
                }
            })
            enqueue(best, floorNum);
        }

        elevators.forEach(function(e){
            e.on("idle", function() {
                e.goToFloor(0);
            });  

            e.on("passing_floor", function(floorNum, direction) { 
                if (isInQueue(e, floorNum) || isInPressedFloors(e, floorNum)) {
                    e.goToFloor(floorNum, true);
                    dequeue(e, floorNum);
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