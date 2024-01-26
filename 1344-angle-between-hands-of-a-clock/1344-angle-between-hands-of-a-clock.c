double angleClock(int hour, int minutes) {
    float factor = ((5.5 * minutes) - (30 * hour));
    if (factor < 0){
        factor = (-1)*factor;
    }
    if (factor > 180){ 
        return (360-(factor));
    }
    else{
        return (factor);
    } 
}