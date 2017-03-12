{
    init: function(elevators, floors) {
        floors.forEach(function(floor) {
            floor.goingUp = false;
            floor.goingDown = false;
            floor.on("up_button_pressed", function() {
                floor.goingUp = true;
                callElevator(floor.floorNum(), "up");
            });
            floor.on("down_button_pressed", function() {
                floor.goingDown = true;
                callElevator(floor.floorNum(), "down");
            });
        });

        elevators.forEach(function(elevator) {
            elevator.addFloor = function(floorNum) {
                if (this.destinationQueue.indexOf(floorNum) == -1) {
                    this.destinationQueue.push(floorNum);
                }
                this.checkDestinationQueue();
            };
            elevator.removeFloor = function(floorNum) {
                this.destinationQueue = this.destinationQueue.filter(function(x) {return x != floorNum});
                this.checkDestinationQueue();
            };
            elevator.sortQueue = function(currFloor, direction) {
                queue = this.destinationQueue;
                less = queue.filter(function(x) {return x < currFloor}).sort().reverse();
                greater = queue.filter(function(x) {return x > currFloor}).sort();
                if (direction == "down") {
                    this.destinationQueue = [currFloor].concat(less, greater);
                } else {
                    this.destinationQueue = [currFloor].concat(greater, less);
                }
                this.checkDestinationQueue();
            }
            elevator.setIndicators = function(floorNum, direction) {
                if (floorNum == floors.length - 1) {
                    this.goingDownIndicator(true); 
                    this.goingUpIndicator(false);
                } else if (floorNum == 0) {
                    this.goingUpIndicator(true); 
                    this.goingDownIndicator(false);
                } else {
                    this.goingUpIndicator(this.destinationQueue[0] >= floorNum);
                    this.goingDownIndicator(this.destinationQueue[0] <= floorNum);
                }
            }
            elevator.on("idle", function() {
                this.addFloor(0);
            });
            elevator.on("passing_floor", function(floorNum, direction) {
                f = floors[floorNum];
                if (f.goingUp == true && direction == "up") {
                    this.addFloor(floorNum);
                    this.sortQueue(floorNum, direction);
                }
                if (f.goingDown == true && direction == "down") {
                    this.addFloor(floorNum);
                    this.sortQueue(floorNum, direction);
                }
                this.setIndicators(floorNum, direction);
            });
            elevator.on("stopped_at_floor", function(floorNum) {
                this.removeFloor(floorNum);
                if (this.loadFactor < 0.8) {
                    if (this.destinationDirection() == "down") {
                        floors[floorNum].goingDown = false;
                    } else {
                        floors[floorNum].goingUp = false;
                    }
                }
            });
            elevator.on("floor_button_pressed", function(floorNum) {
                this.addFloor(floorNum);
            })
        });
        
        function callElevator(floorNum, direction) {
            els = elevators.filter(function(e) { 
                return (direction == "up" && e.currentFloor() > floorNum) || (direction == "down" && e.currentFloor() < floorNum) 
            });
            if (els.length == 0) {els = elevators}
            best = els.sort(function(x, y) {return x.loadFactor() - y.loadFactor()})[0];
            best.addFloor(floorNum);
        }
    },
    update: function(dt, elevators, floors) {
        // We normally don't need to do anything here
    }
}