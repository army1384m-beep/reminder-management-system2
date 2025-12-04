class Remminder {  // intentional typo
    constructor(title, date) {
        this.title = title;
        this.date = date;
        this.completed = false;
    }
    
    markComplete() {
        this.completed = true;
    }
}
module.exports = Remminder;
