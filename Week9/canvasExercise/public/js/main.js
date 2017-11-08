let canvas = document.getElementById('canvasArea');
if (canvas.getContext) {
    let context = canvas.getContext('2d');
    let centerX = canvas.width / 2;
    let centerY = canvas.height / 2;
    let radius = 180;
    
    // Blue outer circle
    context.beginPath();
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    context.fillStyle = 'blue';
    context.fill();
    
    // white circle
    context.beginPath();
    context.arc(centerX, centerY, radius - 40, 0, 2 * Math.PI, false);
    context.fillStyle = 'white';
    context.fill();
    
    // yellow circle
    context.beginPath();
    context.arc(centerX, centerY, radius - 45, 0, 2 * Math.PI, false);
    context.fillStyle = 'yellow';
    context.fill();
    
    // white circle
    context.beginPath();
    context.arc(centerX, centerY, radius - 90, 0, 2 * Math.PI, false);
    context.fillStyle = 'white';
    context.fill();
    
    // white red
    context.beginPath();
    context.arc(centerX, centerY, radius - 95, 0, 2 * Math.PI, false);
    context.fillStyle = 'red';
    context.fill();
};