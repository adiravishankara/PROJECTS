(function () {
        var $container = $('#circle');
        var $slider = $('#slider');
        var sliderW2 = $slider.width()/2;
        var sliderH2 = $slider.height()/2;    
        var radius = 15;
        var deg = 0;    
        var elP = $('#circle').offset();
        var elPos = { x: elP.left, y: elP.top};
        var X = 0, Y = 0;
        var mdown = false;
        $('#circle')
        .mousedown(function (e) { mdown = true; })
        .mouseup(function (e) { mdown = true; })
        .mousemove(function (e) {
            if (mdown) {
               var mPos = {x: e.clientX-elPos.x, y: e.clientY-elPos.y};
               var atan = Math.atan2(mPos.x-radius, mPos.y-radius);
               deg = -atan/(Math.PI/180) + 180; // final (0-360 positive) degrees from mouse position 
                
               X = Math.round(radius* Math.sin(deg*Math.PI/180));    
               Y = Math.round(radius*  -Math.cos(deg*Math.PI/180));
               $slider.css({ left: X+radius-sliderW2, top: Y+radius-sliderH2 });              
               // AND FINALLY apply exact degrees to ball rotation
               $slider.css({ WebkitTransform: 'rotate(' + deg + 'deg)'});
               $slider.css({ '-moz-transform': 'rotate(' + deg + 'deg)'});
               //
               // PRINT DEGREES
               $('input[name="angle"]').val(Math.ceil(deg));
            }
        });
})();