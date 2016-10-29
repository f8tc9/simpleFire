(function() {
    // 第一关
    var first = {
        obstacles: [],
        total: 2,
        init: function() {
            this.obstacles.push(targets.add({
                x: -100,
                y: 0,
                z: -400,
                ry: 0,
                leave: function() {
                    this.rx += 0.3;
                    this.z -= 1.5;
                    if(this.z <= -450) {
                        this.destory();
                    }
                }
            }));
            

            this.obstacles.push(targets.add({
                x: 100,
                y: 0,
                z: -400,
                ry: 0,
                leave: function() {
                    this.rx += 0.3;
                    this.z -= 1.5;
                    if(this.z <= -450) {
                        this.destory();
                    }
                }
            }));
        },
        over: function() {
            second.init();

            targets.remove(obstacles[0].index);
            targets.remove(obstacles[1].index);
        }
    };

    // 第二关
    var second = {
        obstacles: [],
        total: 3,
        init: function() {
            var i;
            for(i = 0; i < 3; i++) {
                targets.add({
                    x: 400,
                    y: Math.random() * 300,
                    z: 200 - Math.random() * 400,
                    moveDir: 0.5 + Math.random(),
                    ry: Math.PI / 2,
                    leave: function() {
                        this.rx += 0.3;
                        this.x += 1.5;
                        if(this.x >= 450) {
                            this.destory();
                        }
                    }
                }, function() {
                    this.z += this.moveDir;
                    if(this.z >= 400) {
                        this.moveDir *= -1;
                    } else if(this.z <= -400) {
                        this.moveDir *= -1;
                    }
                });
            }

            
        }
    };

    // 第三关
    var third = {
        total: 5,
        init: function() {
            var i;
            for(i = 0; i < 5; i++) {
                targets.add({
                    x: 200 - (Math.random() * 400),
                    y: Math.random() * 300,
                    z: 400,
                    moveDir: 1 + Math.random() * 2,
                    ry: 0,
                    leave: function() {
                        this.rx += 0.3;
                        this.z += 1.5;
                        if(this.z >= 450) {
                            this.destory();
                        }
                    }
                }, function() {
                    this.x += this.moveDir;
                    if(this.x >= 400) {
                        this.moveDir *= -1;
                    } else if(this.x <= -400) {
                        this.moveDir *= -1;
                    }
                });
            }
        }
    };

    var level = {
        curr: 0,
        levels: [first, second, third],
        init: function() {
            this.levels[this.curr].init();
        },
        next: function() {
            this.curr++;

            if(this.curr < 3) {
                this.init();

                setTimeout(function() {
                    audio.done();
                }, 1000);
            } else {
                this.end();
            }
            
        },
        check: function() {
            --this.levels[this.curr].total;
            if(this.levels[this.curr].total === 0) {
                this.next();
            }
        },
        end: function() {
            setTimeout(function() {
                audio.end();
                // alert('Good Game');
            }, 1000);
            
        }
    };

    window.level = level;
})();
